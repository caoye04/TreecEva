def analyze_storage_efficiency(inventory_levels, layout_zones):
    efficiency_map = {}
    total_items = sum(inventory_levels)
    zone_count = len(layout_zones)
    avg_per_zone = total_items / zone_count if zone_count else 0

    for i, level in enumerate(inventory_levels):
        zone_id = layout_zones[i % len(layout_zones)]
        efficiency_map[zone_id] = level / (avg_per_zone + 1e-5)
    
    return efficiency_map


def detect_overlap_regions(primary_zones, backup_zones):
    # Irrelevant helper function - not used in final result
    primary_set = set(primary_zones)
    backup_set = set(backup_zones)
    return primary_set.intersection(backup_set)


def calculate_remaining_capacity(layout, damaged_parts):
    base_matrix = [[1 for _ in range(5)] for _ in range(5)]
    
    # Simulate damage masking
    for x, y in damaged_parts:
        if 0 <= x < 5 and 0 <= y < 5:
            base_matrix[x][y] = 0

    capacity = 0
    for row in base_matrix:
        for cell in row:
            capacity += cell
    
    return capacity * 10  # Each unit cell holds 10 units

# Main execution
inventory_data = [120, 150, 90, 200, 130]
zone_identifiers = ['A', 'B', 'C', 'D', 'E']

# Distractor: unused intermediate analysis
efficiency_results = analyze_storage_efficiency(inventory_data, zone_identifiers)

# Layout represented as coordinate tuples
warehouse_layout = [(i, j) for i in range(5) for j in range(5)]
damaged_sections = [(1, 1), (1, 3), (3, 1), (3, 3), (2, 2)]

# Extra computation with bitwise red herring
checksum = 0
for coord in warehouse_layout:
    checksum ^= (coord[0] + coord[1])  # Irrelevant to final answer

# Actual target calculation
final_capacity = calculate_remaining_capacity(warehouse_layout, damaged_sections)

# Print result as required
print(f"Target result: {final_capacity}")