from generated.grid import *

class Solver:
    def __init__(self, grid) -> int:
        self.grid = grid

    def check_row(self, row, num):
        for i in range(9):
            if self.grid[row][i] == num:
                return False

    def check_column(self, col, num):
        for i in range(9):
            if self.grid[i][col] == num:
                return False
        return True

    def check_small_grid(self, row: int, col: int, num: int):
        first_index_row_box = row // 3
        first_index_col_box = col // 3
        for i in range(3):
            for j in range(3):
                if self.grid[first_index_row_box + i][first_index_col_box + j] == num:
                    return False
        return True

    def check_no_zero(self) -> bool:
        for row in self.grid:
            for col in row:
                if col == 0:
                    return False
        return True

    # def is_solved(self):
    #     for row in range(9):
    #         for col in range(9):
    #             if (
    #                 self.check_row()
    #                 and self.check_column()
    #                 and self.check_small_grid()
    #                 and self.check_no_zero()
    #             ):
    #                 return True

    def is_box_valid(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    for num in range(1, 10):
                        if (
                            self.check_row(row, num)
                            and self.check_column(col, num)
                            and self.check_small_grid(row, col, num)
                        ):
                            self.grid[row][col] = num
                            print_grid(self.grid)
    
    def get(self):
        print(self.grid)



solver = Solver(replace_to_0(get_sudoku("sudoku1.txt")))
solver.is_box_valid()