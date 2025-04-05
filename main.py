from map_randomizers.generator import Generator
from map_randomizers.perlinnoise1d import PerlinNoise1D
from map_randomizers.perlinnoise2d import PerlinNoise2D
from map_randomizers.cellularautomata import CellularAutomata
from map_randomizers.drunkardwalk import DrunkardsWalk
import random

class QuantumCheeseball:
    def __init__(self, anchor=None, width=60, height=30):
        self.anchor = anchor or random.randint(0, 999999)
        self.width = width
        self.height = height
        self.reset_modules()

    def reset_modules(self):
        self.gen = Generator(self.anchor, width=self.width, height=self.height)
        self.p_noise = PerlinNoise1D(width=self.width, seed=self.anchor)
        self.noise2d = PerlinNoise2D(width=self.width, height=self.height, seed=self.anchor)
        self.c_automata = CellularAutomata(self.width, self.height, wall_chance=0.65, seed=self.anchor)
        self.d_walk = DrunkardsWalk(self.width, self.height)

    def view_generator(self):
        self.gen.view_grid()

    def view_perlin_1d(self):
        for sample_index in range(20):
            x = sample_index * 0.1
            value = self.p_noise.noise(x)
            print(f"x = {x:.2f}, noise = {value:.3f}")

    def view_perlin_2d(self):
        scale = 0.1
        for y in range(self.height):
            row = ""
            for x in range(self.width):
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

    def run_cellular_automata(self):
        self.c_automata.simulate(steps=5)
        self.c_automata.display()

    def run_drunkards_walk(self):
        self.d_walk.walk(steps=300)
        self.d_walk.display()

    def run(self):
        print("=== QuantumCheeseball CLI ===")
        print(f"Current Seed: {self.anchor}")
        print("Format: a:x:y:s  (Algorithm:X:Y:Seed)")
        print("Algorithms:")
        print(" 1 - View Generator Grid")
        print(" 2 - View Perlin Noise 1D Samples")
        print(" 3 - View Perlin Noise 2D Map")
        print(" 4 - Run Cellular Automata")
        print(" 5 - Run Drunkard's Walk")
        print(" 0 - Quit")

        while True:
            user_input = input("Enter command: ").strip()
            print(user_input)
            if not user_input:
                continue
            if user_input == "0":
                print("Goodbye!")
                break
            parts = user_input.split(":")

            if len(parts) != 4:
                print("Invalid format. Please use a:x:y:s")
                continue

            try:
                a, x, y, s = map(int, parts)
            except ValueError:
                print("Invalid input. All fields must be integers.")
                continue

            # Update width, height, and seed
            if (x != self.width) or (y != self.height) or (s != self.anchor):
                self.width = x
                self.height = y
                self.anchor = s
                self.reset_modules()
                print(f"Seed updated to {self.anchor}")
                print(f"Map size updated to {self.width}x{self.height}")

            if a == 1:
                self.view_generator()
            elif a == 2:
                self.view_perlin_1d()
            elif a == 3:
                self.view_perlin_2d()
            elif a == 4:
                self.run_cellular_automata()
            elif a == 5:
                self.run_drunkards_walk()
            else:
                print("Unknown algorithm number.")

if __name__ == "__main__":
    qc = QuantumCheeseball()
    qc.run()
