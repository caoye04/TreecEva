def calculate_region_overlap():
    regions_a = {1, 2, 3, 5, 8, 13, 21}
    regions_b = {2, 3, 6, 8, 12, 21}
    regions_c = {10, 11, 12}  # Irrelevant set for minor distraction
    
    coverage_overlap = len(regions_a & regions_b)
    
    total_unique = len(regions_a | regions_b)
    
    return coverage_overlap

result = calculate_region_overlap()
print(f"Target result: {result}")