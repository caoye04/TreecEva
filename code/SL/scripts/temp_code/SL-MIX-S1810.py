import itertools
from math import gcd
from functools import reduce

class SurveyNode:
    def __init__(self, matrix):
        self.matrix = matrix
        self.next = None

def compute_lcm_of_list(numbers):
    return reduce(lambda a, b: abs(a * b) // gcd(a, b), numbers)

def get_adjacent_cells(rows, cols, r, c):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    adjacent = []
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            adjacent.append((nr, nc))
    return adjacent

def find_connected_components(matrix):
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False]*cols for _ in range(rows)]
    components = []
    
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] > 0 and not visited[r][c]:
                component = []
                stack = [(r, c)]
                while stack:
                    curr_r, curr_c = stack.pop()
                    if visited[curr_r][curr_c]:
                        continue
                    visited[curr_r][curr_c] = True
                    component.append((curr_r, curr_c))
                    for nr, nc in get_adjacent_cells(rows, cols, curr_r, curr_c):
                        if matrix[nr][nc] > 0 and not visited[nr][nc]:
                            stack.append((nr, nc))
                components.append(component)
    return components

# Initialize linked list of survey grids
grid1 = [
    [0, 5, 0, 0],
    [3, 4, 0, 2],
    [0, 0, 0, 0]
]
grid2 = [
    [1, 0, 6, 0],
    [0, 0, 7, 0],
    [8, 0, 0, 0]
]
head = SurveyNode(grid1)
head.next = SurveyNode(grid2)

# Process grids and calculate excavation volume
excavation_volume = 0
lcm_values = []

node = head
while node:
    components = find_connected_components(node.matrix)
    for component in components:
        area = len(component)
        avg_height = sum(node.matrix[r][c] for r, c in component) / area
        lcm_values.append(area)
        # Volume calculation using geometric scaling
        excavation_volume += area * avg_height * 0.5
    node = node.next

if lcm_values:
    total_lcm = compute_lcm_of_list(lcm_values)
    excavation_volume *= total_lcm / max(lcm_values)

print(f"Result: {int(excavation_volume)}")