def calculate_final_score(data, importance):
    # Irrelevant pre-processing: normalize keys (distractor)
    normalized_keys = {k.strip().lower(): v for k, v in data.items()}
    temp_values = [v ** 0.5 for v in importance.values()]  # Unused transformation

    # Semi-relevant: filter only high-priority metrics
    priority_metrics = {k: v for k, v in data.items() if 'performance' in k or 'efficiency' in k}

    # Core logic: weighted harmonic mean of selected results
    weighted_inv = sum(
        importance[k] / v if v != 0 else 0
        for k, v in priority_metrics.items()
    )
    total_weight = sum(importance[k] for k in priority_metrics)
    harmonic_base = total_weight / weighted_inv if weighted_inv != 0 else 0

    # Additional distraction: exponential decay adjustment (not used)
    decay_adjustment = lambda x: x * 0.95 ** len(data)
    _ = decay_adjustment(harmonic_base)  # Dead computation

    # Use dictionary and set operations to determine bonus multiplier
    metric_names = set(data.keys())
    bonus_triggers = {'performance_alpha', 'efficiency_zeta'}
    bonus_multiplier = 1.2 if bonus_triggers.issubset(metric_names) else 1.0

    # Final score with bonus
    raw_score = harmonic_base * bonus_multiplier
    offset = len(priority_metrics) - len(normalized_keys)  # Red herring
    final_score = int(raw_score - offset * 0.1)  # Deterministic integer result

    return final_score

# Main execution block
dataset = {
    'performance_alpha': 12.0,
    'efficiency_zeta': 8.0,
    'performance_beta': 16.0,
    'memory_usage': 4.5,  # Not in priority
    'latency': 20.0       # Not in priority
}

weights_scheme = {
    'performance_alpha': 3,
    'efficiency_zeta': 2,
    'performance_beta': 1,
    'latency': 1
}

# Key statement
temp_result = {k: v + 1 for k, v in dataset.items()}  # Distractor assignment
final_score = calculate_final_score(dataset, weights_scheme)
print(f"Result: {final_score}")