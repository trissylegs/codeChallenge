class Table:
    def __init__(self, width: int, height: int):
        if width <= 0:
            raise ValueError(f"width must be greater than 0. (width = {width})")
        if height <= 0:
            raise ValueError(f"height must be greater than 0. (height = {height})")
        self.width = width
        self.height = height

    def new_position(self, x: int, y: int, dx: int, dy: int):
        new_x = x + dx
        new_y = y + dy
        if not(0 <= new_x < self.width):
            new_x = x
        if not(0 <= new_y < self.height):
            new_y = y
        return new_x, new_y
