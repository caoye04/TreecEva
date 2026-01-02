from itertools import compress, cycle

def analyze_trend(data_sequence):
    trends = []
    for i in range(1, len(data_sequence)):
        if data_sequence[i] > data_sequence[i-1]:
            trends.append(1)
        elif data_sequence[i] < data_sequence[i-1]:
            trends.append(-1)
        else:
            trends.append(0)
    return trends

def smooth_signal(signal):
    smoothed = [signal[0]]
    for i in range(1, len(signal)-1):
        smoothed.append(round((signal[i-1] + signal[i] + signal[i+1]) / 3, 2))
    smoothed.append(signal[-1])
    return smoothed

def compute_aggregate(metrics, importance_weights):
    normalized = {}
    total_weight = sum(importance_weights.values())
    temp_result = 0
    
    # Irrelevant pre-processing (distractor)
    offset = len(metrics) * 2
    dummy_shift = [x % 7 for x in range(offset)]
    
    for key in metrics:
        if key in importance_weights and metrics[key] is not None:
            normalized[key] = metrics[key] / (sum(metrics.values()) or 1)
    
    # Weighted aggregation
    weighted_sum = 0
    for key in normalized:
        weighted_sum += normalized[key] * importance_weights[key]
    
    # Dummy logic with dead-end computation
    anomaly_flag = False
    if len(normalized) > 5:
        anomaly_flag = True
        temp_accum = 0
        for val in normalized.values():
            temp_accum += val ** 2
    
    final_value = round(weighted_sum * 100, 2)
    return int(final_value)

# Main execution
raw_input_data = [120, 135, 130, 145, 160, 155, 170]
trend_analysis = analyze_trend(raw_input_data)
filtered_signal = smooth_signal(raw_input_data)

# Simulate metric logging from multiple sources
event_flags = [True, False, True, True, False]
active_indices = list(compress(range(len(filtered_signal)), cycle([True, False])))

metrics_log = {
    'latency': 89,
    'throughput': 142,
    'consistency': 76,
    'availability': 94,
    'resilience': 68,
    'efficiency': 115
}

weights = {
    'latency': 0.15,
    'throughput': 0.25,
    'consistency': 0.10,
    'availability': 0.20,
    'resilience': 0.10,
    'efficiency': 0.20
}

# Red herring: unused transformation
distorted_metrics = {k: v * 1.15 for k, v in metrics_log.items() if v > 90}

# Key statement
final_score = compute_aggregate(metrics_log, weights)

# Print result
print(f"Result: {final_score}")