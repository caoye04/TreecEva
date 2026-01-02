from collections import defaultdict, Counter

# Simulated system metrics from a distributed computing environment
def get_system_metrics():
    return {
        'cpu_usage': [0.78, 0.82, 0.75, 0.90, 0.68],
        'memory_pressure': [0.85, 0.77, 0.88, 0.91, 0.74],
        'disk_io': [120, 135, 110, 145, 105],
        'network_latency_ms': [23, 45, 19, 52, 31],
        'request_throughput': [880, 920, 850, 940, 870]
    }

# Legacy function - not used but looks relevant
def calculate_legacy_score(data):
    score = 0
    for val in data['cpu_usage']:
        score += int(val * 100) // 3
    return score * 0.7

# Red herring: complex bit manipulation with no real impact
def analyze_entropy(seq):
    entropy = 0
    for i in range(len(seq)):
        if i % 2 == 0:
            entropy ^= int(seq[i] * 100)
        else:
            entropy |= int(seq[i] * 50)
    return bin(entropy).count('1')

# Unused diagnostic tool
def run_diagnostics(data):
    diagnostics = defaultdict(int)
    for key, values in data.items():
        diagnostics[f'{key}_count'] = len(values)
        diagnostics[f'{key}_flag'] = any(v > 0.9 * max(values) for v in values)
    return dict(diagnostics)

# Core evaluation logic
weights = {
    'efficiency': 0.3,
    'stability': 0.25,
    'responsiveness': 0.2,
    'throughput': 0.25
}

# Misleading intermediate calculation
baseline_offset = sum([0.75, 0.80, 0.70]) / 3 * 100  # Looks important, unused

# Real processing begins here
def preprocess_metrics(raw):
    processed = {}
    
    # Efficiency: weighted combo of CPU and memory
    cpu_avg = sum(raw['cpu_usage']) / len(raw['cpu_usage'])
    mem_avg = sum(raw['memory_pressure']) / len(raw['memory_pressure'])
    processed['efficiency'] = (cpu_avg * 0.6 + mem_avg * 0.4)
    
    # Stability: low variance in CPU and memory
    cpu_var = sum((x - cpu_avg) ** 2 for x in raw['cpu_usage']) / len(raw['cpu_usage'])
    mem_var = sum((x - mem_avg) ** 2 for x in raw['memory_pressure']) / len(raw['memory_pressure'])
    stability_score = 1 - ((cpu_var + mem_var) / 2)
    processed['stability'] = max(0.0, min(1.0, stability_score))
    
    # Responsiveness: inverse of average latency
    avg_lat = sum(raw['network_latency_ms']) / len(raw['network_latency_ms'])
    processed['responsiveness'] = 1 / (1 + avg_lat / 100)
    
    # Throughput: normalized to baseline
    base_tput = 800
    current_tput = sum(raw['request_throughput']) / len(raw['request_throughput'])
    throughput_ratio = current_tput / base_tput
    processed['throughput'] = min(1.2, throughput_ratio)
    
    return processed

# Another decoy function that processes disk but isn't integrated
def assess_disk_health(io_list):
    peaks = [x for x in io_list if x > 120]
    return len(peaks) < 3

# Key function that computes final result
def evaluate_performance(metrics, w):
    total = 0.0
    for key in w:
        if key in metrics:
            total += metrics[key] * w[key]
    # Final adjustment based on data length patterns
    metric_lengths = [len(v) if isinstance(v, list) else 1 for v in get_system_metrics().values()]
    length_penalty = abs(sum(metric_lengths) - 25) * 0.01
    return int((total - length_penalty) * 1000)  # Scale up for precision

# Irrelevant string manipulation distraction
diag_id = "SYSMON_" + "".join([chr(65 + (hash('perf') % 26)) for _ in range(3)])
timestamp_parts = [2023, 11, 5, 14, 30]
sync_token = '-'.join(map(str, timestamp_parts[:3])) + ':' + ':'.join(f'{x:02d}' for x in timestamp_parts[3:])

# Data collection
raw_metrics = get_system_metrics()

# Dead code path - appears to be used but isn't
if 'disk_io' in raw_metrics:
    health_status = assess_disk_health(raw_metrics['disk_io'])
    debug_flag = True

# Preprocess only necessary metrics
cleaned = preprocess_metrics(raw_metrics)

# UNUSED: entropy analysis on two fields
cpu_entropy = analyze_entropy(raw_metrics['cpu_usage'])
latency_entropy = analyze_entropy(raw_metrics['network_latency_ms'])

# Diagnostics collected but ignored
diags = run_diagnostics(raw_metrics)

# THIS IS THE KEY STATEMENT
final_score = evaluate_performance(cleaned, weights)

# More distractions
feature_mask = 0b1101 ^ 0b1010
scaling_factor = feature_mask * 0.25

# Spurious list comprehensions
anomalies = [i for i, x in enumerate(raw_metrics['network_latency_ms']) if x > 40]
indexed_pairs = list(zip(anomalies, [raw_metrics['request_throughput'][i] for i in anomalies]))

# Final irrelevant slicing operation
recent_cpu = raw_metrics['cpu_usage'][-3:]
projected_load = sum(recent_cpu) / len(recent_cpu) + 0.05

# Output the target result
print(f"Result: {final_score}")