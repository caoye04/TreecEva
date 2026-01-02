from collections import defaultdict, Counter
import math

# Simulated system metrics over time (timestamp -> resource usage)
system_metrics = [
    {'time': 100, 'cpu': 75, 'mem': 82, 'disk_io': 45, 'net_in': 30, 'net_out': 20},
    {'time': 105, 'cpu': 68, 'mem': 85, 'disk_io': 52, 'net_in': 35, 'net_out': 25},
    {'time': 110, 'cpu': 90, 'mem': 88, 'disk_io': 60, 'net_in': 40, 'net_out': 30},
    {'time': 115, 'cpu': 70, 'mem': 70, 'disk_io': 40, 'net_in': 50, 'net_out': 35},
    {'time': 120, 'cpu': 60, 'mem': 65, 'disk_io': 35, 'net_in': 45, 'net_out': 40}
]

# Irrelevant red herring: network anomaly detection (unused)
def detect_anomalies(metrics):
    anomalies = []
    for m in metrics:
        if m['net_in'] > 100 or m['net_out'] > 100:
            anomalies.append(m['time'])
    return anomalies

# Decoy function: calculates memory fragmentation (never called)
def calculate_fragmentation(seq):
    frag_score = 0
    for i in range(1, len(seq)):
        frag_score += abs(seq[i] - seq[i-1])
    return frag_score / len(seq)

# Auxiliary transformation: extract time-series for a given key
def extract_series(metrics, key):
    return [m[key] for m in metrics]

# Misleading intermediate: normalize values between 0 and 100
def normalize(series):
    min_val, max_val = min(series), max(series)
    if max_val == min_val:
        return [50 for _ in series]
    return [100 * (x - min_val) / (max_val - min_val) for x in series]

# Distractor: simulate load balancing decision (not used in final logic)
load_distribution = defaultdict(lambda: 0)
total_load = sum(m['cpu'] + m['mem'] for m in system_metrics)
for metric in system_metrics:
    ratio = (metric['cpu'] + metric['mem']) / total_load
    load_distribution['node_A'] += ratio * 0.6
    load_distribution['node_B'] += ratio * 0.4

# Real logic begins here — performance metric processor
def compute_stability_index(values):
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    std_dev = math.sqrt(variance)
    return round(mean_val - std_dev, 4)

def analyze_trend(series):
    trend_score = 0
    for i in range(1, len(series)):
        if series[i] >= series[i-1]:
            trend_score += 1
        else:
            trend_score -= 0.5
    return trend_score

# Composite evaluation with multiple concepts
def evaluate_component(data, weight_map):
    result_set = {}
    for k, w in weight_map.items():
        raw_series = extract_series(data, k)
        norm_series = normalize(raw_series)  # Used only for specific components
        stability = compute_stability_index(raw_series)
        trend = analyze_trend(raw_series)
        # Only CPU and mem contribute to final score
        if k in ['cpu', 'mem']:
            result_set[k] = stability * 0.7 + trend * 0.3
        else:
            result_set[k] = 0  # Suppressed but not obvious
    return result_set

# High-level orchestrator with conditional logic and data structure manipulation
def evaluate_performance(metrics, config):
    # Config contains irrelevant keys
    relevant_keys = ['cpu', 'mem']
    weights = {key: 1.0 for key in relevant_keys}
    
    # Dead code path: handles disk which is ignored
    if 'disk_io' in [m for m in metrics[0].keys()]:
        weights['disk_io'] = 0.0  # Overwritten but misleading
    
    component_scores = evaluate_component(metrics, weights)
    
    # Bit manipulation red herring
    magic_flag = 0b1010
    adjustment = (magic_flag & 0b1100) >> 2  # Always evaluates to 2
    
    # Final aggregation
    base_score = sum(component_scores.values())
    
    # Conditional bonus based on trend consistency (only applies if both increasing)
    cpu_vals = extract_series(metrics, 'cpu')
    mem_vals = extract_series(metrics, 'mem')
    if cpu_vals[-1] < cpu_vals[0] and mem_vals[-1] < mem_vals[0]:
        penalty = 15
    else:
        penalty = 5
    
    # Apply penalty and bit-derived adjustment
    final_raw = base_score - penalty + adjustment
    
    # Set of operations distraction
    all_keys = set(metrics[0].keys())
    excluded = {'time'}
    active = all_keys - excluded
    if 'net_in' in active and 'net_out' in active:
        final_raw += 0.0  # No-op, but looks meaningful
    
    # Critical assignment
    final_score = round(final_raw * 1.5, 4)
    
    # Unused counter (distractor)
    action_counter = Counter()
    action_counter['evaluated'] += 1
    action_counter['adjusted'] += 1
    
    return final_score

# Benchmark configuration with decoy fields
benchmark_data = {
    'version': '2.1',
    'mode': 'performance',
    'calibration': [0.85, 0.90, 0.92],
    'thresholds': {'critical': 90, 'warning': 70}
}

metric_set = system_metrics

# Key execution point
final_score = evaluate_performance(metric_set, benchmark_data)
print(f"Result: {final_score}")