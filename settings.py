""" Window size and other settings for our Game"""
width = 1520
height = 800
grid_size_columns = 6  # if 6 use cell.width =12 and cell.height =4 to fill properly
grid_size_rows = 6
grid_size = grid_size_columns * grid_size_rows
cell_count = grid_size
mined_count = int(25/100 * grid_size)
