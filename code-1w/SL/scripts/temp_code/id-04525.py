def evaluate_performance(weights, results):
    # Normalize results using min-max scaling (irrelevant for final score but adds computation)
    min_val = min(results.values())
    max_val = max(results.values())
    normalized = {k: (v - min_val) / (max_val - min_val + 1e-8) for k, v in results.items()}

    # Misleading transformation: apply logarithmic adjustment (not used in final logic)
    log_adjusted = {k: round(10 * (v + 1)) for k, v in normalized.items()}

    # Key metric mapping with lambda-based scoring rules
    scoring_rules = {
        'accuracy': lambda x: x * 0.4,
        'latency': lambda x: (1 - x) * 0.3,  # Inverted since lower latency is better
        'throughput': lambda x: x * 0.2,
        'energy': lambda x: (1 - x) * 0.1
    }

    # Apply bitwise mask to simulate hardware constraint (distractor)
    mask = 0b1111
    masked_weights = {k: w * mask & 0b1000 for k, w in weights.items()}  # Only upper bit matters? Not really used.

    # Actual weighted sum uses original weights and raw_results, ignoring normalized paths
    total = 0.0
    for metric, weight in weights.items():
        raw_value = results.get(metric, 0)
        if metric in scoring_rules:
            total += scoring_rules[metric](raw_value)

    # Additional distraction: sort normalized values (dead code path)
    sorted_norm = sorted(normalized.items(), key=lambda x: x[1], reverse=True)
    for i, (name, val) in enumerate(sorted_norm):
        if i > 2:  # truncate top 3
            break

    return round(total * 100, 4)  # Scale to percentage-like score


# Main execution
metric_weights = {
    'accuracy': 0.4,
    'latency': 0.3,
    'throughput': 0.2,
    'energy': 0.1
}

raw_results = {
    'accuracy': 0.92,
    'latency': 0.45,
    'throughput': 0.78,
    'energy': 0.63
}

# Placeholder variables (distractors)
dummy_data = [0.1, 0.2, 0.3]
data_checksum = sum(dummy_data) * 1000
temp_result = {k: v**2 for k, v in raw_results.items()}

# Critical statement
final_score = evaluate_performance(metric_weights, raw_results)

print(f"Result: {final_score}")