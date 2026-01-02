def analyze_sensor_array(raw_readings, calibration_factor):
    # Irrelevant preprocessing: normalize data (not used in final result)
    normalized = [round(x * 0.98 + 2.1, 2) for x in raw_readings if x > 0]
    outlier_count = sum(1 for x in raw_readings if x < -100 or x > 100)

    # Distractor: complex but unused transformation
    transformed = []
    for i, val in enumerate(raw_readings):
        if i % 3 == 0:
            transformed.append(val ^ 255)
        elif i % 4 == 0:
            transformed.append(~val)

    # Real computation begins: extract diagnostic bands
    low_freq = [x for i, x in enumerate(raw_readings) if i % 2 == 0]
    high_freq = [x for i, x in enumerate(raw_readings) if i % 2 == 1]

    # Compute checksums with modular arithmetic (only low_freq_checksum matters)
    low_freq_checksum = sum(low_freq) % 1000
    high_freq_checksum = sum(high_freq) % 777  # Dead end

    # Use enumerate and zip: align readings with calibration map
    calib_map = [calibration_factor * (i + 1) for i in range(len(low_freq))]
    paired_readings = list(zip(low_freq, calib_map))
    adjustment_log = []
    total_adjustment = 0

    for idx, (reading, calib) in enumerate(paired_readings):
        if idx % 2 == 0:
            adjusted = (reading + calib) // 2
        else:
            adjusted = int(reading * (calib / 100))
        adjustment_log.append((idx, adjusted))
        total_adjustment += adjusted

    # Secondary distractor: sorting unrelated data
    decoy_data = [(x, i) for i, x in enumerate(high_freq)]
    decoy_data.sort(key=lambda x: x[1], reverse=True)
    decoy_data = [x[0] for x in decoy_data[::2]]  # Unused beyond here

    # Critical path: compute health metrics
    rolling_window = []
    for i in range(len(paired_readings) - 1):
        diff = abs(paired_readings[i][0] - paired_readings[i+1][0])
        rolling_window.append(diff * calibration_factor)

    stability_index = sum(rolling_window) / len(rolling_window) if rolling_window else 0

    # Aggregate score from multiple sources (only some are relevant)
    base_health = low_freq_checksum * 2
    noise_penalty = len([x for x in rolling_window if x > 5]) * 3
    aggregate_health_score = base_health - noise_penalty + int(stability_index)

    # System offset derived from tuple unpacking and integer division
    config_tuple = (1234, 5678, 9012)
    primary, secondary, tertiary = config_tuple
    system_offset = (primary // 100) - (secondary // 1000) * 2

    # Final computation – this is the key statement
    final_diagnostic = aggregate_health_score + system_offset

    # Red herring: another variable that looks important
    predicted_failure_window = (tertiary % 500) + outlier_count

    # Output required format
    print(f"Result: {final_diagnostic}")

    return final_diagnostic

# Setup input data
sensor_readings = [150, -200, 300, 100, -150, 400, 250, -300]
calibration_input = 3

# Execute function
diagnostic_result = analyze_sensor_array(sensor_readings, calibration_input)