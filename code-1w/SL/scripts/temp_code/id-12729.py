def analyze_sensor_overlap():
    sensor_a_coverage = {12.5, 15.0, 18.7, 20.1, 22.3, 25.6}
    sensor_b_coverage = {15.0, 17.2, 20.1, 23.8, 25.6, 27.9}
    
    # Calculate intersection and symmetric difference
    intersection = sensor_a_coverage & sensor_b_coverage
    symmetrical_difference = sensor_a_coverage ^ sensor_b_coverage
    
    # Extract key metrics
    intersection_max = max(intersection) if intersection else 0
    symmetrical_difference_avg = sum(symmetrical_difference) / len(symmetrical_difference) if symmetrical_difference else 0
    
    # Final decision metric based on conservative estimate
    result = min(symmetrical_difference_avg, intersection_max)
    
    # Irrelevant logging (minimal distraction)
    readings_count = len(sensor_a_coverage) + len(sensor_b_coverage)
    average_reading = (sum(sensor_a_coverage) + sum(sensor_b_coverage)) / readings_count
    
    print(f"Result: {result}")

analyze_sensor_overlap()