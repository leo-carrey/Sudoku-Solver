class force_brute:
    def __init__(self, grid):
        self.grid = grid

    def validate_grid(self, grid):
        for row in range(9):
            for col in range(9):
                num = grid[row][col]
                if num != 0 and not self.is_valid_move(grid, row, col, num):
                    return False
        return True

    # Function to check if a move is valid
    def is_valid_move(self, grid, row, col, num):
        # Check if the number is not already in the row
        if num in grid[row]:
            return False

        # Check if the number is not already in the column
        if num in [grid[i][col] for i in range(9)]:
            return False

        # Check if the number is not already in the 3x3 box
        start_row = 3 * (row // 3)
        start_col = 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if grid[i][j] == num:
                    return False
        return True

    def get_empty_pos(self, sudoku_grid):
        num_pos = []
        for row in range(9):
            for col in range(9):
                num = sudoku_grid[row][col]
                if num == 0:
                    num_pos.append((row, col))
        return num_pos

    def count_limite(self, num_pos):
        count = 0
        for _ in range(len(num_pos)):
            count *= 10
            count += 9
        return count

    def start_number(self, num_pos):
        start_number_str = ""
        for _ in range(len(num_pos)):
            start_number_str += "1"
        return int(start_number_str)

    def solve_sudoku(self, sudoku_grid):
        num_pos = self.get_empty_pos(sudoku_grid)
        start_count = self.start_number(num_pos)
        end_count = self.count_limite(num_pos)
        for num in range(start_count, end_count + 1):
            new_num = list(str(num))
            for j, (row, col) in enumerate(num_pos):
                sudoku_grid[row][col] = int(new_num[j])
            if self.validate_grid(sudoku_grid):
                return sudoku_grid
