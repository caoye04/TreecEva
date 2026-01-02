from collections import defaultdict
from itertools import combinations

# Simulate a thermal fusion process in a grid-based reactor core
def initialize_reactor_grid(size, base_temp):
    grid = defaultdict(lambda: base_temp)
    for i in range(size):
        for j in range(size):
            grid[(i, j)] = base_temp + (i * j) % 7
    return grid

# Identify unstable cells based on neighbor variance
def find_unstable_cells(grid, size, variance_threshold=4.0):
    unstable = []
    for i in range(size):
        for j in range(size):
            neighbors = [grid[(i + dx, j + dy)] for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)] if (i+dx, j+dy) in grid]
            if neighbors:
                mean_neighbor = sum(neighbors) / len(neighbors)
                variance = sum((x - mean_neighbor) ** 2 for x in neighbors) / len(neighbors)
                if variance > variance_threshold:
                    unstable.append((i, j))
    return unstable

# Calculate effective thermal capacity considering fusion chains
def calculate_thermal_capacity(grid, threshold):
    size = int(len(grid) ** 0.5)
    fusion_matrix = [[0] * size for _ in range(size)]
    
    # Build fusion interaction matrix
    for i in range(size):
        for j in range(size):
            cell_val = grid[(i, j)]
            neighbor_vals = [grid[(i + dx, j + dy)] for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)] if (i+dx, j+dy) in grid]
            if neighbor_vals:
                max_neighbor = max(neighbor_vals)
                stability_score = abs(cell_val - max_neighbor) / (max_neighbor + 1e-8)
                fusion_matrix[i][j] = cell_val if stability_score < 0.6 else max_neighbor
    
    # Compute cumulative fusion yield
    total_yield = 0.0
    active_sites = 0
    for row in fusion_matrix:
        for val in row:
            if val > threshold:
                total_yield += val * 0.85
                active_sites += 1
    
    # Dummy calculations to increase interference (distractors)
    avg_yield_per_site = total_yield / active_sites if active_sites else 0
    redundancy_check = sum(1 for row in fusion_matrix for x in row if x > 0 and x < threshold)
    consistency_metric = len([c for c in combinations([1,2,3,4], 2) if c[1] - c[0] > 1])  # Irrelevant use of itertools
    
    # Final capacity determined by scaled total yield
    thermal_capacity = int(total_yield - redundancy_check * 0.5)  # Core answer computation
    
    # More irrelevant state tracking
    diagnostic_log = defaultdict(int)
    diagnostic_log['scans'] += 1
    diagnostic_log['anomalies'] = redundancy_check
    
    return thermal_capacity

# Main execution flow
if __name__ == "__main__":
    reactor_size = 5
    base_temperature = 23
    safety_threshold = 28
    
    core_grid = initialize_reactor_grid(reactor_size, base_temperature)
    unstable_positions = find_unstable_cells(core_grid, reactor_size, variance_threshold=3.5)
    
    # Introduce minor corrections for instability (not affecting final thermal capacity logic)
    for pos in unstable_positions:
        core_grid[pos] = base_temperature + 5  # Stabilization pulse
    
    thermal_capacity = calculate_thermal_capacity(core_grid, safety_threshold)
    
    # Output result as required
    print(f"Result: {thermal_capacity}")