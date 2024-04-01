import time

class SudokuSolver:
    def __init__(self, txt_path):
        self.txt_path = txt_path
        self.parsed_text = self.parse_text()
        self.clean_txt = self.remove_backslash()
        self.clean_int = self.transform_to_int(self.clean_txt)
        self.flattened_grid = self.flatten_grid(self.clean_int)

    def parse_text(self):
        with open(self.txt_path, "r") as txt_file:
            return txt_file.readlines()

    def remove_backslash(self):
        new_txt_arr = []
        for line in self.parsed_text:
            clean_line = line.replace("\n", "")
            clean_line = clean_line.replace("_", "0")
            new_txt_arr.append(clean_line)
        return new_txt_arr
    
    def transform_to_int(self, cleaned_txt):
        cleaned_int = []
        for line in cleaned_txt:
            int_line = []
            for character in line:
                int_line.append(int(character))
            cleaned_int.append(int_line)
        return cleaned_int

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

    def solve_sudoku(self):
        start_time = time.time()  # start recording
        if self.solve_sudoku_recursive(self.flattened_grid):  # call function
            end_time = time.time()  # end recording
            elapsed_time = end_time - start_time  # calcul time execution
            print("Temps d'exécution :", elapsed_time, "secondes")
            return True
        else:
            return False

    def solve_sudoku_recursive(self, grid):
        row, col = self.find_empty_location(grid)
        if row is None:
            return True
        
        for num in range(1, 10):
            if self.is_valid(grid, row, col, num):
                grid[row * 9 + col] = num
                
                if self.solve_sudoku_recursive(grid):
                    return True
                
                grid[row * 9 + col] = 0
        
        return False

if __name__ == "__main__":
    solver = SudokuSolver("Sudoku-Solver/assets/sudoku_folder/sudoku5.txt")
    
    # Resolve Sudoku
    if solver.solve_sudoku():
        print("Sudoku résolu :")
        # Print the solved Sudoku in a grid format
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                print(solver.flattened_grid[i * 9 + j], end=" ")
            print()
    else:
        print("Aucune solution trouvée.")
