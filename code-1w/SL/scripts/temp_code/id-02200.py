from itertools import product

def calculate_zone_utilization(zones):
    utilization = 0
    for zone in zones:
        if len(zone) > 2:
            utilization += sum(zone) // len(zone)
    return utilization

def detect_overloaded_sectors(grid):
    overload_count = 0
    sector_loads = []
    for row in grid:
        row_sum = sum(row)
        sector_loads.append(row_sum)
        if row_sum > 15:
            overload_count += 1
    temp_analysis = [load * 2 for load in sector_loads if load > 10]  # distractor
    return overload_count

def calculate_remaining_capacity(grid, exclusions):
    total_slots = 0
    used_slots = 0
    all_positions = list(product(range(4), range(4)))
    valid_positions = set(all_positions) - set(exclusions)
    
    # Simulate dynamic reallocation (distraction with intermediate tracking)
    reallocated = 0
    transfer_log = []
    for i, j in valid_positions:
        total_slots += 1
        if grid[i][j] > 0:
            used_slots += 1
        if grid[i][j] == 3 and i + j < 4:
            reallocated += 1
            transfer_log.append((i, j))
    
    # Secondary validation pass (semi-relevant)
    unused_excluded = 0
    for pos in exclusions:
        if 0 <= pos[0] < 4 and 0 <= pos[1] < 4 and grid[pos[0]][pos[1]] == 0:
            unused_excluded += 1
    
    efficiency_factor = calculate_zone_utilization([row for row in grid])
    overload = detect_overloaded_sectors(grid)
    
    # Core logic masked by auxiliary computations
    base_capacity = total_slots * 2
    deduction = used_slots * 3 + overload * 4 + reallocated * 2
    final_capacity = base_capacity - deduction - unused_excluded
    
    # Print result as required
    print(f"Result: {final_capacity}")
    return final_capacity

# Setup environment
warehouse_grid = [
    [1, 0, 3, 2],
    [0, 3, 1, 0],
    [2, 1, 0, 3],
    [3, 0, 2, 1]
]
blocked_positions = [(0, 1), (1, 1), (2, 3)]
initial_estimate = sum(sum(row) for row in warehouse_grid) * 2  # irrelevant baseline
auxiliary_set = set(product([0, 1], repeat=2))  # dead code path helper

# Key execution point
final_capacity = calculate_remaining_capacity(warehouse_grid, blocked_positions)