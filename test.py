from math import sqrt
def is_grid_square(len_grid):
    return len_grid % 9 == 0 and sqrt(len_grid) % 1 == 0

    

def transform_grid_2D(grid):
    len_grid = len(grid)
    if not is_grid_square(len_grid):
       raise 
    
    n = sqrt(len_grid)
    

