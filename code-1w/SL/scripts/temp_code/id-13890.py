import math

# Simulated sensor data with noise and redundant fields
data_stream = [
    {'id': 'A7', 'temp_raw': 95.4, 'vibration': 0.87, 'status_flag': 1, 'timestamp': 1623456789, 'aux_power': 230},
    {'id': 'B3', 'temp_raw': 102.1, 'vibration': 1.03, 'status_flag': 0, 'timestamp': 1623456792, 'aux_power': 234},
    {'id': 'C9', 'temp_raw': 98.7, 'vibration': 0.94, 'status_flag': 1, 'timestamp': 1623456795, 'aux_power': 228}
]

# Irrelevant baseline calibration (distractor)
baseline_calib = {
    'gain': 1.02,
    'offset': -0.35,
    'thresholds': {'low': 90, 'high': 100},
    'legacy_mode': True
}

# Decoy function that is never called
def legacy_process(arr):
    return [x ** 0.5 for x in arr if x > 0]

# Unused intermediate transformation
raw_temps = [entry['temp_raw'] for entry in data_stream]
avg_temp = sum(raw_temps) / len(raw_temps)
adjusted_temps = [t * 0.98 + 0.5 for t in raw_temps]  # Distractor adjustment

# Real processing begins here
config = {
    'scale_factor': 0.75,
    'active_filters': ['outlier_suppress', 'drift_compensate'],
    'debug_level': 3
}

# Transform: extract relevant metrics and apply real scaling
def transform_entry(entry):
    temp_c = (entry['temp_raw'] - 32) * 5/9  # Convert to Celsius
    normalized_vibe = entry['vibration'] ** 2
    health_score = 100 - (temp_c - 35) * 2 - (normalized_vibe * 10)
    return {
        'node': entry['id'],
        'temp_c': round(temp_c, 2),
        'risk_metric': normalized_vibe,
        'health': max(0, min(100, health_score)),
        'valid': entry['status_flag'] == 1
    }

decode_id = lambda x: (ord(x[0]) - ord('A')) * 10 + int(x[1])  # Maps A7->7, B3->13, C9->29

transformed_data = []
for item in data_stream:
    processed = transform_entry(item)
    processed['node_code'] = decode_id(processed['node'])
    
    # Introduce misleading conditional branch (dead logic path)
    if processed['health'] > 90:
        processed['class'] = 'A'
    elif processed['health'] > 70:
        processed['class'] = 'B'
    else:
        # This block runs but field is unused
        processed['class'] = 'C+'
        anomaly_factor = math.log(processed['risk_metric'] + 1)
    
    # Another red herring: cumulative checksum not used later
    checksum = 0
    for char in processed['node']:
        checksum += ord(char)
    processed['checksum'] = checksum  # Dead assignment
    
    transformed_data.append(processed)

# Secondary distractor: set-based filtering that isn't used
valid_nodes = {d['node'] for d in transformed_data if d['valid']}
expired_nodes = {'X1', 'Y2'}
overlap = valid_nodes & expired_nodes  # Always empty

# Aggregation function with nested logic
aggregation_rules = [
    lambda x: x['temp_c'] * 0.4,
    lambda x: x['risk_metric'] * -5.0,
    lambda x: x['health'] * 0.6 if x['valid'] else 0
]

def process_metrics(data_list, cfg):
    total_score = 0.0
    scale = cfg['scale_factor']
    
    for record in data_list:
        # Apply each rule with conditional override (complex logic)
        partial = 0
        for rule in aggregation_rules:
            contribution = rule(record)
            # Misleading short-circuit that doesn't trigger
            if contribution > 100 or contribution < -100:
                contribution = 100 if contribution > 0 else -100
            partial += contribution
            
        # Only valid nodes contribute fully
        if record['valid']:
            total_score += partial * scale
        else:
            total_score += partial * 0.1  # Not triggered due to all being valid
    
    # Final nonlinear transformation
    if total_score > 0:
        final_val = math.tanh(total_score / 100) * 500
    else:
        final_val = math.exp(total_score / 200) * 250
    
    # Key execution point
    final_diagnostic = int(round(final_val))
    
    # Dead code paths below
    if final_diagnostic < 0:
        flag_state = -1
    elif final_diagnostic == 0:
        flag_state = 0
    else:
        flag_state = 1
        secondary_lock = flag_state << 2
    
    return final_diagnostic

# Execute critical statement
final_diagnostic = process_metrics(transformed_data, config)
print(f"Result: {final_diagnostic}")