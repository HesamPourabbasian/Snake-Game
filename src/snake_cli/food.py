from tkinter import Canvas
import random
from config import GAME_WIDTH, GAME_HEIGHT, SPACE_SIZE, FOOD_COLOR

class Food:
    def __init__(self, canvas: Canvas):
        self.canvas = canvas
        self.coordinates = self._generate_position()
        self.canvas.create_oval(
            self.coordinates[0], self.coordinates[1],
            self.coordinates[0] + SPACE_SIZE, self.coordinates[1] + SPACE_SIZE,
            fill=FOOD_COLOR, tag="food"
        )

    def _generate_position(self):
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        return [x, y]