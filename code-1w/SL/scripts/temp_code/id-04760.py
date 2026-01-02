def analyze_coverage():
    sensor_a_regions = {1, 2, 3, 4, 5, 6}
    sensor_b_regions = {4, 5, 6, 7, 8, 9}
    sensor_c_regions = {2, 4, 6, 8, 10}

    # Union of all regions covered by sensors B and C
    combined_b_c = sensor_b_regions.union(sensor_c_regions)

    # Find regions covered by both A and (B or C)
    common_regions = sensor_a_regions.intersection(combined_b_c)

    # Count how many regions are jointly covered by A and at least one of B or C
    overlap_count = len(common_regions)

    # Irrelevant tracking variable (minimal interference)
    total_unique_regions = len(sensor_a_regions | sensor_b_regions | sensor_c_regions)

    print(f"Target result: {overlap_count}")

analyze_coverage()