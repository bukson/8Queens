import tkinter as tk
from enum import unique

from PIL import Image, ImageTk

from solution_finder import find_solutions, get_column_indexes, Board


class EightQueensVisualiser():
    def __init__(self):
        self.unique = True
        self.non_unique_solutions = [get_column_indexes(s) for s in find_solutions(unique=False)]
        self.unique_solutions = [get_column_indexes(s) for s in find_solutions(unique=True)]
        self.solutions = self.unique_solutions
        self.current_index = 0
        self.board_size = 800
        self.root = tk.Tk()
        self.root.title("8-Queens Problem")
        self.queen_image = self._load_queen_image()

        self.canvas = tk.Canvas(self.root, width=self.board_size, height=self.board_size)
        self.canvas.grid(row=0, column=0, columnspan=6)

        self.index_label = tk.Label(self.root, text=f"Solution: 1/{len(self.solutions)}")
        self.index_label.grid(row=1, column=0, columnspan=6)

        self.button_previous = tk.Button(self.root, text="Previous", command=lambda: self.show_previous_solution())
        self.button_previous.grid(row=2, column=1, pady=10, columnspan=2)

        self.button_next = tk.Button(self.root, text="Next", command=lambda: self.show_next_solution())
        self.button_next.grid(row=2, column=3, pady=10, columnspan=2)

        self.button_unique = tk.Button(self.root, text="Toggle Uniqueness", command=lambda: self.toggle_uniqueness())
        self.button_unique.grid(row=3, column=0, pady=10, columnspan=2)

        self.unique_label = tk.Label(self.root, text=f"Unique Solution")
        self.unique_label.grid(row=3, column=2, pady=10, columnspan=2)

        self.button_exit = tk.Button(self.root, text="Exit", command=self.root.destroy)
        self.button_exit.grid(row=3, column=4, pady=10, columnspan=2)

    def _load_queen_image(self):
        queen_image_raw = Image.open("queen.png")
        queen_image_resized = queen_image_raw.resize(
            (self.board_size // 8, self.board_size // 8))
        return ImageTk.PhotoImage(queen_image_resized)


    def draw_chessboard(self, solution:list[int]) -> None:
        self.canvas.delete("all")
        cell_size = self.board_size // 8

        for row in range(8):
            for col in range(8):
                color = "white" if (row + col) % 2 == 0 else "black"
                x1, y1 = col * cell_size, row * cell_size
                x2, y2 = x1 + cell_size, y1 + cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

        for row, col in enumerate(solution):
            x_center = col * cell_size + cell_size // 2
            y_center = row * cell_size + cell_size // 2
            self.canvas.create_image(x_center, y_center, image=self.queen_image)


    def update_solution(self) -> None:
        solution = self.solutions[self.current_index]
        self.draw_chessboard(solution)
        self.index_label.config(text=f"Solution: {self.current_index + 1}/{len(self.solutions)}")
        unique_text = "Non Unique Solutions" if not self.unique else "Unique Solutions"
        self.unique_label.config(text=unique_text)


    def show_next_solution(self) -> None:
        if self.current_index < len(self.solutions) - 1:
            self.current_index += 1
            self.update_solution()


    def show_previous_solution(self) -> None:
        if self.current_index > 0:
            self.current_index -= 1
            self.update_solution()


    def toggle_uniqueness(self) -> None:
        self.unique = not self.unique
        self.solutions = self.unique_solutions if self.unique else self.non_unique_solutions
        if self.current_index >= len(self.solutions) - 1:
            self.current_index = len(self.solutions) - 1
        self.update_solution()


    def start(self) -> None:
        self.update_solution()
        self.root.mainloop()

if __name__ == "__main__":
    application = EightQueensVisualiser()
    application.start()