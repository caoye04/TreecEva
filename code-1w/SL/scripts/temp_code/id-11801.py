import itertools

# System health monitoring simulation with red herrings and multiple data paths
def analyze_component_stream(data_stream, threshold=75):
    alert_count = 0
    stable_windows = 0
    rolling_avg = 0
    temp_buffer = []

    for val in data_stream:
        temp_buffer.append(val)
        if len(temp_buffer) > 3:
            temp_buffer.pop(0)
        
        rolling_avg = sum(temp_buffer) / len(temp_buffer)

        if rolling_avg > threshold:
            alert_count += 1
        else:
            stable_windows += 1

    # Distractor: this function returns something irrelevant to final result
    return alert_count * 2


# Irrelevant helper: simulates network latency profiling (dead code path)
def calculate_latency_profile(sequence, delay_factor=0.1):
    base_delays = [delay_factor * x for x in sequence]
    adjusted = [d + 0.05 for d in base_delays if d < 0.5]
    return sum(adjusted) / len(adjusted) if adjusted else 0.0


# Core diagnostic engine with hidden logic chain
def run_system_diagnostics():
    # Real input data
    sensor_readings = [68, 72, 74, 80, 85, 78, 70, 65]
    calibration_sequence = [3, 5, 7, 11]
    fault_flags = [False, True, False, True]

    # Distractor variables
    dummy_weight = 0.0
    unused_metric = None
    placeholder_array = [0] * 10

    # Step 1: Compute moving average over window size 2
    moving_averages = [(sensor_readings[i] + sensor_readings[i+1]) / 2 
                       for i in range(len(sensor_readings)-1)]

    # Step 2: Count how many exceed dynamic threshold
    dynamic_threshold = 73 + (len(calibration_sequence) % 5)
    high_load_periods = len([x for x in moving_averages if x > dynamic_threshold])

    # Step 3: Apply bitmask filtering based on fault flags (irrelevant but looks important)
    masked_values = []
    for i, flag in enumerate(fault_flags):
        if not flag and i < len(calibration_sequence):
            masked_values.append(calibration_sequence[i])
    # Unused: masked_values

    # Step 4: Generate all pairwise products using itertools (core relevance)
    pairs = list(itertools.combinations(calibration_sequence, 2))
    pair_products = [a * b for a, b in pairs]
    product_sum = sum(pair_products)  # Used later

    # Step 5: Simulate diagnostic confidence decay
    confidence = 100.0
    for _ in range(high_load_periods):
        confidence *= 0.9

    # Step 6: Aggregate health score from multiple sources
    base_health = sum(sensor_readings) / len(sensor_readings)
    trend_score = sensor_readings[-1] - sensor_readings[0]  # +ve is good
    aggregate_health_score = base_health + (trend_score * 1.5)

    # Step 7: Hidden bias term derived from product sum modulo effect
    system_bias = product_sum % 17

    # Step 8: Final computation — critical line
    final_diagnostic = aggregate_health_score + system_bias

    # Distractor: calling irrelevant functions
    _ = analyze_component_stream(sensor_readings, threshold=70)
    _ = calculate_latency_profile(calibration_sequence)

    # Output target result
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Execute main logic
run_system_diagnostics()