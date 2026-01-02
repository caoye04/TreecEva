from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_stream = [
    {'cpu': 75, 'mem': 80, 'latency': 45, 'req_sec': 230},
    {'cpu': 82, 'mem': 65, 'latency': 60, 'req_sec': 190},
    {'cpu': 60, 'mem': 90, 'latency': 30, 'req_sec': 250},
    {'cpu': 90, 'mem': 85, 'latency': 70, 'req_sec': 180},
    {'cpu': 70, 'mem': 75, 'latency': 50, 'req_sec': 210}
]

# Irrelevant historical baselines (distractor)
historical_averages = defaultdict(float)
historical_averages['cpu'] = 65.4
historical_averages['mem'] = 72.1
historical_averages['latency'] = 55.3

# Decoy function - looks important but unused
def calculate_health_legacy(data):
    score = 0
    for entry in data:
        if entry['cpu'] > 80:
            score -= 10
        if entry['mem'] > 85:
            score -= 8
    return max(score, -50)

# Misleading intermediate transformation (dead path)
transformed = [defaultdict(int) for _ in range(len(telemetry_stream))]
for i, t in enumerate(telemetry_stream):
    transformed[i]['load_index'] = t['cpu'] * 0.6 + t['mem'] * 0.4
    transformed[i]['efficiency'] = t['req_sec'] / (t['latency'] + 1)

# Unused aggregation (red herring)
efficiency_stats = Counter()
for t in transformed:
    bucket = int(t['efficiency'] // 5)
    efficiency_stats[bucket] += 1

# Real processing begins here
aggregated_metrics = defaultdict(list)
for sample in telemetry_stream:
    aggregated_metrics['cpu_load'].append(sample['cpu'])
    aggregated_metrics['memory_usage'].append(sample['mem'])
    aggregated_metrics['response_time'].append(sample['latency'])
    aggregated_metrics['throughput'].append(sample['req_sec'])

# Compute summary statistics
metrics = {}
metrics['peak_load'] = max(aggregated_metrics['cpu_load'])
metrics['avg_memory'] = sum(aggregated_metrics['memory_usage']) / len(aggregated_metrics['memory_usage'])
metrics['min_latency'] = min(aggregated_metrics['response_time'])
metrics['std_throughput'] = (sum((x - (sum(aggregated_metrics['throughput'])/len(aggregated_metrics['throughput'])))**2 for x in aggregated_metrics['throughput']) / len(aggregated_metrics['throughput'])) ** 0.5

# Threshold policy (looks configurable but is fixed)
thresholds = {
    'critical_cpu': 85,
    'high_mem': 80,
    'latency_warning': 50,
    'throughput_stdev_max': 25
}

# Core analysis logic with nested conditions and bit manipulation red herring
flag_register = 0b0
performance_flags = []

if metrics['peak_load'] > thresholds['critical_cpu']:
    flag_register |= 0b1000
    performance_flags.append('high_cpu_peak')

if metrics['avg_memory'] > thresholds['high_mem']:
    flag_register |= 0b0100
    performance_flags.append('elevated_memory')

if metrics['min_latency'] < thresholds['latency_warning']:
    flag_register |= 0b0010
    performance_flags.append('low_latency_observed')

if metrics['std_throughput'] > thresholds['throughput_stdev_max']:
    flag_register |= 0b0001
    performance_flags.append('unstable_throughput')

# Distractor: complex bit analysis with no impact
is_symmetric = (flag_register & 0b1000) >> 3 == (flag_register & 0b0001)
is_balanced = bin(flag_register).count('1') % 2 == 0

# Actual scoring logic
base_score = 100

# Deductions based on flags
penalties = {
    'high_cpu_peak': 25,
    'elevated_memory': 15,
    'unstable_throughput': 20
}

# This list comprehension filters only relevant penalties (avoids applying 'low_latency_observed')
applied_penalties = [penalties[f] for f in performance_flags if f in penalties]

total_penalty = sum(applied_penalties)

# Bonus for low latency if memory isn't elevated (conditional bonus logic)
if 'low_latency_observed' in performance_flags and 'elevated_memory' not in performance_flags:
    total_penalty -= 10  # Net bonus by reducing penalty

# Final nonlinear adjustment (simulates diminishing returns)
adjusted_score = base_score - total_penalty
if adjusted_score > 70:
    final_score = adjusted_score * (1 + 0.05 * math.exp(-0.1 * metrics['std_throughput']))
else:
    final_score = adjusted_score

# Execution point of interest: after calling analyze_performance
# Wrapper to simulate modular design (but inline for clarity)
def analyze_performance(met, thres):
    # Recompute flag register (identical logic, distracts from reuse)
    fr = 0
    if met['peak_load'] > thres['critical_cpu']:
        fr |= 0b1000
    if met['avg_memory'] > thres['high_mem']:
        fr |= 0b0100
    if met['min_latency'] < thres['latency_warning']:
        fr |= 0b0010
    if met['std_throughput'] > thres['throughput_stdev_max']:
        fr |= 0b0001
    
    # Reuse main scoring logic
    pfs = []
    if met['peak_load'] > thres['critical_cpu']:
        pfs.append('high_cpu_peak')
    if met['avg_memory'] > thres['high_mem']:
        pfs.append('elevated_memory')
    if met['std_throughput'] > thres['throughput_stdev_max']:
        pfs.append('unstable_throughput')
    if met['min_latency'] < thres['latency_warning']:
        pfs.append('low_latency_observed')
    
    applied = [penalties[f] for f in pfs if f in penalties]
    total_p = sum(applied)
    
    if 'low_latency_observed' in pfs and 'elevated_memory' not in pfs:
        total_p -= 10
    
    score = 100 - total_p
    if score > 70:
        score *= (1 + 0.05 * math.exp(-0.1 * met['std_throughput']))
    return int(score)  # Discretize final result

final_score = analyze_performance(metrics, thresholds)
print(f"Target result: {final_score}")