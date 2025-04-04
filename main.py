from map_randomizers.generator import Generator
from map_randomizers.perlinnoise1d import PerlinNoise1D
from map_randomizers.perlinnoise2d import PerlinNoise2D
import random
class QuantumCheeseball:
    def __init__(self, anchor=None):
        self.anchor = anchor or random.randint(0, 999999)
        self.gen = Generator(self.anchor)
        self.p_noise = PerlinNoise1D(self.anchor)
        self.noise2d = PerlinNoise2D(seed=42)
    def run(self):
        self.gen.view_grid()
        for sample_index in range(20):
            x = sample_index * 0.1
            value = self.p_noise.noise(x)
            print(f"x = {x:.2f}, noise = {value:.3f}")
        width = 60
        height = 30
        scale = 0.1

        for y in range(height):
            row = ""
            for x in range(width):
                noise_value = self.noise2d.noise(x * scale, y * scale)
                if noise_value < -0.3:
                    row += "~"
                elif noise_value < 0.0:
                    row += ","
                elif noise_value < 0.3:
                    row += "."
                else:
                    row += "^"
            print(row)
if __name__ == "__main__":
    qc = QuantumCheeseball()
    qc.run()
