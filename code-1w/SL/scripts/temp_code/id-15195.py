import math

def analyze_signal(pattern):
    if len(pattern) < 3:
        return 0
    return sum([p ** 2 for p in pattern]) // len(pattern)

def decode_sequence(seq):
    decoded = 0
    for i, s in enumerate(seq):
        decoded += s * (2 ** i)
    return decoded

def validate_checksum(data):
    return sum(data) % 16 == 0

def filter_noisy_readings(readings):
    return [r for r in readings if r > 0.1]

def calculate_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        prob = v / total
        if prob > 0:
            entropy -= prob * math.log(prob, 2)
    return round(entropy, 6)

def merge_states(state_a, state_b):
    merged = {}
    for k in set(state_a.keys()) | set(state_b.keys()):
        merged[k] = state_a.get(k, 0) + state_b.get(k, 0)
    return merged

def simulate_failure_mode(mode):
    if mode == 'overheat':
        return 999
    elif mode == 'timeout':
        return -999
    else:
        return 0

def compute_diagnostic_score(metrics):
    base = metrics.get('power', 0)
    stress = metrics.get('load', 0)
    temp = metrics.get('temperature', 25)
    
    # Irrelevant distraction: unused complex calculation
    hypothetical_yield = (base * 1.5) + (stress * 0.75) - (temp * 0.2)
    adjusted_stress = max(stress - temp * 0.3, 0)
    
    score = base * 2
    if stress > 75:
        score += 20
    if temp > 80:
        score -= 30
    
    # Real logic path uses this
    if temp < 0 or stress == 0:
        score = score // 2
    
    return score

def process_metrics(log_data, system_state):
    # Distractor: unused signal analysis
    signal_pattern = [1, 0, 1, 1]
    signal_analysis = analyze_signal(signal_pattern)
    
    # Distractor: decoding irrelevant sequence
    test_sequence = [1, 0, 1]
    decoded_value = decode_sequence(test_sequence)
    
    # Distractor: checksum validation (not used in final result)
    raw_data_stream = [1, 2, 3, 4, 5, 6, 7, 8]
    is_valid = validate_checksum(raw_data_stream)
    
    # Real data processing begins
    filtered_logs = filter_noisy_readings([0.05, 0.3, 0.6, 0.01, 0.8])
    entropy = calculate_entropy(filtered_logs)
    
    # Simulate multiple failure modes (only one matters)
    failures = {
        'mode_a': simulate_failure_mode('overheat'),
        'mode_b': simulate_failure_mode('timeout'),
        'mode_c': simulate_failure_mode('none')
    }
    
    # Merging states - partially relevant
    active_state = merge_states(system_state, {'load': 85, 'temperature': 82})
    
    # Compute diagnostic score - actual contributor
    temp_metrics = {
        'power': 45,
        'load': active_state['load'],
        'temperature': active_state['temperature']
    }
    
    initial_score = compute_diagnostic_score(temp_metrics)
    
    # Conditional expression with string method red herring
    status_flag = 'CRITICAL' if initial_score < 40 else 'NORMAL'
    masked_flag = status_flag.lower().replace('critical', 'safe')  # irrelevant
    
    # Final computation using entropy and score
    adjustment_factor = 1.0
    if entropy > 0.5 and 'load' in active_state:
        adjustment_factor = 1.2
    
    # Key variable assignment
    final_diagnostic = int(initial_score * adjustment_factor)
    
    # Dead code path - misleading
    if final_diagnostic < 0:
        final_diagnostic = abs(final_diagnostic)
        final_diagnostic = final_diagnostic * 2  # never reached
    
    return final_diagnostic

# Main execution
log_entries = ['ERROR: timeout', 'INFO: boot', 'WARN: high temp']
system_status = {'power': 45, 'load': 70}

# Trigger the key statement
target_result = process_metrics(log_entries, system_status)
print(f"Target result: {target_result}")