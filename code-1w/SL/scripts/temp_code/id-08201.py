import itertools

# Simulated system telemetry data
technical_logs = [
    {'timestamp': 1648753200, 'cpu_load': 0.78, 'mem_used': 8240, 'disk_io': 142, 'errors': 3},
    {'timestamp': 1648753260, 'cpu_load': 0.82, 'mem_used': 8520, 'disk_io': 156, 'errors': 5},
    {'timestamp': 1648753320, 'cpu_load': 0.69, 'mem_used': 7980, 'disk_io': 134, 'errors': 2},
    {'timestamp': 1648753380, 'cpu_load': 0.91, 'mem_used': 9100, 'disk_io': 198, 'errors': 8},
    {'timestamp': 1648753440, 'cpu_load': 0.88, 'mem_used': 8870, 'disk_io': 176, 'errors': 6}
]

# System configuration parameters (some are red herrings)
system_config = {
    'max_temp': 95,
    'fan_speed_rpm': 7200,
    'network_buffer_kb': 2048,
    'retry_attempts': 3,
    'cache_size_mb': 512
}

# Thresholds for health monitoring (critical)
system_thresholds = {
    'cpu_load_warn': 0.80,
    'mem_used_warn': 8500,
    'disk_io_warn': 150,
    'error_rate_critical': 7
}

# Irrelevant preprocessing: normalize timestamps to days since epoch
epoch_days = [entry['timestamp'] // 86400 for entry in technical_logs]
unique_days = list(set(epoch_days))

day_pairs = list(itertools.combinations(unique_days, 2))

# Distractor function: calculates temperature estimates (unused)
def estimate_core_temp(base_temp, load_factor, duration_minutes):
    return base_temp + (load_factor * 0.45) * (duration_minutes / 60)

# Another decoy: network jitter simulation (never called)
def simulate_jitter(packets, latency_ms):
    jittered = []
    for i in range(packets):
        variation = (i % 7) * 0.17
        jittered.append(latency_ms + variation)
    return jittered

# Real processing begins here
recent_errors = [log['errors'] for log in technical_logs if log['cpu_load'] > system_thresholds['cpu_load_warn']]

# Misleading intermediate: cumulative error score (partially relevant)
cumulative_error_score = sum(recent_errors) * 1.25

# Extract high-load entries
high_load_periods = [
    log for log in technical_logs 
    if log['cpu_load'] > system_thresholds['cpu_load_warn']
]

# Compute memory pressure index using slicing and filtering
memory_snapshots = [log['mem_used'] for log in technical_logs]
recent_memory_trend = memory_snapshots[-3:]  # last three readings
memory_pressure_index = sum(recent_memory_trend) / len(recent_memory_trend)

# Disk I/O anomaly detection
high_io_events = [
    log for log in technical_logs 
    if log['disk_io'] > system_thresholds['disk_io_warn']
]

# Critical diagnostic logic chain
anomaly_flags = 0
if len(high_load_periods) >= 2:
    anomaly_flags += 1
if memory_pressure_index > 8400:
    anomaly_flags += 1
if len(high_io_events) >= 2:
    anomaly_flags += 1
if cumulative_error_score > 15:
    anomaly_flags += 1

# Set-based correlation analysis (key concept)
error_prone_indices = {i for i, log in enumerate(technical_logs) if log['errors'] > 4}
high_cpu_indices = {i for i, log in enumerate(technical_logs) if log['cpu_load'] > 0.85}

# Intersection reveals correlated failure modes
critical_overlap = error_prone_indices & high_cpu_indices
overlap_severity = len(critical_overlap) * 2

# Secondary distractor: unused time-delta analysis
time_gaps = [
    technical_logs[i+1]['timestamp'] - technical_logs[i]['timestamp'] 
    for i in range(len(technical_logs)-1)
]
avg_time_gap = sum(time_gaps) / len(time_gaps)

# Unused derived metric: synthetic health score
def compute_synthetic_health(errors_list, io_vals):
    weighted_sum = 0
    for e in errors_list:
        for v in io_vals[:2]:
            weighted_sum += e * (v / 100)
    return weighted_sum / (len(errors_list) + 1)

synthetic_health = compute_synthetic_health(recent_errors, [log['disk_io'] for log in high_io_events])

# Core diagnostic processor
reliability_factors = []
for log in technical_logs:
    risk_score = 0
    if log['cpu_load'] > system_thresholds['cpu_load_warn']:
        risk_score += 1
    if log['mem_used'] > system_thresholds['mem_used_warn']:
        risk_score += 1
    if log['errors'] > system_thresholds['error_rate_critical']:
        risk_score += 2  # higher weight
    reliability_factors.append(5 - risk_score)

# Aggregation through conditional logic
system_stability = sum(
    factor for factor in reliability_factors 
    if factor < 4
) + (anomaly_flags * 0.5)

# Final processing with tuple unpacking distraction
summary_stats = (cumulative_error_score, memory_pressure_index, len(high_io_events))
(error_score, mem_idx, io_count) = summary_stats

# Actual answer computation path
baseline = 100
attenuation = 0.8 if overlap_severity >= 2 else 1.0
penalty = (anomaly_flags ** 2) * 3

# Key statement
final_diagnostic = int(baseline * attenuation - penalty + overlap_severity)

print(f"Result: {final_diagnostic}")