import itertools

# Simulated sensor data processing with red herrings and complex transformations
def process_sensor_array(raw_readings):
    filtered = [x for x in raw_readings if x > 0.1]
    shifted = [(x * 1.05) % 1.7 for x in filtered]
    
    # Irrelevant transformation branch (dead logic path)
    temp_buffer = []
    for val in shifted:
        temp_buffer.append(val ** 2 + 0.01)
    temp_buffer = [t for t in temp_buffer if t < 2.0]  # Unused downstream

    # Core slicing operation (relevant)
    windowed = shifted[::2]  # Every second element

    # Bit manipulation decoy
    bit_noise = 0
    for i in range(len(windowed)):
        bit_noise ^= int(windowed[i] * 100) & 0xF
    bit_noise += 100  # Distractor, not used later

    # Generate phase-shifted duplicates (red herring)
    phantom_slices = []
    for i in range(3):
        phantom_slices.append(shifted[i:i+4])

    # Real computation begins: encode segments using XOR folding
    def fold_sequence(seq):
        result = 0
        for item in seq:
            result ^= int(item * 1000)
        return result % 97

    encoded_segments = []
    for i in range(0, len(windowed) - 3, 3):
        chunk = windowed[i:i+3]
        encoded_segments.append(fold_sequence(chunk))

    # Decoy statistical analysis (misleading intermediate)
    mean_val = sum(windowed) / len(windowed) if windowed else 0
    variance_proxy = sum((x - mean_val) ** 2 for x in windowed) / len(windowed) if windowed else 0
    entropy_approx = -(mean_val * variance_proxy)  # Looks important, unused

    # Conditional expression chain with distractors
    threshold_flag = 'high' if mean_val > 0.5 else 'low'
    correction_factor = 1.1 if threshold_flag == 'high' else 0.9
    scaling_hint = correction_factor * 0.85 if variance_proxy > 0.1 else correction_factor * 1.2

    # Weight assignment with irrelevant combinatorics
    indices = list(range(len(encoded_segments)))
    combinations = list(itertools.combinations(indices, min(2, len(indices))) if len(indices) > 1 else [(0,)])
    combo_score = sum(abs(c[0] - c[-1]) if len(c) > 1 else 0 for c in combinations)  # Unused metric

    # Actual weights based on segment length (subtle but deterministic)
    base_weight = len(encoded_segments) if encoded_segments else 1
    weights = [base_weight * (i + 1) for i in range(len(encoded_segments))]

    # Final aggregation function (critical execution point)
    def aggregate_metrics(segments, wts):
        total = 0
        for seg, wt in zip(segments, wts):
            total += seg * wt
        return total % 100000

    final_diagnostic = aggregate_metrics(encoded_segments, weights)

    # Dead code path: alternate algorithm never reached
    if False:
        backup = 0
        for s in encoded_segments:
            backup += s << 2
        final_diagnostic = backup % 50000

    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Entry point with fixed input
sensor_input = [0.12, 0.91, 0.33, 0.08, 0.67, 1.05, 0.44, 0.21, 0.76, 0.52]
process_sensor_array(sensor_input)