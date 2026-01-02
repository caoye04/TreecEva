def analyze_sensor_data(raw_readings, calibration_sequence):
    # Irrelevant preprocessing: normalize timestamps (not used in final result)
    normalized_times = [t % 86400 for t in range(len(raw_readings) + 5)]
    temp_buffer = [0] * len(calibration_sequence)
    for i, val in enumerate(calibration_sequence):
        if i % 2 == 0:
            temp_buffer[i] = val ** 0.5
        else:
            temp_buffer[i] = val // 3

    # Distractor: complex frequency analysis with unused outcome
    fft_peaks = []
    for j in range(1, len(raw_readings) - 1):
        if raw_readings[j] > raw_readings[j-1] and raw_readings[j] > raw_readings[j+1]:
            fft_peaks.append(j)
    smoothed = [x * 0.9 for x in raw_readings if x > 0]

    # Real computation begins: filter valid sensor pulses
    valid_pulses = [x for x in raw_readings if 50 < x < 200]
    
    # Misleading branch with dead-end logic
    if sum(valid_pulses) > 1000:
        outlier_mode = True
        adjustment_map = {i: v * 1.1 for i, v in enumerate(valid_pulses)}
        # But we don't use adjustment_map later

    # Core signal integration using zip and enumerate
    integrated_signal = 0
    for idx, (a, b) in enumerate(zip(valid_pulses, valid_pulses[1:])):
        if idx % 2 == 0:
            integrated_signal += (a + b) * 0.5
        else:
            integrated_signal -= (a * 0.1)

    # Secondary metric: pulse stability (used later)
    stability_scores = []
    for i in range(1, len(valid_pulses)):
        diff = abs(valid_pulses[i] - valid_pulses[i-1])
        stability_scores.append(1 / (1 + diff) if diff != 0 else 1)
    
    average_stability = sum(stability_scores) / len(stability_scores) if stability_scores else 0

    # Decoy function call that appears important but returns unused value
    def compute_entropy(seq):
        from math import log
        freq = {}
        for item in seq:
            freq[item] = freq.get(item, 0) + 1
        total = len(seq)
        entropy = 0
        for count in freq.values():
            p = count / total
            entropy -= p * log(p)
        return entropy
    
    entropy_diagnostics = compute_entropy([int(x) for x in raw_readings if x > 25])

    # Unused data structure transformation (distractor)
    reshaped_data = [[raw_readings[i], raw_readings[i+1]] 
                     for i in range(0, len(raw_readings)-1, 2)]
    transposed = list(zip(*reshaped_data))

    # Actual path to answer starts here
    baseline_reference = sum(calibration_sequence) / len(calibration_sequence)
    aggregate_score = integrated_signal + baseline_reference * 0.25

    # Conditional correction based on stability
    if average_stability > 0.7:
        correction_factor = 1.35
    elif average_stability > 0.5:
        correction_factor = 1.15
    else:
        correction_factor = 0.9
    
    # Offset derived from length parity (subtle but deterministic)
    offset_value = len(valid_pulses) % 7 * 2.5

    # Key assignment point
    final_diagnostic = aggregate_score * correction_factor + offset_value

    # Red herring: modify unused tracking list
    diagnostic_log = []
    diagnostic_log.append(('final', final_diagnostic * 0.1))
    diagnostic_log.append(('checksum', sum(integrated_signal for _ in range(1))))  # Confusing reuse of name

    print(f"Result: {final_diagnostic}")

# Execute with fixed inputs
data_stream = [120, 85, 190, 210, 150, 170, 45, 180, 160]
calib_seq = [100, 105, 95, 110, 90]
analyze_sensor_data(data_stream, calib_seq)