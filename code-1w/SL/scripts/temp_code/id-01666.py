def preprocess_readings(raw_data):
    filtered = [x for x in raw_data if x > 0]
    baseline = sum(filtered) / len(filtered)
    adjusted = [x - baseline for x in filtered]
    return adjusted


def generate_quantum_signature(readings):
    signature = 0
    for i, val in enumerate(readings):
        signature ^= int(val * (i + 1)) % 256
    return signature

def evaluate_health_metrics(logs):
    stats = {}
    total_entries = len(logs)
    error_count = sum(1 for log in logs if 'ERR' in log)
    warning_count = sum(1 for log in logs if 'WRN' in log)
    stats['error_rate'] = error_count / total_entries if total_entries else 0
    stats['warning_density'] = warning_count / total_entries if total_entries else 0
    stats['health_score'] = (total_entries - error_count) / total_entries if total_entries else 0
    return stats

def transform_coordinates(coord_set):
    transformed = []
    for x, y in coord_set:
        rotated_x = x * 0.866 - y * 0.5
        rotated_y = x * 0.5 + y * 0.866
        transformed.append((rotated_x, rotated_y))
    magnitude = sum(x**2 + y**2 for x, y in transformed)**0.5
    return magnitude

def analyze_system_state(signature):
    binary_rep = bin(signature)[2:].zfill(8)
    ones_count = binary_rep.count('1')
    chunk_a = int(binary_rep[:4], 2)
    chunk_b = int(binary_rep[4:], 2)
    
    # Irrelevant transformation path (dead logic)
    temp_map = {i: (i * 3 + 7) % 10 for i in range(10)}
    mapped_vals = [temp_map.get(int(b), 0) for b in binary_rep]
    dummy_reduction = sum(mapped_vals[i] * (i+1) for i in range(len(mapped_vals))) % 100
    
    # Distractor: unused complex structure
    debug_info = {
        'raw_bits': binary_rep,
        'parity_check': signature % 2,
        'inverted_sig': int(binary_rep[::-1], 2),
        'placeholder_analysis': 'NONE'
    }
    
    # Actual diagnostic logic
    if ones_count >= 5:
        if chunk_a > chunk_b:
            level = 3
        else:
            level = 2
    else:
        if abs(chunk_a - chunk_b) <= 2:
            level = 1
        else:
            level = 0
    
    severity_index = (signature * ones_count) % 97
    final_diagnostic = (level * 1000) + severity_index
    
    # Red herring: unrelated data structure operations
    history_log = set()
    for i in range(3):
        history_log.add(f"diagnostic_pass_{i}_level_{level}")
    metadata_cache = {f"key_{i}": pow(level, i+1) for i in range(4)}
    
    # Final irrelevant computation
    phantom_sum = sum(pow(severity_index, i) % 101 for i in range(1, 4)) % 500
    
    return final_diagnostic

# Simulated sensor inputs (irrelevant to final answer but part of preprocessing)
raw_sensor_data = [12.1, -5.3, 18.7, 0.0, 23.5, -45.2, 15.8, 9.4]
processed_readings = preprocess_readings(raw_sensor_data)

# System logs for health evaluation (not used in final result)
system_logs = [
    'INFO: boot sequence completed',
    'ERR: disk I/O timeout',
    'WRN: temperature threshold exceeded',
    'INFO: network interface up',
    'ERR: database connection lost',
    'WRN: high memory pressure'
]
health_report = evaluate_health_metrics(system_logs)

# Coordinate transformation test case (distractor)
geolocation_points = [(3.2, 1.8), (5.1, -2.4), (-1.0, 4.3)]
navigation_metric = transform_coordinates(geolocation_points)

# Critical execution path
quantum_signature = generate_quantum_signature(processed_readings)
final_diagnostic = analyze_system_state(quantum_signature)
print(f"Result: {final_diagnostic}")