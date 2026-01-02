def evaluate_performance(weights, results):
    # Normalize results using min-max scaling
    min_val = min(results.values())
    max_val = max(results.values())
    range_val = max_val - min_val if max_val != min_val else 1
    
    normalized = {k: (v - min_val) / range_val for k, v in results.items()}
    
    # Irrelevant transformation: reverse string keys (no effect on computation)
    reversed_keys = {k[::-1]: v for k, v in normalized.items()}
    dummy_lookup = {k.upper(): k.lower() for k in weights.keys()}

    # Weighted aggregation using lambda for dynamic scoring
    weighted_sum = sum(map(lambda item: normalized[item[0]] * weights.get(item[0], 0), weights.items()))
    total_weight = sum(weights.values())
    
    # Secondary score path (dead end - not used but looks important)
    geometric_mean_weight = (weights['accuracy'] * weights['efficiency']) ** 0.5
    shadow_score = (weighted_sum / total_weight) * 0.9 + 10  # Unused

    # Apply bonus for high consistency (actual logic branch)
    consistency_ratio = normalized['accuracy'] / normalized['reliability']
    bonus = 5 if consistency_ratio > 0.95 else 2
    
    # Final score calculation
    base_score = weighted_sum / total_weight * 100
    final_score = base_score + bonus
    
    # Extra red herring: simulate logging overhead
    log_entries = []
    for k, v in normalized.items():
        log_entries.append(f"Metric '{k}' scored {v:.3f}")
    # Simulated write (no side effects)
    
    return int(final_score)

# Main execution
metric_weights = {
    'accuracy': 0.4,
    'efficiency': 0.3,
    'latency': 0.1,
    'reliability': 0.2
}

raw_results = {
    'accuracy': 89,
    'efficiency': 76,
    'latency': 45,
    'reliability': 85
}

intermediate_total = sum(raw_results.values())  # Distractor variable
scaling_factor = intermediate_total / 100  # Misleading normalization hint

# Key statement
final_score = evaluate_performance(metric_weights, raw_results)
print(f"Result: {final_score}")