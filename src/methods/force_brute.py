def draw(puzzle):
    for r in range(len(puzzle)):
        if r == 0 or r == 3 or r == 6:
            print("+-------+-------+-------+")
        for c in range(len(puzzle[r])):
            if c == 0 or c == 3 or c ==6:
                print("| ", end = "")
            if puzzle[r][c] != 0:
                print(puzzle[r][c], end = " ")
            else:
                print(end = "  ")
            if c == 8:
                print("|")
    print("+-------+-------+-------+")
    
puzzleToSolve =  [[0, 7, 2, 9, 0, 0, 0, 3, 0],
                  [0, 0, 1, 0, 0, 6, 0, 8, 0],
                  [0, 0, 0, 0, 4, 0, 0, 6, 0],
                  [9, 6, 0, 0, 0, 4, 1, 0, 8],
                  [0, 4, 8, 7, 0, 5, 0, 9, 6],
                  [0, 0, 5, 6, 0, 8, 0, 0, 3],
                  [0, 0, 0, 4, 0, 2, 0, 1, 0],
                  [8, 5, 0, 0, 6, 0, 3, 2, 7],
                  [1, 0, 0, 8, 5, 0, 0, 0, 0]]

s = ''.join(map(str,[''.join(map(str, i)) for i in puzzleToSolve]))

print("Sudoku Problem")
draw(puzzleToSolve)
print(s)