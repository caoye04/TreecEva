def analyze_sensor_readings(readings):
    baseline = sum(readings) / len(readings)
    deviations = [abs(x - baseline) for x in readings]
    threshold = 0.5 * baseline
    significant_indices = [i for i, dev in enumerate(deviations) if dev > threshold]
    
    # Irrelevant distraction: noise filtering (not used in final result)
    filtered_noise = [x for x in readings if x > 10]
    avg_noise = sum(filtered_noise) / len(filtered_noise) if filtered_noise else 0
    
    # Core logic
    slice_start = max(1, len(significant_indices) - 2)
    indices = significant_indices[slice_start:]  # Last one or two significant positions
    processed_data = [x * 1.1 for x in readings]  # Apply scaling
    adjustment_factor = 0.9 if len(indices) > 1 else 1.2
    result = processed_data[indices[-1]] * adjustment_factor
    return result

# Input data
sensor_readings = [8, 12, 5, 23, 9, 14]
final_output = analyze_sensor_readings(sensor_readings)
print(f"Result: {final_output}")