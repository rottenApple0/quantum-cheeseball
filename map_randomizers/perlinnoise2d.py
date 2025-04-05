import math
import random

class PerlinNoise2D:
    def __init__(self, width, height, scale=0.1, seed=None):
        """
        width: number of horizontal points
        height: number of vertical points
        scale: how zoomed in/out the noise should be
        seed: random seed for reproducibility
        """
        self.width = width
        self.height = height
        self.scale = scale
        
        if seed is not None:
            random.seed(seed)
        self.permutation_table = list(range(256))
        random.shuffle(self.permutation_table)
        self.permutation_table += self.permutation_table  # repeat to avoid overflow

    def fade(self, t):
        """Smooth curve function for interpolation."""
        return t * t * t * (t * (t * 6 - 15) + 10)

    def lerp(self, a, b, weight):
        """Linear interpolation."""
        return a + weight * (b - a)

    def grad(self, hash_value, x_offset, y_offset):
        """Get a 2D gradient based on hash value."""
        h = hash_value & 3  # Only 4 directions (00, 01, 10, 11)
        if h == 0:
            return x_offset + y_offset
        elif h == 1:
            return -x_offset + y_offset
        elif h == 2:
            return x_offset - y_offset
        else:  # h == 3
            return -x_offset - y_offset

    def noise(self, x_position, y_position):
        """Get Perlin noise value at a specific (x, y) world position."""
        # Scale coordinates
        x_position *= self.scale
        y_position *= self.scale

        # Find unit grid cell containing point
        x0 = math.floor(x_position)
        y0 = math.floor(y_position)
        x1 = x0 + 1
        y1 = y0 + 1

        # Relative x and y inside the cell
        x_relative = x_position - x0
        y_relative = y_position - y0

        # Fade curves for x and y
        u = self.fade(x_relative)
        v = self.fade(y_relative)

        # Hash coordinates of the 4 corners
        aa = self.permutation_table[self.permutation_table[x0 & 255] + (y0 & 255)]
        ab = self.permutation_table[self.permutation_table[x0 & 255] + (y1 & 255)]
        ba = self.permutation_table[self.permutation_table[x1 & 255] + (y0 & 255)]
        bb = self.permutation_table[self.permutation_table[x1 & 255] + (y1 & 255)]

        # Add blended results from 4 corners
        value_aa = self.grad(aa, x_relative, y_relative)
        value_ba = self.grad(ba, x_relative - 1, y_relative)
        value_ab = self.grad(ab, x_relative, y_relative - 1)
        value_bb = self.grad(bb, x_relative - 1, y_relative - 1)

        # Interpolate
        lerp_x1 = self.lerp(value_aa, value_ba, u)
        lerp_x2 = self.lerp(value_ab, value_bb, u)
        final_value = self.lerp(lerp_x1, lerp_x2, v)

        return final_value

    def generate_map(self):
        """Generate a full 2D array of noise values."""
        noise_map = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                value = self.noise(x, y)
                row.append(value)
            noise_map.append(row)
        return noise_map

    def __call__(self, x_position, y_position):
        return self.noise(x_position, y_position)
