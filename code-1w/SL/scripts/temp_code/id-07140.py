def analyze_sensor_data(raw_readings, calibration_sequence):
    # Irrelevant transformation (dead code path)
    normalized_data = [x * 0.98 for x in raw_readings if x > 0]

    # Distractor: complex but unused calculation
    entropy_proxy = 0
    for i in range(len(calibration_sequence)):
        if calibration_sequence[i] % 2 == 0:
            entropy_proxy += i * calibration_sequence[i]

    # Real processing begins: filter valid signals
    filtered_signals = []
    for idx, val in enumerate(raw_readings):
        if idx % 3 == 0 and val > 50:
            filtered_signals.append(val)

    # Misleading intermediate: looks important but unused
    temp_envelope = [max(filtered_signals[i:i+3]) for i in range(0, len(filtered_signals)-2)]
    spike_count = sum(1 for x in temp_envelope if x > 150)

    # Core logic: compute base aggregate using slicing and zip
    segment_a = filtered_signals[:len(filtered_signals)//2]
    segment_b = filtered_signals[len(filtered_signals)//2:]
    
    paired_diffs = []
    for a, b in zip(segment_a, segment_b):
        paired_diffs.append(abs(a - b))

    aggregate_score = sum(paired_diffs) * 0.75

    # Bit manipulation red herring
    masked_values = [x & 0xFF for x in calibration_sequence]
    checksum = 0
    for v in masked_values:
        checksum ^= v

    # Another decoy function call
    def calculate_thermal_drift(seq):
        return sum(x**0.5 for x in seq if x < 100) // 1
    
    dummy_drift = calculate_thermal_drift(calibration_sequence)

    # Critical control flow with nested conditions
    offset_basis = 0
    for i, reading in enumerate(calibration_sequence):
        if i > 5:
            if reading < 40:
                offset_basis += 2
            elif reading > 80:
                offset_basis -= 1

    # Correction factor derived from bit counting
    active_bits = bin(offset_basis).count('1')
    correction_factor = active_bits * 11

    # Key assignment point
    final_diagnostic = aggregate_score + correction_factor

    # Print required result
    print(f"Result: {final_diagnostic}")

    # Unused but plausible data structure
    diagnostics_log = {
        'readings_processed': len(filtered_signals),
        'spike_events': spike_count,
        'drift_estimate': dummy_drift,
        'final_diagnostic': final_diagnostic
    }

    return final_diagnostic

# Inputs
sensor_input = [120, 45, 67, 200, 89, 55, 180, 95, 70, 210, 130]
calib_seq = [30, 85, 92, 10, 67, 78, 88, 25, 95, 5]

# Execution
result = analyze_sensor_data(sensor_input, calib_seq)