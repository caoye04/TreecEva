def analyze_set_overlap():
    # Sensor coverage areas represented as sets of grid cells
    sensor_a_coverage = {1, 2, 3, 4, 5, 6, 7, 8}
    sensor_b_coverage = {5, 6, 7, 8, 9, 10, 11, 12}
    sensor_c_coverage = {8, 9, 10, 13, 14, 15}

    # Find overlapping regions between sensors
    overlap_ab = sensor_a_coverage & sensor_b_coverage
    overlap_bc = sensor_b_coverage & sensor_c_coverage
    overlap_ac = sensor_a_coverage & sensor_c_coverage

    # Critical intersection: area covered by all three sensors
    common_intersection = sensor_a_coverage & sensor_b_coverage & sensor_c_coverage

    # Filter out intersections with less than 2 cells for reliability
    valid_intersections = set()
    if len(overlap_ab) >= 2:
        valid_intersections.add('AB')
    if len(overlap_bc) >= 2:
        valid_intersections.add('BC')
    if len(overlap_ac) >= 2:
        valid_intersections.add('AC')
    if len(common_intersection) >= 1:
        valid_intersections.add('ABC')

    result = len(valid_intersections)
    print(f"Target result: {result}")

analyze_set_overlap()