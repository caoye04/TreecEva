from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_streams = {
    'cpu_load': [0.78, 0.82, 0.91, 0.65, 0.77, 0.88, 0.95, 0.73],
    'memory_usage': [0.64, 0.71, 0.79, 0.81, 0.85, 0.92, 0.88, 0.77],
    'disk_iops': [120, 135, 110, 142, 138, 155, 128, 133],
    'network_latency_ms': [23, 45, 32, 28, 51, 44, 39, 35]
}

# System health thresholds
system_thresholds = {
    'critical_load': 0.90,
    'high_memory': 0.80,
    'max_iops': 150,
    'latency_warning': 40
}

# Irrelevant baseline metrics (distractor)
baseline_metrics = {
    'uptime_days': 45,
    'user_count': 1278,
    'active_sessions': 47,
    'cache_hit_ratio': 0.89
}

# Auxiliary function - looks important but not used in final calculation
def calculate_health_score(metrics, weights):
    return sum(metrics[k] * w for k, w in weights.items() if k in metrics)

# Unused diagnostic mode flag (red herring)
diagnostic_mode = True
enable_tracing = False  # Dead code switch

# Data transformation pipeline
log_data = defaultdict(list)
for key, values in telemetry_streams.items():
    normalized = [round(v / max(values), 3) for v in values]
    log_data[key] = normalized

# Spurious intermediate aggregation (distractor)
spike_count = 0
for stream in telemetry_streams.values():
    spike_count += sum(1 for val in stream if isinstance(val, float) and val > 0.85)

# Fake anomaly detection (dead path)
anomalies = []
if enable_tracing:
    for name, data in telemetry_streams.items():
        if max(data) - min(data) > 0.3:
            anomalies.append(name)

# Real processing begins: extract critical indicators
critical_events = 0
degradation_periods = 0

for timestamp in range(len(telemetry_streams['cpu_load'])):
    load = telemetry_streams['cpu_load'][timestamp]
    mem = telemetry_streams['memory_usage'][timestamp]
    iops = telemetry_streams['disk_iops'][timestamp]
    latency = telemetry_streams['network_latency_ms'][timestamp]
    
    # Count sustained high load with memory pressure
    if load > system_thresholds['critical_load']:
        critical_events += 1
    
    # Degradation: high memory + high latency
    if mem > system_thresholds['high_memory'] and latency > system_thresholds['latency_warning']:
        degradation_periods += 1

# Secondary metric: efficiency ratio (partially relevant)
efficiency_ratio = 0
if critical_events > 0:
    efficiency_ratio = round(degradation_periods / critical_events, 3)

# Bit manipulation decoy (irrelevant)
status_flag = 0x1A5E
status_flag ^= 0xFFFF
status_flag >>= 4
checksum = sum([status_flag & 0xF for _ in range(3)])  # Distractor computation

# Core diagnostic logic
indicator_map = defaultdict(int)
for key, values in log_data.items():
    above_threshold = len([v for v in values if v > 0.8])
    indicator_map[key] = above_threshold

# Weighted scoring using dictionary operations
diagnostic_weights = {'cpu_load': 1.5, 'memory_usage': 1.8, 'disk_iops': 0.8, 'network_latency_ms': 1.2}
score_components = []
for k, v in indicator_map.items():
    if k in diagnostic_weights:
        score_components.append(v * diagnostic_weights[k])

raw_score = sum(score_components)

# Final non-linear transformation
adjusted_score = math.log(raw_score + 1) * 100

# Misleading rounding operation (looks final but isn't)
preliminary_diagnostic = round(adjusted_score, 2)

# Actual final computation chain
buffer_states = [telemetry_streams['disk_iops'][i] % 10 for i in range(8)]
entropy = 0
freq_dist = Counter(buffer_states)
for freq in freq_dist.values():
    p = freq / 8
    entropy -= p * math.log2(p)

# Key statement
final_diagnostic = int(round(preliminary_diagnostic + (entropy * 10), 0))

print(f"Result: {final_diagnostic}")