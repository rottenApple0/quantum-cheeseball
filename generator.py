import random
from typing import List


class Generator:
    def __init__(self, anchor: int, width: int = 4, height: int = 4):
        self.anchor = anchor
        self.width = width
        self.height = height
        random.seed(self.anchor)
        self.grid: List[List[int]] = [[random.randint(0, 1) for _ in range(width)] for _ in range(height)]

    def view_grid(self):
        for row in self.grid:
            print(''.join(str(tile) for tile in row))