def analyze_metrics(data, threshold=0.75):
    weighted_sum = 0
    normalization_factor = len(data) * (len(data) + 1) / 2
    temp_buffer = []

    for i, entry in enumerate(reversed(data)):
        raw_value = entry['metric'] * (i + 1)
        adjusted = raw_value * (entry.get('weight', 1.0) or 1.0)
        temp_buffer.append(adjusted)
        weighted_sum += adjusted

    avg_temp = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
    return weighted_sum / normalization_factor if normalization_factor else 0


def evaluate_performance(config):
    readings = [
        {'metric': 0.8, 'weight': 1.2},
        {'metric': 0.6, 'weight': 0.9},
        {'metric': 0.9, 'weight': 1.5},
        {'metric': 0.7}
    ]

    base_score = analyze_metrics(readings)
    
    # Distraction block: irrelevant statistics
    outlier_count = 0
    for r in readings:
        if r['metric'] > 0.85:
            outlier_count += 1
    deviation_estimate = (outlier_count * 1.7) ** 0.5

    # Conditional expression with side-effect-free computation
    penalty = 0.1 if any(r['metric'] < 0.5 for r in readings) else 0.05
    bonus = 0.08 if all(r.get('weight', 1.0) >= 0.9 for r in readings) else 0

    # Core logic
    stability_check = [readings[i]['metric'] >= readings[i-1]['metric'] for i in range(1, len(readings))]
    trend_score = sum(stability_check) / len(stability_check) if stability_check else 0

    final_score = (base_score * 0.6) + (trend_score * 0.3) + (bonus - penalty)

    # Unused derived values to increase cognitive load
    projected_next = base_score * (1 + trend_score * 0.1)
    volatility_index = max(r['metric'] for r in readings) - min(r['metric'] for r in readings)

    return final_score

# Main execution
config_settings = {"mode": "strict", "version": 2}
result = evaluate_performance(config_settings)
final_score = round(result * 100, 2)
print(f"Result: {final_score}")