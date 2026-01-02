import itertools

# Simulate sensor readings with noise and valid data
def process_sensor_data():
    raw_readings = [12, 15, 14, 0, 18, 13, 0, 16, 19, 17]
    baseline_offset = 5
    noise_filter_threshold = 10
    temp_accumulator = []
    filtered_values = []

    # Misleading preprocessing: this block adjusts but isn't used in final path
    adjusted_readings = [x + baseline_offset for x in raw_readings if x > 0]
    average_adjusted = sum(adjusted_readings) / len(adjusted_readings)

    # Actual processing begins: extract non-zero values using slicing
    valid_readings = raw_readings[::1]  # Full copy to simulate inspection
    for reading in valid_readings:
        if reading > 0:
            temp_accumulator.append(reading * 0.9)  # Apply transmission loss

    # Use conditional expression to decide filtering approach
    method_flag = 'strict'
    threshold = 14 if method_flag == 'strict' else 10

    # Filter based on dynamic threshold
    filtered_values = [v for v in temp_accumulator if v >= threshold]

    # Compute rolling average using itertools to create sliding pairs (distraction)
    paired_rolls = list(itertools.pairwise(filtered_values))
    roll_avgs = [(a + b) / 2 for a, b in paired_rolls]  # Not used later

    # Key computation: sum of filtered, scaled values
    processed_sum = sum(filtered_values)

    # Red herring: unused statistical measures
    max_val = max(filtered_values) if filtered_values else 0
    min_val = min(filtered_values) if filtered_values else 0
    range_val = max_val - min_val

    # Correction factor based on number of valid windows (uses slicing and counting)
    window_size = 2
    valid_windows = [filtered_values[i:i+window_size] for i in range(len(filtered_values) - window_size + 1)]
    full_windows = [w for w in valid_windows if len(w) == window_size]
    correction_factor = len(full_windows) * 0.5 if full_windows else 1.0

    # Dead code: simulation of calibration that doesn't affect result
    calibration_sequence = [0.1 * i for i in range(10)]
    final_calibration = sum(c for c in calibration_sequence if c < 0.5)  # Unused

    # Critical assignment point
    final_output = processed_sum * correction_factor

    # Print result for evaluation
    print(f"Result: {final_output}")

    return final_output

# Execute function
process_sensor_data()