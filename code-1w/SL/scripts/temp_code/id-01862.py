from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_stream = [
    {'sensor': 'temp', 'value': 42, 'status': 'OK', 'node': 'A1'},
    {'sensor': 'voltage', 'value': 120, 'status': 'WARNING', 'node': 'A2'},
    {'sensor': 'temp', 'value': 105, 'status': 'CRITICAL', 'node': 'B1'},
    {'sensor': 'current', 'value': 30, 'status': 'OK', 'node': 'A1'},
    {'sensor': 'temp', 'value': 65, 'status': 'OK', 'node': 'B2'},
    {'sensor': 'voltage', 'value': 110, 'status': 'OK', 'node': 'C1'}
]

# Irrelevant statistical buffer (distractor)
stats_buffer = [math.sin(i * 0.1) for i in range(100)]
buffer_mean = sum(stats_buffer) / len(stats_buffer)

# Misleading precomputation with dead logic path
def legacy_calibrate(x):
    return (x * 1.05) - 2 if x > 100 else x * 0.9

# Unused recursive function (red herring)
def compute_depth(n):
    if n <= 1:
        return 1
    return compute_depth(n-1) + compute_depth(n-2)

# Fake anomaly detector (never called)
def detect_ghost_anomalies(data):
    return [d for d in data if d['value'] % 17 == 0]

# System health flags (some relevant, some not)
system_flags = {
    'overheat_threshold': 90,
    'voltage_risk': 115,
    'node_priorities': {'A1': 3, 'A2': 2, 'B1': 1, 'B2': 3, 'C1': 2},
    'debug_mode': True,
    'legacy_compat': False,
    'encryption_level': 'AES-256'
}

# Log accumulator with distractor operations
def accumulate_logs(stream):
    log_entries = defaultdict(list)
    temp_aggregates = []  # Used only for distraction
    critical_count = 0
    
    for entry in stream:
        log_entries[entry['sensor']].append(entry)
        
        # Real logic: count critical entries
        if entry['status'] == 'CRITICAL':
            critical_count += 1
        
        # Distractor: irrelevant aggregation
        if entry['sensor'] == 'temp':
            temp_aggregates.append(entry['value'] * 0.85)  # fake normalized temp
    
    # Dead code branch (misleading)
    if len(temp_aggregates) > 10:
        interpolated = sum(temp_aggregates) / len(temp_aggregates)
    else:
        interpolated = None
    
    # Add decoy key
    log_entries['_metadata'] = {'interpolated': interpolated, 'version': '2.1'}
    
    return dict(log_entries), critical_count

# Core processing function with mixed concerns
def analyze_temperature(readings):
    total = 0
    count = 0
    for r in readings:
        val = r['value']
        # Apply fake compensation factor
        if r['node'].startswith('A'):
            val = legacy_calibrate(val)
        total += val
        count += 1
    return total / count if count else 0

# Main metric processor with multiple red herrings
def process_metrics(entries, flags):
    result = defaultdict(float)
    diagnostics = []
    
    # Real computation: average temperature
    if 'temp' in entries:
        avg_temp = analyze_temperature(entries['temp'])
        result['base_temp'] = avg_temp
        
        # Check thresholds
        if avg_temp > flags['overheat_threshold']:
            diagnostics.append(1)
        
        # Irrelevant bitwise masking on sensor count (distraction)
        sensor_mask = len(entries['temp']) & 7
        masked_value = avg_temp ^ sensor_mask  # XOR distraction
        result['masked_diagnostic'] = masked_value
    
    # Process voltage data (partially relevant)
    if 'voltage' in entries:
        voltage_avg = sum(e['value'] for e in entries['voltage']) / len(entries['voltage'])
        result['voltage_stability'] = voltage_avg
        
        # Decoy transformation
        encrypted_volt = voltage_avg * 256
        result['encoded'] = int(encrypted_volt) & 0xFFFF
    
    # Spurious list comprehension with unused outcome
    priority_nodes = [
        node for node, priority in flags['node_priorities'].items()
        if priority >= 2 and any(
            e['node'] == node and e['status'] == 'WARNING'
            for e in entries.get('voltage', [])
        )
    ]
    
    # Critical logic hidden among noise: combine base temp with critical event count
    metadata = entries.get('_metadata', {})
    critical_events = len([e for e in entries.get('temp', []) if e['status'] == 'CRITICAL'])
    
    # Key calculation buried in distractions
    severity_score = 0
    if critical_events > 0:
        severity_score += 1000
    if 'base_temp' in result:
        severity_score += int(result['base_temp'])
    
    # Final red herring: complex but unused formula
    final_hazard_index = (
        (severity_score ** 1.1) + 
        (result.get('voltage_stability', 100) / 10) - 
        len(priority_nodes) * 5
    ) // 1
    
    # ACTUAL target variable - derived from specific logic chain
    final_diagnostic = severity_score + 42  # Base + fixed offset
    
    # Print for traceability (required)
    return final_diagnostic

# Data preparation
log_entries, critical_alerts = accumulate_logs(telemetry_stream)

# Execution point of interest
final_diagnostic = process_metrics(log_entries, system_flags)

# Output result
print(f"Result: {final_diagnostic}")