""" Create a basic MineSweeper Game"""

import tkinter as tk
import settings
import utilities
from MineSweeperCells import Cell


def draw_the_window():
    root = tk.Tk()
    root.geometry(f'{settings.width}x{settings.height}')
    root.title("MineSweeper")
    root.configure(bg='black')
    root.resizable(False, False)  # Height and Width Resizing False
    top_frame = tk.Frame(root, bg=utilities.frame_color_top, width=utilities.width_percent(percentage=100),
                         height=utilities.height_percent(percentage=25))
    top_frame.place(x=0, y=0)
    game_title_top = tk.Label(top_frame, bg='black', fg='pink', text='MineSweeper Game', font=('Arial', 60))
    game_title_bottom = tk.Label(top_frame, bg='black', fg='pink', text='Mouse Left Click --> How Many Mines nearby '
                                                                        '\n                          Mouse Right Click --> If you suspect its a mine, '
                                                                        'then Mark as Mine'
                                                                        '\n                                         To Win Find all non Mined Cells', font=('Arial', 20))
    game_title_top.place(x=utilities.width_percent(percentage=25), y=0)
    game_title_bottom.place(x=utilities.width_percent(percentage=5), y=100)
    left_frame = tk.Frame(root, bg=utilities.frame_color_left, width=utilities.width_percent(percentage=25),
                          height=utilities.height_percent(percentage=75))
    left_frame.place(x=0, y=utilities.height_percent(percentage=25))  # Y axis for left frame to stat just below tp frame
    center_frame = tk.Frame(root, bg=utilities.frame_color_center, width=utilities.width_percent(percentage=75),
                            height=utilities.height_percent(percentage=75))
    center_frame.place(x=utilities.width_percent(percentage=25), y=utilities.height_percent(percentage=25))  # Y axis for left
    # frame to start just below top frame and X axis just after left frame ends
    for my_rows in range(settings.grid_size_rows):
        for my_cols in range(settings.grid_size_columns):
            c = Cell(x=my_cols, y=my_rows)
            c.create_button_object(center_frame)
            c.cell_button_object.grid(column=my_cols, row=my_rows)
    # Call the label from the Class
    Cell.create_cell_count_label(left_frame)
    Cell.cell_count_label_object.place(x=0, y=0)
    Cell.randomize_mines()
    root.mainloop()


if __name__ == '__main__':
    draw_the_window()




