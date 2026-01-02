def analyze_detection_areas():
    # Define sensor detection zones using sets
    sensor_coverage = {1, 2, 3, 4, 5, 6, 7}
    predicted_zones = {5, 6, 7, 8, 9, 10}

    # Calculate overlapping regions
    coverage_overlap = sensor_coverage.intersection(predicted_zones)
    
    # Auxiliary metric: total unique zones observed
    total_observed = len(sensor_coverage.union(predicted_zones))
    
    # Secondary derived value (distraction)
    missing_zones = predicted_zones - sensor_coverage
    
    # Final output variable
    result = len(coverage_overlap)
    print(f"Result: {result}")

analyze_detection_areas()