def analyze_trend(data, threshold=0.5):
    above_threshold = list(filter(lambda x: x > threshold, data))
    below_threshold = [x for x in data if x <= threshold]
    trend_value = len(above_threshold) - len(below_threshold)
    dummy_calc_1 = sum(x ** 2 for x in above_threshold) if above_threshold else 0
    return trend_value


def compute_volatility(series):
    if len(series) < 2:
        return 0
    diffs = [abs(series[i] - series[i-1]) for i in range(1, len(series))]
    avg_diff = sum(diffs) / len(diffs)
    squared_devs = [(d - avg_diff) ** 2 for d in diffs]
    variance = sum(squared_devs) / len(squared_devs) if squared_devs else 0
    return variance * 100


def evaluate_performance(metrics, weights):
    normalized = {}
    temp_store = []
    for key, value in metrics.items():
        max_val = 100 if 'score' in key else 10
        norm_val = value / max_val
        normalized[key] = norm_val
        temp_store.append(norm_val)
    
    adjusted_weights = {}
    total_weight = sum(weights.values())
    for k, v in weights.items():
        adjusted_weights[k] = v / total_weight if total_weight != 0 else 0
    
    composite = 0
    for k in normalized:
        if k in adjusted_weights:
            composite += normalized[k] * adjusted_weights[k]
    
    # Distractor block: irrelevant transformation
    transformed = [x * 1.5 for x in temp_store[::2]]
    dummy_sum = sum(transformed)
    temp_result = dummy_sum * 0.1
    
    # Actual logic step
    adjustment_factor = 1.2 if composite > 0.7 else 0.9
    final_raw = composite * adjustment_factor * 100
    
    # More distraction: unused volatility simulation
    simulated_series = [final_raw + i*0.3 for i in range(5)]
    spike_count = sum(1 for x in simulated_series if x > 85)
    
    return int(final_raw)

# Main execution
raw_data = [0.8, 0.3, 0.9, 0.6, 0.2, 0.7]
trend_strength = analyze_trend(raw_data)
dummy_trend_copy = trend_strength * 2
volatility = compute_volatility([trend_strength, 2, -1, 4, 3])
unused_metrics = {'stability': volatility, 'noise': 0.4}

metrics = {
    'accuracy_score': 88,
    'response_time': 6,
    'reliability_score': 94,
    'latency': 3
}

weights = {
    'accuracy_score': 0.4,
    'reliability_score': 0.35,
    'response_time': 0.15,
    'latency': 0.1
}

intermediate_result = sum(metrics.values()) // len(metrics)
placeholder = [x for x in weights.keys() if 'score' in x]
event_count = len(raw_data)

final_score = evaluate_performance(metrics, weights)
Result: {final_score}