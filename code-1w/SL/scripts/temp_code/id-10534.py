import itertools

def analyze_signal_strength(raw_samples, config_params):
    # Irrelevant pre-processing block (dead path)
    if len(raw_samples) == 0:
        return [0] * len(config_params.get('channels', [1]))

    baseline_offset = config_params.get('offset', 10)
    scaling_factor = config_params.get('scale', 1.5)
    adjusted_samples = [int((x + baseline_offset) * scaling_factor) for x in raw_samples]

    # Distractor: complex but unused transformation
    shifted_waveform = []
    for i, val in enumerate(adjusted_samples):
        shift = (val >> (i % 3)) & 7
        shifted_waveform.append(val ^ shift if i % 4 == 0 else val)

    # Actual relevant logic begins here
    valid_range_mask = [50 < x < 200 for x in adjusted_samples]
    filtered_peaks = [v for v, m in zip(adjusted_samples, valid_range_mask) if m]

    # Simulate multi-threshold analysis with grouping
    threshold_groups = {}
    for level in [60, 85, 110]:
        threshold_groups[level] = len([x for x in filtered_peaks if x > level])

    # Red herring: unused recursive function
    def recursive_energy(acc, depth):
        if depth <= 0 or acc < 5:
            return acc
        return recursive_energy(acc // 2 + (acc % 7), depth - 1)

    # Meaningless accumulation (distractor)
    dummy_accumulator = 0
    for group in itertools.combinations_with_replacement([1, 2, 3], 3):
        dummy_accumulator += sum(group) * 2

    return {'readings': filtered_peaks, 'groups': threshold_groups}

def validate_calibration(sequence):
    # Unused validation routine (dead code path)
    checksum = 0
    for i, val in enumerate(sequence):
        checksum ^= (val + i) % 255
    return checksum == 128

def process_readings(data_dict, thresholds):
    readings = data_dict['readings']
    groups = data_dict['groups']

    # Real computation starts
    aggregate_score = 0
    for t, count in groups.items():n        weighted_contribution = count * (t // 10)
        aggregate_score += weighted_contribution

    # Decoy logic with misleading intermediate
    temp_buffer = []
    for idx, val in enumerate(readings):
        if idx % 5 == 0:
            temp_buffer.append(val % 17)
        elif val % 2 == 0 and idx < 20:
            temp_buffer.append(val // 3)

    # Final computation using correct path
    base = len(readings)
    modifier = sum(groups.keys()) / 100
    final_diagnostic = base * int(modifier) + aggregate_score

    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Main execution
if __name__ == "__main__":
    sensor_data = [
        45, 55, 67, 78, 88, 95, 102, 115, 123, 134,
        145, 150, 158, 167, 175, 180, 188, 192, 198, 205,
        210, 66, 77, 89, 99, 111, 122, 133, 144, 155
    ]

    config = {
        'offset': 12,
        'scale': 1.2,
        'channels': [1, 2, 3, 4],
        'mode': 'diagnostic'
    }

    # Unused variables (distractors)
    calibration_sequence = [12, 34, 56, 78, 90, 23, 45, 67]
    validation_result = validate_calibration(calibration_sequence)

    processed_output = analyze_signal_strength(sensor_data, config)
    threshold_levels = [60, 85, 110]

    final_diagnostic = process_readings(processed_output, threshold_levels)