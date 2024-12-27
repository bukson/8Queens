import tkinter as tk
from enum import unique

from PIL import Image, ImageTk

from solution_finder import find_solutions, get_column_indexes


def draw_chessboard(canvas, solution):
    global queen_image
    global board_size
    canvas.delete("all")
     # Chessboard size
    cell_size = board_size // 8

    for row in range(8):
        for col in range(8):
            color = "white" if (row + col) % 2 == 0 else "black"
            x1, y1 = col * cell_size, row * cell_size
            x2, y2 = x1 + cell_size, y1 + cell_size
            canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    # Place queens
    for row, col in enumerate(solution):
        x_center = col * cell_size + cell_size // 2
        y_center = row * cell_size + cell_size // 2
        canvas.create_image(x_center, y_center, image=queen_image)


def update_solution(canvas):
    global current_index
    global unique_label
    global index_label
    global unique
    solution = solutions[current_index]
    draw_chessboard(canvas, solution)
    index_label.config(text=f"Solution: {current_index + 1}/{len(solutions)}")
    unique_text = "Non Unique Solutions" if not unique else "Unique Solutions"
    unique_label.config(text=unique_text)


def next_solution(canvas):
    global current_index
    if current_index < len(solutions) - 1:
        current_index += 1
    update_solution(canvas)


def previous_solution(canvas):
    global current_index
    if current_index > 0:
        current_index -= 1
    update_solution(canvas)


def toggle_uniqueness():
    global unique
    global solutions
    global current_index
    unique = not unique
    solutions = [get_column_indexes(s) for s in find_solutions(unique=unique)]
    if current_index >= len(solutions) -1:
        current_index = len(solutions) -1
    update_solution(canvas)

unique = True
solutions = [get_column_indexes(s) for s in find_solutions(unique=unique)]
current_index = 0
board_size = 800
root = tk.Tk()
root.title("8-Queens Problem")

queen_image_raw = Image.open("queen.png")  # Replace with your queen PNG file
queen_image_resized = queen_image_raw.resize((board_size//8, board_size//8))  # Adjust size to fit the chessboard
queen_image = ImageTk.PhotoImage(queen_image_resized)

# Canvas for the chessboard
canvas = tk.Canvas(root, width=board_size, height=board_size)
canvas.grid(row=0, column=0, columnspan=2)

# Label to display solution index
index_label = tk.Label(root, text=f"Solution: 1/{len(solutions)}")
index_label.grid(row=1, column=0, columnspan=3)

# Navigation buttons
btn_previous = tk.Button(root, text="Previous", command=lambda: previous_solution(canvas))
btn_previous.grid(row=2, column=0, pady=10)

btn_next = tk.Button(root, text="Next", command=lambda: next_solution(canvas))
btn_next.grid(row=2, column=1, pady=10)

btn_unique = tk.Button(root, text="Toggle Uniqueness", command=lambda: toggle_uniqueness())
btn_unique.grid(row=3, column=0, pady=10)

unique_label = tk.Label(root, text=f"Unique Solution")
unique_label.grid(row=3, column=1)

# Draw the initial solution
update_solution(canvas)

root.mainloop()
