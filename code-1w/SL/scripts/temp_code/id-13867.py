def calculate_performance(data):
    # Preprocessing: extract relevant metrics
    raw_values = [entry['metric'] for entry in data]
    weights = list(map(lambda x: 0.5 if x < 50 else 0.8, raw_values))

    # Irrelevant transformation: baseline adjustment (not used in final calculation)
    baseline_adjusted = [val - 10 for val in raw_values if val > 20]
    offset_correction = sum(baseline_adjusted) / len(baseline_adjusted) if baseline_adjusted else 0

    # Core computation
    weighted_sum = sum(val * weight for val, weight in zip(raw_values, weights))
    total_weight = sum(weights)
    average_performance = weighted_sum / total_weight if total_weight else 0

    # Secondary metric: count high performers (distractor)
    high_performers = len([v for v in raw_values if v >= 75])
    bonus_factor = 1.1 if high_performers > 2 else 1.0

    # Final scoring with conditional scaling
    if average_performance >= 60:
        final_score = average_performance * bonus_factor
    else:
        final_score = average_performance * 0.9

    # Unused diagnostic log
    diagnostics = {
        'input_count': len(data),
        'max_raw': max(raw_values),
        'min_raw': min(raw_values),
        'offset': offset_correction
    }

    return final_score

# Input data
benchmark_data = [
    {'id': 1, 'metric': 45},
    {'id': 2, 'metric': 82},
    {'id': 3, 'metric': 67},
    {'id': 4, 'metric': 91},
    {'id': 5, 'metric': 54}
]

# Execute and print result
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")