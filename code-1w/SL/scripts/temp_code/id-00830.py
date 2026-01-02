import itertools

# Simulated system telemetry data
log_entries = [
    {'timestamp': 1001, 'cpu_load': 78.2, 'mem_usage': 4321, 'disk_io': 120, 'error_count': 1},
    {'timestamp': 1002, 'cpu_load': 85.7, 'mem_usage': 5103, 'disk_io': 95, 'error_count': 0},
    {'timestamp': 1003, 'cpu_load': 92.1, 'mem_usage': 5988, 'disk_io': 150, 'error_count': 3},
    {'timestamp': 1004, 'cpu_load': 67.3, 'mem_usage': 3920, 'disk_io': 80, 'error_count': 0},
    {'timestamp': 1005, 'cpu_load': 73.9, 'mem_usage': 4701, 'disk_io': 110, 'error_count': 2}
]

# System health thresholds
system_thresholds = {
    'critical_cpu': 90.0,
    'high_mem': 5500,
    'max_disk_io': 140,
    'error_burst': 2
}

# Irrelevant helper (decoy)
def calculate_network_latency(packets, distance):
    total_delay = 0
    for p in packets:
        total_delay += (p['size'] / p['bandwidth']) * distance
    return total_delay  # Never used

# Another decoy: unused data transformation
tamper_proof_hash = sum([len(str(entry['timestamp'])) for entry in log_entries]) * 31
snapshot_interval = tamper_proof_hash % 7 == 0

# Misleading intermediate metrics
cpu_spikes = [e for e in log_entries if e['cpu_load'] > 80]
major_errors = list(filter(lambda x: x['error_count'] >= system_thresholds['error_burst'], log_entries))

# Red herring function
def analyze_security_threats(entries):
    suspicious = 0
    for e in entries:
        if e['disk_io'] > 130 and e['error_count'] > 0:
            suspicious += 1
    return suspicious * 100  # Computed but not part of final result

# Unused but plausible-looking aggregation
baseline_avg_cpu = sum(e['cpu_load'] for e in log_entries) / len(log_entries)
memory_trend = [e['mem_usage'] for e in log_entries]

# Real logic begins here — complex data processing with distractors

def detect_anomaly_sequence(data_stream):
    anomalies = []
    for i in range(1, len(data_stream)):
        prev, curr = data_stream[i-1], data_stream[i]
        if (curr['cpu_load'] > prev['cpu_load'] and 
            curr['mem_usage'] > prev['mem_usage'] and 
            curr['error_count'] > prev['error_count']):
            anomalies.append(i)
    return anomalies

# More distraction: generate all pairs (not actually needed)
all_pairs = list(itertools.combinations([e['timestamp'] for e in log_entries], 2))
pair_count_metric = len(all_pairs)  # Looks important, unused

# Critical diagnostic function
def aggregate_metrics(entries, thresholds):
    # Step 1: Filter entries above critical CPU
    high_cpu = list(filter(lambda x: x['cpu_load'] >= thresholds['critical_cpu'], entries))
    
    # Step 2: Check memory pressure
    mem_pressure = len([e for e in entries if e['mem_usage'] > thresholds['high_mem']])
    
    # Step 3: Disk IO bursts
    disk_bursts = len([e for e in entries if e['disk_io'] > thresholds['max_disk_io']])
    
    # Step 4: Error clustering using sliding window
    error_window_alerts = 0
    for i in range(len(entries) - 2):
        window = entries[i:i+3]
        if sum(e['error_count'] for e in window) >= thresholds['error_burst']:
            error_window_alerts += 1
    
    # Step 5: Cross-check anomaly sequence
    sequences = detect_anomaly_sequence(entries)
    
    # Step 6: Weighted score calculation
    score = 0
    score += len(high_cpu) * 15
    score += mem_pressure * 10
    score += disk_bursts * 8
    score += error_window_alerts * 12
    score += len(sequences) * 5
    
    # Step 7: Apply threshold-based multiplier
    if len(high_cpu) >= 2 or mem_pressure >= 2:
        score *= 1.25
    else:
        score *= 0.9
    
    # Step 8: Final adjustment using bit manipulation (obscure but valid)
    # Only apply if odd number of timestamps modulo 3
    control_flag = sum(e['timestamp'] for e in entries) % 3
    if control_flag & 1:
        score = int(score) ^ 4321  # XOR with constant if flag is odd
    else:
        score = int(score) + 100
    
    return int(score)

# Decoy call that looks important
security_score = analyze_security_threats(log_entries)

# Actual target computation
final_diagnostic = aggregate_metrics(log_entries, system_thresholds)

# Output the result as required
print(f"Result: {final_diagnostic}")