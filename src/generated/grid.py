# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

from icecream import ic

def open_txt(txt_path: str) -> str:
    with open(txt_path, "r") as file:
        return file.readlines()


def create_grid(width: int,height: int) -> list[list[int]]:
    grid = []
    for _ in range(height):
        sub_grid = []
        for _ in range(width):
            sub_grid.append(0)
        grid.append(sub_grid)
    return grid

def parse_line(line: str) -> list[int]:
    new_line = line[:-1]
    print(new_line)
    new_line = line.replace("_","0")
    new_line = list(new_line)[:-1]
    ic(new_line)
    parsed_line = []
    for letter in new_line:
        parsed_line.append(int(letter))
    return parsed_line

def parse_txt(txt_file: list[str]) -> list[list[int]]:
    parsed_txt = []
    for line in txt_file:
        parsed_txt.append(parse_line(line))
    return parsed_txt

sudoku_path = "assets/sudoku_folder/sudoku1.txt"
sudoku_txt = open_txt(sudoku_path)

ic(parse_txt(sudoku_txt))