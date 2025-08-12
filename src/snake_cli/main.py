from tkinter import Tk, Label, Canvas
from config import GAME_WIDTH, GAME_HEIGHT, BACKGROUND_COLOR
from game_logic import GameLogic

def main():
    window = Tk()
    window.title("Snake Game")
    window.resizable(False, False)

    score_label = Label(window, text="Score: 0", font=('consolas', 40))
    score_label.pack()

    canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
    canvas.pack()

    window.update()
    # Center the window
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    game = GameLogic(window, canvas, score_label)

    # Bind controls
    window.bind("<Left>", game.change_direction)
    window.bind("<Right>", game.change_direction)
    window.bind("<Up>", game.change_direction)
    window.bind("<Down>", game.change_direction)

    game.next_turn()

    window.mainloop()

if __name__ == "__main__":
    main()