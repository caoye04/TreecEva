def analyze_trend(values):
    trend = 0
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            trend += 1
        elif values[i] < values[i-1]:
            trend -= 1
    return trend

# Irrelevant helper function (decoy)
def compute_entropy(data):
    import math
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    entropy = 0.0
    total = len(data)
    for count in freq.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

# Unused but plausible transformation
def transform_sequence(seq):
    return [x ** 0.5 for x in seq if x > 0]

# Simulated system metrics and benchmarks
metrics = {
    'response_time': [120, 115, 118, 110, 105, 102, 100],
    'throughput': [85, 88, 90, 92, 93, 94, 95],
    'error_rate': [0.02, 0.03, 0.01, 0.04, 0.02, 0.01, 0.005],
    'cpu_load': [65, 68, 70, 72, 71, 69, 67]
}

benchmark_data = {
    'base_line': [100, 90, 80, 70, 60, 50, 40],
    'thresholds': {'latency': 110, 'success': 0.98},
    'weights': {'trend': 0.4, 'stability': 0.3, 'peak': 0.3}
}

# Distractor variables
baseline_trend = analyze_trend(benchmark_data['base_line'])
entropy_probe = compute_entropy([1, 1, 2, 2, 3])
phantom_data = transform_sequence([16, 25, 36, 49])

# Real computation begins here
response_trend = analyze_trend(metrics['response_time'])
stability_dev = 0
for val in metrics['response_time']:
    if abs(val - 110) > 10:
        stability_dev += 1

# Simulated peak performance capture
peak_response = max(metrics['response_time'])
peak_throughput = max(metrics['throughput'])

# Intermediate scores with misleading components
temporal_score = response_trend * 5
stability_score = (7 - stability_dev) * 3
throughput_bonus = 0
if peak_throughput >= 90:
    throughput_bonus = 10

# Dummy logic path (dead end)
if baseline_trend > 0:
    throughput_bonus += 5  # never reached due to baseline_trend being negative

# Key data transformation using slicing and zip
recent_performance = list(zip(
    metrics['response_time'][2:],
    metrics['throughput'][2:],
    metrics['error_rate'][2:]
))

# Additional irrelevant processing
summary_stats = {}
for idx, (rt, tp, er) in enumerate(recent_performance):
    summary_stats[f'step_{idx}'] = {
        'efficiency': rt * tp / 100,
        'quality': 1 - er
    }

# Real scoring logic
valid_periods = 0
for rt, tp, er in recent_performance:
    if rt <= benchmark_data['thresholds']['latency'] and (1 - er) >= benchmark_data['thresholds']['success']:
        valid_periods += 1

# Final integration using dictionary lookup and weighting
weight_config = benchmark_data['weights']
raw_trend_component = weight_config['trend'] * temporal_score
raw_stability_component = weight_config['stability'] * stability_score
raw_peak_component = weight_config['peak'] * (peak_throughput / 10)

# Actual final score calculation
final_score = raw_trend_component + raw_stability_component + raw_peak_component + throughput_bonus

# This print is required for traceability
print(f"Result: {final_score}")