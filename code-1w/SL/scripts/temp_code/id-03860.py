from collections import defaultdict, Counter

# Simulated system telemetry data
timing_data = [0.12, 0.08, 0.15, 0.09, 0.11, 0.13, 0.07, 0.10]
packet_sequence = [1, 2, 3, 4, 5, 6, 7, 8]
cpu_loads = [0.45, 0.67, 0.52, 0.89, 0.44, 0.71, 0.66, 0.58]

# Irrelevant baseline reference (distractor)
baseline_avg = sum([0.1, 0.2, 0.15, 0.18, 0.13]) / 5

# Misleading transformation (dead path)
def legacy_normalization(data):
    mean = sum(data) / len(data)
    return [x / mean for x in data]

normalized_loads = legacy_normalization(cpu_loads)  # Unused result

# Real processing begins
system_flags = []
for load in cpu_loads:
    if load > 0.8:
        system_flags.append('HIGH')
    elif load < 0.5:
        system_flags.append('LOW')
    else:
        system_flags.append('NORMAL')

# Build timing log with enumeration and zipping (core relevance)
timing_log = []
for i, (t, p) in enumerate(zip(timing_data, packet_sequence)):
    status = 'CRITICAL' if t > 0.11 else 'OK'
    timing_log.append({
        'index': i,
        'latency': t,
        'packet_id': p,
        'status': status
    })

# Decoy function using Counter (irrelevant)
def analyze_redundancy(log):
    statuses = [entry['status'] for entry in log]
    return Counter(statuses)

redundancy_report = analyze_redundancy(timing_log)  # Computed but unused

# Fake aggregation (misleading intermediate)
temp_aggregate = 0
for entry in timing_log:
    temp_aggregate += entry['latency'] * 100

# Actual key logic: detect anomalies and correlate
anomaly_count = 0
for entry, flag in zip(timing_log, system_flags):
    if entry['status'] == 'CRITICAL' and flag == 'HIGH':
        anomaly_count += 1

# Hidden accumulator using defaultdict (relevant)
metric_store = defaultdict(float)
for entry in timing_log:
    metric_store[entry['status']] += entry['latency']

# Auxiliary calculation with bit manipulation red herring
bitmask = 0
for i in range(3):
    bitmask |= (1 << i)  # Results in 7, unused later

# Core correlation: combine timing distribution and system state
def compute_phase_coherence(metrics, flags):
    critical_latencies = metrics['CRITICAL']
    high_count = flags.count('HIGH')
    return critical_latencies * high_count

phase_score = compute_phase_coherence(metric_store, system_flags)

# Final diagnostic depends on multiple hidden paths
def aggregate_metrics(log, flags):
    total_critical = sum(1 for e in log if e['status'] == 'CRITICAL')
    recent_packet_bias = sum(e['packet_id'] for e in log[-3:])  # Last three packets
    flag_ratio = flags.count('NORMAL') / len(flags)
    
    # The real answer derivation (non-obvious combination)
    base = total_critical * 1000
    adjustment = int(recent_packet_bias * 10 * flag_ratio)
    return base + adjustment + int(phase_score * 10)

final_diagnostic = aggregate_metrics(timing_log, system_flags)
print(f"Target result: {final_diagnostic}")