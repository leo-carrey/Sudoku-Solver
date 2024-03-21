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


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # display grid and number in grid
    draw_grid(screen)
    draw_numbers(screen, parse_txt(sudoku1_txt))

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    clock.tick(60)  

pygame.quit()
