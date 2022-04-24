""" Setup configurable Window panes utilities"""
import settings

frame_color_top = 'black'
frame_color_left = 'black'
frame_color_center = 'black'


def height_percent(percentage: int) -> int:
    return int((settings.height / 100) * percentage)


def width_percent(percentage: int) -> int:
    return int((settings.width / 100) * percentage)


def cell_width_size() -> int:
    return int(settings.width * 75/100 * 1/settings.grid_size_columns * 1/8)


def cell_height_size() -> int:
    return int(settings.height * 75/100 * 1/settings.grid_size_rows * 1/19)
