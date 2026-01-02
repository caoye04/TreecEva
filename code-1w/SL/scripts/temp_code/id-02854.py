from itertools import compress, cycle

def main():
    # System parameters for network channel optimization
    base_frequencies = [2.4, 3.6, 4.9, 5.2, 5.7]
    signal_strengths = [88, 75, 94, 67, 82]
    interference_levels = [31, 45, 22, 53, 38]

    # Derived metrics
    snr_ratios = [s / i for s, i in zip(signal_strengths, interference_levels)]
    weighted_scores = [(f * snr) for f, snr in zip(base_frequencies, snr_ratios)]

    # Threshold logic with distractor variables
    avg_score = sum(weighted_scores) / len(weighted_scores)
    deviation_from_avg = [abs(ws - avg_score) for ws in weighted_scores]
    outlier_mask = [d > 1.5 for d in deviation_from_avg]  # Not actually used later

    # Efficiency computation with red herring transformations
    efficiency_candidates = []
    temp_accumulator = 0
    for idx, score in enumerate(weighted_scores):
        if idx % 2 == 0:
            temp_accumulator += score * 0.9
        else:
            temp_accumulator += score * 1.1
        efficiency_candidates.append(temp_accumulator)

    # Irrelevant normalization attempt (dead-end path)
    max_efficiency = max(efficiency_candidates)
    normalized_efficiency = [e / max_efficiency for e in efficiency_candidates]  # Unused

    # Core logic: generate binary pattern based on SNR and apply filtering
    snr_flags = [snr > 2.0 for snr in snr_ratios]
    filtered_scores = list(compress(weighted_scores, snr_flags))

    # Simulate cyclic load balancing across 3 virtual nodes
    load_cycle = cycle([1, 2, 3])
    node_loads = [next(load_cycle) for _ in range(len(filtered_scores))]

    # Aggregate by node (unnecessary complexity)
    aggregated_by_node = [0, 0, 0]
    for i, fs in enumerate(filtered_scores):
        node_idx = node_loads[i] - 1
        aggregated_by_node[node_idx] += fs

    # Final thresholding and efficiency log generation
    threshold = sum(aggregated_by_node) / len(aggregated_by_node) * 0.75
    efficiency_log = [fs for fs in filtered_scores if fs > threshold]

    # Misleading bitwise adjustment (appears important but unused)
    magic_key = 0b1010
    shifted_scores = [int(fs) ^ magic_key for fs in efficiency_log]  # Distractor

    # Critical assignment: optimization function applied to efficiency log
    final_bandwidth = optimize_allocation(efficiency_log, threshold)

    # Print result as required
    print(f"Result: {final_bandwidth}")

    return final_bandwidth


def optimize_allocation(log, thresh):
    # Simple but disguised formula: sum of squares divided by threshold, floored
    if not log:
        return 0
    raw_sum_sq = sum(x ** 2 for x in log)
    adjustment_factor = 1.25
    return int((raw_sum_sq / thresh) // adjustment_factor)

# Unused helper - adds cognitive load
def calculate_entropy(data):
    from math import log2
    total = sum(data)
    probabilities = [x / total for x in data]
    return -sum(p * log2(p) for p in probabilities if p > 0)

# Execute program
result = main()