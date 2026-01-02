def analyze_sensor_readings():
    raw_readings = [105, 23, 78, 91, 44, 67, 83, 50, 72, 60, 55, 41, 88, 39, 77]
    
    # Irrelevant transformation: temperature normalization (not used in final result)
    normalized_temps = [round((temp - 32) * 5/9, 2) for temp in raw_readings]
    avg_normalized = sum(normalized_temps) / len(normalized_temps)
    
    # Key processing steps
    outlier_threshold = 85
    high_readings = [x for x in raw_readings if x > outlier_threshold]
    low_readings = [x for x in raw_readings if x <= 50]
    
    # Simulate data calibration offset (semi-relevant but ultimately unused)
    calibrated_low = [val + 5 for val in low_readings if val < 45]
    
    # Core logic with slicing and filtering
    sorted_readings = sorted(raw_readings, reverse=True)
    middle_slice = sorted_readings[3:-3]  # Trim highest and lowest extremes
    
    # Boolean filtering: valid readings are even numbers in the middle range
    valid_readings = [v for v in middle_slice if v % 2 == 0]
    
    # Destructuring assignment (unpacking)
    first_valid, *rest_valid = valid_readings
    
    # Set operations to remove duplicates (though none exist, demonstrates idiom)
    unique_valid = list(set(valid_readings))
    unique_valid.sort(reverse=True)  # Restore order
    
    # Final filtering based on conditional rule
    filtered_data = [num for num in unique_valid if num > first_valid - 20]
    
    # Target computation
    filtered_sum = sum(filtered_data)
    
    # Dead code path - misleading accumulation
    cumulative_total = 0
    for reading in raw_readings:
        if reading % 7 == 0:
            cumulative_total += reading  # Unused in result
    
    # Print required output
    print(f"Result: {filtered_sum}")

analyze_sensor_readings()