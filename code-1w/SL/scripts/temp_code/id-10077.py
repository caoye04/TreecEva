def calculate_remaining_capacity(grid, restrictions):
    total_cells = len(grid) * len(grid[0])
    blocked_count = 0

    # Analyze restricted zones using set operations
    restriction_set = set(tuple(zone) for zone in restrictions)
    temp_analysis = [z for z in restrictions if sum(z) > 3]  # Irrelevant filtering

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) in restriction_set:
                blocked_count += 1
                grid[i][j] = False  # Mark as unavailable
            elif i == j:
                grid[i][j] = True  # Diagonal heuristic (semi-relevant)
            else:
                grid[i][j] = bool((i + j) % 2)  # Pattern fill (partially relevant)

    # Simulate capacity adjustment with conditional expression
    base_capacity = total_cells - blocked_count
    overflow_buffer = 10 if base_capacity > 50 else 5
    maintenance_reserve = 7 if any(len(row) > 5 for row in grid) else 3

    # Secondary scan: count uppercase-like labels (distractor logic)
    label_series = [chr(65 + i) for i in range(len(grid))]  # A, B, C...
    letter_sum = sum(ord(c) for c in label_series)  # Dead computation

    # Final capacity calculation with conditional expression
    adjusted_utilization = base_capacity * 0.9 if blocked_count > 0 else base_capacity
    final_capacity = int(adjusted_utilization - maintenance_reserve + overflow_buffer)

    return final_capacity


# Initialize warehouse layout (8x8 grid)
warehouse_grid = [[None for _ in range(8)] for _ in range(8)]
blocked_zones = [(0, 1), (1, 3), (2, 5), (3, 7), (4, 0), (5, 2), (6, 4), (7, 6)]

# Redundant character frequency analysis (distractor)
text_reference = "inventory_flow_8x8"
char_count = {c: text_reference.count(c) for c in set(text_reference)}
case_adjusted_keys = ''.join(c.upper() if c.islower() else c for c in text_reference)

# Execute main logic
final_capacity = calculate_remaining_capacity(warehouse_grid, blocked_zones)
print(f"Result: {final_capacity}")