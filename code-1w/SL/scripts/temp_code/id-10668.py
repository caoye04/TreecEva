from collections import defaultdict
import math

# Simulate system performance metrics over time
time_logs = [1.2, 0.8, 1.5, 0.9, 1.1]
error_counts = [2, 0, 1, 0, 3]
throughput = [450, 520, 480, 510, 470]

# Irrelevant backup data (distractor)
backup_timestamps = [1623456789, 1623456849, 1623456909]
redundant_flags = [False, True, False]

# Build metric dictionary using list comprehension and zip
metrics = defaultdict(float)
for i, (t, e, thr) in enumerate(zip(time_logs, error_counts, throughput)):
    metrics[f'latency_{i}'] = t
    metrics[f'errors_{i}'] = e
    metrics[f'throughput_{i}'] = thr

# Unused transformation (dead code path - distractor)
transformed = list(map(lambda x: math.log(x + 1), time_logs))
filtered_throughput = [val for val in throughput if val > 490]

# Weight configuration for evaluation
weights = {
    'latency_penalty': 0.4,
    'error_multiplier': 0.35,
    'throughput_bonus': 0.25
}

# Helper function to compute adjusted score
def evaluate_performance(data, w):
    base_latency = sum(v for k, v in data.items() if 'latency_' in k)
    total_errors = sum(v for k, v in data.items() if 'errors_' in k)
    total_throughput = sum(v for k, v in data.items() if 'throughput_' in k)
    
    # Intermediate irrelevant computation (distractor)
    avg_latency = base_latency / len(time_logs)
    peak_throughput = max(v for k, v in data.items() if 'throughput_' in k)
    stability_score = sum(1 for x in time_logs if abs(x - avg_latency) < 0.3)
    
    # Actual scoring logic
    latency_score = 100 * math.exp(-base_latency)
    error_score = 100 - (total_errors * 15)
    throughput_score = min(100, total_throughput / 5)
    
    # Final weighted combination
    weighted_sum = (
        latency_score * w['latency_penalty'] +
        error_score * w['error_multiplier'] +
        throughput_score * w['throughput_bonus']
    )
    
    # Red herring normalization (not actually changing anything)
    normalized = weighted_sum * (1.0 if weighted_sum >= 70 else 0.95)
    return int(round(normalized))

# Additional unused helper (distractor)
def analyze_trend(values):
    return 'increasing' if values[-1] > values[0] else 'decreasing'

# Critical execution point
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")