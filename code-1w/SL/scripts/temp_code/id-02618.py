def evaluate_performance(metrics, weights):
    # Normalize metrics using min-max scaling (irrelevant for final logic but adds cognitive load)
    normalized = {}
    for k, v in metrics.items():
        normalized[k] = (v - 50) / 50 if v > 50 else 0.0

    # Distractor: Calculate entropy-like measure (not used in result)
    import math
    entropy = 0.0
    for v in metrics.values():
        if v > 0:
            entropy -= (v / 100) * math.log(v / 100 + 1e-9)

    # Key logic begins: filter high-performing categories
    passing = {k: v for k, v in metrics.items() if v >= 75}
    
    # Bonus logic: if 'latency' is low and 'throughput' is high, apply multiplier
    bonus_applied = False
    throughput_score = metrics.get('throughput', 0)
    latency_score = metrics.get('latency', 100)
    energy_score = metrics.get('energy', 50)
    security_score = metrics.get('security', 50)

    efficiency_ratio = throughput_score / (latency_score + 1)  # Avoid division by zero
    
    # Conditional expression with slicing distraction
    category_slice = list(passing.keys())[::2] if len(passing) > 1 else list(passing.keys())
    slice_influence = len(category_slice) * 2

    base_score = sum(passing.values())

    # Apply conditional bonus
    if efficiency_ratio > 0.8 and energy_score > 60:
        base_score *= 1.2
        bonus_applied = True
    
    # Bitwise flag check for security-hardened systems
    security_flag = security_score & 15  # Lower nibble as status
    if security_flag >= 8:
        base_score += 10

    # Final adjustment using weighted sum on original weights (key insight)
    weighted_sum = sum(metrics[k] * weights[k] for k in metrics if k in weights)
    
    # Critical decision point: use adjusted base_score only if no major failures
    has_critical_failure = any(v < 40 for v in metrics.values())
    
    final_score = base_score if not has_critical_failure else weighted_sum * 0.5
    
    # Red herring: unused data structure
    summary_report = {
        'metrics': metrics.copy(),
        'normalized': normalized,
        'entropy': round(entropy, 3),
        'bonus_applied': bonus_applied,
        'audit_trail': [f'{k}:{v}' for k, v in metrics.items() if v > 70]
    }

    return int(final_score)

# Main execution
metrics = {
    'throughput': 88,
    'latency': 70,
    'energy': 68,
    'security': 85,
    'usability': 90
}
benchmark_weights = {
    'throughput': 0.3,
    'latency': 0.2,
    'energy': 0.15,
    'security': 0.25,
    'usability': 0.1
}

# Key statement
final_score = evaluate_performance(metrics, benchmark_weights)
print(f"Result: {final_score}")