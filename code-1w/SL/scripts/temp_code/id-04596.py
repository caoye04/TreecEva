def analyze_efficiency(data, threshold=0.75):
    if not data:
        return 0
    processed = [x for x in data if x > threshold]
    return len(processed) / len(data) if data else 0

optimization_levels = [0.62, 0.78, 0.85, 0.67, 0.91, 0.73, 0.88]

def adjust_weights(values, factor=1.1):
    temp_result = 0
    for i, val in enumerate(values):
        if i % 3 == 0:
            temp_result += val * factor
        elif i % 3 == 1:
            temp_result += val + 0.05
        else:
            temp_result += val ** 0.5
    return temp_result // 1  # integer division

baseline_config = {
    'tolerance': 0.05,
    'active': True,
    'mode': 'aggressive',
    'version': 2
}

legacy_thresholds = [0.5, 0.6, 0.7, 0.8]
obsolete_flag = False

intermediate_metrics = []
for idx, level in enumerate(optimization_levels):
    score = level * (idx + 1)
    normalized = score / (score + 0.1)
    intermediate_metrics.append(normalized)

# Irrelevant transformation chain
buffer_data = [round(x, 2) for x in intermediate_metrics]
decoy_sum = sum(buffer_data[:3]) * 1.5
offset_correction = len(buffer_data) > 5

# Distractor: fake aggregation path
aggregate_snapshot = {
    'raw': optimization_levels.copy(),
    'temp_adj': adjust_weights(optimization_levels),
    'meta': {'processed': True, 'valid': False}
}

if aggregate_snapshot['meta']['valid']:
    final_normalization = 0
else:
    filtered_metrics = [m for m in intermediate_metrics if m > 0.65]
    efficiency_ratio = analyze_efficiency(filtered_metrics, 0.7)
    adjusted_ratio = efficiency_ratio * 1.2 if efficiency_ratio > 0.5 else efficiency_ratio * 0.8
    
    # Key distraction: complex but unused calculation
    shadow_calc = 0
    for x in filtered_metrics:
        shadow_calc += x ** 2
    shadow_calc = round(shadow_calc, 3)
    
    # Real computation path starts here
    base_value = sum(filtered_metrics) * 100
    penalty = 0
    if len(filtered_metrics) < 5:
        penalty = 15
    bonus = 10 if adjusted_ratio >= 0.8 else 5 if adjusted_ratio >= 0.6 else 0
    
    metrics = {
        'base': base_value,
        'penalty': penalty,
        'bonus': bonus,
        'count': len(filtered_metrics),
        'ratio': adjusted_ratio
    }

# Dead function - never called
def deprecated_evaluation(vec):
    return sum(vec) / (max(vec) - min(vec))

auxiliary_cache = {}
temp_key = 'interim'

# Misleading early assignment
final_score = 42  # This will be overwritten

# Critical execution point
final_score = evaluate_performance(metrics, baseline_config)

# Actual function definition after usage (legal in Python due to def hoisting in execution)
def evaluate_performance(perf_metrics, config):
    if not config['active']:
        return 0
    
    raw_base = perf_metrics['base']
    net_adjustment = perf_metrics['bonus'] - perf_metrics['penalty']
    
    # Simulated calibration
    calibration_factor = 1.0
    if perf_metrics['count'] >= 4:
        calibration_factor += 0.1
    if perf_metrics['ratio'] > 0.75:
        calibration_factor += 0.05
    
    # Composite calculation with rounding
    calibrated = raw_base * calibration_factor
    result = calibrated + net_adjustment
    
    # Final gate
    tolerance_band = config['tolerance'] * 100
    if abs(result - 400) < tolerance_band:
        return 400
    
    return int(round(result))

print(f"Target result: {final_score}")