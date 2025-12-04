def process_engineering_data(sensor_readings):
    # Filter valid readings (distractor: unused in final calculation)
    valid_readings = [x for x in sensor_readings if x > 5]
    reading_sum = sum(valid_readings)  # Distractor operation
    
    # Process main data with enumerate
    data_points = [12, 8, 15, 6, 20, 3, 18]
    processed_values = []
    for idx, value in enumerate(data_points):
        if value > 10:
            processed_values.append(value * 2)
        else:
            processed_values.append(value + 5)
    
    # Apply correction factors (partial distractor)
    correction_factors = [1, 2, 1, 2, 1, 2, 1]
    corrected_data = [x * y for x, y in zip(processed_values, correction_factors)]
    
    # Select final items based on threshold
    threshold = 25
    valid_items = [item for item in corrected_data if item > threshold]
    
    # Final calculation
    final_output = sum(valid_items)
    print(f"Target result: {final_output}")

# Execute the function
sensor_data = [7, 4, 9, 12, 2, 15, 6]
process_engineering_data(sensor_data)