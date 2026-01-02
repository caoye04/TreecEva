from collections import defaultdict, Counter

# Simulated system metrics over time
timestamps = [1, 2, 3, 4, 5, 6, 7, 8]
errors = [0, 1, 1, 0, 2, 1, 0, 1]
latency_ms = [120, 150, 130, 110, 160, 145, 135, 125]
throughput = [100, 95, 98, 102, 90, 97, 101, 99]

# Irrelevant auxiliary data (distractor)
dummy_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
useless_map = {k: v for k, v in zip(dummy_labels, latency_ms)}
offset_correction = sum([x % 10 for x in throughput])  # Misleading computation

# Aggregating real-time metrics
metric_data = defaultdict(list)
for t, e, l, tp in zip(timestamps, errors, latency_ms, throughput):
    metric_data['error_count'].append(e)
    metric_data['latency'].append(l)
    metric_data['tp'].append(tp)

# Secondary derived stats (some useful, some not)
avg_latency = sum(metric_data['latency']) / len(metric_data['latency'])
max_error_window = max([sum(errors[i:i+3]) for i in range(len(errors)-2)])  # Complex but unused
smoothed_tp = [throughput[i] + 0.5 * (throughput[i-1] if i > 0 else 0) for i in range(len(throughput))]

# Noise injection for robustness testing (distractor)
noise_floor = [abs((i * 0.1) ** 2 - 0.5) for i in range(len(timestamps))]
adjusted_metrics = [l + n for l, n in zip(latency_ms, noise_floor)]

# Core evaluation logic
def analyze_stability(errors):
    changes = 0
    for i in range(1, len(errors)):
        if errors[i] != errors[i-1]:
            changes += 1
    return changes

def count_critical_latencies(latencies, limit=140):
    return sum(1 for l in latencies if l > limit)

def evaluate_performance(data, threshold):
    # Real contributing components
    stability = analyze_stability(data['error_count'])
    high_latency_count = count_critical_latencies(data['latency'], limit=threshold)
    base_throughput = sum(data['tp']) / len(data['tp'])
    
    # Dummy intermediate calculations (misleading)
    phantom_score = sum(Counter(smoothed_tp).values()) * 0.1  # Looks important
    fallback_metric = offset_correction * 0.25
    
    # Actual formula used
    score = 100
    score -= stability * 2
    score -= high_latency_count * 5
    score += (base_throughput - 95)  # Normalize around baseline
    
    # Dead code branch (never executed - red herring)
    debug_mode = False
    if debug_mode and phantom_score > 50:
        score += 10
    
    return int(score)

# Threshold setting (critical parameter)
threshold = 138

# Final computation
final_score = evaluate_performance(metric_data, threshold)

# Output result as required
print(f"Result: {final_score}")