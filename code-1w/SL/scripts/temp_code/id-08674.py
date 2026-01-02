from collections import defaultdict, Counter

# Simulated system telemetry data
telemetry_stream = [
    {'cpu': 75, 'mem': 60, 'disk': 200, 'latency': 45},
    {'cpu': 80, 'mem': 65, 'disk': 180, 'latency': 50},
    {'cpu': 85, 'mem': 70, 'disk': 150, 'latency': 55},
    {'cpu': 90, 'mem': 75, 'disk': 130, 'latency': 60}
]

# Irrelevant helper function (decoy)
def analyze_disk_health(data):
    total = 0
    for entry in data:
        total += entry['disk'] * 0.1  # arbitrary weight
    return total // len(data)

# Unused transformation function (dead code path)
def transform_metrics(metrics_list):
    transformed = []
    for m in metrics_list:
        transformed.append({
            'load': (m['cpu'] + m['mem']) / 2,
            'response_time': max(m['latency'], 30)
        })
    return transformed

# Misleading intermediate calculation (red herring)
aggregated_disk = sum(e['disk'] for e in telemetry_stream) // len(telemetry_stream)
adjusted_disk = max(aggregated_disk - 100, 0)

# Baseline thresholds for performance evaluation
baseline = {
    'cpu_threshold': 80,
    'mem_threshold': 70,
    'latency_cap': 50,
    'weight_map': {'cpu': 0.4, 'mem': 0.3, 'latency': 0.3}
}

# Extract relevant metrics with list comprehension and zip
cpu_vals = [t['cpu'] for t in telemetry_stream]
mem_vals = [t['mem'] for t in telemetry_stream]
latency_vals = [t['latency'] for t in telemetry_stream]

eval_points = list(zip(cpu_vals, mem_vals, latency_vals))

# Compute rolling average (distractor logic)
def rolling_average(data, window=2):
    if len(data) < window:
        return data[:]
    return [(data[i] + data[i+1]) / 2 for i in range(len(data)-1)]

# Apply rolling average to each metric (irrelevant processing)
cpu_roll = rolling_average(cpu_vals)
mem_roll = rolling_average(mem_vals)
latency_roll = rolling_average(latency_vals)

# Another decoy: frequency counting of rounded CPU usage
rounded_cpu = [round(c/5)*5 for c in cpu_vals]  # round to nearest 5
cpu_frequency = Counter(rounded_cpu)

# Real metric computation begins here — non-obvious due to distractions
metrics = defaultdict(float)
for i, (cpu, mem, lat) in enumerate(eval_points):
    # Weighted deviation from baseline
    cpu_dev = max(0, cpu - baseline['cpu_threshold'])
    mem_dev = max(0, mem - baseline['mem_threshold'])
    lat_dev = max(0, lat - baseline['latency_cap'])
    
    # Accumulate penalty scores with weights
    metrics['cpu_penalty'] += cpu_dev * baseline['weight_map']['cpu']
    metrics['mem_penalty'] += mem_dev * baseline['weight_map']['mem']
    metrics['latency_penalty'] += lat_dev * baseline['weight_map']['latency']

# Secondary distractor: unused correlation check
def compute_correlation(x, y):
    mean_x, mean_y = sum(x)/len(x), sum(y)/len(y)
    num = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(len(x)))
    den_x = sum((xi - mean_x)**2 for xi in x)**0.5
    den_y = sum((yi - mean_y)**2 for yi in y)**0.5
    return num / (den_x * den_y) if den_x * den_y != 0 else 0

# Spurious correlation analysis (never used)
cpu_mem_corr = compute_correlation(cpu_vals, mem_vals)

# Core evaluation function — only one that matters
def evaluate_performance(perf_metrics, base_config):
    total_penalty = sum(perf_metrics.values())
    base_score = 100
    # Apply exponential decay based on total penalty
    import math
    adjusted = base_score * math.exp(-total_penalty / 10)
    return int(round(adjusted))  # deterministic integral score

# Critical statement
final_score = evaluate_performance(metrics, baseline)

# Print result as required
print(f"Result: {final_score}")