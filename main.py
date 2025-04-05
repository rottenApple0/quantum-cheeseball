from map_randomizers.generator import Generator
from map_randomizers.perlinnoise1d import PerlinNoise1D
from map_randomizers.perlinnoise2d import PerlinNoise2D
from map_randomizers.cellularautomata import CellularAutomata
from map_randomizers.drunkardwalk import DrunkardsWalk
import random

class QuantumCheeseball:
    def __init__(self, anchor=None):
        self.anchor = anchor or random.randint(0, 999999)
        self.gen = Generator(self.anchor)
        self.p_noise = PerlinNoise1D(self.anchor)
        self.noise2d = PerlinNoise2D(self.anchor)
        self.c_automata = CellularAutomata(60, 30, wall_chance=0.65, seed=self.anchor)
        self.d_walk = DrunkardsWalk(60, 30)

    def view_generator(self):
        self.gen.view_grid()

    def view_perlin_1d(self):
        for sample_index in range(20):
            x = sample_index * 0.1
            value = self.p_noise.noise(x)
            print(f"x = {x:.2f}, noise = {value:.3f}")

    def view_perlin_2d(self):
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

    def run_cellular_automata(self):
        self.c_automata.simulate(steps=5)
        self.c_automata.display()

    def run_drunkards_walk(self):
        self.d_walk.walk(steps=300)
        self.d_walk.display()

    def run(self):
        while True:
            print("\n=== QuantumCheeseball CLI ===")
            print(f"Seed: {self.anchor}")
            print("1. View Generator grid")
            print("2. View Perlin Noise 1D samples")
            print("3. View Perlin Noise 2D map")
            print("4. Run Cellular Automata simulation")
            print("5. Run Drunkard's Walk")
            print("6. Quit")

            choice = input("Choose an option (1-6): ").strip()

            if choice == "1":
                self.view_generator()
            elif choice == "2":
                self.view_perlin_1d()
            elif choice == "3":
                self.view_perlin_2d()
            elif choice == "4":
                self.run_cellular_automata()
            elif choice == "5":
                self.run_drunkards_walk()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    qc = QuantumCheeseball()
    qc.run()
