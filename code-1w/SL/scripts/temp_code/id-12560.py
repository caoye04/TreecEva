def analyze_distribution(data, mode='even'):
    """Analyzes distribution patterns in data (distractor function)."""
    if mode == 'even':
        return sum(1 for x in data if x % 2 == 0)
    else:
        return sum(1 for x in data if x % 2 == 1)


def preprocess_grid(raw_grid):
    """Preprocess grid by normalizing values (some relevant, some not)."""
    flat = [item for row in raw_grid for item in row]
    avg = sum(flat) / len(flat)
    threshold = avg * 1.2
    
    # Distractor computation: count high/low values
    high_count = len([x for x in flat if x > threshold])
    low_count = len([x for x in flat if x < avg * 0.8])
    balance_score = (high_count - low_count) ** 2 if low_count > 0 else 0

    # Relevant transformation: normalize and cap
    normalized = [[min(max(int(x * 0.95), 1), 100) for x in row] for row in raw_grid]
    return normalized, balance_score


def calculate_stability_index(seq):
    """Calculates stability metric (mostly irrelevant)."""
    diffs = [abs(seq[i] - seq[i-1]) for i in range(1, len(seq))]
    return round(sum(diffs) / len(diffs), 3) if diffs else 0


def calculate_system_capacity(grid, thresholds):
    """Main logic to compute final capacity with moderate interference."""
    temp_grid, score = preprocess_grid(grid)
    
    # Extract edge elements (top, bottom, left, right)
    top_row = temp_grid[0]
    bottom_row = temp_grid[-1]
    left_col = [row[0] for row in temp_grid]
    right_col = [row[-1] for row in temp_grid]
    
    # Distractor: analyze edge parity distribution
    edge_values = top_row + bottom_row + left_col + right_col
    even_edges = analyze_distribution(edge_values, mode='even')
    odd_edges = len(edge_values) - even_edges
    parity_ratio = even_edges / odd_edges if odd_edges != 0 else float('inf')

    # Core logic: find constrained regions
    valid_cells = 0
    penalty_factor = 0
    for i, row in enumerate(temp_grid):
        for j, val in enumerate(row):
            # Check neighborhood constraints
            neighbors = []
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < len(temp_grid) and 0 <= nj < len(row):
                    neighbors.append(temp_grid[ni][nj])
            
            if neighbors:
                neighbor_avg = sum(neighbors) / len(neighbors)
                if val >= thresholds['min_core'] and neighbor_avg >= thresholds['min_neighbor']:
                    valid_cells += 1
                if val < thresholds['min_core'] // 2:
                    penalty_factor += 1
    
    # Secondary distractor: stability of diagonal
    main_diagonal = [temp_grid[i][i] for i in range(min(len(temp_grid), len(temp_grid[0])))]
    stability = calculate_stability_index(main_diagonal)
    
    # Final capacity calculation (key result)
    base_capacity = valid_cells * 100
    adjusted = base_capacity - (penalty_factor * 10)
    final_capacity = max(adjusted, 50)  # Minimum threshold
    
    # Irrelevant logging
    debug_info = {
        'valid': valid_cells,
        'penalty': penalty_factor,
        'stability': stability,
        'parity_ratio': parity_ratio,
        'score': score
    }
    
    return final_capacity

# Main execution
grid_data = [
    [45, 82, 33, 71, 29],
    [67, 91, 58, 44, 76],
    [38, 52, 69, 83, 41],
    [74, 39, 63, 57, 88],
    [56, 77, 42, 68, 35]
]

thresholds = {
    'min_core': 50,
    'min_neighbor': 45
}

final_capacity = calculate_system_capacity(grid_data, thresholds)
print(f"Target result: {final_capacity}")