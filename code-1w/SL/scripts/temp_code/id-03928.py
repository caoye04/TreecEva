def analyze_sensor_data(raw_readings, calibration_sequence):
    # Irrelevant preprocessing: normalize timestamps (unused)
    normalized_times = [t % 86400 for t in range(len(raw_readings) + 5)]
    offset_shift = sum(normalized_times[:3]) / 3 if len(normalized_times) > 2 else 0

    # Distractor: complex but unused transformation
    transformed = []
    for i, val in enumerate(calibration_sequence):
        if i % 3 == 0:
            transformed.append(val ** 0.5 * (i + 1))
        elif i % 3 == 1:
            transformed.append(val // 2)
        else:
            transformed.append(abs(val - 100))

    # Dead code path: never executed due to control flow
    redundant_flag = False
    if len(transformed) > 1000:
        backup_state = [x * 0.1 for x in transformed]
        redundant_flag = True

    # Actual signal extraction (hidden among noise)
    filtered_signals = []
    for reading in raw_readings:
        if reading < 0:
            adjusted = abs(reading) ** 0.5
        elif reading == 0:
            adjusted = 0.1
        else:
            adjusted = reading ** (1/3)  # cube root for compression
        filtered_signals.append(round(adjusted, 4))

    # Decoy metric with misleading name
    peak_magnitude = max(filtered_signals) * 1.5 if filtered_signals else 0

    # Real processing: frequency pattern analysis via indexing
    frequency_weights = []
    for i, sig in enumerate(filtered_signals):
        weight = sig * (i % 7 + 1)  # weighted by position cycle
        frequency_weights.append(weight)

    # Secondary distractor: string-based encoding (irrelevant)
    status_codes = ['OK', 'CAL', 'FLT', 'TRP']
    encoded_diagnostics = ''.join([c for c in status_codes[0] for _ in range(2)])

    # Tertiary irrelevant operation: slicing and zipping unrelated data
    dummy_indices = list(range(10, 30, 2))
    sliced_pairs = list(zip(dummy_indices[::2], [x*2 for x in dummy_indices][::-1]))

    # Core logic buried in middle: detect oscillation baseline
    oscillation_energy = 0
    for i in range(1, len(frequency_weights)):
        delta = frequency_weights[i] - frequency_weights[i-1]
        oscillation_energy += abs(delta) * 0.5

    # Generate multi-stage metrics (only last used)
    aggregate_metrics = [
        sum(filtered_signals[:5]) if len(filtered_signals) >= 5 else 0,
        sum(frequency_weights[::3]),
        oscillation_energy,
        len([x for x in filtered_signals if x > 1.0]),  # count elevated signals
        sum(frequency_weights) / len(frequency_weights)  # mean weighted response
    ]

    # Correction based on calibration parity (actual dependency)
    parity_check = sum(calibration_sequence) % 4
    if parity_check == 0:
        correction_factor = 10
    elif parity_check == 1:
        correction_factor = -7
    elif parity_check == 2:
        correction_factor = 3
    else:
        correction_factor = 0

    # Unused diagnostic flags (red herring)
    system_stable = all(x < 50 for x in calibration_sequence)
    drift_detected = frequency_weights and frequency_weights[-1] > frequency_weights[0]

    # Key assignment: this is the target of the question
    final_diagnostic = aggregate_metrics[-1] + correction_factor

    # Print required output
    print(f"Result: {final_diagnostic}")

# Execute with test data
data_stream = [8, -27, 64, 0, 125, -216, 343]
calibration_profile = [16, 25, 36, 49, 64]
analyze_sensor_data(data_stream, calibration_profile)