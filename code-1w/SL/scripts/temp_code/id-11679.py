def analyze_sensor_data(raw_readings, calibration_offset=0.73):
    # Irrelevant preprocessing: string-based metadata parsing (distractor)
    metadata = 'sensor_v2.1_unit45_tempcal'
    version_info = metadata.split('_')[0].replace('sensor', '').strip('v')
    unit_id = int(metadata.split('_')[1][3:])

    # Real data path begins: clean numeric transformations
    filtered_readings = [x for x in raw_readings if x > 0]
    normalized = [round(x ** 0.5 - calibration_offset, 3) for x in filtered_readings]

    # Distractor: unused list comprehension with zip and enumerate
    indexed_pairs = []
    for i, (a, b) in enumerate(zip(normalized, normalized[1:])):
        trend_score = (b - a) * i  # Computed but never used
        quality_tag = 'HIGH' if abs(trend_score) < 1.5 else 'LOW'
        indexed_pairs.append((i, trend_score, quality_tag))  # Dead storage

    # Set operations: determine outlier thresholds (relevant)
    unique_vals = set(round(v, 2) for v in normalized)
    lower_quartile = sorted(unique_vals)[len(unique_vals)//4]
    upper_quartile = sorted(unique_vals)[-len(unique_vals)//4]
    outliers = {v for v in unique_vals if v < lower_quartile or v > upper_quartile}

    # Key computation chain starts here (nested logic)
    base_magnitude = sum(normalized) / len(normalized)
    fluctuation_index = 0
    for i in range(1, len(normalized)):
        diff = abs(normalized[i] - normalized[i-1])
        if diff > 0.5:
            fluctuation_index += diff * 0.9

    aggregate_score = base_magnitude * 1.7

    # Decoy branch with misleading intermediate result
    if len(outliers) > 10:
        temp_buffer = [abs(hash(str(x))) % 100 for x in normalized]
        buffer_avg = sum(temp_buffer) / len(temp_buffer)
        decoy_correction = buffer_avg * 0.3  # Never applied

    # Temperature simulation using bitwise and arithmetic mix (partially relevant)
    ambient_code = 0b110101
    sensor_heat = (ambient_code >> 2) ^ 0b101
    temperature_base = float(format(sensor_heat, 'b')[::-1], 2)
    temperature_factor = round(temperature_base * 0.42, 3)

    # Final diagnostic calculation (answer point)
    final_diagnostic = aggregate_score + temperature_factor

    # Unused complex data structure (distractor)
    report_summary = {
        'diagnostics': [
            {'stage': 'preprocess', 'valid_points': len(filtered_readings)},
            {'stage': 'normalize', 'avg': round(base_magnitude, 3)},
            {'stage': 'outlier', 'count': len(outliers)}
        ],
        'flags': list(set(['CAL_OK' if calibration_offset > 0.5 else 'CAL_ADJUST']))
    }

    return final_diagnostic

# Main execution
readings = [16.4, 25.1, 9.8, 4.0, 36.0, 64.2, 12.5, 49.7, 81.0, 2.3, 0.1, 100.0]
calib_setting = 0.73
diag_result = analyze_sensor_data(readings, calib_setting)
Result: {diag_result}