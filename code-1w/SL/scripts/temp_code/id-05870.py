def analyze_sensor_array(raw_readings, calibration_offset):
    # Irrelevant preprocessing block (dead code path)
    temp_buffer = [x * 0.98 for x in raw_readings if x > 50]
    normalized = [max(0, x + calibration_offset) for x in raw_readings]

    # Distractor: complex but unused transformation
    fft_proxy = list(map(lambda x: (x ** 2) % 17, normalized[:len(normalized)//2]))
    spike_filter = [x for x in normalized if x > 100]
    baseline = sum(normalized) / len(normalized)

    # Real data path begins here
    adjusted = [x * 1.05 for x in normalized]
    squared_errors = [(x - baseline) ** 2 for x in adjusted]
    mse = sum(squared_errors) / len(squared_errors)

    # Another decoy function that's defined but not used in critical path
    def legacy_recalibrate(data):
        return [d * 0.995 + 3 for d in data]

    # Key transformation
    transformed_data = [x + mse * 0.1 for x in adjusted]

    # Threshold logic with lambda abstraction
    threshold_func = lambda val: val > (baseline * 1.15)

    # Dead branch — looks important but never taken due to fixed condition
    diagnostic_log = []
    if len(temp_buffer) > 100:
        diagnostic_log.append("Buffer overflow")
    else:
        diagnostic_log.append("Nominal buffer")

    # Unused nested structure with misleading metrics
    stats_summary = {
        'peak': max(transformed_data),
        'variance_proxy': sum((x - baseline) ** 3 for x in transformed_data) / len(transformed_data),
        'ignored_flag': False
    }

    # Critical processing function embedded inside
    def process_metrics(data, threshold_fn):
        above_threshold = [x for x in data if threshold_fn(x)]
        if not above_threshold:
            return len(data) * 2
        # Multi-step reduction
        weighted_sum = sum(x * (i + 1) for i, x in enumerate(above_threshold))
        compression_factor = len(data) / (len(above_threshold) + 1)
        intermediate = weighted_sum / (compression_factor + 0.5)
        # Final manipulation
        result = int(intermediate - (mse * 0.25))
        return result

    # Execution point of interest
    final_diagnostic = process_metrics(transformed_data, threshold_func)

    # Red herring print (not part of logic)
    # print(f'Debug: {len(spike_filter)}, Baseline: {baseline:.2f}')

    # Output the required result
    print(f"Result: {final_diagnostic}")

# Input data with realistic sensor readings
sensor_input = [87, 92, 95, 76, 88, 91, 84, 90, 79, 85, 93, 89, 82, 86, 88]
calib_offset = -5

# Entry point
analyze_sensor_array(sensor_input, calib_offset)