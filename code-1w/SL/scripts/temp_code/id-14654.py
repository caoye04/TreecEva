def analyze_sensor_data(raw_readings, thresholds):
    # Irrelevant preprocessing: normalize all values (not actually used in final result)
    normalized = [round((x - min(raw_readings)) / (max(raw_readings) - min(raw_readings)) * 100, 2) for x in raw_readings]
    spike_count = 0
    trend_segments = []

    # Real logic begins: detect upward trends above threshold
    for i in range(1, len(raw_readings)):
        if raw_readings[i] > thresholds['upper'] and raw_readings[i-1] <= thresholds['upper']:
            spike_count += 1
            if i >= 3:
                segment = raw_readings[i-3:i+1]
                trend_segments.append(sum(segment) / len(segment))  # Average of trend window

    # Distractor: complex but unused signal smoothing
    def smooth_signal(data, factor=0.3):
        if len(data) < 2:
            return data
        smoothed = [data[0]]
        for i in range(1, len(data)):
            smoothed.append(smoothed[-1] * (1 - factor) + data[i] * factor)
        return smoothed

    # Unused call
    smoothed_diagnostics = smooth_signal([x for x in raw_readings if x > thresholds['lower']])

    # Real path: derive baseline from first third of data
    baseline_region = raw_readings[:len(raw_readings)//3]
    baseline_avg = sum(baseline_region) / len(baseline_region)

    # Compute deviation score only on meaningful spikes
    deviation_score = 0
    for seg_avg in trend_segments:
        if seg_avg > baseline_avg * 1.1:
            deviation_score += (seg_avg - baseline_avg) * 1.5

    # Decoy structure: entropy calculation not used
    from math import log2
    def calculate_entropy(arr):
        freq = {}
        for x in arr:
            freq[x] = freq.get(x, 0) + 1
        total = len(arr)
        return -sum((count/total) * log2(count/total) for count in freq.values())

    entropy_diagnostic = calculate_entropy([int(x) % 10 for x in raw_readings])  # Unused

    # Conditional branching with red herring
    mode_flag = 'A'
    if len(trend_segments) > 5:
        mode_flag = 'B'
    elif deviation_score > 100:
        mode_flag = 'C'
    else:
        mode_flag = 'D'  # Actual path taken

    # Simulate diagnostic codes based on mode (only one affects final result)
    codes = {'A': 750, 'B': 880, 'C': 920, 'D': 105}
    initial_diagnostic = codes[mode_flag]

    # Data transformation chain with slicing
    history_log = [baseline_avg, spike_count, len(trend_segments), deviation_score, entropy_diagnostic]
    recent_history = history_log[-3:]  # Slice last three
    growth_pattern = [recent_history[i] - recent_history[i-1] for i in range(1, len(recent_history))]

    adjustment_factor = 1.0
    if any(x < 0 for x in growth_pattern):
        adjustment_factor = 0.9
    elif deviation_score > 50:
        adjustment_factor = 1.1
    else:
        adjustment_factor = 1.2  # This branch taken

    intermediate_result = int(initial_diagnostic * adjustment_factor)

    # Complex but irrelevant bit manipulation decoy
    def obfuscate_value(val):
        val = (val ^ 0xABC) + 37
        val = (val << 2) & 0xFFFF
        val = (val ^ (val >> 4))
        return val & 0x7FFF

    obfuscated = obfuscate_value(intermediate_result)  # Dead end

    # Final aggregation function (real)
    def aggregate_metrics(metrics_list, flags):
        base = metrics_list[0]
        if flags.get('strict_mode', False):
            return base * 0.85
        return int(base * 1.0)  # No change

    # Processing chain built from prior results
    processing_chain = [intermediate_result, deviation_score, spike_count]
    validation_flags = {'strict_mode': False, 'debug_override': True}

    final_diagnostic = aggregate_metrics(processing_chain, validation_flags)

    # Spurious list slicing operations (distractors)
    shadow_copy = processing_chain[::]
    reversed_slice = shadow_copy[::-1]
    mid_segment = shadow_copy[1:2]

    # Only this print matters
    print(f"Result: {final_diagnostic}")

# Inputs
readings = [23.1, 24.5, 25.3, 26.0, 30.2, 35.1, 40.3, 27.5, 28.9, 31.0, 33.2, 36.8, 29.4, 30.1]
limits = {'lower': 20.0, 'upper': 30.0}

# Entry point
analyze_sensor_data(readings, limits)