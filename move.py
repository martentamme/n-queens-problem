class Move:

    def __init__(self, col: int, new_row: int):
        self.col = col
        self.new_row = new_row

    def get_col(self):
        return self.col

    def get_new_row(self):
        return self.new_row
