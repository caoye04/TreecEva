def analyze_node_health(node_data, threshold=0.75):
    return len([x for x in node_data if x > threshold]) / len(node_data) if node_data else 0

# Simulate sensor array data (irrelevant to final result)
sensor_readings = [0.62, 0.71, 0.83, 0.91, 0.45, 0.52, 0.67]
filtered_sensors = [s for s in sensor_readings if s > 0.5]
avg_sensor = sum(filtered_sensors) / len(filtered_sensors) if filtered_sensors else 0

def process_logs(log_entries):
    error_count = 0
    for entry in log_entries:
        if 'ERROR' in entry:
            error_count += 1
    return error_count  # Dead function - never called

# System telemetry streams
telemetry_stream_a = [0.81, 0.85, 0.79, 0.92, 0.88]
telemetry_stream_b = [0.68, 0.73, 0.77, 0.69]
telemetry_stream_c = [0.91, 0.94, 0.89, 0.95, 0.93, 0.90]

def normalize_stream(stream):
    min_val, max_val = min(stream), max(stream)
    return [(x - min_val) / (max_val - min_val) for x in stream] if max_val > min_val else stream

# Misleading diagnostic chain
calibration_factor = 1.05
adjusted_telemetry = [x * calibration_factor for x in telemetry_stream_a]
normalized_telemetry = normalize_stream(adjusted_telemetry)
dummy_metric = sum(normalized_telemetry) / len(normalized_telemetry)

# Core network node health data (key input)
network_nodes = [
    {'id': 'N1', 'metrics': [0.81, 0.88, 0.76, 0.92]},
    {'id': 'N2', 'metrics': [0.69, 0.73, 0.65, 0.71]},
    {'id': 'N3', 'metrics': [0.93, 0.95, 0.91, 0.94]},
    {'id': 'N4', 'metrics': [0.52, 0.58, 0.61, 0.55]}
]

system_load = {
    'peak_hour': 0.88,
    'avg_load': 0.76,
    'spike_count': 3
}

# Decoy data structures
historical_stats = {
    'weekly_high': 0.95,
    'monthly_avg': 0.72,
    'downtime_events': 2
}

snapshot_buffer = []
for i in range(3):
    snapshot_buffer.append({'cycle': i, 'data': telemetry_stream_a[:]})

# Auxiliary processing functions
def calculate_stability(metrics):
    if not metrics:
        return 0.0
    mean = sum(metrics) / len(metrics)
    variance = sum((x - mean) ** 2 for x in metrics) / len(metrics)
    return 1 / (1 + variance)

def evaluate_consistency(readings):
    sorted_vals = sorted(readings)
    gaps = [sorted_vals[i+1] - sorted_vals[i] for i in range(len(sorted_vals)-1)]
    return sum(gaps) / len(gaps) if gaps else 0

# Complex aggregation with conditional logic and set operations
health_scores = []
for node in network_nodes:
    raw_health = analyze_node_health(node['metrics'])
    stability = calculate_stability(node['metrics'])
    consistency = evaluate_consistency(node['metrics'])
    
    # Conditional expression determining effective weight
    weight = 1.5 if stability > 0.9 else (1.2 if consistency > 0.1 else 0.8)
    
    # Apply weighted combination
    effective_score = (raw_health * 0.6 + stability * 0.3 + consistency * 0.1) * weight
    health_scores.append(effective_score)

# Secondary metric from system load
load_penalty = 0.1 if system_load['spike_count'] > 2 else 0.05

# Main aggregation logic
base_aggregate = sum(health_scores) / len(health_scores) if health_scores else 0
adjusted_aggregate = base_aggregate * (1 - load_penalty)

# Set-based filtering of high-performing nodes
healthy_values = {round(score, 2) for score in health_scores if score >= 0.75}
performance_caps = {0.75, 0.80, 0.85, 0.90}
overlap_count = len(healthy_values & performance_caps)

# Final adjustment based on overlap (minor influence)
overlap_bonus = 0.01 * overlap_count

# Critical statement
final_diagnostic = adjusted_aggregate + overlap_bonus

print(f"Result: {final_diagnostic}")