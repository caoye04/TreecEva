def analyze_pattern(sequence):
    """Irrelevant function analyzing sequence patterns."""
    count = 0
    for i in range(len(sequence)):
        if sequence[i] == (i % 3):
            count += 1
    return count * 2

# Irrelevant data structures
test_sequence = [0, 1, 2, 0, 1, 2, 0]
dummy_result = analyze_pattern(test_sequence)

# Real metric processing
metric_weights = {
    'accuracy': 0.4,
    'latency': 0.3,
    'throughput': 0.2,
    'energy': 0.1
}

raw_results = {
    'accuracy': 92.5,
    'latency': 75.0,
    'throughput': 88.0,
    'energy': 64.0
}

# Decoy normalization function (never used)
normalize_metric = lambda x, m: round((x / m) * 100, 2)

# Actual weighted scoring with distractors
def apply_weight(value, weight):
    """Apply weight to a metric value."""
    return value * weight

def adjust_for_baseline(score, base=50):
    """Adjust score relative to baseline (distractor)."""
    if score > base:
        return score + (score - base) * 0.1
    return score

# Unused recursive reducer
def reduce_scores(scores_list, idx=0):
    if idx == len(scores_list) - 1:
        return scores_list[idx]
    return scores_list[idx] + 0.5 * reduce_scores(scores_list, idx + 1)

# Misleading intermediate calculation
temp_adjusted = {}
for k, v in raw_results.items():
    temp_adjusted[k] = adjust_for_baseline(v) if v > 70 else v

# Core evaluation logic hidden among noise
evaluate_performance = lambda weights, results: sum(
    apply_weight(results[metric], weights[metric]) 
    for metric in weights
)

# Dead code path - looks important but unused
consolidated_metrics = []
for key in sorted(raw_results.keys()):
    normalized = normalize_metric(raw_results[key], 100)
    consolidated_metrics.append((key, normalized))

# Key execution point
final_score = evaluate_performance(metric_weights, raw_results)

# Print required result
print(f"Result: {final_score}")