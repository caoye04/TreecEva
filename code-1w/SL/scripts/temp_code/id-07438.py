from collections import defaultdict, Counter

# Simulate system benchmark data with noise and metadata
def generate_benchmark_data():
    raw_metrics = [
        (1, 'latency', 45), (2, 'throughput', 89), (3, 'latency', 52),
        (4, 'cpu_load', 70), (5, 'throughput', 92), (6, 'latency', 48),
        (7, 'memory', 60), (8, 'throughput', 87), (9, 'cpu_load', 75)
    ]
    
    # Misleading auxiliary structure
    aux_lookup = {i: f"metric_{i}" for i in range(1, 10)}
    aux_lookup.update({x: x**2 for x in [11, 12, 13]})  # Dead-end computation
    
    data = defaultdict(list)
    for seq_id, key, value in raw_metrics:
        data[key].append(value)
        if key == 'latency':
            data['latency_smoothed'].append(value * 0.95)  # Distractor: not used later
    
    return dict(data)

def analyze_trend(values):
    """Determine if values are improving (negative trend) or degrading"""
    if len(values) < 2:
        return 0
    trend_sum = 0
    for i in range(1, len(values)):
        trend_sum += (values[i-1] - values[i])  # Positive if improving
    return trend_sum

def validate_stability(metrics):
    """Fake validation that computes but doesn't influence final result"""
    stability_check = 0
    for k, v in metrics.items():
        if 'load' in k:
            stability_check += sum(v) % 10
        elif 'throughput' in k:
            stability_check += len(v) * 2
    # Result unused — red herring
    return stability_check > 5

def calculate_performance(metrics):
    # Extract relevant series
    throughput_vals = metrics.get('throughput', [])
    latency_vals = metrics.get('latency', [])
    
    # Real computations for score
    avg_throughput = sum(throughput_vals) / len(throughput_vals) if throughput_vals else 0
    avg_latency = sum(latency_vals) / len(latency_vals) if latency_vals else 0
    
    # Normalize to a 0-100 scale: higher is better
    throughput_score = min(avg_throughput, 100)
    latency_score = max(0, 100 - avg_latency)  # Lower latency → higher score
    
    # Trend bonus/penalty
    throughput_trend = analyze_trend(throughput_vals)
    latency_trend = analyze_trend(latency_vals)
    
    trend_bonus = 0
    if throughput_trend > 0:
        trend_bonus += 8
    if latency_trend > 0:
        trend_bonus += 5  # System is improving
    
    # Dummy string processing - looks important but only minor effect
    metric_names = ''.join(metrics.keys())
    if 'cpu' in metric_names:
        trend_bonus -= 2  # Slight penalty for CPU presence (arbitrary)
    
    # Final weighted score
    base_score = 0.6 * throughput_score + 0.4 * latency_score
    final_score = base_score + trend_bonus
    
    # Irrelevant formatting distraction
    report_str = f"Performance: {final_score:.1f}%.".replace('%', ' percent')
    word_count = len(report_str.split())
    
    # Unused variables - increase cognitive load
    peak_throughput = max(throughput_vals) if throughput_vals else 0
    smoothed_latency = [x * 0.95 for x in latency_vals]
    
    return int(round(final_score))

# Main execution flow
benchmark_data = generate_benchmark_data()

# Preliminary inspection (no side effects)
data_counter = Counter()
for k, vals in benchmark_data.items():
    data_counter[k] += len(vals)

system_class = ""if sum(data_counter.values()) > 10 else "Legacy"

# Key statement
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")