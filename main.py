import tkinter as tk

def draw_chessboard(canvas, solution):
    canvas.delete("all")
    size = 400  # Chessboard size
    cell_size = size // 8

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
        radius = cell_size // 4
        canvas.create_oval(
            x_center - radius, y_center - radius,
            x_center + radius, y_center + radius,
            fill="red"
        )

# Example solution (list of column indices for each row)
solution = [0, 4, 7, 5, 2, 6, 1, 3]

# Create GUI
root = tk.Tk()
root.title("8-Queens Problem")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

draw_chessboard(canvas, solution)

root.mainloop()
