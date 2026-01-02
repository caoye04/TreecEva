def calculate_sensor_coverage():
    sensor_range = 8
    base_position = 3
    target_zone = set(range(10, 25))

    # Calculate positions covered by sensor
    coverage_start = base_position - sensor_range // 2
    coverage_end = base_position + sensor_range // 2
    unique_positions = set(range(coverage_start, coverage_end))

    # Irrelevant debug variable (minimal distraction)
    debug_mode = False

    # Key computation
    coverage_score = len(unique_positions.intersection(target_zone))
    
    # Print result as required
    print(f"Target result: {coverage_score}")

    return coverage_score

# Execute function
calculate_sensor_coverage()