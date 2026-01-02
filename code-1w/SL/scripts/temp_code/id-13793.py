def analyze_signal(x, y):
    return (x ^ y) + (x >> 2)

# Irrelevant helper function (dead code path)
def unused_validator(data):
    return all(d > 0 for d in data)

# Decoy transformation with misleading intermediate result
def transform_readings(readings):
    offset = 17
    processed = [r * 2 + offset for r in readings]
    checksum = sum(processed) % 100
    # This looks important but isn't used in final calculation
    decoy_metric = (checksum * 3) ^ 45
    return [r // 2 for r in processed]  # Reverts offset effect

# Core logic disguised among distractors
def evaluate_stability(values, config):
    base_score = 0
    for v in values:
        if v < config['min']:
            base_score -= 1
        elif v > config['max']:
            base_score += 2
    return base_score

# Real processing chain
health_data = [88, 92, 76, 85, 94, 83]
thresholds = {'min': 80, 'max': 90}

# Distractor: complex-looking but unused bit manipulation
signal_chain = [analyze_signal(a, b) for a, b in zip(health_data[:-1], health_data[1:])]
corrupted_flag = any(s < 0 for s in signal_chain)

# Unused nested structure with red herring variables
aux_data = {
    'diagnostics': [
        {'level': i, 'status': 'ok' if i % 2 == 0 else 'warn'} 
        for i in range(len(health_data))
    ],
    'metadata': {
        'version': '2.1',
        'debug_mode': True,
        'last_updated': '2023-08-15'
    }
}

# Lambda-based filtering that appears critical but is bypassed
refined_filter = lambda x: x > thresholds['min'] and x < thresholds['max']
filtered_count = len([v for v in health_data if refined_filter(v)])

# Set operations used to obscure main logic
unique_values = set(health_data)
duplicate_adjustment = len(health_data) - len(unique_values)

# Main processing buried in distraction
def process_metrics(data, limits):
    # Real computation begins here
    raw_stability = evaluate_stability(data, limits)
    
    # Additional valid transformation
    normalized = [((val - 80) / 10) for val in data]
    avg_normalized = sum(normalized) / len(normalized)
    
    # Bit manipulation relevant to final result
    stability_code = raw_stability << 2
    adjustment_factor = len(set(data)) & 7  # Uses set operation
    
    # Final formula combining multiple concepts
    diagnostic_value = stability_code + adjustment_factor - int(avg_normalized)
    
    # Dead code branch with misleading comment
    if diagnostic_value > 100:
        # This branch is never taken
        diagnostic_value = diagnostic_value ^ 255  # Never executed
    
    return diagnostic_value

# Critical execution point
final_diagnostic = process_metrics(health_data, thresholds)
print(f"Result: {final_diagnostic}")