def analyze_signal_strength(signal_data, threshold=0.75):
    filtered = [x for x in signal_data if x > threshold]
    return len(filtered) / len(signal_data) if signal_data else 0


def compute_entropy(values):
    from math import log2
    total = sum(values)
    if total == 0:
        return 0
    probabilities = [v / total for v in values]
    entropy = -sum(p * log2(p) for p in probabilities if p > 0)
    return round(entropy, 4)


def transform_sequence(seq):
    # Distractor: modifies sequence but not used in final path
    shifted = seq[-3:] + seq[:-3]
    mirrored = shifted[::-1]
    return [x ^ 1 for x in mirrored]  # Bitwise distraction


def validate_checksum(data):
    # Irrelevant validation function (dead code path)
    checksum = sum(data[i] * (i + 1) for i in range(len(data))) % 256
    return checksum == 42


def calculate_efficiency(ratio, mode='advanced'):
    if mode == 'basic':
        return int(ratio * 100)
    else:
        base = ratio ** 2
        adjusted = base * (1 + (ratio / 10))
        return round(adjusted * 1000)  # Red herring output


def evaluate_performance(metrics, weights):
    # Core logic begins
    weighted_sum = 0.0
    for i in range(len(metrics)):
        if i % 2 == 0:
            weighted_sum += metrics[i] * weights[i] * 1.1  # Boost even indices
        else:
            weighted_sum += metrics[i] * weights[i] * 0.9  # Reduce odd indices

    # Apply non-linear scaling based on combinatorics of active metrics
    active_count = sum(1 for m in metrics if m > 0.5)
    combination_factor = 1
    for k in range(1, active_count + 1):
        combination_factor += 1 / (k + 1)  # Harmonic-like series addition

    intermediate = weighted_sum * combination_factor

    # Use slicing to extract critical subset
    critical_slice = metrics[1:4]  # indices 1,2,3
    slice_adjustment = sum(critical_slice) / len(critical_slice) if critical_slice else 0

    # Final transformation with integer division and rounding
    result = int((intermediate + slice_adjustment * 2) * 100) // 7

    # Decoy assignment (misleading)
    result = result + 5000  # This will be ignored due to scope below

    # Actual final score computed here
    final_score = (intermediate * 100) // 7 + int(slice_adjustment * 100)

    return final_score

# Main execution block
if __name__ == '__main__':
    # Input data
    raw_signals = [0.82, 0.67, 0.91, 0.73, 0.55, 0.88]
    entropy_source = [4, 5, 1, 3, 5, 2, 4]
    sequence_input = [1, 0, 1, 1, 0, 0]
    dummy_data = [12, 34, 56, 78, 90]

    # Irrelevant transformations
    signal_quality = analyze_signal_strength(raw_signals)
    entropy_value = compute_entropy(entropy_source)
    transformed_seq = transform_sequence(sequence_input)
    is_valid = validate_checksum(dummy_data)
    efficiency_score = calculate_efficiency(signal_quality, mode='advanced')

    # Core metric arrays (only these matter for final answer)
    metrics = [0.8, 0.9, 0.75, 0.85, 0.6]
    benchmark_weights = [0.2, 0.3, 0.15, 0.25, 0.1]

    # Key computation
    final_score = evaluate_performance(metrics, benchmark_weights)

    # Output target result
    print(f"Target result: {final_score}")