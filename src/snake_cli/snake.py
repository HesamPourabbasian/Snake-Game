from tkinter import Canvas
from config import SPACE_SIZE, SNAKE_COLOR, BODY_PARTS

class Snake:
    def __init__(self, canvas: Canvas):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
        self.canvas = canvas

        for i in range(BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = self.canvas.create_rectangle(
                x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                fill=SNAKE_COLOR, tags="snake"
            )
            self.squares.append(square)

    def move(self, x: int, y: int):
        self.coordinates.insert(0, (x, y))
        square = self.canvas.create_rectangle(
            x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR
        )
        self.squares.insert(0, square)

    def remove_tail(self):
        del self.coordinates[-1]
        self.canvas.delete(self.squares[-1])
        del self.squares[-1]