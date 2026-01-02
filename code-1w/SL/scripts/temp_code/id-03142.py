def analyze_sensor_readings(readings):
    # Initialize tracking variables
    cumulative_total = 0
    outlier_count = 0
    temp_buffer = []

    for value in readings:
        cumulative_total += value
        if abs(value - cumulative_total / len(temp_buffer + [value])) > 50:
            outlier_count += 1
        temp_buffer.append(value)

    # Compute moving average over window of 3
    moving_averages = []
    for i in range(2, len(readings)):
        window_avg = sum(readings[i-2:i+1]) / 3
        moving_averages.append(window_avg)

    # Misleading transformation (not used later)
    transformed_vals = [x * 0.95 + 2.1 for x in moving_averages]
    shifted_data = readings[1:] + [readings[0]]  # Circular shift - irrelevant

    # Core logic: extract every second element, then filter by threshold
    subset_data = readings[::2]  # Every second reading
    normalized_data = [x - min(subset_data) for x in subset_data]
    relevant_data = [x for x in normalized_data if x > 10]

    # Key computation point
    filtered_sum = sum(relevant_data)

    # Additional red herring computations
    squared_residuals = [x**2 for x in readings if x < 0]
    dummy_agg = sum(squared_residuals) * 0.1 if squared_residuals else 0

    # Final output
    print(f"Result: {filtered_sum}")

# Input data
sensor_readings = [85, 102, 77, 144, 68, 131, 90, 119]
analyze_sensor_readings(sensor_readings)