def compute_overlap():
    # Define geographic regions as sets of grid cells
    region_a_coords = [101, 102, 103, 104, 105, 106]
    region_b_coords = [103, 104, 105, 107, 108]

    # Threshold for minimum coverage (irrelevant to final result)
    min_coverage_threshold = 3

    # Convert to sets for intersection operation
    region_a_set = set(region_a_coords)
    region_b_set = set(region_b_coords)

    # Compute overlapping grid cells between regions
    coverage_overlap = region_a_set & region_b_set

    # Secondary metric: total unique cells (distractor)
    all_covered_cells = region_a_set | region_b_set
    total_area = len(all_covered_cells)

    # Return size of overlap as integer result
    return len(coverage_overlap)

result = compute_overlap()
print(f"Result: {result}")