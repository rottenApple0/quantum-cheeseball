import random

class DrunkardsWalk:
    def __init__(self, width, height, start_x=None, start_y=None):
        self.width = width
        self.height = height
        self.map = [['*' for _ in range(width)] for _ in range(height)]  # Wall by default

        # Start in the middle if no start given
        self.x = start_x if start_x is not None else width // 2
        self.y = start_y if start_y is not None else height // 2

    def is_in_bounds(self, x, y):
        """Check if (x, y) is within the map bounds."""
        return 0 <= x < self.width and 0 <= y < self.height

    def walk(self, steps):
        """Perform the drunkard's walk."""
        for _ in range(steps):
            self.map[self.y][self.x] = '_'  # Mark as floor

            direction = random.choice(['up', 'down', 'left', 'right'])

            if direction == 'up':
                new_y = self.y - 1
                if self.is_in_bounds(self.x, new_y):
                    self.y = new_y
            elif direction == 'down':
                new_y = self.y + 1
                if self.is_in_bounds(self.x, new_y):
                    self.y = new_y
            elif direction == 'left':
                new_x = self.x - 1
                if self.is_in_bounds(new_x, self.y):
                    self.x = new_x
            elif direction == 'right':
                new_x = self.x + 1
                if self.is_in_bounds(new_x, self.y):
                    self.x = new_x

    def display(self):
        """Print the map nicely."""
        for row in self.map:
            print(''.join(row))

    def get_map(self):
        """Return the internal map (useful if you want to draw it in your game)."""
        return self.map
