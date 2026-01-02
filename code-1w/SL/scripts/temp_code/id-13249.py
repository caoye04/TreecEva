def normalize_sensor_value(val, min_val=0, max_val=100):
    """
    Normalizes sensor reading to [0, 1] range.
    This function is unused in final computation but included as distraction.
    """
    return (val - min_val) / (max_val - min_val)


def validate_readings(readings):
    """
    Validates that all readings are within expected bounds.
    Returns False if any reading is out of range.
    """
    for r in readings:
        if r < -50 or r > 150:
            return False
    return True


def calculate_thermal_capacity(data_points):
    """
    Computes effective thermal capacity based on filtered temperature cycles.
    Uses enumerate and zip for indexed processing of paired data.
    """
    cycle_peaks = []
    baseline_offset = 20.5
    adjustment_factor = 0.87

    # Simulate multiple processing passes with some irrelevant tracking
    temp_history = []
    fluctuation_score = 0
    for i, val in enumerate(data_points):
        adjusted = val - baseline_offset
        temp_history.append(adjusted)
        if adjusted > 10:
            fluctuation_score += 1.5
        elif adjusted < -10:
            fluctuation_score -= 0.5

    # Irrelevant smoothing pass (dead computation path)
    smoothed = []
    window_size = 3
    for i in range(len(temp_history)):
        start = max(0, i - window_size // 2)
        end = min(len(temp_history), i + window_size // 2 + 1)
        avg = sum(temp_history[start:end]) / (end - start)
        smoothed.append(avg)

    # Actual relevant logic: detect rising-falling cycles using zip
    filtered_points = [t for t in temp_history if abs(t) > 5]
    paired_shift = list(zip(filtered_points, filtered_points[1:]))
    rise_fall_cycles = 0
    for idx, (current, next_val) in enumerate(paired_shift):
        if current < 0 and next_val > 0:
            rise_fall_cycles += 1
        elif current > 0 and next_val < 0:
            rise_fall_cycles += 1  # count both transitions

    # Compute base capacity from average magnitude
    if len(filtered_points) == 0:
        base_capacity = 0
    else:
        base_capacity = sum(abs(x) for x in filtered_points) / len(filtered_points)

    # Final capacity combines base level and cycle dynamics
    enhancement_factor = 1 + (rise_fall_cycles * 0.05)
    final_capacity = base_capacity * enhancement_factor * adjustment_factor

    # Dead code: logging unused metrics
    diagnostic_flag = False
    if final_capacity > 50:
        diagnostic_flag = True
    debug_log = f'Final cycles detected: {rise_fall_cycles}, Flag: {diagnostic_flag}'

    return round(final_capacity, 4)

# Main execution block
sensor_readings = [25, 30, 18, 65, 70, 15, 10, 40, 85, 90, 22, 12, 8, 50, 55]

# Distraction: unused normalized version
normalized_readings = [normalize_sensor_value(x, 0, 100) for x in sensor_readings]

# Validate input (used, but simple)
is_valid = validate_readings(sensor_readings)
if not is_valid:
    thermal_capacity = 0
else:
    # Preprocessing: apply offset before analysis
    processed_readings = []
    offset = 20
    for val in sensor_readings:
        processed_readings.append(val - offset)

    # Core calculation
    thermal_capacity = calculate_thermal_capacity(processed_readings)

# Additional red herring variables
average_reading = sum(sensor_readings) / len(sensor_readings)
peak_count = len([x for x in sensor_readings if x > 80])
phantom_metric = (average_reading * peak_count) ** 0.5

# Output result as required
print(f"Result: {thermal_capacity}")