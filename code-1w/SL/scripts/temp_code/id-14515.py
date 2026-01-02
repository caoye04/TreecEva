def analyze_trend(values):
    if len(values) < 3:
        return False
    trend_up = all(values[i] <= values[i+1] for i in range(len(values)-1))
    trend_down = all(values[i] >= values[i+1] for i in range(len(values)-1))
    return trend_up or trend_down

initial_buffer = [12, 15, 22, 30, 38]
dummy_weights = [0.1, 0.2, 0.3, 0.2, 0.1]
weighted_sum = sum(initial_buffer[i] * dummy_weights[i] for i in range(len(initial_buffer)))

scaling_factor = 1.5
adjusted_values = [x * scaling_factor for x in initial_buffer if x > 20]

# Misleading transformation (not used in final result)
transformed = [x ** 0.5 for x in adjusted_values]
avg_transformed = sum(transformed) / len(transformed) if transformed else 0

metric_data = {
    'response_time': [100, 120, 90, 110],
    'success_rate': [0.92, 0.95, 0.89, 0.94],
    'retry_count': [2, 1, 3, 1]
}

thresholds = {
    'response_time': 115,
    'success_rate': 0.90,
    'retry_count': 2
}

status_flags = {
    key: sum(1 for val in metric_data[key] if (key == 'response_time' and val <= thresholds[key]) or \
                        (key == 'success_rate' and val >= thresholds[key]) or \
                        (key == 'retry_count' and val <= thresholds[key])) >= 2
    for key in metric_data.keys()
}

consistency_check = analyze_trend(metric_data['response_time'])

# Dummy intermediate calculations (distractors)
baseline_deviation = sum(abs(x - 100) for x in metric_data['response_time'])
penalty_rate = 0.05 * baseline_deviation

# Core logic leading to answer
def evaluate_performance(metrics, limits):
    score = 100
    for key, readings in metrics.items():
        limit = limits[key]
        if key == 'response_time':
            for rt in readings:
                if rt > limit:
                    score -= 5
        elif key == 'success_rate':
            for sr in readings:
                if sr < limit:
                    score -= 10
        elif key == 'retry_count':
            for rc in readings:
                if rc > limit:
                    score -= 15
    if not status_flags['success_rate']:
        score -= 20
    if consistency_check:
        score += 10
    return score

final_score = evaluate_performance(metric_data, thresholds)
print(f"Result: {final_score}")