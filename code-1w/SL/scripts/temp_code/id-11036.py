import math

# Irrelevant helper function (decoy)
def analyze_health(vital_signs):
    return sum(v[1] for v in vital_signs if v[0] == 'pulse')

# Unused transformation map
diagnostic_weights = {
    'temperature': 0.3,
    'respiration': 0.25,
    'blood_pressure': 0.45
}

# Red herring data list
vitals_log = [
    ('temperature', 98.6),
    ('respiration', 16),
    ('pulse', 72),
    ('oxygen', 98)
]

# Another decoy function with dead logic
def compute_stress_index(readings):
    stress = 0
    for r in readings:
        if r[0] == 'cortisol':
            stress += r[1] * 1.5
    return stress if stress > 0 else 0

# Core processing function with relevant logic buried
def transform_metrics(raw):
    processed = []
    for k, v in raw.items():
        if k in ['latency', 'throughput', 'error_rate']:
            processed.append((k, round(math.log(v + 1) * 100, 4)))
    return dict(processed)

# Lambda for dynamic threshold (actual use)
score_boost = lambda x: x * 1.1 if x > 85 else x * 0.95

# Simulated metric source
def generate_metrics():
    # Distractor variables
    temp_cache = [math.sin(i) for i in range(5)]
    _ = sum(temp_cache)  # unused

    base_data = {
        'latency': 120,
        'throughput': 450,
        'error_rate': 3,
        'timestamp': 1712345678,
        'version': '2.1.0'
    }
    return base_data

# Recursive normalization function (used)
def normalize_recursive(values, depth=0):
    if depth >= 3 or not values:
        return values
    updated = {}
    for k, v in values.items():
        updated[k] = v / (1 + depth * 0.05)
    return normalize_recursive(updated, depth + 1)

# Main evaluation logic
def evaluate_performance(data_dict):
    # Step 1: Transform raw metrics
    transformed = transform_metrics(data_dict)
    
    # Step 2: Extract key components
    latency_score = transformed.get('latency', 0)
    throughput_score = transformed.get('throughput', 0)
    error_score = transformed.get('error_rate', 0)
    
    # Step 3: Compute composite
    raw_composite = (latency_score * 0.4 + throughput_score * 0.5 - error_score * 0.1)
    
    # Step 4: Apply recursive normalization (simulate system calibration)
    norm_input = {'raw': raw_composite}
    normalized = normalize_recursive(norm_input)
    calibrated = normalized['raw']
    
    # Step 5: Apply conditional boost via lambda
    boosted = score_boost(calibrated)
    
    # Step 6: Final adjustment using modular arithmetic (key step)
    final_value = abs(int(boosted)) % 97321
    
    # Irrelevant branching (dead path)
    if len(data_dict) > 10:
        anomaly_flag = True
        audit_trace = []
        for _ in range(5):
            audit_trace.append('checked')
    
    # Decoy calculation with no effect
    _ = (calibrated ** 2) / 1000
    
    return final_value

# Execution flow
if __name__ == '__main__':
    # Generate realistic input
    metric_data = generate_metrics()
    
    # Evaluate system performance
    final_score = evaluate_performance(metric_data)
    
    # Print result as required
    print(f"Target result: {final_score}")