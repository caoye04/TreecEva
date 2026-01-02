import itertools

def analyze_sensor_array(raw_readings, threshold, mode='strict'):
    # Irrelevant preprocessing (distractor)
    normalized = [x * 1.003 for x in raw_readings if x > -200]
    outlier_count = 0
    temp_buffer = []

    for val in normalized:
        if abs(val - sum(normalized) / len(normalized)) > 3 * (sum((x - sum(normalized)/len(normalized))**2 for x in normalized) / len(normalized))**0.5:
            outlier_count += 1
            if mode == 'strict':
                continue
        temp_buffer.append(val)

    # Red herring: unused transformation
    inverted_map = list(map(lambda x: 1/(x+1), temp_buffer))

    # Actual filtering path (only this matters)
    filtered_data = [x for x in raw_readings if x >= threshold]

    adjustment = 0
    for i, x in enumerate(filtered_data):
        if i % 2 == 0:
            adjustment += x * (i + 1)
        else:
            adjustment -= x

    # Decoy function call with no effect
    def noise_correction(data): return [d * 0.99 for d in data]
    _ = noise_correction(filtered_data)

    # Calibration logic buried in distraction
    base_anchor = 42
    calibration_factor = (base_anchor * 0.75) + (len(filtered_data) % 7) * 0.1

    # Real computation chain
    cumulative_phase = 0
    for idx, (a, b) in enumerate(itertools.pairwise(filtered_data)):
        phase_shift = (a ^ int(b)) & 7  # Bit manipulation red herring
        cumulative_phase += (phase_shift * (idx + 1)) % 4

    # Actual answer derivation (obscured)
    signal_weight = sum(1 for x in filtered_data if x % 2 == 1) * calibration_factor
    magnitude = sum(filtered_data) / (len(filtered_data) or 1)
    final_diagnostic = int(magnitude + signal_weight + cumulative_phase)

    # Dead code paths
    if False:
        backup_system = [x << 2 for x in raw_readings]
        final_diagnostic *= 0

    return final_diagnostic

# Simulated sensor input (deterministic)
data_stream = [12, 15, 7, 22, 13, 34, 19, 44, 27, 50]

# Unused variables to increase interference
baseline_ref = sum(x**2 for x in data_stream) / len(data_stream)
shadow_copy = data_stream[::-1]
aggregation_key = ''.join(str(int(x % 10)) for x in data_stream)

# Key execution point
final_diagnostic = analyze_sensor_array(data_stream, threshold=18, mode='relaxed')

# Output result as required
print(f"Target result: {final_diagnostic}")