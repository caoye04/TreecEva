from itertools import product


def calculate_load(x, y):
    # Irrelevant helper function that computes a transformed coordinate load
    return (x ** 2 + y) % 13

def calculate_peak(grid, bounds):
    max_sum = 0
    temp_buffer = []
    
    for i in range(bounds[0]):
        row_total = 0
        for j in range(bounds[1]):
            # Relevant computation: accumulate diagonal elements
            if i == j:
                row_total += grid[i][j] * 2
            # Distractor: store side calculations not used later
            load_val = calculate_load(i, j)
            temp_buffer.append(load_val)
        if row_total > max_sum:
            max_sum = row_total
    
    # Semi-relevant transformation: scale by factor derived from bounds
    adjustment_factor = (bounds[0] + bounds[1]) // 4
    max_sum += adjustment_factor
    
    # Dead code path: never executed due to fixed condition, but looks plausible
    if len(temp_buffer) < 0:
        cleanup = [x for x in temp_buffer if x > 5]
        max_sum -= sum(cleanup)
    
    return max_sum

# Initialize simulation grid with meaningful data
grid = [
    [3, 1, 4, 2],
    [5, 7, 1, 8],
    [3, 9, 6, 2],
    [1, 4, 1, 5]
]

# Define operational bounds
bounds = (4, 4)

# Track auxiliary metrics (distractor variables)
current_phase = "diagnostic"
phase_code = hash(current_phase) % 100
baseline_score = 0
for coords in product(range(2), repeat=2):
    baseline_score += grid[coords[0]][coords[1]]

# Key computational step
peak_capacity = calculate_peak(grid, bounds)

# Print result for evaluation
print(f"Result: {peak_capacity}")