def analyze_component(reading, threshold=75):
    """Irrelevant helper that processes sensor readings."""
    if reading > threshold:
        return (reading * 0.8) + 10
    else:
        return (reading * 1.1) - 5

# Distractor: Sensor array data (not used in final computation)
sensor_readings = [68, 72, 94, 88, 79]
adjusted_readings = [analyze_component(x) for x in sensor_readings]


def transform_sequence(seq):
    """Misleading transformation on string sequences."""
    return ''.join(sorted(set(seq), reverse=True))

# Unused symbolic sequence
event_code = "gamma_alpha_beta"
processed_event = transform_sequence(event_code)


def compute_entropy(values):
    """Dead-end function: computes Shannon entropy (not used)."""
    import math
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log2(p) for p in probs)

entropy_value = compute_entropy([10, 20, 30])

# Core logic begins here — actual relevant data
baseline_metrics = {"latency": 45, "throughput": 120, "error_rate": 2}

supplemental_data = [18, 22, 19, 25, 17]
trimmed = [x for x in supplemental_data if x >= 18]  # Filters to [18,22,19,25]

def derive_calibration_factor(data):
    """Computes calibration factor using average and range."""
    avg = sum(data) / len(data)
    span = max(data) - min(data)
    return round(avg / (span + 1), 3)

calibration = derive_calibration_factor(trimmed)  # (18+22+19+25)/4 = 21; span=7 → 21/8 ≈ 2.625

# Set operations: core component
metric_set = {'throughput', 'jitter', 'bandwidth', 'latency'}
required_fields = {'latency', 'throughput', 'error_rate'}
optional_fields = {'jitter', 'bandwidth', 'retries'}

# Actual intersection used in logic
present_optionals = metric_set & optional_fields  # {'jitter', 'bandwidth'} → size 2

benchmark_data = {
    'latency': baseline_metrics['latency'] * 0.9,  # 40.5
    'throughput': baseline_metrics['throughput'] * 1.15,  # 138.0
    'error_rate': baseline_metrics['error_rate'],
    'jitter': 14,
    'bandwidth': 86
}

# Main evaluation logic
def evaluate_performance(metrics, data):
    score = 0
    
    if 'latency' in metrics and data['latency'] < 41:
        score += 25
    
    if 'throughput' in metrics:
        throughput_bonus = 10 if data['throughput'] > 130 else 5
        score += throughput_bonus
    
    # Conditional on set intersection size
    if len(present_optionals) >= 2:
        score += 15
    
    # Calibration-based adjustment
    adjusted_score = score * calibration  # score = 25+10+15 = 50 → 50 * 2.625 = 131.25
    
    # Final nonlinear transformation (key step)
    final = int(adjusted_score ** 0.5) * 10  # sqrt(131.25) ≈ 11.456 → int → 11 → *10 = 110
    
    # Dead code branch — never executed due to constant
    debug_mode = False
    if debug_mode:
        print(f'Diagnostic: {adjusted_score=}, {score=}')
    
    return final

# Execution point of interest
final_score = evaluate_performance(metric_set, benchmark_data)

# Irrelevant aggregation
summary_stats = {
    'max_reading': max(sensor_readings),
    'event_length': len(processed_event),
    'calibration_rounded': round(calibration, 2)
}

print(f'Target result: {final_score}')