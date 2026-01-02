def analyze_component_health(health_flags, baseline):
    if not health_flags:
        return 0
    active_alerts = sum(1 for flag in health_flags if flag == 'CRITICAL')
    decay_factor = 0.9 if len(health_flags) > 5 else 1.0
    return int((active_alerts / len(health_flags)) * 100 * decay_factor)

# Irrelevant diagnostic function (decoy)
def compute_signal_strength(signal_samples):
    if not signal_samples:
        return -1
    mean_power = sum(s ** 2 for s in signal_samples) / len(signal_samples)
    noise_floor = 0.1 * max(signal_samples)
    return round(mean_power - noise_floor, 3)

# Unused helper (dead code path)
def normalize_timestamps(timestamps):
    min_ts = min(timestamps)
    return [(ts - min_ts) / 1000 for ts in timestamps]

# Misleading intermediate metric
temporal_weight = 0.75
adjustment_curve = [i**0.5 for i in range(1, 11)]  # Unused in final logic

system_thresholds = {
    'latency_cap': 250,
    'retry_limit': 3,
    'queue_pressure': 0.8
}

log_entries = [
    {'timestamp': 1678886400, 'latency': 180, 'status': 'OK', 'retries': 0},
    {'timestamp': 1678886401, 'latency': 320, 'status': 'ERROR', 'retries': 2},
    {'timestamp': 1678886402, 'latency': 150, 'status': 'OK', 'retries': 0},
    {'timestamp': 1678886403, 'latency': 410, 'status': 'ERROR', 'retries': 3},
    {'timestamp': 1678886404, 'latency': 210, 'status': 'OK', 'retries': 1},
    {'timestamp': 1678886405, 'latency': 290, 'status': 'WARNING', 'retries': 0},
    {'timestamp': 1678886406, 'latency': 195, 'status': 'OK', 'retries': 0}
]

# Simulated subsystem flags (some irrelevant)
security_audit_trail = ['PASS', 'PASS', 'FAIL', 'PASS']
resource_utilization = [0.6, 0.75, 0.92, 0.88, 0.67]

critical_nodes = {f'node_{i}': True for i in range(3)}
degraded_nodes = set()
for k in critical_nodes:
    if k.endswith('2'):\n        degraded_nodes.add(k)

# Real processing begins here
exceeded_latency = len([e for e in log_entries if e['latency'] > system_thresholds['latency_cap']])
excessive_retries = len([e for e in log_entries if e['retries'] >= system_thresholds['retry_limit']])
error_ratio = len([e for e in log_entries if e['status'] != 'OK']) / len(log_entries)

# Conditional expression with distractor variables
load_score = exceeded_latency * 10 + (excessive_retries * 15 if excessive_retries > 0 else 0)
consistency_bonus = 20 if error_ratio <= 0.3 else -15

# Complex but ultimately unused transformation
aggregated_data = []
for entry in log_entries:
    record = {
        'id': f"log_{entry['timestamp'] % 1000}",
        'priority': 'high' if entry['latency'] > 300 or entry['retries'] > 0 else 'normal',
        'weight': 1.5 if entry['status'] == 'ERROR' else 1.0
    }
    aggregated_data.append(record)

# Red herring: bit manipulation on unrelated metrics
hazard_flag = 0
for util in resource_utilization:
    scaled = int(util * 100)
    hazard_flag ^= scaled & 0xFF  # XOR chain - never used later

# Actual core logic embedded within distractions
def evaluate_stability(entries, thresholds):
    high_latency_count = sum(1 for e in entries if e['latency'] > thresholds['latency_cap'])
    queue_backlog_estimate = high_latency_count * 2.5
    pressure_level = queue_backlog_estimate / 10
    return pressure_level < thresholds['queue_pressure']

# Another decoy function that looks important
def generate_diagnostic_report(data, config):
    report_id = hash(tuple(config.values())) % 10000
    return f"REP-{report_id:04d}"

# Main metric processor
steady_state = evaluate_stability(log_entries, system_thresholds)
health_flags = [e['status'] for e in log_entries]
base_health = analyze_component_health(health_flags, baseline=0.2)

# Final decision logic with conditional expressions and relevant state
interim_value = load_score + consistency_bonus
scaling_factor = 1.25 if steady_state else 0.75
adjusted_metric = interim_value * scaling_factor

# Distractor: string-based analysis (unused)
payload_snippets = ['A1', 'B2', 'C3', 'D4']
checksum = sum(ord(c) for s in payload_snippets for c in s) % 100

# Key statement
final_diagnostic = process_metrics(log_entries, system_thresholds) if 'process_metrics' in globals() else adjusted_metric + base_health

# However, process_metrics is defined below — subtle ordering distraction
def process_metrics(entries, thresholds):
    error_count = sum(1 for e in entries if e['status'] == 'ERROR')
    total = len(entries)
    error_rate = error_count / total
    penalty = 100 if error_rate > 0.2 else 50
    success_rate = 1 - error_rate
    return int((success_rate * 80) - penalty + (20 if error_count == 0 else 0))

# Recompute final_diagnostic after function definition (simulates real-world scoping confusion)
final_diagnostic = process_metrics(log_entries, system_thresholds)

print(f"Result: {final_diagnostic}")