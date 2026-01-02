from collections import defaultdict, Counter
import math

# Simulated system metrics over time
temporal_metrics = [
    {'cpu': 70, 'mem': 45, 'latency': 120, 'requests': 95},
    {'cpu': 85, 'mem': 60, 'latency': 140, 'requests': 110},
    {'cpu': 55, 'mem': 40, 'latency': 95, 'requests': 90},
    {'cpu': 90, 'mem': 75, 'latency': 200, 'requests': 120}
]

# Irrelevant utility function (decoy)
def normalize(value, min_val=0, max_val=100):
    return (value - min_val) / (max_val - min_val)

# Unused transformation map
transform_map = defaultdict(lambda: lambda x: x * 1.1)
for k in ['cpu', 'mem']:
    transform_map[k] = lambda x: min(x * 1.05, 100)

# Benchmark thresholds (real reference data)
benchmark_thresholds = {
    'latency_critical': 180,
    'request_high': 100,
    'cpu_warning': 80
}

# Phantom scoring (red herring)
phantom_weights = [0.1, 0.3, 0.4, 0.2]
phantom_total = sum(w * w for w in phantom_weights)  # Useless computation

# Actual metric processor
def extract_key_signals(metrics_list):
    signals = []
    for entry in metrics_list:
        # Compute derived feature: efficiency ratio
        eff = (entry['requests'] / (entry['latency'] + 1)) * 10
        # Bit manipulation as identifier hash (obscure but deterministic)
        flag = ((entry['cpu'] > 80) << 2) | ((entry['mem'] > 50) << 1) | (entry['latency'] > 150)
        signals.append({'eff': round(eff, 2), 'flag': flag})
    return signals

# Signal aggregator with conditional logic
def aggregate_flags(signal_list):
    counter = Counter()
    high_load_count = 0
    for s in signal_list:
        counter[s['flag']] += 1
        if s['flag'] & 4:  # CPU > 80
            high_load_count += 1
    return dict(counter), high_load_count

# Decoy data structure
junk_cache = {}
for i in range(3):
    junk_cache[f'key_{i}'] = [math.sin(j * 0.1) for j in range(10)]

# Core evaluation logic
metric_set = extract_key_signals(temporal_metrics)
flag_summary, load_count = aggregate_flags(metric_set)

# Secondary processing: efficiency trends
efficiency_values = [s['eff'] for s in metric_set]
sorted_eff = sorted(efficiency_values)
median_eff = (sorted_eff[1] + sorted_eff[2]) / 2  # Median of 4 elements

# Fake normalization chain
dummy_norm = [normalize(e, min(sorted_eff), max(sorted_eff)) for e in efficiency_values]

# Real decision path
baseline_flag = 0
for key in flag_summary:
    if key & 1 and flag_summary[key] >= 2:  # High latency in multiple instances
        baseline_flag |= 2
    if (key >> 2) == 1:  # High CPU
        baseline_flag |= 1

# Set operation to filter relevant states
valid_flags = {k for k in flag_summary.keys() if k in {0, 1, 2, 3, 4, 5, 6, 7}}
active_flags = valid_flags - {0}  # Remove idle state

# Critical evaluation function
def evaluate_performance(metrics, data_ref):
    raw_sum = sum(m['eff'] for m in metrics)
    penalty = 0
    
    # Logical conditions with short-circuiting
    if len(active_flags) > 2 and (baseline_flag & 2) and not (baseline_flag & 4 < 1):
        penalty += 15
    if median_eff < 5.0 or load_count >= 2:
        penalty += 10
    
    # Complex conditional expression
    bonus = 5 if (len({m['flag'] for m in metrics}) == 4 and raw_sum > 20) else 0
    
    # Final score calculation
    score = int(raw_sum - penalty + bonus)
    return score

# Execute main logic
benchmark_data = temporal_metrics  # Reference passed but lightly used
final_score = evaluate_performance(metric_set, benchmark_data)

# Irrelevant post-processing
extended_analysis = []
for i, m in enumerate(metric_set):
    extended_analysis.append({
        'index': i,
        'encoded': m['eff'] ^ m['flag'],  # Bitwise XOR red herring
        'tag': 'A' if m['flag'] % 2 else 'B'
    })

# Output result
print(f"Result: {final_score}")