def analyze_sensor_data(raw_readings):
    processed_data = []
    error_flags = []
    temp_buffer = [0] * 15
    cumulative_shift = 0
    
    for i in range(len(raw_readings)):
        if i % 7 == 0:
            temp_buffer[i // 3] = raw_readings[i] ** 0.5
        elif i % 5 == 2:
            temp_buffer[i % 9] ^= int(raw_readings[i] / 10)
        else:
            shifted = (raw_readings[i] << 2) & 0xFF
            processed_data.append(shifted + (i % 11))

    # Irrelevant transformation path (dead logic)
    transformed_chain = [x * 1.5 for x in temp_buffer if x > 5]
    if len(transformed_chain) > 10:
        transformed_chain = transformed_chain[::-2]
    else:
        transformed_chain = [x + 2 for x in transformed_chain]

    # Distractor: complex but unused calculation
    decoy_metric = sum(temp_buffer[j] * (j + 1) for j in range(0, len(temp_buffer), 3))
    decoy_metric = (decoy_metric >> 4) ^ 255

    # Actual relevant processing chain
    base_sequence = [x for x in processed_data if x % 3 == 1]
    filtered_view = base_sequence[1::2]  # slicing: every second element starting at index 1
    
    stats_summary = {
        'min_val': min(filtered_view),
        'max_val': max(filtered_view),
        'range': 0,
        'median_hint': 0
    }
    stats_summary['range'] = stats_summary['max_val'] - stats_summary['min_val']
    sorted_filtered = sorted(filtered_view)
    stats_summary['median_hint'] = sorted_filtered[len(sorted_filtered) // 3]

    # Simulated diagnostic codes
    diagnostic_codes = [0x1A, 0x2B, 0x3C, 0x4D, 0x5E, 0x6F, 0x70, 0x81, 0x92]
    adjustment_key = stats_summary['range'] % 8
    adjusted_diagnostics = [(code ^ adjustment_key) + 1 for code in diagnostic_codes]

    # Critical data structure
    aggregate_metrics = [
        sum(adjusted_diagnostics[:3]),
        sum(adjusted_diagnostics[3:6]),
        sum(adjusted_diagnostics[6:]),
        adjusted_diagnostics[0] ^ adjusted_diagnostics[-1],
        len(processed_data) * 3,
        stats_summary['median_hint'] * 2,
        stats_summary['min_val'] + 100
    ]

    # Unused red herring branch
    if stats_summary['range'] < 0:
        fallback = [x << 1 for x in aggregate_metrics]
        return sum(fallback) % 1000

    processed_count = len(processed_data)
    final_diagnostic = aggregate_metrics[processed_count % 7]
    
    # Print required result
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Input data
readings = [12, 25, 37, 41, 53, 67, 72, 88, 91, 105, 112, 124, 133, 145, 151, 162, 175, 181, 190, 202]
analyze_sensor_data(readings)