import math

# Simulated sensor data processing with noise filtering and phase analysis
def process_sensor_readings(raw_data, threshold=0.75, phase_shift=4):
    # Irrelevant pre-processing: normalize unrelated metrics
    normalized_metrics = [round((x - min(raw_data)) / (max(raw_data) - min(raw_data) + 1e-9), 3) for x in raw_data]
    entropy_score = 0.0
    for val in normalized_metrics:
        if val > 0:
            entropy_score -= val * math.log(val)

    # Real signal detection: extract significant oscillations
    signal_peaks = []
    for i in range(1, len(raw_data) - 1):
        if raw_data[i] > raw_data[i - 1] and raw_data[i] > raw_data[i + 1] and raw_data[i] > threshold:
            signal_peaks.append(i)

    # Distractor: unused peak analysis
    peak_derivatives = []
    for i in range(1, len(signal_peaks)):
        peak_derivatives.append(signal_peaks[i] - signal_peaks[i - 1])

    # Core logic: identify valid entries based on parity and index conditions
    indexed_pairs = list(enumerate(raw_data))
    valid_entries = []
    for idx, value in indexed_pairs:
        if idx % 2 == 0 and isinstance(value, int) and value % 3 == 1:
            valid_entries.append(value)

    # Misleading transformation chain
    temp_buffer = [x * 2 for x in valid_entries if x < 10]
    temp_buffer = [x for x in temp_buffer if x not in [4, 8]]
    buffer_sum = sum(temp_buffer)

    # Critical computation path
    backup_flag = False
    if len(valid_entries) > 3:
        subset = valid_entries[1:-1]
        alt_sum = 0
        for x in subset:
            alt_sum += x ^ 2  # Bitwise distraction
        if alt_sum > 10:
            backup_flag = True

    # Key statement with distractors around it
    baseline_correction = math.floor(math.cos(math.pi / 4) * 100)
    reference_map = {i: v for i, v in enumerate([1, 1, 2, 3, 5, 8, 13])}
    fallback_value = sum(reference_map.values())

    filtered_phase = sum(valid_entries) * phase_shift // 2

    # Dead code path: never executed due to constant condition
    if False:
        shadow_copy = valid_entries.copy()
        for _ in range(3):
            shadow_copy = [x >> 1 for x in shadow_copy]
        filtered_phase = sum(shadow_copy)

    # Unused finalization steps
    final_diagnostic = {
        'entries': len(valid_entries),
        'peak_count': len(signal_peaks),
        'buffer_total': buffer_sum,
        'corrected': baseline_correction
    }

    return filtered_phase

# Simulated input - deterministic sensor pattern
sensor_input = [1, 0.8, 4, 7, 0.92, 10, 13, 0.65, 16, 19]

result = process_sensor_readings(sensor_input, threshold=0.75, phase_shift=4)
print(f"Result: {result}")