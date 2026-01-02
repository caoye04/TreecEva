def analyze_sensor_data(raw_data, threshold=0.75):
    # Simulate preprocessing: normalize and filter noise
    normalized = [round(x * 0.98 + 0.5, 3) for x in raw_data]
    noise_floor = sum(normalized) / len(normalized)
    filtered = [x for x in normalized if x > noise_floor * 0.5]

    # Irrelevant transformation: frequency analysis (not used later)
    freq_map = {}
    for val in filtered:
        rounded_val = round(val, 1)
        freq_map[rounded_val] = freq_map.get(rounded_val, 0) + 1
    avg_frequency = sum(freq_map.values()) / len(freq_map) if freq_map else 0

    # Slice operation to extract recent stable readings
    window_size = 8
    recent_stable = filtered[-window_size:] if len(filtered) >= window_size else filtered[:]

    # Apply correction factor using bitwise logic (simulates hardware adjustment)
    corrected = []
    for i, val in enumerate(recent_stable):
        shift_factor = i % 3
        adjusted = val * (1.0 + (0.01 * ((i + 1) & 3)))  # Bitwise AND modulator
        if i % 4 == 0:
            adjusted = round(adjusted, 2)
        corrected.append(adjusted)

    # Compute rolling average and detect anomalies
    cumulative = 0
    rolling_averages = []
    for j in range(len(corrected)):
        cumulative += corrected[j]
        rolling_averages.append(cumulative / (j + 1))

    anomaly_count = 0
    reference_avg = sum(rolling_averages) / len(rolling_averages) if rolling_averages else 0
    for avg in rolling_averages:
        if abs(avg - reference_avg) > 0.1:
            anomaly_count += 1

    # Dummy state tracking (distractor)
    system_state_log = []
    for k in range(anomaly_count):
        state_code = (k ^ 7) | 2  # XOR and OR bit manipulation
        system_state_log.append(f'STATE_{state_code}')

    # Core validation function
    def validate_purity_levels(readings):
        if not readings:
            return 0
        base_score = sum(readings) / len(readings)
        fluctuation = sum(
            abs(readings[i] - readings[i-1]) 
            for i in range(1, len(readings))
        )
        penalty = fluctuation * 0.15
        purity_index = base_score - penalty
        return round(purity_index, 3)

    # --- Key Statement ---
    filtration_score = validate_purity_levels(corrected)

    # Unrelated post-processing (dead path)
    if filtration_score < threshold:
        backup_mode = True
        fallback_value = sum(corrected[::2]) / len(corrected[::2])
        filtration_score = round(fallback_value, 3)  # Not triggered due to data

    print(f"Result: {filtration_score}")
    return filtration_score

# Input data (controlled)
data_snapshot = [1.2, 1.3, 1.1, 1.4, 1.35, 1.28, 1.33, 1.27, 1.31, 1.29]
analyze_sensor_data(data_snapshot, threshold=0.75)