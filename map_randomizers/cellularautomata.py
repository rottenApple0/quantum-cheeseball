import random

class CellularAutomata:
    def __init__(self, width, height, wall_chance=0.45, seed=None):
        self.width = width
        self.height = height
        self.wall_chance = wall_chance
        self.seed = seed
        
        if seed is not None:
            random.seed(seed)
        
        self.grid = self._initialize_grid()
    
    def _initialize_grid(self):
        return [['#' if random.random() < self.wall_chance else '.' for _ in range(self.width)] for _ in range(self.height)]
    
    def _count_wall_neighbors(self, x, y):
        count = 0
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dy == 0 and dx == 0:
                    continue  # Skip self
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if self.grid[ny][nx] == '#':
                        count += 1
                else:
                    count += 1  # Treat out-of-bounds as wall
        return count

    def simulate(self, steps=5):
        for _ in range(steps):
            new_grid = [row.copy() for row in self.grid]
            for y in range(self.height):
                for x in range(self.width):
                    wall_count = self._count_wall_neighbors(x, y)
                    if wall_count >= 5:
                        new_grid[y][x] = '#'
                    else:
                        new_grid[y][x] = '.'
            self.grid = new_grid

    def display(self):
        for row in self.grid:
            print(''.join(row))
