from collections import defaultdict, Counter

# Simulated system performance metrics over time
timestamped_logs = [
    {'cpu': 70, 'memory': 65, 'latency_ms': 45, 'requests': 120},
    {'cpu': 85, 'memory': 70, 'latency_ms': 50, 'requests': 130},
    {'cpu': 60, 'memory': 60, 'latency_ms': 40, 'requests': 110},
    {'cpu': 90, 'memory': 80, 'latency_ms': 70, 'requests': 100},
    {'cpu': 75, 'memory': 75, 'latency_ms': 48, 'requests': 125}
]

# Irrelevant historical data (distractor)
historical_stats = defaultdict(lambda: 0)
for log in timestamped_logs:
    if log['cpu'] > 80:
        historical_stats['high_cpu_count'] += 1
    if log['latency_ms'] > 60:
        historical_stats['high_latency_count'] += 1

# Misleading transformation (dead path)
transformed = [dict(sorted(log.items())) for log in timestamped_logs]
sorted_by_cpu = sorted(timestamped_logs, key=lambda x: x['cpu'], reverse=True)

def compute_efficiency(cpu, mem, latency):
    # Outdated formula (decoy function)
    base = (cpu * 0.3) + (mem * 0.2)
    penalty = latency * 0.05
    return max(0, base - penalty)

def extract_trends(logs):
    trends = {}
    cpu_vals = [log['cpu'] for log in logs]
    mem_vals = [log['memory'] for log in logs]
    latency_vals = [log['latency_ms'] for log in logs]
    
    # Real trend indicators
    trends['cpu_stable'] = abs(cpu_vals[-1] - cpu_vals[0]) < 20
    trends['memory_growth'] = mem_vals[-1] > mem_vals[0]
    trends['avg_latency'] = sum(latency_vals) / len(latency_vals)
    
    # Distractor computations
    trends['peak_request_ratio'] = max(logs, key=lambda x: x['requests'])['requests'] / min(logs, key=lambda x: x['requests'])['requests']
    trends['total_data_points'] = len(logs) * 4  # arbitrary
    
    return trends

def analyze_outliers(logs):
    outliers = []
    latencies = [l['latency_ms'] for l in logs]
    avg_lat = sum(latencies) / len(latencies)
    for i, l in enumerate(logs):
        if l['latency_ms'] > avg_lat * 1.5:
            outliers.append(i)
    return outliers  # unused later

def calculate_weighted_metric(log, weights):
    # Core calculation used later
    score = 0
    score += (100 - log['latency_ms']) * weights.get('responsiveness', 0.4)  # lower latency = better
    score += log['requests'] * weights.get('throughput', 0.3)
    score -= abs(log['cpu'] - 75) * weights.get('stability', 0.2)  # penalize deviation from ideal CPU
    score -= abs(log['memory'] - 70) * weights.get('efficiency', 0.1)  # ideal memory usage
    return score

def evaluate_performance(metrics_list, weight_config):
    # Main scoring logic
    raw_scores = []
    for entry in metrics_list:
        s = calculate_weighted_metric(entry, weight_config)
        raw_scores.append(s)
    
    # Aggregate final score
    total = sum(raw_scores)
    adjustment_factor = 1.0
    
    # Conditional adjustment based on trend (real dependency)
    trends = extract_trends(metrics_list)
    if trends['cpu_stable'] and trends['avg_latency'] < 50:
        adjustment_factor = 1.1
    
    # Red herring: bitwise manipulation with no real effect
    magic_flag = 0b1010 ^ 0b1100 & 0b1111
    if magic_flag == 10:
        adjustment_factor *= 1.05  # never reached due to XOR result
    
    final_raw = sum(raw_scores) * adjustment_factor
    
    # Decoy normalization (unused)
    normalized = [round((s - min(raw_scores)) / (max(raw_scores) - min(raw_scores)) * 100) for s in raw_scores if max(raw_scores) != min(raw_scores)]
    
    return int(round(final_raw))

# Unused recursive helper (distractor)
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

def generate_synthetic_data(count):
    import random
    random.seed(42)
    data = []
    for _ in range(count):
        data.append({
            'cpu': random.randint(50, 95),
            'memory': random.randint(50, 85),
            'latency_ms': random.randint(30, 80),
            'requests': random.randint(90, 140)
        })
    return data

# Weight configuration (key input)
weights = {
    'responsiveness': 0.4,
    'throughput': 0.3,
    'stability': 0.2,
    'efficiency': 0.1
}

# Real execution path
metrics = timestamped_logs
final_score = evaluate_performance(metrics, weights)

# Print required output
print(f"Result: {final_score}")