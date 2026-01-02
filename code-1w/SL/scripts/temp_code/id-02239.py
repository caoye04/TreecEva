def compute_sensor_overlap():
    # Define two sensor detection areas as sets of grid coordinates
    sensor_area_a = set()
    sensor_area_b = set()

    # Populate area A: rectangular region (0,0) to (4,4)
    for x in range(5):
        for y in range(5):
            sensor_area_a.add((x, y))

    # Populate area B: diagonal band with offset
    for i in range(3, 8):
        sensor_area_b.add((i-3, i-1))  # Points: (0,2), (1,3), (2,4), (3,5), (4,6)

    # Compute overlap between the two sensor regions
    coverage_overlap = sensor_area_a.intersection(sensor_area_b)
    
    # Secondary metric: efficiency ratio (irrelevant to main answer but adds context)
    total_detected = len(sensor_area_a) + len(sensor_area_b)
    efficiency_ratio = total_detected / (len(coverage_overlap) + 1)  # Avoid division by zero

    # Output target result
    print(f"Result: {len(coverage_overlap)}")

compute_sensor_overlap()