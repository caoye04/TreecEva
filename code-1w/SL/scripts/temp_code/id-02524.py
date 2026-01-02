def preprocess_readings(raw_readings):
    processed = {}
    for sensor, values in raw_readings.items():
        avg = sum(values) / len(values)
        processed[sensor] = round(avg, 2)
    return processed

raw_sensor_data = {
    'temp': [98.6, 99.1, 97.3, 98.8, 100.2],
    'pulse': [72, 75, 78, 74, 80],
    'respiration': [16, 18, 15, 17, 16],
    'oxygen': [98, 97, 99, 96, 98]
}

# Irrelevant normalization function (dead code path)
def normalize_signal(signal):
    max_val = max(signal)
    min_val = min(signal)
    return [(x - min_val) / (max_val - min_val) for x in signal]

# Unused transformation
def fourier_approximate(series):
    result = 0
    for i, x in enumerate(series):
        result += x * (i % 3 + 1)
    return result

processed_readings = preprocess_readings(raw_sensor_data)

# Threshold configuration map (used later)
threshold_map = {
    'temp': {'min': 97, 'max': 99, 'weight': 0.3},
    'pulse': {'min': 60, 'max': 100, 'weight': 0.25},
    'respiration': {'min': 12, 'max': 20, 'weight': 0.2},
    'oxygen': {'min': 95, 'max': 100, 'weight': 0.25}
}

# Decoy scoring system (never called)
def calculate_risk_score(metrics):
    score = 0
    for k, v in metrics.items():
        if k == 'temp':
            score += abs(v - 98.6) * 10
        elif k == 'pulse':
            score += max(0, v - 80) * 2
    return round(score, 2)

# Auxiliary function to check individual metric validity
def is_within_bounds(value, bounds):
    return bounds['min'] <= value <= bounds['max']

# Bit manipulation red herring (unused)
def encode_status_code(metric_key, value):
    key_hash = 0
    for c in metric_key:
        key_hash ^= ord(c)
    normalized = int((value - 90) * 10) if value > 90 else 0
    return (key_hash << 4) | (normalized & 0xF)

# Complex analysis with distractors
def analyze_metrics(metrics, config):
    status_flags = {}
    deviation_scores = {}
    weighted_deviation = 0.0
    
    # Meaningful but partially distracting intermediate calculations
    total_weighted_value = 0.0
    total_weight = 0.0
    
    for sensor_name, reading in metrics.items():
        cfg = config[sensor_name]
        
        # Real logic branch
        expected_mid = (cfg['min'] + cfg['max']) / 2
        deviation = abs(reading - expected_mid)
        
        # Distractor: complex bit-based flag (not used in final logic)
        raw_flag = 1 if reading >= expected_mid else 0
        encoded_flag = (raw_flag << 2) ^ 3
        status_flags[sensor_name] = bool(encoded_flag & 1)
        
        # Real contribution
        weight = cfg['weight']
        deviation_scores[sensor_name] = deviation * weight
        weighted_deviation += deviation * weight
        
        # Accumulator distraction (partially relevant)
        total_weighted_value += reading * weight
        total_weight += weight
    
    # Secondary metric (distractor)
    average_metric_value = total_weighted_value / total_weight if total_weight else 0
    
    # Additional decoy logic
    def generate_diagnostics(devs, avg_val):
        base = sum(devs.values()) * 100
        checksum = 0
        for d in devs.values():
            checksum ^= int(d * 10)
        return base + checksum
    
    # Unused diagnostic
    dummy_diag = generate_diagnostics(deviation_scores, average_metric_value)
    
    # Final computation — only this matters
    inverse_deviation = 100 - (weighted_deviation * 5)
    
    # Apply arbitrary scaling found in legacy systems
    scaled_diagnostic = round(inverse_deviation * 1.07, 4)
    
    # Final output variable
    final_diagnostic = int(round(scaled_diagnostic))
    
    # Dead code: simulation override (never triggered)
    if False and 'debug_mode' in metrics:
        final_diagnostic = 42
        
    return final_diagnostic

health_data = preprocess_readings(raw_sensor_data)
final_diagnostic = analyze_metrics(health_data, threshold_map)
print(f"Result: {final_diagnostic}")