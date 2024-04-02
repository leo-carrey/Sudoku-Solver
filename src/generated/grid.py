import pygame

class Display_interface():
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
        self.current_grid_index = 0  # Keep track of the current grid
        self.sudoku_files = [
            "assets/sudoku_folder/sudoku1.txt",
            "assets/sudoku_folder/sudoku2.txt",
            "assets/sudoku_folder/sudoku3.txt",
            "assets/sudoku_folder/sudoku4.txt",
            "assets/sudoku_folder/sudoku5.txt"
        ]
        self.sudoku_grids = [self.parse_txt(self.open_txt(file)) for file in self.sudoku_files]
        self.sudoku_grid = self.sudoku_grids[self.current_grid_index]  # Start with the first sudoku
        

    def open_txt(self, txt_path):
        with open(txt_path, "r") as file:
            return file.readlines()
        
    def parse_txt(self, txt_file):
        grid = []
        for line in txt_file:
            # Remove newline characters and replace placeholders
            line = line.strip().replace('_', '0')
            # Convert each character in the line to an integer
            row = [int(char) for char in line]
            grid.append(row)
        return grid

    def swap_sudoku_grid(self):
        self.current_grid_index = (self.current_grid_index + 1) % len(self.sudoku_grids)
        self.sudoku_grid = self.sudoku_grids[self.current_grid_index]
        self.show_solved_grid = False  # Reset to show unsolved grid
        
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

    def run(self, methods):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()
                        if self.solve_button_rect.collidepoint(mouse_pos):
                            solved, solved_grid = methods(self.sudoku_grid)
                            if solved:
                                self.show_solved_grid = True
                            else:
                                print("No solution exists!")
                        elif self.swap_button_rect.collidepoint(mouse_pos):
                            self.swap_sudoku_grid()

            self.screen.fill("white")
            self.draw_grid()

            if self.show_solved_grid:
                self.draw_numbers(solved_grid)
            else:
                self.draw_numbers(self.sudoku_grid)

            self.solve_button_rect = self.draw_button("Solve", (60, 580))
            self.swap_button_rect = self.draw_button("Swap", (150, 580))  # Add the swap button

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        
