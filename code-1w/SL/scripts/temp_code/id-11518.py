def analyze_system_metrics(raw_data, thresholds):
    # Irrelevant pre-processing: normalize data (not actually used in final result)
    normalized = [max(0.0, min(1.0, x / 100.0)) for x in raw_data]
    filtered_data = [x for x in raw_data if x > thresholds['min'] and x < thresholds['max']]

    # Distractor variables: energy metrics with no impact
    total_energy = sum([x * 1.05 for x in raw_data if x % 2 == 0])
    peak_moment = max(enumerate(raw_data), key=lambda pair: pair[1])
    energy_correction = total_energy * 0.987 if peak_moment[0] > 5 else total_energy * 1.013

    # Real computation begins: frequency analysis
    frequencies = {}
    for val in filtered_data:
        frequencies[val] = frequencies.get(val, 0) + 1

    # Bit manipulation red herring
    masked_values = []
    for k in frequencies.keys():
        masked = k ^ 0b1101 & 0b11111  # XOR and AND mask - not used later
        masked_values.append(masked * 0.1)

    # Actual signal extraction via slicing and zip
    time_series = raw_data[::2]  # Every other sample
    reference_series = [x - 1 for x in raw_data[1::2]]
    correlations = []
    for a, b in zip(time_series, reference_series):
        correlation = (a - b) ** 2
        correlations.append(correlation)

    # Decoy recursive function (never called)
    def recursive_dampener(n, depth=0):
        if depth > 5 or n < 1:
            return 0
        return n * 0.8 + recursive_dampener(n - 2, depth + 1)

    # Another distraction: unused data structure transformation
    struct_map = {i: {'raw': raw_data[i], 'inv': 1/(raw_data[i]+1)} for i in range(len(raw_data))}
    temp_aggregate = sum([v['inv'] for v in struct_map.values()]) * 0.01

    # Key intermediate: summation over correlations with rounding
    signal_strength = sum(correlations)
    rounded_strength = round(signal_strength, 2)

    # Conditional logic red herring
    status_flag = ""
    if rounded_strength > 50:
        status_flag = "WARNING"
        adjustment = -2
    elif rounded_strength < 10:
        status_flag = "IDLE"
        adjustment = 5
    else:
        status_flag = "STABLE"
        adjustment = 0  # This branch triggers

    # Core calculation chain (actual path to answer)
    base_health = len(filtered_data) * 3
    variation_metric = abs(max(frequencies.keys(), default=0) - min(frequencies.keys(), default=0))
    aggregate_health_score = base_health + (variation_metric // 2)

    # Hidden dependency on enumerate index sum
    index_sum = sum(idx for idx, val in enumerate(raw_data) if val >= thresholds['min'])
    system_bias = -(index_sum % 7)  # Negative bias derived from position

    # Correction factor via slicing and average
    window = raw_data[3:7]
    correction_factor = sum(window) / len(window) if window else 1
    correction_factor = int(correction_factor)  # Truncate to integer

    # Final diagnostic computed here — this is the target
    final_diagnostic = aggregate_health_score + system_bias * correction_factor

    # Dead code path: never executed but looks important
    if final_diagnostic < 0:
        final_diagnostic = abs(final_diagnostic) ^ 0b1010

    # Irrelevant post-processing
    diagnostic_log = f"Final: {final_diagnostic}, Status: {status_flag}"
    debug_trace = [final_diagnostic + i for i in range(3)]

    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Inputs
sensor_data = [12, 15, 9, 20, 18, 25, 14, 10]
config = {'min': 10, 'max': 30}

# Execute
result = analyze_system_metrics(sensor_data, config)