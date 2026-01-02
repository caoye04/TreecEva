import itertools

# Simulated sensor data with noise and redundant fields
data = [
    {'temp': 23.5, 'humidity': 65, 'pressure': 1013, 'valid': True, 'seq_id': 1},
    {'temp': 24.1, 'humidity': 67, 'pressure': 1012, 'valid': True, 'seq_id': 2},
    {'temp': 22.9, 'humidity': 70, 'pressure': 1015, 'valid': False, 'seq_id': 3},
    {'temp': 25.3, 'humidity': 60, 'pressure': 1010, 'valid': True, 'seq_id': 4},
    {'temp': 26.0, 'humidity': 58, 'pressure': 1009, 'valid': True, 'seq_id': 5}
]

# Weight configuration for scoring (some weights are irrelevant)
weights = {
    'temp_w': 0.5,
    'humidity_w': 0.3,
    'pressure_w': 0.1,
    'altitude_w': 0.0,  # Irrelevant - no altitude in data
    'dummy_w': 0.0       # Red herring
}

# Auxiliary function that looks important but is unused
def calculate_baseline(dataset):
    total = 0
    for d in dataset:
        total += d['temp'] * 0.1 + d['humidity'] * 0.05
    return total / len(dataset) if dataset else 0

# Another decoy: transforms data into useless format
def encrypt_sequence(ids):
    result = 0
    for i in ids:
        result ^= i << 2
    return result  # Never used

# Real processing function with embedded distractions
def normalize_value(val, min_val, max_val):
    # Simulate normalization even if not fully used
    return (val - min_val) / (max_val - min_val) if max_val > min_val else 0

def process_metrics(dataset, config):
    # Step 1: Filter valid entries
    valid_data = [d for d in dataset if d['valid']]
    
    # Step 2: Extract sequences and do irrelevant bitwise analysis
    seq_ids = [d['seq_id'] for d in dataset]
    encrypted_seq = 0
    for i in seq_ids:
        encrypted_seq ^= (i << 3) | (i >> 1)  # Complex but unused
    
    # Step 3: Compute base metrics
    avg_temp = sum(d['temp'] for d in valid_data) / len(valid_data)
    avg_humidity = sum(d['humidity'] for d in valid_data) / len(valid_data)
    
    # Step 4: Spurious correlation check (dead logic path)
    correlated_count = 0
    for a, b in itertools.combinations(valid_data, 2):
        if abs(a['temp'] - b['temp']) < 1.0 and abs(a['humidity'] - b['humidity']) < 3:
            correlated_count += 1
    adjustment_factor = 0.9 if correlated_count > 2 else 1.0
    
    # Step 5: Normalize values using fake bounds (partial distraction)
    norm_temp = normalize_value(avg_temp, 20.0, 30.0)
    norm_humidity = normalize_value(avg_humidity, 50.0, 80.0)
    
    # Step 6: Use dictionary to map normalized scores (only some used)
    score_components = {
        'thermal': norm_temp * 100,
        'moisture': norm_humidity * 100,
        'pressure_score': 0  # Placeholder
    }
    
    # Step 7: Calculate pressure trend (distraction)
    pressures = [d['pressure'] for d in valid_data]
    pressure_change = pressures[-1] - pressures[0] if len(pressures) > 1 else 0
    if pressure_change < 0:
        score_components['pressure_score'] = 10
    else:
        score_components['pressure_score'] = 5
    
    # Step 8: Apply weighted sum — only temp_w and humidity_w matter
    raw_score = (
        score_components['thermal'] * config['temp_w'] +
        score_components['moisture'] * config['humidity_w'] +
        score_components['pressure_score'] * config['pressure_w']
    )
    
    # Step 9: Apply adjustment from correlation (but adjustment_factor is always 1.0 here)
    adjusted_score = raw_score * adjustment_factor
    
    # Step 10: Final nonlinear transformation (simulates calibration)
    final_score = int(adjusted_score) + (adjusted_score % 1)  # Preserve decimal
    
    # Step 11: Red herring — conditional expression that evaluates but doesn't affect
    status_flag = 'OK' if final_score > 50 else 'LOW'
    log_entry = f'Status: {status_flag}, Score: {final_score:.2f}'
    
    # Step 12: Return actual answer
    return final_score

# Execution entry point
final_score = process_metrics(data, weights)
print(f"Result: {final_score}")