import math

def analyze_pattern(sequence):
    # Irrelevant function: analyzes frequency but not used in main flow
    freq = {}
    for item in sequence:
        freq[item] = freq.get(item, 0) + 1
    normalized = {k: v / len(sequence) for k, v in freq.items()}
    return sum(normalized.values())


def decode_signal(signal_str):
    # Misleading transformation: looks important but unused
    decoded = []
    for c in signal_str:
        decoded.append(ord(c) ^ 7)
    return [x % 256 for x in decoded]

# System telemetry simulation
telemetry_stream = [
    "S01:28.3,OK", "S02:19.8,ERR", "S01:29.1,OK", "S03:0.0,N/A",
    "S01:27.9,OK", "S02:20.2,OK", "S04:999,ALT"
]

# Parse logs into structured entries
log_entries = []
error_count = 0
placeholder_sum = 0.0

for entry in telemetry_stream:
    try:
        sensor_id, rest = entry.split(':', 1)
        temp_str, status = rest.split(',', 1)
        temperature = float(temp_str)
        
        log_entries.append({
            'sensor': sensor_id,
            'temp': temperature,
            'status': status.strip(),
            'flagged': status.strip() != 'OK',
            'timestamp': hash(entry) % 10000
        })
        
        if 'ERR' in status:
            error_count += 1
            placeholder_sum += temperature
    except Exception as e:
        continue

# System state with multiple components (some irrelevant)
system_state = {
    'nodes': ['N1', 'N2', 'N3'],
    'thresholds': {
        'critical': 95.0,
        'warning': 80.0,
        'baseline': 25.0
    },
    'checksum_ref': 0xABCD,
    'active_sensors': {'S01', 'S02', 'S03'},
    'maintenance_window': False,
    'version': 'v2.1.9'
}

# Decoy data structure - looks like it's used but isn't
historical_aggregates = {
    'weekly_avg': 22.1,
    'peak_load': 999,
    'downtime_events': [],
    'last_calibration': {'phase': 3, 'result': 0.97}
}

# Auxiliary function that appears critical but is only partially used
def compute_derived_index(entries, config):
    total = 0
    anomalies = 0
    recent_flags = []
    
    for e in entries:
        if e['flagged']:
            anomalies += 1
            recent_flags.append(e['timestamp'])
        base_val = e['temp'] * 1.05
        if e['sensor'] == 'S04':
            base_val *= 0.1  # Correction factor
        total += base_val
    
    avg_temp = total / len(entries) if entries else 0
    
    # This block modifies a decoy variable
    temp_snapshot = [e['temp'] for e in entries if not e['flagged']]
    if temp_snapshot:
        mean_clean = sum(temp_snapshot) / len(temp_snapshot)
        variance = sum((x - mean_clean)**2 for x in temp_snapshot) / len(temp_snapshot)
        historical_aggregates['dynamic_var'] = round(variance, 3)
    
    return {
        'index': round(avg_temp * (10 - min(anomalies, 5)), 2),
        'anomaly_rate': round(anomalies / len(entries), 3) if entries else 0
    }

# Core processing with red herrings and distractions
def process_metrics(entries, state):
    # Key variables
    diagnostic_score = 0
    active_diagnoses = set()
    temp_readings = []
    sensor_coverage = set()
    
    # Extract readings and perform intermediate calculations
    for record in entries:
        t_val = record['temp']
        s_id = record['sensor']
        
        temp_readings.append(t_val)
        sensor_coverage.add(s_id)
        
        # Real logic: accumulate score based on thresholds
        if t_val > state['thresholds']['critical']:
            diagnostic_score += 13
            active_diagnoses.add('OVERHEAT')
        elif t_val < 0 and record['status'] == 'ERR':
            diagnostic_score += 7
            active_diagnoses.add('FREEZE_FAULT')
        
        # Distractor: builds a set but doesn't affect final score
        if 'ALT' in record['status']:
            active_diagnoses.add('ALTERNATE_MODE')
    
    # Real contribution to answer
    baseline = state['thresholds']['baseline']
    deviation_total = 0
    for val in temp_readings:
        if val > 0:  # Ignore invalid zero readings
            deviation_total += abs(val - baseline)
    
    avg_deviation = deviation_total / len(temp_readings) if temp_readings else 0
    
    # Critical formula step
    diagnostic_score += int(avg_deviation)
    
    # Dead code path - looks like it updates score but doesn't
    if len(sensor_coverage) > 4:
        extra_weight = math.log(len(sensor_coverage))
        diagnostic_score += int(extra_weight)  # Never reached
    
    # Another decoy operation
    unused_merge = system_state['active_sensors'].union({'S05', 'S06'})
    sorted_timestamps = sorted([r['timestamp'] for r in entries])
    mid_point = sorted_timestamps[len(sorted_timestamps)//2] if sorted_timestamps else 0
    
    # Final computation using dictionary lookup distraction
    modifiers = {
        'N1': 1.1, 'N2': 0.95, 'N3': 1.0,
        'default': 0.8
    }
    
    net_modifier = 1.0
    for node in state['nodes']:
        net_modifier *= modifiers.get(node, modifiers['default'])
    
    # The real final answer calculation
    final_raw = diagnostic_score * 2
    
    # Apply meaningless rounding to mimic complexity
    final_diagnostic = int(round(final_raw + (mid_point % 10)))
    
    return final_diagnostic

# Execute main logic
temp_analysis = compute_derived_index(log_entries, system_state)
final_diagnostic = process_metrics(log_entries, system_state)

# Print result as required
print(f"Target result: {final_diagnostic}")