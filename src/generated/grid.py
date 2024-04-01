import pygame

class Display_interface:
    def __init__(self):
        pygame.init()
        self.BLACK = (0, 0, 0)
        self.WIDTH = 540
        self.HEIGHT = 600
        self.CELL_SIZE = self.WIDTH // 9
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.show_solved_grid = False
        self.sudoku1_txt = self.open_txt("assets/sudoku_folder/sudoku1.txt")
        self.sudoku2_txt = self.open_txt("assets/sudoku_folder/sudoku2.txt")
        self.sudoku3_txt = self.open_txt("assets/sudoku_folder/sudoku3.txt")
        self.sudoku4_txt = self.open_txt("assets/sudoku_folder/sudoku4.txt")
        self.sudoku5_txt = self.open_txt("assets/sudoku_folder/sudoku5.txt")


    def open_txt(self, txt_path):
        with open(txt_path, "r") as file:
            return file.readlines()

    def parse_line(self, line: str) -> list[int]:
        new_line = line[:-1]
        new_line = line.replace("_", "0")
        new_line = list(new_line)[:-1]
        parsed_line = []
        for letter in new_line:
            parsed_line.append(int(letter))
        return parsed_line

    def parse_txt(self, txt_file: list[str]) -> list[list[int]]:
        parsed_txt = []
        for line in txt_file:
            parsed_txt.append(self.parse_line(line))
        return parsed_txt

    def draw_grid(self):
        for i in range(10):
            if i % 3 == 0:
                line_thickness = 4
            else:
                line_thickness = 1
            pygame.draw.line(self.screen, self.BLACK, (0, i * self.CELL_SIZE),
                            (self.WIDTH, i * self.CELL_SIZE), line_thickness)
            pygame.draw.line(self.screen, self.BLACK, (i * self.CELL_SIZE, 0),
                            (i * self.CELL_SIZE, self.HEIGHT - self.CELL_SIZE), line_thickness)

    def draw_numbers(self, grid):
        font = pygame.font.Font(None, 40)
        for i in range(9):
            for j in range(9):
                if grid[i][j] != 0:
                    num_surface = font.render(str(grid[i][j]), True, self.BLACK)
                    self.screen.blit(
                        num_surface, (j * self.CELL_SIZE + 15, i * self.CELL_SIZE + 10))

    def draw_button(self, text, position):
        font = pygame.font.Font(None, 30)
        button_text = font.render(text, True, self.BLACK)
        button_rect = button_text.get_rect(center=position)
        pygame.draw.rect(self.screen, (250, 0, 250), button_rect, 20)
        self.screen.blit(button_text, button_rect)
        return button_rect

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()
                        if self.solve_button_rect.collidepoint(mouse_pos):
                            sudoku_grid = self.parse_txt(self.sudoku1_txt)  # Assuming always the first sudoku
                            solved, solved_grid = self.solve_sudoku(sudoku_grid)
                            if solved:
                                self.show_solved_grid = True
                            else:
                                print("No solution exists!")

            self.screen.fill("white")
            self.draw_grid()

            if self.show_solved_grid:
                self.draw_numbers(solved_grid)
            else:
                self.draw_numbers(sudoku_grid)

            button_position = (60, 580)
            self.solve_button_rect = self.draw_button("Solve", button_position)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
