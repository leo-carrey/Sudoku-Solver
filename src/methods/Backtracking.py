def parse_text(txt_path: str) -> list[str]:
    with open(txt_path, "r") as txt_file:
        return txt_file.readlines()

def remove_backslash(txt_file: list[str]) -> list[str]:
    new_txt_arr = []
    for line in txt_file:
        clean_line = line.replace("\n", "")
        clean_line = clean_line.replace("_", "0")
        new_txt_arr.append(clean_line)
    return new_txt_arr
    
def transform_to_int(cleaned_txt):   # Convert str in int
    cleaned_int = []
    for line in cleaned_txt:
        int_line = []
        for character in line:
            int_line.append(int(character))
        cleaned_int.append(int_line) #transform each character in integers
    return cleaned_int

def find_empty_location(grid):
    for empty_box in range(81):
        if grid[empty_box] == 0:
            return empty_box // 9, empty_box % 9
    return None, None

def is_valid(grid, row, col, number):
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

def solve_sudoku(grid):
    row, col = find_empty_location(grid)
    if row is None:
        return True
    
    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row * 9 + col] = num
            
            if solve_sudoku(grid):
                return True
            
            grid[row * 9 + col] = 0
    
    return False

if __name__ == "__main__":
    txt_path = "Sudoku-Solver/assets/sudoku_folder/sudoku1.txt"
    parsed_text = parse_text(txt_path)
    cleaned_txt = remove_backslash(parsed_text)
    
    cleaned_int = transform_to_int(cleaned_txt)
    
    # Flatten the 2D list into a 1D list
    flattened_grid = [num for sublist in cleaned_int for num in sublist]
    
    # Resolve Sudoku
    if solve_sudoku(flattened_grid):
        print("Sudoku résolu :")
        # Print the solved Sudoku in a grid format
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                print(flattened_grid[i * 9 + j], end=" ")
            print()
    else:
        print("Aucune solution trouvée.")
