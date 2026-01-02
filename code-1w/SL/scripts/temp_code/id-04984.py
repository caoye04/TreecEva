def analyze_sensor_overlap():
    # Simulate sensor readings from two monitoring systems
    system_a_readings = {12, 25, 34, 47, 56, 63, 72, 88, 91}
    system_b_readings = {25, 33, 47, 59, 63, 77, 88, 101}

    # Find common detections between both systems
    common_elements = system_a_readings.intersection(system_b_readings)

    # External calibration set with expected valid outputs
    potential_set = {25, 47, 63, 88, 95, 99}

    # Filter only those readings that are both common and within expected range
    final_overlap = common_elements.intersection(potential_set)

    # Irrelevant auxiliary variable (minimal distraction for intervention level 5)
    calibration_score = sum(potential_set) // len(potential_set)

    # Result output
    print(f"Target result: {len(final_overlap)}")

analyze_sensor_overlap()