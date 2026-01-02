import math

def analyze_signal_strength(signal_data, threshold=0.75):
    # Irrelevant signal processing function (dead code path)
    filtered = [x for x in signal_data if x > threshold]
    return sum(filtered) / len(signal_data) if signal_data else 0.0

def compute_entropy(values):
    # Unused entropy calculation (distractor)
    total = sum(values)
    probabilities = [(v / total) for v in values if v > 0]
    return -sum(p * math.log2(p) for p in probabilities)

def transform_coordinates(x, y, z):
    # Geospatial red herring - not used in main logic
    radius = math.sqrt(x**2 + y**2 + z**2)
    lat = math.atan2(z, math.sqrt(x**2 + y**2))
    lon = math.atan2(y, x)
    return (radius, lat, lon)

def accumulate_diagnostics(records):
    # Heavily nested accumulator with mixed data types
    accumulator = {}
    temp_cache = []
    for r in records:
        key = r['id'] % 10
        if key not in accumulator:
            accumulator[key] = {'count': 0, 'values': [], 'active': True}
        
        processed_val = (r['value'] ** 2 + r['timestamp'] % 7) // 3
        
        if r['status'] & 1:
            processed_val -= r['flags'].get('offset', 0)
        
        accumulator[key]['values'].append(processed_val)
        accumulator[key]['count'] += 1
        
        temp_cache.append({'ref': key, 'data': processed_val})
    
    # Dead code: temp_cache is never used again
    if len(temp_cache) > 100:
        temp_cache.clear()
    
    return accumulator

def filter_anomalies(diag_map, min_count=3):
    # Filter logic that modifies state
    cleaned = {}
    for k, v in diag_map.items():
        if v['count'] >= min_count and v['active']:
            cleaned[k] = sum(v['values'])
    return cleaned

def aggregate_metrics(log_entries, system_state):
    # Core computation buried in distractions
    base_score = 0
    adjustment_factor = system_state.get('calibration', 1.0)
    
    # Real path starts here
    raw_sum = sum(entry['value'] for entry in log_entries)
    entry_count = len(log_entries)
    
    # Bit manipulation red herring
    masked_sum = raw_sum & 0xFFFF
    
    # Lambda for dynamic weighting (actual use)
    weight_fn = lambda x: 1.1 if x % 2 == 0 else 0.9
    weighted_sum = sum(weight_fn(e['id']) * e['value'] for e in log_entries)
    
    # Dictionary-based state mutation
    stats = {
        'total': raw_sum,
        'weighted': weighted_sum,
        'count': entry_count
    }
    
    if stats['count'] > 0:
        stats['avg_raw'] = stats['total'] / stats['count']
        stats['avg_weighted'] = stats['weighted'] / stats['count']
    
    # Actual answer derivation
    base_score += int(stats['avg_weighted'] * 100)
    
    # Conditional bit flip based on system mode (distractor)
    if system_state['mode'] == 'diagnostic':
        base_score ^= system_state.get('debug_key', 0)
    
    # Final adjustment using modular arithmetic
    calibration_offset = (system_state['version'] * 17) % 13
    final_score = base_score + calibration_offset
    
    # Decoy variable with misleading name
    diagnostic_checksum = (final_score * 3) % 97
    
    # The real target variable
    final_diagnostic = final_score * adjustment_factor
    
    return final_diagnostic

# Simulated input data
log_entries = [
    {'id': 101, 'value': 42, 'timestamp': 1678886400, 'status': 3, 'flags': {'offset': 2}},
    {'id': 102, 'value': 38, 'timestamp': 1678886460, 'status': 1, 'flags': {}},
    {'id': 103, 'value': 45, 'timestamp': 1678886520, 'status': 3, 'flags': {'offset': 1}},
    {'id': 104, 'value': 39, 'timestamp': 1678886580, 'status': 0, 'flags': {}},
    {'id': 105, 'value': 44, 'timestamp': 1678886640, 'status': 1, 'flags': {}}
]

system_state = {
    'mode': 'diagnostic',
    'version': 5,
    'calibration': 1.2,
    'debug_key': 255,
    'thresholds': [0.5, 0.7, 0.9],
    'active_sensors': {1, 3, 4, 7}
}

# Unused but plausible-looking intermediate steps
signal_data = [0.8, 0.6, 0.9, 0.7, 0.5]
dummy_entropy = compute_entropy([8, 4, 2, 1])
geo_coords = transform_coordinates(100, 200, 50)

diag_map = accumulate_diagnostics(log_entries)
cleaned_diagnostics = filter_anomalies(diag_map)

# Critical execution point
final_diagnostic = aggregate_metrics(log_entries, system_state)

print(f"Result: {final_diagnostic}")