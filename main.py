import generator
import random

class QuantumCheeseball:
    def __init__(self, anchor=None):
        self.anchor = anchor or random.randint(0, 999999)
        self.gen = generator.Generator(self.anchor)

    def run(self):
        self.gen.view_grid()

if __name__ == "__main__":
    qc = QuantumCheeseball()
    qc.run()
