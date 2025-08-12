from tkinter import Canvas, Button, ALL
from config import GAME_WIDTH, GAME_HEIGHT, SPEED, SPACE_SIZE
from snake import Snake
from food import Food

class GameLogic:
    def __init__(self, window, canvas: Canvas, score_label):
        self.window = window
        self.canvas = canvas
        self.score_label = score_label
        self.score = 0
        self.direction = 'down'
        self.snake = Snake(canvas)
        self.food = Food(canvas)

    def next_turn(self):
        x, y = self.snake.coordinates[0]

        if self.direction == "up":
            y -= SPACE_SIZE
        elif self.direction == "down":
            y += SPACE_SIZE
        elif self.direction == "left":
            x -= SPACE_SIZE
        elif self.direction == "right":
            x += SPACE_SIZE

        self.snake.move(x, y)

        if x == self.food.coordinates[0] and y == self.food.coordinates[1]:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.canvas.delete("food")
            self.food = Food(self.canvas)
        else:
            self.snake.remove_tail()

        if self.check_collisions():
            self.game_over()
        else:
            self.window.after(max(50, SPEED - self.score * 5), self.next_turn)

    def change_direction(self, event):
        new_direction = event.keysym.lower()
        if new_direction == "left" and self.direction != "right":
            self.direction = "left"
        elif new_direction == "right" and self.direction != "left":
            self.direction = "right"
        elif new_direction == "up" and self.direction != "down":
            self.direction = "up"
        elif new_direction == "down" and self.direction != "up":
            self.direction = "down"

    def check_collisions(self):
        x, y = self.snake.coordinates[0]
        if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
            return True
        for body_part in self.snake.coordinates[1:]:
            if x == body_part[0] and y == body_part[1]:
                return True
        return False

    def game_over(self):
        self.canvas.delete(ALL)
        self.canvas.create_text(
            GAME_WIDTH / 2, GAME_HEIGHT / 2 - 50,
            text=f"GAME OVER\nScore: {self.score}",
            fill="red", font=('consolas', 40)
        )
        try_again_btn = Button(
            self.window,
            text="Try Again",
            font=('consolas', 20),
            command=self.restart_game
        )
        self.canvas.create_window(
            GAME_WIDTH / 2, GAME_HEIGHT / 2 + 50,
            window=try_again_btn
        )

    def restart_game(self):
        self.score = 0
        self.direction = 'down'
        self.score_label.config(text=f"Score: {self.score}")
        self.canvas.delete(ALL)
        self.snake = Snake(self.canvas)
        self.food = Food(self.canvas)
        self.next_turn()