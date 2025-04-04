import math
import random

class PerlinNoise1D:
    def __init__(self, seed=None):
        if seed is not None:
            random.seed(seed)
        self.permutation_table = list(range(256))
        random.shuffle(self.permutation_table)
        self.permutation_table += self.permutation_table  # repeat the table
    
    def fade(self, distance):
        """Smooth the interpolation curve."""
        return distance * distance * distance * (distance * (distance * 6 - 15) + 10)
    
    def lerp(self, value_a, value_b, weight):
        """Linear interpolation between two values."""
        return value_a + weight * (value_b - value_a)
    
    def gradient(self, hash_value, distance_from_grid_point):
        """Return the gradient (-1 or 1) times the distance."""
        return (1 if hash_value % 2 == 0 else -1) * distance_from_grid_point
    
    def noise(self, x_position):
        """Calculate Perlin noise at a given x position."""
        # Find surrounding grid points
        left_grid_point = math.floor(x_position)
        right_grid_point = left_grid_point + 1

        # Distance from x_position to left grid point
        distance_from_left = x_position - left_grid_point

        # Hash values for the grid points
        left_hash = self.permutation_table[left_grid_point & 255]
        right_hash = self.permutation_table[right_grid_point & 255]

        # Calculate the gradients
        left_gradient = self.gradient(left_hash, distance_from_left)
        right_gradient = self.gradient(right_hash, distance_from_left - 1)

        # Smooth the distance
        smooth_distance = self.fade(distance_from_left)

        # Interpolate between the gradients
        return self.lerp(left_gradient, right_gradient, smooth_distance)

# Usage example
if __name__ == "__main__":
    noise_generator = PerlinNoise1D(seed=42)

    for sample_index in range(20):
        x = sample_index * 0.1
        value = noise_generator.noise(x)
        print(f"x = {x:.2f}, noise = {value:.3f}")
