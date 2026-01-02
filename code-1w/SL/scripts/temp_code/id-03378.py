import math

def analyze_component_health(raw_readings, baseline):
    adjusted = [(r - baseline) ** 2 for r in raw_readings if r > 0]
    return sum(adjusted) / len(adjusted) if adjusted else 0.0

def validate_checksum(sequence):
    # Irrelevant validation function (dead path)
    chk = 0
    for x in sequence:
        chk = (chk ^ x) * 13 % 97
    return chk == 42

def decode_payload(encoded_data):
    # Decoding that looks important but isn't used in final result
    decoded = {}
    for k, v in encoded_data.items():
        if isinstance(v, list) and len(v) > 0:
            shifted = [((x << 2) & 255) for x in v]
            decoded[k + '_decoded'] = shifted
    return decoded

def compute_aggregate_stress(metrics):
    stress_levels = []
    for sensor_id, readings in metrics.items():
        avg = sum(readings) / len(readings)
        variance = sum((x - avg) ** 2 for x in readings) / len(readings)
        stress = math.sqrt(avg * variance)
        if stress > 15.0:
            stress_levels.append(stress * 0.85)
        else:
            stress_levels.append(stress)
    return round(sum(stress_levels), 4)

def evaluate_system_integrity(flags, logs):
    # Complex but ultimately unused integrity check
    critical_flags = [f for f in flags if 'ERR' in f]
    error_count = len(critical_flags)
    warning_count = len([f for f in flags if 'WRN' in f])
    score = (error_count * 10) - warning_count
    return score < 5

def process_metrics(entries, thresholds):
    diagnostics = {}
    total_entries = 0
    
    for entry in entries:
        node_id = entry['node']
        temp = entry['temp']
        pressure = entry['pressure']
        rpm = entry['rpm']
        
        # Real-time anomaly detection
        if node_id not in diagnostics:
            diagnostics[node_id] = {'anomalies': 0, 'score': 100}
        
        threshold = thresholds.get(node_id, {'t': 75, 'p': 100, 'r': 3000})
        
        if temp > threshold['t']:
            diagnostics[node_id]['anomalies'] += 1
            diagnostics[node_id]['score'] -= 15
        
        if pressure > threshold['p']:
            diagnostics[node_id]['anomalies'] += 1
            diagnostics[node_id]['score'] -= 10
        
        if rpm > threshold['r']:
            diagnostics[node_id]['anomalies'] += 1
            diagnostics[node_id]['score'] -= 20
        
        total_entries += 1
    
    # Aggregation logic with red herring variables
    total_anomalies = sum(d['anomalies'] for d in diagnostics.values())
    avg_score = sum(d['score'] for d in diagnostics.values()) / len(diagnostics)
    system_rating = avg_score - (total_anomalies * 2.5)
    
    # Final transformation (this is where the answer comes from)
    final_value = int(system_rating * 3) % 100000
    
    # Distractor: early exit that is never triggered due to data
    if total_entries > 1000:
        return -1  # Dead code path
    
    return final_value

# Simulated telemetry data (relevant input)
log_entries = [
    {'node': 'A1', 'temp': 85, 'pressure': 95, 'rpm': 2800},
    {'node': 'A1', 'temp': 70, 'pressure': 110, 'rpm': 3200},
    {'node': 'B2', 'temp': 90, 'pressure': 105, 'rpm': 2900},
    {'node': 'B2', 'temp': 80, 'pressure': 90, 'rpm': 3100},
    {'node': 'C3', 'temp': 65, 'pressure': 85, 'rpm': 2700}
]

# Threshold configuration (used in processing)
system_thresholds = {
    'A1': {'t': 75, 'p': 100, 'r': 3000},
    'B2': {'t': 80, 'p': 100, 'r': 3000},
    'C3': {'t': 70, 'p': 95, 'r': 2800}
}

# Irrelevant data structures (distractors)
raw_sensor_stream = [23, 84, 15, 92, 10, 88, 56, 77]
baseline_calibration = 20
checksum_sequence = [12, 45, 67, 89, 23, 56]
encoded_diagnostics = {
    'status': [1, 0, 1],
    'flags': [255, 128, 64]
}

# Unused function calls (misleading execution flow)
_ = analyze_component_health(raw_sensor_stream, baseline_calibration)
_ = validate_checksum(checksum_sequence)
_ = decode_payload(encoded_diagnostics)

# System flag array (looks important but unused in final calculation)
system_flags = ['OK', 'ERR_LINK', 'WRN_TEMP_HIGH', 'OK', 'ERR_DISK']
_ = evaluate_system_integrity(system_flags, log_entries)

# Key computation
final_diagnostic = process_metrics(log_entries, system_thresholds)

# Output result
print(f"Target result: {final_diagnostic}")