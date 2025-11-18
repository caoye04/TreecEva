from functools import reduce
from math import gcd

def compute_visibility(grid, watcher_pos):
    rows, cols = len(grid), len(grid[0])
    visible = set()
    wx, wy = watcher_pos
    
    # Check all positions in the grid
    for i in range(rows):
        for j in range(cols):
            if (i, j) == (wx, wy):
                continue
            dx, dy = j - wy, i - wx
            if dx == 0 and dy == 0:
                continue
            
            # Reduce direction vector to simplest form
            g = gcd(abs(dx), abs(dy))
            if g == 0:
                g = 1
            step_x, step_y = dx // g, dy // g
            
            # Walk along the line of sight
            clear_path = True
            x, y = wy + step_x, wx + step_y
            while 0 <= x < cols and 0 <= y < rows and (y, x) != (i, j):
                if grid[y][x] > grid[wx][wy]:
                    clear_path = False
                    break
                x += step_x
                y += step_y
            
            if clear_path:
                visible.add((i, j))
    return visible

# Grid representing elevations
plot_elevations = [
    [10, 15, 20, 10],
    [12, 14, 18, 16],
    [11, 13, 19, 17],
    [9,  16, 21, 12]
]

watcher_position = (1, 1)
visible_zones = len(compute_visibility(plot_elevations, watcher_position))
print(f"Result: {visible_zones}")