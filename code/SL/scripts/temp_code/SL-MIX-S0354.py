def process_energy_readings(readings):
    # Filter valid readings and calculate total
    valid_readings = [r for r in readings if 10 <= r <= 100]
    total_energy = sum(valid_readings)
    
    # Distractor: Calculate average but don't use it
    avg_energy = total_energy / len(valid_readings) if valid_readings else 0
    
    # Process filtered values with conditional transformation
    filtered_values = [r for r in valid_readings if r > 25]
    processed_data = [x * 2 if x % 2 == 0 else x + 3 for x in filtered_values]
    
    # More distractor operations
    max_value = max(processed_data) if processed_data else 0
    sorted_data = sorted(processed_data)
    
    # Final calculation using specific processed data
    final_result = sum(processed_data[1:-1]) if len(processed_data) > 2 else sum(processed_data)
    
    print(f"Target result: {final_result}")
    return final_result

# Initialize sensor readings
sensor_data = [15, 42, 8, 67, 91, 34, 28, 105, 56, 23]
result = process_energy_readings(sensor_data)