import itertools

# Simulated sensor data processing with performance scoring
raw_data = [15, 27, 12, 8, 33, 41, 20, 7, 18, 24]
decoy_data = [x ** 2 for x in raw_data if x % 3 == 0]  # Irrelevant computation

# Filtering valid signals using sliding window
valid_signals = []
for i in range(len(raw_data) - 2):
    window = raw_data[i:i+3]
    if sum(window) > 40 and window[1] % 2 == 1:
        valid_signals.append(window[1])

# Dead code path - never used but looks important
def analyze_outliers(data):
    return [x for x in data if x < 10 or x > 30]

unused_analysis = analyze_outliers(raw_data)

temp_offsets = [abs(raw_data[i] - raw_data[i+1]) for i in range(len(raw_data)-1)]
smoothed = [sum(raw_data[i:i+3]) // 3 for i in range(0, len(raw_data), 3)]

# Key data transformation chain
transformed = list(map(lambda x: (x * 2 + 1) % 25, valid_signals))

# Decoy statistical summary
mean_decoy = sum(decoy_data) / len(decoy_data) if decoy_data else 0
counter_freq = {x: transformed.count(x) for x in set(transformed)}

# Simulated metric calculation
latency = len(valid_signals) * 1.5
throughput = sum(transformed) / 2.0
accuracy = len([x for x in transformed if x > 10])
reliability = len(set(transformed))

# Unused complex structure - red herring
nested_diagnostic = {
    'levels': [
        {'layer': 'A', 'values': [v for v in transformed if v < 10]},
        {'layer': 'B', 'values': [v for v in transformed if v >= 10]}
    ],
    'checksum': sum(transformed) ^ 255
}

# Weight configuration (some weights are decoys)
weight_config = {
    'latency': 0.1,
    'throughput': 0.4,
    'accuracy': 0.3,
    'reliability': 0.2,
    'stability': 0.0,  # Unused weight
    'robustness': 0.0   # Unused weight
}

metrics = {
    'latency': latency,
    'throughput': throughput,
    'accuracy': accuracy,
    'reliability': reliability
}

weights = [weight_config[k] for k in metrics.keys()]

# Core evaluation logic obscured by distractions
def evaluate_performance(perf_metrics, weight_vector):
    weighted_sum = 0.0
    for idx, key in enumerate(metrics.keys()):
        if key in ['latency', 'throughput']:
            # Invert latency for scoring alignment
            value = perf_metrics['throughput'] - perf_metrics['latency']
        elif key == 'accuracy':
            value = perf_metrics['accuracy'] * 2
        else:
            value = perf_metrics[key]
        weighted_sum += value * weight_vector[idx]
    
    # Final nonlinear transformation
    result = int((weighted_sum ** 1.5) // 10)
    
    # Decoy side-effect computation
    _ = [x for x in itertools.combinations_with_replacement([1,2], 2)]
    
    return result

# Critical execution point
final_score = evaluate_performance(metrics, weights)

# Distractor output
intermediate_report = {
    'count': len(raw_data),
    'peak': max(raw_data),
    'noise_ratio': len(decoy_data) / len(raw_data)
}

Result: {final_score}