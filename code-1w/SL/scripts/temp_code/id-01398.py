import math

def preprocess_signals(raw_data):
    # Irrelevant preprocessing function (dead code path)
    return [x * 1.05 for x in raw_data if x > 0]

def validate_calibration(calib_seq):
    # Misleading validation logic
    checksum = sum((i+1) * val for i, val in enumerate(calib_seq))
    return checksum % 17 == 0

def generate_phase_shift(n):
    # Distractor: generates unused phase patterns
    return [(math.sin(i * 0.5) + math.cos(i * 0.3)) for i in range(n)]

def accumulate_momentum(buffer, factor=0.85):
    # Red herring computation
    momentum = 0
    for val in buffer:
        momentum = momentum * factor + val
    return round(momentum, 4)

def calculate_entropy(sequence):
    # Decoy function: looks important but unused in critical path
    from collections import Counter
    counts = Counter(sequence)
    total = len(sequence)
    entropy = -sum((count/total) * math.log2(count/total) for count in counts.values())
    return round(entropy, 4)

def extract_core_features(dataset):
    # Unused complex transformation
    features = []
    for row in dataset:
        sq = sum(x**2 for x in row)
        norm = math.sqrt(sq) if sq > 0 else 0
        features.append([x/norm for x in row] if norm > 0 else row)
    return features

def calculate_efficiency(matrix, thresholds):
    # Core logic embedded within noise
    rows, cols = len(matrix), len(matrix[0])
    aggregated = [0] * cols
    
    # Accumulate column sums only for values above dynamic threshold
    for i in range(rows):
        dynamic_factor = (i + 1) / rows
        for j in range(cols):
            if matrix[i][j] > thresholds[j] * dynamic_factor:
                aggregated[j] += matrix[i][j] * 0.75
    
    # Real computation begins here — mean of non-zero aggregates
    non_zero = [val for val in aggregated if val > 0]
    if not non_zero:
        return 0.0
    
    base_efficiency = sum(non_zero) / len(non_zero)
    
    # Apply correction based on sparsity
    sparsity_ratio = len(non_zero) / len(aggregated)
    if sparsity_ratio > 0.6:
        base_efficiency *= 1.2
    else:
        base_efficiency *= 0.85
    
    # Final adjustment using bitwise manipulation (actual use)
    intensity_flag = sum(1 for row in matrix for x in row if x > 50)
    shift_level = (intensity_flag & 7)  # Use lower 3 bits
    adjusted = base_efficiency * (1 + (shift_level * 0.025))
    
    return round(adjusted, 6)

# Main execution with multiple distractions
if __name__ == '__main__':
    # Irrelevant sensor calibration sequence (misleads with importance)
    calibration_sequence = [3, 7, 2, 9, 5, 8, 1, 6, 4]
    is_valid = validate_calibration(calibration_sequence)

    # Fake signal processing pipeline
    raw_signals = [12.3, 45.1, 67.8, 23.4, 89.0]
    filtered = preprocess_signals(raw_signals)
    phase_pattern = generate_phase_shift(10)

    # Momentum accumulation on decoy data
    dummy_buffer = [0.5, 1.2, 0.8, 1.6, 0.9]
    momentum_score = accumulate_momentum(dummy_buffer)

    # Entropy calculation on unrelated pattern
    test_sequence = [1, 1, 0, 1, 0, 0, 1, 1]
    bit_entropy = calculate_entropy(test_sequence)

    # REAL INPUT DATA (buried among distractors)
    flow_matrix = [
        [30, 60, 90, 25],
        [70, 85, 40, 65],
        [50, 95, 75, 35],
        [80, 70, 85, 45]
    ]
    
    threshold_map = [40, 65, 50, 30]

    # Critical assignment — this is what the question targets
    thermal_gradient = calculate_efficiency(flow_matrix, threshold_map)

    # Extra red herring: unpacking unrelated results
    feature_set = extract_core_features(flow_matrix)
    avg_features = [sum(col)/len(col) for col in zip(*feature_set)] if feature_set else []

    # Print final target result as required
    print(f"Result: {thermal_gradient}")