import math

# Simulated sensor data and system state for a distributed server cluster
temperature_readings = [23.5, 24.1, 22.7, 25.3, 26.0, 23.9, 24.4]
latency_ticks = [127, 133, 119, 145, 138, 122, 131]
cpu_loads = [0.68, 0.72, 0.65, 0.79, 0.81, 0.64, 0.70]

# Irrelevant auxiliary variables (distractors)
baseline_offset = 1.07
normalization_factor = 0.94
padding_bytes = b'\x00\x01\x02'
metadata_cache = {'version': '2.1', 'schema': 'delta-v3'}

# Unused function - red herring
def decrypt_key(key_str):
    return key_str[::-1].encode('utf-8')

# Another decoy: complex-looking but unused transformation
transform_pipeline = lambda x: list(map(lambda y: (y ** 0.5) * 3.14159, x))
processed_temps = transform_pipeline([t + 2 for t in temperature_readings])

# Misleading intermediate calculation with no impact
aggregate_checksum = 0
for val in latency_ticks:
    aggregate_checksum ^= int(val * 10) % 256

# System state flags
system_state = {
    'nodes_active': 7,
    'overload_threshold_breached': False,
    'maintenance_mode': False,
    'replication_factor': 3
}

# Log data as formatted strings
log_entries = [
    "ERR:disk_full | WARN:high_latency | INFO:sync_ok",
    "INFO:startup | DEBUG:retry_3",
    "WARN:cpu_spike | INFO:mem_ok",
    "INFO:heartbeat | WARN:net_jitter",
    "ERR:auth_fail | WARN:clock_drift",
    "INFO:backup_success | DEBUG:chunk_7",
    "WARN:temp_rise | INFO:fan_spd_up"
]

# String manipulation with slicing and case conversion (relevant)
severity_counts = {'info': 0, 'warn': 0, 'err': 0}
for entry in log_entries:
    parts = entry.split('|')
    for part in parts:
        tag = part.strip().lower()
        if 'info' in tag:
            severity_counts['info'] += 1
        elif 'warn' in tag:
            severity_counts['warn'] += 1
        elif 'err' in tag:
            severity_counts['err'] += 1

# Distractor: unused string processing chain
token_stream = []
for entry in log_entries:
    tokens = entry.replace(':', '|').split('|')
    cleaned = [t.strip().upper() for t in tokens]
    token_stream.extend(cleaned[1:])  # Skip first element arbitrarily

# Real processing begins: compute weighted health score
health_weights = {
    'temp_stability': 0.3,
    'latency_stability': 0.4,
    'cpu_balance': 0.2,
    'log_severity': 0.1
}

# Metric 1: Temperature variance
mean_temp = sum(temperature_readings) / len(temperature_readings)
variance_temp = sum((t - mean_temp) ** 2 for t in temperature_readings) / len(temperature_readings)
normalized_temp_score = 100 * math.exp(-variance_temp * 0.1)

# Metric 2: Latency trend analysis using slicing
recent_latencies = latency_ticks[-4:]  # Last four readings
older_latencies = latency_ticks[:3]   # First three readings
latency_trend = sum(recent_latencies) - sum(older_latencies)
latency_score = 100 if latency_trend <= 0 else max(40, 100 - latency_trend * 0.5)

# Metric 3: CPU load balance across nodes
mean_cpu = sum(cpu_loads) / len(cpu_loads)
cpu_variance = sum((c - mean_cpu) ** 2 for c in cpu_loads)
balance_score = 90 * math.exp(-cpu_variance * 5)

# Metric 4: Log-derived anomaly index
error_penalty = severity_counts['err'] * 15
warning_penalty = severity_counts['warn'] * 5
info_bonus = min(severity_counts['info'], 10) * 1
log_score = 100 - error_penalty - warning_penalty + info_bonus

# Composite health metric
composite_health = (
    normalized_temp_score * health_weights['temp_stability'] +
    latency_score * health_weights['latency_stability'] +
    balance_score * health_weights['cpu_balance'] +
    log_score * health_weights['log_severity']
)

# Secondary diagnostic: pattern scan in logs using lambda
pattern_matcher = lambda s: 'ERR' in s or 'WARN' in s and 'INFO' not in s[:s.index('INFO')] if 'INFO' in s else False
strict_alert_count = sum(1 for log in log_entries if pattern_matcher(log.replace(' ', '')))

# Tertiary metric: dynamic threshold adjustment
if system_state['nodes_active'] > 5 and not system_state['maintenance_mode']:
    threshold_adjustment = 1.1
else:
    threshold_adjustment = 0.85

adjusted_health = composite_health * threshold_adjustment

# Final diagnostic computation
base_diagnostic = int(round(adjusted_health))

# Introduce irrelevant bit manipulation (distractor)
calibration_flag = 0b101010
masked_diagnostics = base_diagnostic ^ calibration_flag & 0xFF

# Key statement
final_diagnostic = process_metrics(log_data, system_state)

# Placeholder function to simulate modular design (inlined logic was already computed)
def process_metrics(log_data, sys_state):
    # All real work was done above; this just bundles final logic
    temp_contrib = normalized_temp_score * health_weights['temp_stability'] / 0.3
    latency_contrib = latency_score * health_weights['latency_stability'] / 0.4
    balance_contrib = balance_score * health_weights['cpu_balance'] / 0.2
    log_contrib = log_score * health_weights['log_severity'] / 0.1
    
    # Weighted sum again for confirmation
    total = temp_contrib * 0.3 + latency_contrib * 0.4 + balance_contrib * 0.2 + log_contrib * 0.1
    adjusted = total * threshold_adjustment
    return int(round(adjusted))

# Execution flow continues...
final_diagnostic = process_metrics(log_data, system_state)

# Print result
print(f"Target result: {final_diagnostic}")