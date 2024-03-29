import pprint

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

def divide_into_nine_list(cleaned_int):    # Divide each line into 9 lists
    divided_list = []           # New list to store other lists
    for newlist in range(0, len(cleaned_int), 9): # Loop from 0 to 9
        sublist = cleaned_int[newlist:newlist+9]        # Extract list one by one
        divided_list.append(sublist) 
    return divided_list

def identify_column(divided_list):
    columns = []
    for sublist in divided_list:
        columns.append(sublist[0])  # Add the first element of the list
        for index in sublist[1:]:  # Iterate over the next elements of the list
            columns.append(index)
    return columns

def identify_grid(divided_list):
    grids = []
    for i in range(0, 9, 3):  # Loop to increase grid 3x3 by 3
        for j in range(0, 9, 3):
            grid = []
            for k in range(3):  # Loop to extract each row from grid
                if i + k < len(divided_list):  # Check if row index is valid
                    for l in range(3):
                        if j + l < len(divided_list[i + k]):  # Check if column index is valid
                            grid.append(divided_list[i + k][j + l])
            grids.append(grid)
    return grids

def find_empty_location(grid, l):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                l[0] = row
                l[1] = col
                return True
    return False

def is_valid(new_text_arr, sublist, columns, number):
    # Check if the number is present in the row
    for x in range(9):
        if new_text_arr[sublist][x] == number:
            return False
    
    # Check if the number is present in the column
    for x in range(9):
        if new_text_arr[x][columns] == number:
            return False
    
    # Check if the number is present in the 3x3 square
    start_row = sublist - sublist % 3
    start_col = columns - columns % 3
    for i in range(3):
        for j in range(3):
            if new_text_arr[i + start_row][j + start_col] == number:
                return False
    
    return True

def find_empty_location(grid, l):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                l[0] = row
                l[1] = col
                return True
    return False

def solve_sudoku(new_text_arr):
    l = [0, 0]
    if not find_empty_location(new_text_arr, l):
        return True
    
    row, col = l[0], l[1]
    
    for num in range(1, 10):
        if is_valid(new_text_arr, row, col, num):
            new_text_arr[row][col] = num
            
            if solve_sudoku(new_text_arr):
                return True
            
            new_text_arr[row][col] = 0
    
    return False

if __name__ == "__main__":
    txt_path = "Sudoku-Solver/assets/sudoku_folder/sudoku2.txt"
    parsed_text = parse_text(txt_path)
    cleaned_txt = remove_backslash(parsed_text)
    
    cleaned_int = transform_to_int(cleaned_txt)
    divided_list = divide_into_nine_list(cleaned_int)
    columns = identify_column(divided_list)
    grids = identify_grid(divided_list)

    
    # Resolve Sudoku
    if solve_sudoku(divided_list):
        print("Sudoku résolu :")
        pprint.pprint(divided_list)
    else:
        print("Aucune solution trouvée.")
