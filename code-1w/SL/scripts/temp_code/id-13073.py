def preprocess_signal(signal, threshold=0.75):
    """Irrelevant preprocessing function for noise filtering."""
    return [s * 0.9 for s in signal if s > threshold]


def compute_entropy(data):
    """Misleading function: computes Shannon entropy but not used in final result."""
    from math import log
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    total = len(data)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p)
    return round(entropy, 6)

def extract_features(dataset, mode='advanced'):
    """Distraction: complex feature extraction that isn't used."""
    features = []
    for i, row in enumerate(dataset):
        if i % 2 == 0:
            features.append(sum([x ** 0.5 for x in row if x > 0]))
    return features

def validate_checksum(sequence):
    """Dead code path: validates XOR checksum, never called."""
    xor_sum = 0
    for val in sequence:
        xor_sum ^= (val & 0xFF)
    return xor_sum == 0xAA

def aggregate_metrics(sensor_log, calibration):
    """Core function: computes diagnostic score based on bit patterns and alignment."""
    # Key variables
    baseline_shift = 0
    bit_correlation = 0
    match_count = 0

    # Irrelevant initialization (distractor)
    anomaly_flags = [False] * len(sensor_log)
    temporal_weights = [0.5 ** i for i in range(len(calibration))]

    # Real logic starts here
    for idx, record in enumerate(sensor_log):
        if idx >= len(calibration):
            continue
        
        # Compute aligned bit difference
        calibrated_val = calibration[idx]
        raw_val = record[0]  # Only first element matters
        
        # Extract lower 8 bits and XOR
        xor_bits = (raw_val ^ calibrated_val) & 0xFF
        
        # Count set bits (population count)
        ones = bin(xor_bits).count('1')
        
        # Accumulate only when index is odd (critical condition)
        if idx % 2 == 1:
            match_count += ones

        # Side computation: affects nothing (red herring)
        if ones > 4:
            anomaly_flags[idx] = True

    # Another distraction: unused transformation
    reshaped_data = list(zip(*sensor_log))
    transposed_mean = sum(reshaped_data[0]) / len(reshaped_data[0]) if reshaped_data else 0

    # Core calculation (depends only on match_count)
    scaling_factor = 12.5
    adjustment = -3
    
    # Final metric built from controlled steps
    intermediate = match_count * scaling_factor
    final_diagnostic = int(intermediate + adjustment)

    return final_diagnostic

# Main execution block
if __name__ == '__main__':
    # Simulated turbine sensor readings (list of lists)
    turbine_data = [
        [203, 156, 12],
        [198, 144, 10],
        [205, 160, 13],
        [199, 158, 11],
        [201, 155, 14]
    ]

    # Calibration reference (XOR baseline)
    calibration_sequence = [195, 205, 190, 210, 198]

    # Dead variables (distractors)
    sampling_rate = 1000  # Hz
    gain_factor = 2.0
    offset_table = {i: i*3 + 1 for i in range(10)}
    metadata_tags = ['A7', 'B2', 'C9']

    # Signal processing chain (irrelevant calls)
    filtered = preprocess_signal([row[0] for row in turbine_data])
    features = extract_features(turbine_data)

    # Actual answer-producing call
    final_diagnostic = aggregate_metrics(turbine_data, calibration_sequence)

    # Print result as required
    print(f"Result: {final_diagnostic}")