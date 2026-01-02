def compute_system_metrics():
    base_load = 17
    peak_capacity = 93
    maintenance_overhead = 8
    temp_buffer = 0

    # Simulate sensor readings over time
    sensor_data = [base_load + i * 2 for i in range(5)]
    adjusted_readings = []

    for reading in sensor_data:
        if reading > peak_capacity:
            temp_buffer += 1
            reading = peak_capacity
        adjusted_reading = reading - maintenance_overhead
        adjusted_readings.append(max(adjusted_reading, 0))

    # Calculate transient intermediate values
    transient_sum = sum([x % 11 for x in adjusted_readings])
    scaling_factor = len(adjusted_readings) / (transient_sum or 1)

    # Apply non-linear correction using lambda
    corrector = lambda x: round(x * (1 + 0.1 * (x < 50)), 2)
    corrected_values = [corrector(val) for val in adjusted_readings]

    # Compute stability score (distraction metric)
    stability_score = 0
    for i in range(1, len(corrected_values)):
        stability_score += abs(corrected_values[i] - corrected_values[i-1])

    avg_corrected = sum(corrected_values) / len(corrected_values)
    max_observed = max(corrected_values)

    # Efficiency logic with conditional expression
    efficiency_numerator = avg_corrected * (1 + (max_observed > 60))
    efficiency_denominator = base_load * 1.5

    efficiency_ratio = efficiency_numerator / efficiency_denominator

    # Final aggregation with irrelevant auxiliary data
    final_metrics = []
    system_flags = [False, True, False]
    if any(system_flags):
        temp_flag_value = sum(system_flags) * 100
        temp_buffer += temp_flag_value

    final_metrics.append(efficiency_ratio)

    print(f"Result: {efficiency_ratio}")

compute_system_metrics()