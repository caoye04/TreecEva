import math

# Simulated telemetry data from satellite subsystems
telemetry_stream = [
    {'id': 101, 'temp': 48.2, 'voltage': 3.31, 'cycles': 1205, 'status': 'active'},
    {'id': 102, 'temp': 51.7, 'voltage': 3.29, 'cycles': 1206, 'status': 'active'},
    {'id': 205, 'temp': 62.1, 'voltage': 3.18, 'cycles': 892,  'status': 'degraded'},
    {'id': 304, 'temp': 45.0, 'voltage': 3.35, 'cycles': 1501, 'status': 'active'},
    {'id': 207, 'temp': 70.3, 'voltage': 3.01, 'cycles': 703,  'status': 'failed'},
    {'id': 109, 'temp': 49.8, 'voltage': 3.33, 'cycles': 1198, 'status': 'active'}
]

# Irrelevant auxiliary mapping (distractor)
component_map = {101: 'sensor_A', 102: 'sensor_B', 205: 'actuator_X', 304: 'power_Y', 207: 'cooling_Z', 109: 'sensor_C'}

# System-wide thresholds (some irrelevant fields included)
system_specs = {
    'temp_limit': 65.0,
    'voltage_window': (3.10, 3.40),
    'min_cycles': 800,
    'priority_factor': 1.85,
    'calibration_offset': 0.07
}

# Legacy debugging flag (dead code path)
debug_mode_enabled = False
log_level = 'WARNING' if debug_mode_enabled else 'CRITICAL'

# Historical baseline (unused but plausible)
historical_avg_cycles = 1150.4

# Data transformation pipeline
processed_nodes = []
error_flags = []

for entry in telemetry_stream:
    normalized_id = entry['id'] % 100
    adjusted_temp = entry['temp'] - system_specs['calibration_offset']
    voltage_ok = system_specs['voltage_window'][0] <= entry['voltage'] <= system_specs['voltage_window'][1]
    cycle_health = 'good' if entry['cycles'] >= system_specs['min_cycles'] else 'low'

    # Conditional expression for status weighting (critical concept)
    weight = 1.5 if entry['status'] == 'active' else (0.5 if entry['status'] == 'degraded' else 0.0)

    # Compute health score with weighted components
    temp_penalty = max(0, (entry['temp'] - system_specs['temp_limit']) * 0.2) if entry['temp'] > system_specs['temp_limit'] else 0
    health_score = 100 - temp_penalty - (10 if not voltage_ok else 0) - (5 if cycle_health == 'low' else 0)
    health_score = max(10, min(100, health_score)) * weight

    processed_nodes.append({
        'node': normalized_id,
        'score': round(health_score, 2),
        'class': cycle_health,
        'v_ok': voltage_ok
    })

    if entry['voltage'] < system_specs['voltage_window'][0]:
        error_flags.append(f"LOW_VOLT_{normalized_id}")

# Unused sorting (distractor operation)
sorted_by_node = sorted(processed_nodes, key=lambda x: x['node'])

# Simulated log aggregation with red herring variables
log_data = []
temp_bucket = {i: 0 for i in range(45, 75, 5)}

for node in processed_nodes:
    category = 'A' if node['score'] >= 75 else 'B' if node['score'] >= 50 else 'C'
    bucket_key = (int(node['score']) // 10) * 10
    if 40 <= bucket_key < 70:
        temp_bucket[bucket_key] += 1

    log_data.append({
        'ref': f"N{node['node']:02d}",
        'cat': category,
        'flag': node['v_ok']
    })

# Additional unused statistic (misleading intermediate)
failure_rate_estimate = len([x for x in telemetry_stream if x['status'] == 'failed']) / len(telemetry_stream)

# Core diagnostic logic buried among distractions
def analyze_health(nodes):
    total = sum(node['score'] for node in nodes)
    count = len([node for node in nodes if node['score'] > 0])
    return total / count if count > 0 else 0

# Redundant function (decoy)
def legacy_evaluate(stream):
    return sum(1 for item in stream if item['temp'] > 50) * 2.5

# Another decoy - never called
max_possible_score = lambda n: n * 100 * 1.5

# Threshold computation with conditional expression
system_threshold = 65.0 if len(telemetry_stream) > 5 else 60.0

# Critical processing function
def process_metrics(log_entries, threshold):
    # Extract numeric part from reference and map to scores
    extracted_scores = []
    for entry in log_entries:
        ref_num = int(entry['ref'][1:])
        source_node = next((n for n in processed_nodes if n['node'] == ref_num), None)
        if source_node:
            extracted_scores.append(source_node['score'])
    
    # Compute moving average (window size 2) if enough data
    if len(extracted_scores) >= 2:
        averages = [(extracted_scores[i] + extracted_scores[i+1]) / 2 
                    for i in range(len(extracted_scores)-1)]
        smoothed = sum(averages) / len(averages)
    else:
        smoothed = extracted_scores[0] if extracted_scores else 0
    
    # Apply threshold-based scaling
    scaling_factor = 1.1 if smoothed > threshold else 0.9
    adjusted = smoothed * scaling_factor
    
    # Final adjustment based on active component ratio
    active_count = sum(1 for e in telemetry_stream if e['status'] == 'active')
    ratio = active_count / len(telemetry_stream)
    final_value = adjusted * (1 + (ratio - 0.5) * 0.4)  # Max ±20% adjustment
    
    return round(final_value, 4)

# Execution point of interest
final_diagnostic = process_metrics(log_data, system_threshold)

# Print result as required
print(f"Target result: {final_diagnostic}")