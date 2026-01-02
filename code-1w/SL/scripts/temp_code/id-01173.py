def evaluate_performance(metrics, weights):
    # Normalize metrics (irrelevant for final result but adds cognitive load)
    normalized = {}
    for k, v in metrics.items():
        if v > 0:
            normalized[k] = (v - 10) / (20 - 10) if v != 20 else 1.0
        else:
            normalized[k] = 0

    # Distractor: Compute auxiliary scores with no impact
    aux_scores = []
    for i in range(3):
        temp = (i + 1) * 0.1
        aux_scores.append(temp ** 2)

    # Actual logic begins: transform key metric using modular arithmetic
    raw_efficiency = metrics['efficiency']
    adjusted_efficiency = (raw_efficiency * 13) % 97

    # Use dictionary and conditional expression
    bonuses = {
        'speed': 5 if metrics['response_time'] < 100 else 2,
        'accuracy': 8 if metrics['error_rate'] < 0.05 else 3,
        'load': metrics['max_throughput'] // 1000
    }

    # Simulated weight adjustments (some are unused)
    extended_weights = {**weights}
    extended_weights['temporal'] = 0.05  # Unused distractor
    extended_weights['stability'] = 0.12 # Not used

    # Core calculation chain
    base_score = 0
    base_score += adjusted_efficiency * weights['efficiency']
    base_score += metrics['uptime'] * weights['reliability']

    # Conditional bonus logic with tuple unpacking
    critical_bonuses = [bonuses['speed'], bonuses['accuracy']]
    speed_bonus, accuracy_bonus = critical_bonuses
    if speed_bonus > 3:
        base_score += accuracy_bonus
        multiplier = 1.25
    else:
        multiplier = 0.9

    # Final composition with misleading intermediate steps
    temp_result = base_score * multiplier
    noise_offset = sum(aux_scores) - 0.14  # evaluates to 0 due to prior computation
    final_score = int(temp_result + noise_offset) + bonuses['load']

    return final_score

# Main execution context
metrics = {
    'efficiency': 67,
    'response_time': 85,
    'error_rate': 0.03,
    'uptime': 99.7,
    'max_throughput': 12500
}

weights = {
    'efficiency': 1.5,
    'reliability': 0.8
}

# Key statement
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")