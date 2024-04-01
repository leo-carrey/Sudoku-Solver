import time
from math import sqrt

class SudokuSolver:
    def flatten_grid(self, grid):
        flattened_grid = []
        for sublist in grid:
            for num in sublist:
                flattened_grid.append(num)
        return flattened_grid

    def find_empty_location(self, grid):
        for empty_box in range(81):
            if grid[empty_box] == 0:
                return empty_box // 9, empty_box % 9
        return None, None

    def is_valid(self, grid, row, col, number):
        # Check if the number is present in the row
        for x in range(9):
            row_start_index = row * 9
            cell_index = row_start_index + x
            cell_value = grid[cell_index]
            if cell_value == number:
                return False
        
        # Check if the number is present in the column
        for x in range(9):
            col_start_index = col
            cell_index = col_start_index + x * 9
            cell_value = grid[cell_index]
            if cell_value == number:
                return False
        
        # Check if the number is present in the 3x3 square
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if grid[(i + start_row) * 9 + (j + start_col)] == number:
                    return False
        
        return True
    
    
    def is_grid_square(self, len_grid):
        return len_grid % 9 == 0 and sqrt(len_grid) % 1 == 0

    def transform_grid_2D(self, grid):
        len_grid = len(grid)
        if not self.is_grid_square(len_grid):
            raise 
        
        total = len(grid)
        size = int(sqrt(total))
        result = []
        for i in range(0, total, size):
            result.append(grid[i:i + size])
        return result


    def solve_sudoku(self, grid):
        flattened_grid = self.flatten_grid(grid)
        start_time = time.time()  # start recording
        if solved_grid := self.solve_sudoku_recursive(flattened_grid):  # call function
            end_time = time.time()  # end recording
            elapsed_time = end_time - start_time  # calcul time execution
            print("Temps d'exécution :", elapsed_time, "secondes")
            final_grid = self.transform_grid_2D(solved_grid)
            return True, final_grid
        else:
            return False, final_grid

    def solve_sudoku_recursive(self, grid):
        row, col = self.find_empty_location(grid)
        if row is None:
            return True
        
        for num in range(1, 10):
            if self.is_valid(grid, row, col, num):
                grid[row * 9 + col] = num
                
                if self.solve_sudoku_recursive(grid):
                    return grid
                
                grid[row * 9 + col] = 0
        
        return False

