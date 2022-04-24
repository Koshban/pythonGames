""" Class for drawing Cells in the MineSweeper Game
Create the Basic Cell structure , Add Text to display, and control Cell behavior
"""

from tkinter import Button, Label
import utilities
import random
import settings
import ctypes
import sys


class Cell:
    all_ms = []
    cell_count_label_object = None
    cell_count = settings.cell_count

    def __init__(self, x, y, is_mine=False):  # is_mine is to determine if its a Bomb/Mine or not
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_button_object = None
        self.x = x
        self.y = y

        Cell.all_ms.append(self)  # Append the instantiations of the object

    def __repr__(self):
        return f'Cell({self.x}, {self.y})'

    def create_button_object(self, location):
        button = Button(location, width=utilities.cell_width_size(), height=utilities.cell_height_size())
                        # text=f'{self.x, self.y}')
        button.bind('<Button-1>', self.left_click_action)
        button.bind('<Button-3>', self.right_click_action)
        self.cell_button_object = button

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(location, bg='black', fg='white', text=f'Cells  Left: {Cell.cell_count}',
                    #width=utilities.cell_width_size(), height=utilities.cell_height_size(),
                    font=('Arial', 35))
        Cell.cell_count_label_object = lbl

    def left_click_action(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:  # if 0 mines, display all the nearby cells
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
            """If mines count == number of cells left then Player Wins"""
            if Cell.cell_count == settings.mined_count:
                ctypes.windll.user32.MessageBoxW(0, 'You Won, Congrats!!', 'Game Over', 0)
                sys.exit()

        """If Cell is already Opened then cancel ability to have any other events"""
        self.cell_button_object.unbind('<Button-1>')
        self.cell_button_object.unbind('<Button-3>')

    def get_cell_by_axis(self, x, y):
        """ Return a Cell Object by values of x and y"""
        for cell in Cell.all_ms:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self):
        """  for cell 1,1 the surrounding cells will be 0,0|0,1|0,2|1,0|2,0|2,1|2,2|1,2
        for cells like 0,0 we will get None back and eliminate through the List comprehension """
        surrounding_cells = [
            self.get_cell_by_axis(x=self.x - 1, y=self.y - 1),
            self.get_cell_by_axis(x=self.x - 1, y=self.y),
            self.get_cell_by_axis(x=self.x - 1, y=self.y + 1),
            self.get_cell_by_axis(x=self.x, y=self.y - 1),
            self.get_cell_by_axis(x=self.x + 1, y=self.y - 1),
            self.get_cell_by_axis(x=self.x + 1, y=self.y),
            self.get_cell_by_axis(x=self.x + 1, y=self.y + 1),
            self.get_cell_by_axis(x=self.x, y=self.y + 1)
        ]
        surrounding_cells = [cell for cell in surrounding_cells if cell is not None]
        return surrounding_cells

    @property
    def surrounded_cells_mines_length(self):
        """ How many surrounding blocks are mined"""
        counter = 0
        for x in self.surrounded_cells:
            if x.is_mine:
                counter += 1
        return counter

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1  # Decrease the Number of Cells unopened or not showed
            self.cell_button_object.configure(text=str(self.surrounded_cells_mines_length) + " Mines Nearby")
            """ Replace text of cell count Label with newer count"""
            if Cell.cell_count_label_object:  # If its Not None i.e. within the Frame then proceed
                Cell.cell_count_label_object.configure(text=f'Cells  Left: {Cell.cell_count}')
            """ If this was marked as a Mine Candidate earlier, then on left click change it back to system color"""
            self.cell_button_object.configure(bg='SystemButtonFace')  # Default Tkinter color
        """ Mark the Cell as Opened to prevent Double Counting"""
        self.is_opened = True

    def show_mine(self):
        """ Show its a Mine and Stop the Game"""
        self.cell_button_object.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0, 'You Clicked on a Mine', 'Game Over', 0)
        sys.exit()

    def right_click_action(self, event):
        if not self.is_mine_candidate:
            self.cell_button_object.configure(bg='orange')
            self.is_mine_candidate = True
        else:
            self.cell_button_object.configure(bg='SystemButtonFace')  # Default Tkinter color
            self.is_mine_candidate = False

    @staticmethod
    def randomize_mines():
        mined_cells = random.sample(Cell.all_ms, settings.mined_count)
        for my_cells in mined_cells:
            my_cells.is_mine = True


