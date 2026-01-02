import itertools

def analyze_metrics(data, threshold=0.75):
    # Irrelevant preprocessing: counts string lengths in keys (distractor)
    key_lengths = [len(k) for k in data.keys()]
    avg_length = sum(key_lengths) / len(key_lengths) if key_lengths else 0

    # Semi-relevant transformation: normalize values
    normalized = {k: v / 100.0 for k, v in data.items()}

    # Filter based on threshold (actually used later)
    passed = {k: v for k, v in normalized.items() if v >= threshold}
    return passed, normalized

def calculate_performance(raw_data):
    # Simulate multi-stage evaluation pipeline

    # Step 1: Preprocess with auxiliary function
    filtered_results, full_normalized = analyze_metrics(raw_data, threshold=0.6)

    # Step 2: Generate combinations of metrics (itertools usage - relevant)
    metric_pairs = list(itertools.combinations(filtered_results.keys(), 2))
    pair_count = len(metric_pairs)

    # Step 3: Compute interaction score using lambda (relevant)
    interaction_fn = lambda x, y: round((x * y) ** 0.5, 4)
    interactions = []
    for a, b in metric_pairs:
        score_a = full_normalized[a]
        score_b = full_normalized[b]
        interactions.append(interaction_fn(score_a, score_b))

    base_score = sum(filtered_results.values()) * 100

    # Step 4: Apply conditional adjustment (critical branch)
    adjustment_factor = 1.0
    if pair_count > 3:
        adjustment_factor = 0.9
    elif pair_count == 0:
        adjustment_factor = 0.5
    else:
        adjustment_factor = 0.95

    # Step 5: Add noise from unused computation (distractor)
    temp_states = [0] * 5
    for i in range(len(temp_states)):
        temp_states[i] = (i + 1) * 17 % 7  # Dead-end calculation

    # Step 6: Final aggregation
    stability_penalty = len([x for x in interactions if x < 0.8]) * 2
    raw_final = base_score * adjustment_factor - stability_penalty

    # Final assignment
    final_score = int(round(raw_final))

    # Unused complex string operation (distractor)
    status_msg = "Evaluation complete: " + "_".join(filtered_results.keys()).upper().replace("_", "-")
    msg_checksum = sum(ord(c) for c in status_msg) % 100

    return final_score

# Main execution context
benchmark_data = {
    "throughput": 85,
    "latency": 92,
    "accuracy": 78,
    "consistency": 67,
    "scalability": 90,
    "robustness": 88
}

result = calculate_performance(benchmark_data)
print(f"Result: {result}")