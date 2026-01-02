def analyze_sensor_data(readings):
    base_offset = 0.5
    calibration_factor = 1.2
    temp_buffer = []
    valid_count = 0
    cumulative_sum = 0.0

    for reading in readings:
        adjusted = reading * calibration_factor + base_offset
        if adjusted > 10.0:
            temp_buffer.append(adjusted)
            cumulative_sum += adjusted
            valid_count += 1
        else:
            temp_buffer.append(adjusted * 0.5)  # Distractor: not used later

    filtered_readings = [r for r in temp_buffer if r > 10.0]  # Only strong signals

    def calculate_threshold(data):
        if not data:
            return 0.0
        mean_val = sum(data) / len(data)
        variance = sum((x - mean_val) ** 2 for x in data) / len(data)
        stability_score = 1.0 if variance < 2.0 else 0.5
        
        # Conditional expression (required feature)
        energy_level = mean_val * 1.5 if stability_score > 0.7 else mean_val * 0.8
        
        # Extra computation with dead-end variable
        debug_weight = 1.1  # Unused after this
        energy_threshold = int(energy_level) + 5  # Final integer threshold
        
        # Early return simulation via condition
        if energy_threshold < 0:
            return 0
        return energy_threshold

    # Key statement
    energy_threshold = calculate_threshold(filtered_readings)
    
    # Irrelevant tracking variables
    total_analyzed = len(readings)
    avg_raw = sum(readings) / len(readings) if readings else 0
    
    print(f"Result: {energy_threshold}")
    return energy_threshold

# Input data
sensor_inputs = [7.8, 9.1, 10.5, 11.3, 9.7, 12.0, 8.4]
analyze_sensor_data(sensor_inputs)