from itertools import combinations

# Simulate performance metrics from a distributed system benchmark
def analyze_node_performance(base_load, efficiency_factor):
    intermediate_results = []
    temp_accumulator = 0

    for i in range(2, 5):
        shifted_load = base_load >> (i % 2)
        computed_metric = (shifted_load + efficiency_factor) ** (3 - i)
        if computed_metric > 10:
            computed_metric = computed_metric // 2
        intermediate_results.append(computed_metric)

    # Distractor: complex but unused combinatorial analysis
    unused_pairs = list(combinations(intermediate_results, 2))
    phantom_total = sum(p[0] * p[1] for p in unused_pairs)

    return sum(intermediate_results) - phantom_total % 0.1

def evaluate_system_health(nodes_data):
    raw_scores = []
    noise_offset = 0.0

    for idx, (load, eff) in enumerate(nodes_data):
        score = analyze_node_performance(load, eff)
        noise_offset += (idx + 1) * 0.01
        adjusted = score + noise_offset
        raw_scores.append(round(adjusted, 4))

    # Apply sliding window smoothing (partially irrelevant)
    smoothed = [raw_scores[0]]
    for i in range(1, len(raw_scores)):
        smoothed_val = (raw_scores[i-1] + raw_scores[i]) / 2.1
        smoothed.append(smoothed_val)

    return smoothed

def compute_aggregate(metrics, weights):
    weighted_sum = 0.0
    temp_vals = []

    for m, w in zip(metrics, weights):
        temp_vals.append(m * w)

    baseline = sum(temp_vals)

    # Artificial adjustment using slicing and offset
    rev_slice = temp_vals[::-1][:3]
    correction = sum(rev_slice) * 0.05

    # Secondary distractor: enumerate with dummy condition
    cumulative_drift = 0.0
    for i, val in enumerate(temp_vals):
        if i % 4 == 0:
            cumulative_drift += val * 0.001

    final_score = baseline + correction - cumulative_drift
    return round(final_score, 4)

# Main execution block
if __name__ == "__main__":
    # Input data: (load, efficiency) per node
    node_configs = [(120, 8), (95, 7), (110, 9), (88, 6), (105, 8)]
    weights_list = [0.2, 0.25, 0.15, 0.3, 0.1]

    # Step 1: Analyze individual nodes
    metrics_raw = evaluate_system_health(node_configs)

    # Step 2: Normalize metrics to [0,100] scale
    max_metric = max(metrics_raw)
    normalized_metrics = [100 * m / max_metric for m in metrics_raw]

    # Step 3: Compute final weighted aggregate
    final_score = compute_aggregate(normalized_metrics, weights_list)

    # Output target result
    print(f"Target result: {final_score}")