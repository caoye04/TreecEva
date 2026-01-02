def analyze_signal_pattern(raw_readings):
    temporal_weights = [0.1, 0.3, 0.4, 0.2]
    filtered_values = []
    for i, reading in enumerate(raw_readings):
        if i < len(temporal_weights):
            weighted = reading * temporal_weights[i]
            filtered_values.append(weighted)
        else:
            filtered_values.append(reading * 0.05)

    base_magnitude = sum(filtered_values)
    peak_adjustment = max(filtered_values) * 0.15

    # Irrelevant signal smoothing branch (dead logic - never executed due to prior logic)
    smoothed_curve = []
    for j in range(len(filtered_values) - 1):
        trend = (filtered_values[j+1] - filtered_values[j]) * 0.1
n        smoothed_curve.append(trend)

    # Distractor: unused transformation chain
    shadow_accumulator = 0
    for char in 'diagnostic_buffer':
        shadow_accumulator += ord(char) % 7

    # Actual computation path begins here
    status_flags = {k: v for k, v in enumerate(['OK', 'CAL', 'FLT'])}
    active_flag = status_flags.get(len(raw_readings) % 3, 'UNK')

    # Character frequency distractor
    debug_log = 'sensor_cal_2023'
    freq_map = {}
    for c in debug_log:
        freq_map[c] = freq_map.get(c, 0) + 1
    entropy_proxy = len([v for v in freq_map.values() if v > 1])

    # Key intermediate: group and count readings by parity
    even_count = 0
    odd_sum = 0
    for val in raw_readings:
        if isinstance(val, int) and val % 2 == 0:
            even_count += 1
        else:
            odd_sum += int(val)

    # Real data path: compute aggregate score using bit manipulation
    bitmask = 0b1010
    scaled_even = even_count << 2
    inverted_scale = ~bitmask & 0b1111
    aggregate_score = scaled_even ^ inverted_scale

    # Decoy calculation with zip (unused)
    timestamps = list(range(len(raw_readings)))
    paired_data = list(zip(timestamps, raw_readings))
    dummy_total = 0
    for ts, val in paired_data:
        if ts % 2 == 0:
            dummy_total += val * 0.01

    # Correction factor depends on string method outcome
    mode_indicator = 'ASYNC_MODE_ACTIVE'
    if mode_indicator.endswith('ACTIVE') and 'SYNC' not in mode_indicator:
        adjustment_basis = len(mode_indicator.lower().split('_'))
        correction_factor = adjustment_basis ** 2
    else:
        correction_factor = 1

    # Final diagnostic computed from relevant components only
    final_diagnostic = aggregate_score + correction_factor

    # Red herring: unused recursive function
    def trace_back(index):
        if index <= 0:
            return 0
        return index + trace_back(index - 2)

    # Output only the target variable
    print(f"Result: {final_diagnostic}")

# Input data
input_readings = [8, 15, 12, 7, 22]
analyze_signal_pattern(input_readings)