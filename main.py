from src.generated.grid import Display_interface
from src.methods.Backtracking import SudokuSolver
from src.methods.force_brute import Force_brute

def main():
    Backtracking = SudokuSolver()
    Brute_Force = Force_brute()
    DisplayInterface = Display_interface()
    DisplayInterface.run(Backtracking.solve_sudoku)


if __name__ == "__main__":
    main()
