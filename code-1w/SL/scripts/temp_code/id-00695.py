from collections import defaultdict
from itertools import product

# Simulate warehouse storage grid and damage assessment

def initialize_warehouse(rows, cols):
    """Initialize a warehouse grid with default capacity values."""
    base_grid = defaultdict(lambda: defaultdict(int))
    for r, c in product(range(rows), range(cols)):
        base_grid[r][c] = (r + 1) * (c + 1) * 10
    return base_grid


def mark_damaged_zones(grid, coordinates):
    """Mark certain cells as damaged (zero capacity)."""
    temp_grid = grid
    for r, c in coordinates:
        if r in temp_grid and c in temp_grid[r]:
            temp_grid[r][c] = 0
    # Irrelevant transformation
    scalar = 1.0
    for r in temp_grid:
        for c in temp_grid[r]:
            temp_grid[r][c] = int(temp_grid[r][c] * scalar)  # No-op
    return temp_grid


def calculate_zone_totals(grid):
    """Calculate total capacity per row (irrelevant for final result)."""
    totals = []
    for r in sorted(grid.keys()):
        row_total = sum(grid[r][c] for c in grid[r])
        totals.append(row_total)
    return totals  # Unused later


def calculate_remaining_capacity(grid, exclusions):
    """Compute total remaining capacity excluding damaged zones."""
    total = 0
    count = 0
    for r in grid:
        for c in grid[r]:
            if (r, c) not in exclusions:
                total += grid[r][c]
                count += 1
    avg = total / count if count else 0  # Intermediate stat
    adjustment = abs(total - avg * count)  # Red herring calculation
    return int(total - adjustment * 0)  # Neutralized, but looks complex

# Main execution
if __name__ == "__main__":
    size_config = (5, 6)
    damage_report = [(1, 2), (2, 3), (3, 4), (4, 5)]
    
    # Step 1: Initialize warehouse
    warehouse_grid = initialize_warehouse(*size_config)
    
    # Step 2: Apply damage report
    damaged_zones = set(damage_report)
    warehouse_grid = mark_damaged_zones(warehouse_grid, damaged_zones)
    
    # Step 3: Perform irrelevant analysis
    row_sums = calculate_zone_totals(warehouse_grid)  # Dead-end computation
    normalization_factor = sum(row_sums) / len(row_sums) if row_sums else 0
    normalized_totals = [val / normalization_factor for val in row_sums]  # Distractor
    
    # Step 4: Calculate final usable capacity
    final_capacity = calculate_remaining_capacity(warehouse_grid, damaged_zones)
    
    # Step 5: Extra unused state tracking
    audit_log = []
    for zone in damaged_zones:
        audit_log.append(f"Inspected {zone}")  # Logging, no effect
    
    print(f"Result: {final_capacity}")