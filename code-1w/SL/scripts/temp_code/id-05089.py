def evaluate_performance(metrics, weights):
    base_score = 0
    bonus_factor = 1.2
    penalty_threshold = 85
    temp_adjustment = 0

    # Irrelevant temperature simulation (distractor)
    for temp in range(3):
        temp_adjustment += (temp * 0.1) % 0.3

    # Real scoring logic begins
    raw_sum = sum(metrics[category] for category in ['accuracy', 'latency', 'throughput'])
    weight_sum = sum(weights[cat] for cat in weights)

    normalized = raw_sum / weight_sum if weight_sum else 0

    # Conditional bonus based on performance
    if metrics['accuracy'] >= penalty_threshold:
        base_score += normalized * 1.5
    else:
        base_score += normalized * 0.8

    # Unused path - dead code (distractor)
    if metrics['latency'] < 0:
        emergency_correction = True
        base_score *= 0.9

    # Bitwise check for feature flags (semi-relevant)
    feature_flags = metrics['feature_flags']
    if feature_flags & 4:  # indicates 'optimized'
        base_score += 5

    # Dictionary-based tier adjustment
    tier_bonuses = {'A': 10, 'B': 5, 'C': 0, 'D': -5}
    performance_tier = 'B'
    if metrics['accuracy'] > 90:
        performance_tier = 'A'
    elif metrics['accuracy'] < 70:
        performance_tier = 'C'

    base_score += tier_bonuses[performance_tier]

    # Final non-linear adjustment (relevant)
    final_score = int(base_score ** 0.95)

    return final_score

# Setup data
metrics = {
    'accuracy': 88,
    'latency': 12,
    'throughput': 45,
    'feature_flags': 6,  # binary: 110 -> includes 'optimized' (bit 2)
    'version': '2.1.3',
    'debug_mode': False
}

weights = {
    'accuracy': 4,
    'latency': 2,
    'throughput': 3
}

# Extraneous calculation (distractor)
dummy_tracker = [0]
for i in range(1, 4):
    dummy_tracker.append(dummy_tracker[-1] + i**2)

final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")