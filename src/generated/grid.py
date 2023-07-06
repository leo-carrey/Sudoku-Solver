
def get_sudoku(file_name):
    return open(f"assets/sudoku_folder/{file_name}").read().split()


def print_grid(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j], end=""),
        print()

def replace_to_0(arr):
    new_arr =  []
    new_sub_arr = []
    for row in range(9):
        for column in range(9):
            if arr[row][column] == "_":
                new_sub_arr.append(0)
            else:
                new_sub_arr.append(int(arr[row][column]))
        new_arr.append(new_sub_arr) 
        new_sub_arr = []
    return new_arr


