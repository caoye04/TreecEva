import itertools

# System health monitoring simulation with red herrings and complex logic paths

def analyze_subsystems():
    sensor_a = 78
    sensor_b = 85
    sensor_c = 92
    backup_sensor_x = 65  # Irrelevant backup, never used in primary path
    temp_offset = -3

    # Initial health score based on weighted average
    weights = [0.5, 0.3, 0.2]
    readings = [sensor_a, sensor_b, sensor_c]
    base_health = sum(r * w for r, w in zip(readings, weights))

    # Red herring: diagnostic chain that appears important but leads nowhere
    def internal_audit():
        audit_flag = True
        checksum = 0
        for i in range(3):
            checksum += (readings[i] ^ (weights[i] * 10)) % 7
        if checksum > 10:
            audit_flag = False
        return audit_flag  # Computed but never used

    # Unused decoy function
    def legacy_calibrate(x):
        return x * 1.05 if x < 70 else x * 0.98

    # Real processing begins here — masked by prior noise
    status_codes = [1 if r >= 80 else 0 for r in readings]
    active_alerts = sum(status_codes)

    # Complex conditional masking
    if active_alerts == 0:
        severity_level = 0
    elif active_alerts == 1:
        severity_level = 1
    elif active_alerts == 2:
        severity_level = 3
    else:
        severity_level = 5  # All three above threshold

    # Bit manipulation distraction
    encoded_state = (sensor_a & 0xFF) << 8 | (sensor_b & 0xFF)
    parity_check = bin(encoded_state).count('1') % 2
    _ = parity_check  # Used to simulate critical check, actually irrelevant

    # Core transformation chain (8-12 logic steps including comprehensions, conditionals, etc.)
    adjustment_map = {0: 0.95, 1: 0.98, 3: 1.0, 5: 1.02}
    adjustment_factor = adjustment_map.get(severity_level, 1.0)

    intermediate_score = base_health * adjustment_factor

    # Simulated environmental compensation
    environment_log = [(t, t * 0.1) for t in range(1, 6)]
    decay_rate = sum([v for _, v in environment_log])  # constant: 1.5

    compensated_score = intermediate_score - decay_rate * 2.0

    # Distractor: unused data structure transformation
    history_buffer = list(itertools.accumulate([sensor_a, sensor_b, sensor_c, backup_sensor_x]))
    _ = [x for x in history_buffer if x > 70]  # computed but not used

    # Critical computation path re-emerges
    outlier_detected = any(abs(r - compensated_score) > 15 for r in readings)
    correction_factor = 0.9 if outlier_detected else 1.1

    aggregate_score = round(compensated_score, 2)

    # Dead code branch — looks like it could affect things
    if aggregate_score < 70:
        recovery_mode = True
        offset_threshold = -5
        # This block is never executed
    else:
        recovery_mode = False
        offset_threshold = 12

    # Key assignment statement — target of the question
    final_diagnostic = aggregate_score * correction_factor + offset_threshold

    # Irrelevant visualization prep
    display_palette = ['red', 'yellow', 'green']
    color_index = min(int(aggregate_score // 25), 2)
    _ = display_palette[color_index]  # unused

    # Final output
    print(f"Result: {final_diagnostic}")

    return final_diagnostic

# Entry point
result = analyze_subsystems()