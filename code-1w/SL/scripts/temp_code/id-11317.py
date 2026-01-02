import math

# Simulated sensor fusion system for environmental monitoring
def process_sensor_array(raw_readings, calibration_factor):
    filtered_data = []
    noise_floor = 0.003
    gain_stages = [1.02, 0.98, 1.01, 1.05, 0.97]
    temp_buffer = []

    for idx, reading in enumerate(raw_readings):
        if idx % 4 == 0:
            adjusted = (reading * calibration_factor + noise_floor) * gain_stages[idx % 5]
        elif idx % 3 == 1:
            adjusted = reading * 1.1
        else:
            adjusted = reading * 0.95

        if adjusted > 100:  # saturation guard
            adjusted = 99.9
        
        temp_buffer.append(adjusted + noise_floor)

    # Irrelevant FFT prep (dead path)
    fft_scratch = [0] * len(temp_buffer)
    for i in range(len(temp_buffer)):
        fft_scratch[i] = temp_buffer[i] * 2  # unused

    # Actual filtering path
    decay_weights = [math.exp(-i * 0.1) for i in range(len(temp_buffer))]
    weighted_sum = sum(temp_buffer[i] * decay_weights[i] for i in range(len(temp_buffer)))
    normalization = sum(decay_weights)
    filtered_data.append(weighted_sum / normalization)

    return filtered_data[0] if filtered_data else 0.0


def analyze_pattern_sequence(sequence, mode_flag):
    pattern_score = 0
    sequence_shift = 0
    history_map = {}

    for i, val in enumerate(sequence):
        if val in history_map:
            sequence_shift += i - history_map[val]
        history_map[val] = i

    # Complex but irrelevant transformation chain
    transformed = [(x ** 0.5 + 2.5) * mode_flag for x in sequence if x > 0]
    if len(transformed) > 3:
        transformed = transformed[:3]

    # Real logic: bitwise checksum
    checksum = 0
    for x in sequence:
        checksum ^= int(x) & 255
        checksum = (checksum << 1) | (checksum >> 7)
        checksum &= 0xFF

    pattern_score = checksum + sequence_shift % 50

    # Dead code branches
    if mode_flag < 0:
        alt_score = sum(transformed) * 100  # never used
    else:
        outlier_detect = [x for x in sequence if x > 80]  # computed but unused

    return pattern_score

# Main data processing pipeline
def validate_system_integrity(signals, thresholds):
    status_flags = []
    accumulated_risk = 0

    for sig, thresh in zip(signals, thresholds):
        risk_level = 0
        if sig > thresh * 1.2:
            risk_level = 3
        elif sig > thresh * 1.05:
            risk_level = 2
        elif sig > thresh * 0.9:
            risk_level = 1
        else:
            risk_level = 0

        accumulated_risk += risk_level
        status_flags.append(risk_level)

    # Red herring: complex matrix-like structure (unused)
    flag_matrix = [[f * 2 for _ in range(3)] for f in status_flags]

    # Real output
    return accumulated_risk * 10

# Final aggregation function
def aggregate_metrics(chains, baselines):
    metrics = []    
    auxiliary_cache = {}

    for i, chain in enumerate(chains):
        # Meaningless cache buildup
        key = f"chain_{i}_{chain % 7}"
        auxiliary_cache[key] = chain * 1.01 + 0.5

        # Relevant transformation
        normalized = (chain - min(baselines)) / (max(baselines) - min(baselines) + 1e-8)
        metrics.append(normalized)

    # Distractor: unused statistical moment calculation
    mean_val = sum(metrics) / len(metrics)
    variance = sum((x - mean_val) ** 2 for x in metrics) / len(metrics)
    skew = sum(((x - mean_val) / (variance ** 0.5 + 1e-8)) ** 3 for x in metrics)  # computed but not used

    # Critical computation path
    weighted_combo = 0
    for j, m in enumerate(metrics):
        weight = 1.0 if j % 2 == 0 else 0.5
        weighted_combo += m * weight

    final_adjustment = weighted_combo * 100

    # Decoy finalization
    if final_adjustment > 200:
        final_adjustment = math.log(final_adjustment) * 10  # not triggered

    return int(final_adjustment)

# --- Execution Context ---
if __name__ == "__main__":
    # Input datasets
    primary_readings = [23.5, 45.2, 67.8, 12.1, 89.3, 56.7, 34.0]
    calibration_coeff = 1.03
    
    # Step 1: Sensor processing
    processed_signal = process_sensor_array(primary_readings, calibration_coeff)
    
    # Irrelevant intermediate visualization (distractor)
    display_grid = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(round(processed_signal + i * j, 2))
        display_grid.append(row)
    
    # Step 2: Pattern analysis
    detection_sequence = [15, 45, 67, 12, 89, 56]
    pattern_diagnostic = analyze_pattern_sequence(detection_sequence, mode_flag=1)
    
    # Step 3: System validation
    system_signals = [processed_signal * 2, pattern_diagnostic / 3, 75.0]
    danger_thresholds = [40.0, 25.0, 70.0]
    safety_code = validate_system_integrity(system_signals, danger_thresholds)
    
    # Step 4: Chain assembly (critical path)
    processing_chain = [
        processed_signal,
        pattern_diagnostic,
        safety_code,
        42.0  # magic reset signal
    ]
    
    # Baseline references (with red herring values)
    baseline_signals = [20.0, 40.0, 60.0, 80.0, 100.0, 10.0, 30.0, 50.0, 70.0, 90.0]
    
    # Key execution point
    final_diagnostic = aggregate_metrics(processing_chain, baseline_signals)
    
    # Output result
    print(f"Result: {final_diagnostic}")