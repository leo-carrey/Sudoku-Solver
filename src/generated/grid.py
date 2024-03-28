import pygame

# pygame setup
pygame.init()
BLACK = (0, 0, 0)
WIDTH = 540
HEIGHT = 600
CELL_SIZE = WIDTH // 9
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True


# open a txt file
def open_txt(txt_path: str) -> str:
    with open(txt_path, "r") as file:
        return file.readlines()


sudoku1_path = "assets/sudoku_folder/sudoku1.txt"
sudoku1_txt = open_txt(sudoku1_path)

sudoku2_path = "assets/sudoku_folder/sudoku2.txt"
sudoku2_txt = open_txt(sudoku2_path)

sudoku3_path = "assets/sudoku_folder/sudoku3.txt"
sudoku3_txt = open_txt(sudoku3_path)

sudoku4_path = "assets/sudoku_folder/sudoku4.txt"
sudoku4_txt = open_txt(sudoku4_path)

sudoku5_path = "assets/sudoku_folder/sudoku5.txt"
sudoku5_txt = open_txt(sudoku5_path)


# trasform a list of string into a list of int
def parse_line(line: str) -> list[int]:
    new_line = line[:-1]
    new_line = line.replace("_", "0")
    new_line = list(new_line)[:-1]
    parsed_line = []
    for letter in new_line:
        parsed_line.append(int(letter))
    return parsed_line


# transform a text file into a list of lists of int
def parse_txt(txt_file: list[str]) -> list[list[int]]:
    parsed_txt = []
    for line in txt_file:
        parsed_txt.append(parse_line(line))
    return parsed_txt


# Function to draw Sudoku grid
def draw_grid(screen):
    for i in range(10):
        if i % 3 == 0:
            line_thickness = 4
        else:
            line_thickness = 1
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE),
                        (WIDTH, i * CELL_SIZE), line_thickness)
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0),
                        (i * CELL_SIZE, HEIGHT - CELL_SIZE), line_thickness)


# Function to draw numbers in Sudoku grid
def draw_numbers(screen, grid):
    font = pygame.font.Font(None, 40)
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                num_surface = font.render(str(grid[i][j]), True, BLACK)
                screen.blit(
                    num_surface, (j * CELL_SIZE + 15, i * CELL_SIZE + 10))


def draw_button(screen, text, position):
    font = pygame.font.Font(None, 30)
    button_text = font.render(text, True, BLACK)
    button_rect = button_text.get_rect(center=position)
    pygame.draw.rect(screen, (250, 0, 250), button_rect, 20)
    screen.blit(button_text, button_rect)
    return button_rect


button1_width = 60
button1_height = 580

show_solved_grid = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Check if the left mouse button is clicked
                mouse_pos = pygame.mouse.get_pos()  # Get mouse click position
                if solve_button_rect.collidepoint(mouse_pos):
                    # Load Sudoku from file
                    sudoku_grid = parse_txt(sudoku1_txt)
                    solved, solved_grid = solve_sudoku(sudoku_grid)

                    if solved:
                        show_solved_grid = True
                    else:
                        print("No solution exists!")

    sudoku_grid = parse_txt(sudoku1_txt)

    screen.fill("white")
    draw_grid(screen)

    if show_solved_grid:
        draw_numbers(screen, solved_grid) # Draw the solved grid
    else:
        draw_numbers(screen, sudoku_grid) # Draw the grid

    # Coordinates to place the button
    button_position = (button1_width, button1_height)
    solve_button_rect = draw_button(screen, "Solve", button_position)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()