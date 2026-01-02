def compute_filtration_efficiency(samples):
    base_threshold = 73
    adjustment_rate = 1.07
    temp_cache = []

    for idx, reading in enumerate(samples):
        if idx % 3 == 0:
            adjusted = int(reading * adjustment_rate) + 2
        elif idx % 5 == 0:
            adjusted = reading - (idx % 7)
        else:
            adjusted = reading // 2 + base_threshold

        if reading > 60:
            temp_cache.append(adjusted * 1.5)
        else:
            temp_cache.append(adjusted)

    filtered_readings = [val for val in temp_cache if val > 50]
    cumulative_shift = 0

    for i in range(len(filtered_readings)):
        if i % 2 == 0:
            cumulative_shift += int(filtered_readings[i]) % 19
        else:
            cumulative_shift -= int(filtered_readings[i]) % 11

    # Irrelevant string transformation block (distractor)
    status_labels = ['active', 'idle', 'pending']
    upper_labels = [label.upper()[::-1] for label in status_labels]  # Reversed uppercase
    label_sum = sum([len(label) for label in upper_labels])

    # Dead code path - never executed due to fixed condition (red herring)
    overflow_flag = False
    if len(samples) > 1000:
        backup_buffer = [0] * 1000
        for x in backup_buffer:
            label_sum += x  # This does nothing meaningful

    # Decoy calculation with plausible but unused variables
    decoy_entropy = 0
    for val in samples:
        decoy_entropy ^= int(val % 9)

    normalization_constant = 3
    aggregate_result = int(sum(filtered_readings) + cumulative_shift)
    correction_factor = normalization_constant + (label_sum % 5)

    # Key statement: target variable assignment
    filtration_score = aggregate_result // correction_factor

    # Unused complex data structure (distractor)
    metadata_map = {
        'version': '2.1.0',
        'checksum': decoy_entropy ^ 255,
        'level': (correction_factor * 2) // 3
    }

    # Final red herring: irrelevant bit manipulation
    final_bits = 0
    for i in range(1, 8):
        final_bits |= (i << (i % 4))

    print(f"Result: {filtration_score}")
    return filtration_score

# Input data
sensor_data = [88, 45, 72, 61, 33, 91, 54, 67, 77, 42, 83]
result = compute_filtration_efficiency(sensor_data)