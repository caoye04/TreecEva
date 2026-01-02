def analyze_sensor_data():
    raw_readings = [15, -3, 0, 42, 17, -8, 23, 91, 0, 14, 55, 76, 38, -42]
    offset_adjustment = 5
    adjusted_readings = [x + offset_adjustment for x in raw_readings]

    # Irrelevant transformation: phase shift (not used later)
    phase_shifted = [x * 0.9 for x in adjusted_readings]
    average_phase = sum(phase_shifted) / len(phase_shifted)

    # Distractor: secondary filter with unused result
    high_threshold_filtered = [x for x in adjusted_readings if x > 60]
    temp_aggregate = sum(high_threshold_filtered) // len(high_threshold_filtered) if high_threshold_filtered else 0

    # Actual processing path
    outliers_removed = [x for x in adjusted_readings if x >= 0]
    grouped_in_pairs = [(outliers_removed[i], outliers_removed[i+1]) for i in range(0, len(outliers_removed)-1, 2)]
    paired_averages = [sum(pair)/2 for pair in grouped_in_pairs]

    # Apply threshold and use slicing to ignore last two computed averages (stale data)
    recent_averages = paired_averages[:-2] if len(paired_averages) > 2 else paired_averages
    valid_entries = [avg for avg in recent_averages if avg > 10]

    # Key computation point
    filtered_sum = sum(valid_entries)

    # Dead code: formatting unused result
    report_string = f"Final integrity score: {filtered_sum % 100}"
    metadata_log = {'entries': len(valid_entries), 'checksum': filtered_sum ^ 255}

    print(f"Result: {filtered_sum}")

analyze_sensor_data()