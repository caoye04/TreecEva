def evaluate_performance(metrics, baseline):
    # Irrelevant transformation: case conversion and string manipulation
    labels = ['System_A', 'System_B', 'System_C']
    upper_labels = [label.upper() for label in labels]
    reversed_labels = [label[::-1] for label in upper_labels]

    # Distractor: unused data structure
    historical_data = {
        'Q1': {'load': 85, 'errors': 3},
        'Q2': {'load': 90, 'errors': 2},
        'Q3': {'load': 87, 'errors': 4}
    }

    # Relevant computation begins
    adjusted_metrics = {}
    for k, v in metrics.items():
        if k in ['response_time', 'throughput', 'availability']:
            adjusted_metrics[k] = v * 1.1 if v > baseline[k] else v * 0.95

    # Slice relevant keys for processing
    key_indicators = list(adjusted_metrics.keys())[:3]

    # Intermediate calculation with semi-relevant logic
    performance_bonuses = []
    for i, key in enumerate(key_indicators):
        raw_val = adjusted_metrics[key]
        bonus = (raw_val - baseline[key]) / baseline[key]
        if bonus > 0:
            performance_bonuses.append(bonus * 100)

    # Secondary distractor: dead code path (never executed due to fixed condition)
    debug_mode = False
    if debug_mode:
        print("Debugging info:", performance_bonuses)

    # Core logic: compute final score using bonuses and base adjustments
    base_score = 0
    for key in key_indicators:
        base_score += adjusted_metrics[key]

    bonus_factor = sum(performance_bonuses) / 100 if performance_bonuses else 0.05

    # Final computation
    final_score = base_score * (1 + bonus_factor)

    # Print result as required
    return int(final_score)

# Input data
metrics = {
    'response_time': 95,
    'throughput': 120,
    'availability': 99.8,
    'bandwidth': 450  # irrelevant metric
}
baseline = {
    'response_time': 100,
    'throughput': 110,
    'availability': 99.5
}

# Execution point
final_score = evaluate_performance(metrics, baseline)
print(f"Result: {final_score}")