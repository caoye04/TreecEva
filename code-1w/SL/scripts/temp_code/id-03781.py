import math

# Simulated sensor data processing with performance scoring
def analyze_response_time(raw_logs):
    times = [float(x.split(',')[1]) for x in raw_logs if 'latency' in x]
    return sum(times) / len(times) if times else 0.0

def compute_reliability_index(status_stream):
    valid_count = sum(1 for s in status_stream if s == 'OK')
    return valid_count / len(status_stream) if status_stream else 0.0

def evaluate_consistency_pattern(history):
    changes = 0
    for i in range(1, len(history)):
        if history[i] != history[i-1]:
            changes += 1
    return 1.0 - (changes / (len(history) - 1)) if len(history) > 1 else 1.0

def extract_signal_quality(signal_amplitudes):
    if not signal_amplitudes:
        return 0.0
    avg = sum(signal_amplitudes) / len(signal_amplitudes)
    variance = sum((x - avg) ** 2 for x in signal_amplitudes) / len(signal_amplitudes)
    return math.exp(-variance / (avg + 1e-5))

def mock_calibration_sequence():
    # Dead function - never used, red herring
    calibration_data = [i * 0.987 for i in range(100)]
    adjusted = [math.sin(x) * math.cos(x) for x in calibration_data]
    return sum(adjusted) % 7

def generate_test_workload(n):
    # Unused complex generator - distractor
    for i in range(n):
        yield {
            'id': i,
            'payload': [(i+j) % 7 for j in range(5)],
            'flags': [bool((i>>k) & 1) for k in range(3)]
        }

# Irrelevant helper - looks important but unused
def calculate_entropy(values):
    from collections import Counter
    counts = Counter(values)
    total = len(values)
    return -sum((count/total)*math.log2(count/total) for count in counts.values())

# Real data inputs
logs = [
    'event,latency,120.5',
    'metric,latency,98.3',
    'status,OK',
    'metric,latency,105.1',
    'status,ERROR',
    'metric,latency,110.7',
    'status,OK'
]

statuses = ['OK', 'OK', 'OK', 'ERROR', 'OK', 'OK', 'OK']
config_history = ['A', 'A', 'B', 'B', 'B', 'C', 'C']
amplitudes = [0.8, 0.85, 0.76, 0.91, 0.88, 0.82, 0.79]

# Extract meaningful metrics
response_time = analyze_response_time(logs)
reliability = compute_reliability_index(statuses)
consistency = evaluate_consistency_pattern(config_history)
signal_quality = extract_signal_quality(amplitudes)

# Distractor variables - look like they're part of calculation
baseline_offset = 0.123
normalization_factor = 1.0 / (1 + math.exp(-0.5))
temp_diagnostic = [math.tanh(x * 0.1) for x in range(10)]
shadow_weight = sum(temp_diagnostic) * 0.01

# Real metric weights (some are decoys)
weights = {
    'timing': 0.4,
    'reliability': 0.3,
    'consistency': 0.2,
    'signal': 0.1
}

# Unused weight variants - misleading paths
alt_weights_v1 = {k: v*0.8 for k, v in weights.items()}
alt_weights_v2 = dict(zip(['t', 'r', 'c', 's'], [0.25]*4))

metrics = {
    'timing': max(0.0, 1.0 - response_time / 200.0),
    'reliability': reliability,
    'consistency': consistency,
    'signal': signal_quality
}

# Another dead path - complex but irrelevant
if __name__ == '__main__':
    debug_snapshot = []
    for idx, (k, v) in enumerate(zip(metrics.keys(), metrics.values())):
        debug_snapshot.append(f'{idx}:{k[0]}={v:.3f}')

# Critical function that computes final score
def aggregate_performance(perf_metrics, metric_weights):
    weighted_sum = 0.0
    for key in perf_metrics:
        if key in metric_weights:
            contribution = perf_metrics[key] * metric_weights[key]
            weighted_sum += contribution
    return int(weighted_sum * 1000)  # Discrete scoring unit

# Execute main logic
intermediate_debug = mock_calibration_sequence()  # Useless call
useless_list = [x for x in generate_test_workload(5)]  # Dead computation

final_score = aggregate_performance(metrics, weights)

print(f"Result: {final_score}")