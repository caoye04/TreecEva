def preprocess_grid(grid):
    # Normalizes grid by converting all negative values to zero
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] < 0:
                grid[i][j] = 0
    return grid


def calculate_overlap(regions):
    # Calculates overlapping cells between regions (irrelevant distractor)
    overlap_count = 0
    seen_cells = set()
    for region in regions:
        for cell in region:
            if cell in seen_cells:
                overlap_count += 1
            seen_cells.add(cell)
    return overlap_count


def analyze_distribution(values):
    # Analyzes frequency distribution (dead code path)
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    sorted_vals = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [x[0] for x in sorted_vals]


def calculate_remaining_capacity(grid, blocked):
    processed = preprocess_grid([row[:] for row in grid])
    total_capacity = 0
    max_row_sum = 0
    
    # Track visited coordinates for potential expansion (not used)
    visited = set()
    
    # Simulate capacity accumulation with filtering
    for i in range(len(processed)):
        row_sum = 0
        for j in range(len(processed[i])):
            coord = (i, j)
            if coord in blocked:
                continue
            if processed[i][j] > 0:  # Only count functional units
                total_capacity += processed[i][j]
                row_sum += processed[i][j]
                visited.add(coord)
        if row_sum > max_row_sum:
            max_row_sum = row_sum
    
    # Secondary adjustment based on diagonal symmetry (semi-relevant)
    diag_sum = 0
    for i in range(len(processed)):
        if (i, i) not in blocked and i < len(processed[i]):
            diag_sum += processed[i][i]
    
    # Apply arbitrary efficiency factor (distractor computation)
    efficiency_factor = len(visited) / (len(processed) * len(processed[0]) or 1)
    dummy_score = analyze_distribution([int(efficiency_factor * 100)])
    
    # Final capacity adjusted by diagonal contribution
    final_capacity = total_capacity - diag_sum
    
    # Irrelevant string transformation (pure distraction)
    status_msg = "Capacity analysis complete"
    status_upper = status_msg.upper().replace(" ", "_")
    log_entry = f"{status_upper}: {final_capacity} units"
    
    return final_capacity

# Initialize warehouse layout (simulated storage unit capacities)
warehouse_grid = [
    [8, -2, 5, 3],
    [4, 0, -1, 7],
    [2, 6, 9, -3],
    [-4, 5, 1, 8]
]

# Define blocked positions due to maintenance
blocked_positions = {(0, 1), (1, 2), (3, 0), (2, 3)}

# Compute overlapping regions (distractor call - not used in final result)
regions = [[(0,0), (0,1)], [(0,1), (1,1)], [(1,1), (1,2)]]
overlap = calculate_overlap(regions)

# Main execution point
final_capacity = calculate_remaining_capacity(warehouse_grid, blocked_positions)
print(f"Result: {final_capacity}")