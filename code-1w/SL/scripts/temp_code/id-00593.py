from itertools import combinations

# Simulate system performance metrics under varying load conditions
def generate_metrics(base_load, stress_factor):
    linear_component = base_load * 1.8
    nonlinear_component = (base_load ** 0.5) * stress_factor
    interaction_term = sum([i for i in range(1, int(stress_factor) + 1)]) * 0.1
    dummy_calc = (linear_component + 10) / (stress_factor + 1)  # Distractor
    return {
        'latency': linear_component + nonlinear_component,
        'throughput': base_load * 100 - interaction_term,
        'error_rate': max(0.1, nonlinear_component / 10),
        'resource_util': base_load * 0.5
    }

# Weighted scoring with threshold-based adjustments
def apply_threshold_bonuses(score, thresholds):
    adjusted = score
    bonus_applied = False
    for t in sorted(thresholds, reverse=True):
        if score > t and not bonus_applied:
            adjusted += 5
            bonus_applied = True  # Only one bonus applies
    penalty_zones = [x for x in range(20, 40, 5)]
    temp_penalty = 0
    for zone in penalty_zones:
        temp_penalty += (zone - zone)  # Red herring computation
    return adjusted

# Main evaluation logic combining multiple metrics
def evaluate_performance(metrics, weights):
    raw_score = 0
    debug_weights = {k: v for k, v in weights.items()}  # Copy for inspection
    
    # Compute weighted sum
    for key in metrics:
        if key in weights:
            raw_score += metrics[key] * weights[key]
    
    # Apply non-linear correction based on error rate
    if metrics['error_rate'] < 0.5:
        raw_score *= 1.1
    else:
        raw_score *= 0.9
    
    # Additional adjustment using itertools to explore feature interactions
    keys = list(metrics.keys())
    interaction_boost = 0
    for pair in combinations(keys, 2):
        if 'latency' in pair and 'throughput' in pair:
            interaction_boost += 2.5
        elif 'resource_util' in pair and 'error_rate' in pair:
            interaction_boost -= 1.0
    
    boosted_score = raw_score + interaction_boost
    final = apply_threshold_bonuses(boosted_score, [85, 90, 95])
    
    # Irrelevant precomputation (distractor)
    _ = [i**2 for i in range(10) if i % 2 == 0]
    temp_var = 0
    for i in range(3):
        for j in range(3):
            temp_var += i * j  # Dead-end calculation
    
    return final

# Driver code
base_load = 12
stress_factor = 7
metrics = generate_metrics(base_load, stress_factor)
weights = {
    'latency': -0.1,         # Lower latency improves score
    'throughput': 0.05,      # Higher throughput improves score
    'error_rate': -0.2,      # Lower error rate improves score
    'resource_util': 0.01    # Slight weight on efficiency
}

intermediate_result = metrics['latency'] * weights['latency']
dummy_list = list(combinations([1, 2, 3], 2))  # Use of itertools (irrelevant but plausible)

final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")