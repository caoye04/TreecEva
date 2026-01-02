from collections import defaultdict

# Simulate system telemetry data
telemetry_data = [
    {'cpu': 75, 'mem': 60, 'disk_io': 200, 'latency': 45},
    {'cpu': 80, 'mem': 65, 'disk_io': 220, 'latency': 48},
    {'cpu': 90, 'mem': 75, 'disk_io': 300, 'latency': 55},
    {'cpu': 85, 'mem': 70, 'disk_io': 250, 'latency': 52}
]

# Misleading auxiliary calculation (distractor)
total_measurements = len(telemetry_data)
dummy_avg = sum([entry['cpu'] for entry in telemetry_data]) / total_measurements

# Baseline thresholds for performance evaluation
baseline = {
    'cpu_threshold': 80,
    'mem_threshold': 70,
    'latency_critical': 50
}

# Aggregation using defaultdict (relevant structure)
aggregated = defaultdict(int)
for entry in telemetry_data:
    if entry['cpu'] > baseline['cpu_threshold']:
        aggregated['high_cpu_count'] += 1
    if entry['latency'] > baseline['latency_critical']:
        aggregated['high_latency_count'] += 1

# Secondary distractor: string-based status mapping (semi-relevant)
status_map = {'normal': 1, 'warning': 2, 'critical': 3}
mode_status = ["warning" if entry['cpu'] > 85 else "normal" for entry in telemetry_data]
warning_events = mode_status.count("warning")

# Real metric computation chain
metric_weights = {
    'cpu_weight': 0.4,
    'latency_weight': 0.6
}

# Compute derived metrics
exceedance_ratio = aggregated['high_cpu_count'] / total_measurements
latency_issue_severity = aggregated['high_latency_count'] * 1.5

# Intermediate score with red herring operation
raw_score = (exceedance_ratio * 100) + (latency_issue_severity * 10)  # Scale up
adjusted_score = raw_score - (warning_events * 2)  # Minor correction

# Irrelevant transformation (dead logic path)
temp_diagnostic = ''.join([f"{entry['disk_io']}MB " for entry in telemetry_data])
diagnostic_checksum = sum([ord(c) for c in temp_diagnostic[:10]]) % 17  # Unused

# Core evaluation function
def evaluate_performance(metrics, base):
    # Simulated complex decision logic
    base_factor = 1.0
    if metrics['high_cpu_count'] >= 2:
        base_factor += 0.2
    if metrics['high_latency_count'] >= 2:
        base_factor += 0.3
    
    # Additional fake dependency
    stress_level = 'high' if warning_events > 1 else 'medium'
    if stress_level == 'high':
        base_factor += 0.05  # Distractor increment

    # Actual formula
    performance_penalty = (metrics['high_cpu_count'] * 8) + (metrics['high_latency_count'] * 12)
    base_score = 100 - performance_penalty
    return int(base_score * base_factor)

# Critical statement
final_score = evaluate_performance(aggregated, baseline)

# Output result
print(f"Result: {final_score}")