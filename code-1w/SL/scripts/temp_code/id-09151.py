import itertools

def analyze_sequence(data):
    # Irrelevant analysis function (dead code path)
    return sum(x ** 2 for x in data if x > 0)

def compute_weighted_sum(values, weights):
    # Unused helper with misleading relevance
    return sum(v * w for v, w in zip(values, weights))

def filter_outliers(sequence, threshold=3.0):
    mean_val = sum(sequence) / len(sequence)
    std_dev = (sum((x - mean_val) ** 2 for x in sequence) / len(sequence)) ** 0.5
    return [x for x in sequence if abs(x - mean_val) / std_dev < threshold]

def build_lookup(keys, values):
    # Distractor: builds a dict but not used in main logic
    lookup = {}
    for k, v in zip(keys, values):
        lookup[k] = v * 1.5
    return lookup

def evaluate_performance(metrics, reference):
    # Core logic starts here
    base_scores = []
    for i, val in enumerate(metrics):
        if i % 2 == 0:
            base_scores.append(val * 1.1)
        else:
            base_scores.append(val * 0.9)

    # Apply filtering (some values may be modified)
    adjusted = [x + 0.5 for x in base_scores]

    # Simulate normalization against benchmark
    norm_factor = sum(reference) / 100.0
    normalized = [x / norm_factor for x in adjusted]

    # Bit manipulation red herring
    magic_offset = 0
    temp = int(norm_factor)
    for _ in range(3):
        temp = (temp ^ 15) << 1
        magic_offset += temp & 255

    # Real contribution: aggregate using itertools.cycle to pair with rotating weights
    weights = [0.8, 1.2, 0.9]
    weighted_total = 0
    weight_cycle = itertools.cycle(weights)
    for val, wt in zip(normalized, weight_cycle):
        weighted_total += val * wt
        if weighted_total > 100:  # Decoy condition (never reached)
            break

    # Additional distraction: unused dictionary transformation
    stats = {f"item_{i}": v * v for i, v in enumerate(normalized)}

    # Final adjustment based on length parity (relevant)
    if len(normalized) % 2 == 1:
        final_score = int(weighted_total - magic_offset * 0.1)
    else:
        final_score = int(weighted_total)

    return final_score

# Main execution block
if __name__ == "__main__":
    # Input data
    metrics = [45, 67, 89, 23, 56]
    benchmark_data = [10, 20, 30, 40, 50, 60]

    # Dead computations - irrelevant assignments
    shadow_metrics = [x * 1.05 for x in metrics]
    outlier_free = filter_outliers(shadow_metrics, threshold=2.5)
    lookup_table = build_lookup(['a', 'b', 'c'], [10, 20, 30])
    dummy_result = analyze_sequence(metrics)

    # Key statement
    final_score = evaluate_performance(metrics, benchmark_data)

    # Output result
    print(f"Result: {final_score}")