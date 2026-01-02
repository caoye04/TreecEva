def analyze_pattern(seq, limit):
    count = 0
    for i in range(len(seq)):
        if seq[i] % 2 == 0:
            count += (i + 1) * seq[i]
    return count % limit

# Irrelevant helper function (dead code path)
def legacy_calculate(x, y):
    temp = x ** 2 + y ** 2
    return temp // 3 if temp > 100 else temp

# Unused transformation map
transform_map = {
    'A': lambda x: x * 2,
    'B': lambda x: x + 5,
    'C': lambda x: x - 3,
    'D': lambda x: x ** 0.5
}

# Decoy variables with misleading names
current_epoch = 1729
learning_rate = 0.001
momentum_buffer = [0.9, 0.81, 0.729]

# Real data structures
health_data = [
    {'id': 'P001', 'vitals': [72, 120, 36.6], 'flags': [False, True, False]},
    {'id': 'P002', 'vitals': [85, 135, 37.1], 'flags': [True, True, True]},
    {'id': 'P003', 'vitals': [64, 110, 36.2], 'flags': [False, False, True]}
]

thresholds = {
    'heart_rate_low': 60,
    'heart_rate_high': 100,
    'systolic_low': 90,
    'systolic_high': 140,
    'temp_normal': 37.0
}

# Unused signal processing block (distractor)
signal_chain = [1, -1, 2, -2, 3]
filtered = []
for val in signal_chain:
    if val > 0:
        filtered.append(val ** 2)

# Dictionary-based rule engine (partially used)
rules_engine = {
    'critical': lambda hr, sys: hr < 50 or sys > 180,
    'elevated': lambda hr, sys: 100 <= hr < 110 or 140 <= sys < 160,
    'normal': lambda hr, sys: 60 <= hr <= 100 and 90 <= sys <= 140
}

# Misleading intermediate calculation
baseline_score = 0
for entry in health_data:
    hr = entry['vitals'][0]
    sys = entry['vitals'][1]
    if rules_engine['normal'](hr, sys):
        baseline_score += 1

# Core processing function
def evaluate_risk_level(patient_list, config):
    risk_count = 0
    stability_index = 0
    
    for p in patient_list:
        hr, sys, temp = p['vitals']
        flag_set = p['flags']
        
        # Real logic branch
        if hr > config['heart_rate_high'] or sys > config['systolic_high']:
            risk_count += 1
        
        # Secondary condition
        if temp > config['temp_normal'] and any(flag_set):
            stability_index -= 2
        elif all(flag_set):
            stability_index += 1

    return risk_count, stability_index

# Auxiliary transformation (distractor)
def encode_status(code_sequence):
    encoded = ''
    mapping = {True: 'X', False: 'O'}
    for code in code_sequence:
        encoded += ''.join(mapping[b] for b in code)
        encoded += '|'  
    return encoded.rstrip('|')

# Main metric processor
def process_metrics(data, limits):
    # Step 1: Extract flat arrays
    heart_rates = [entry['vitals'][0] for entry in data]
    systolics = [entry['vitals'][1] for entry in data]
    temps = [entry['vitals'][2] for entry in data]
    
    # Step 2: Compute anomaly scores
    hr_anomalies = sum(1 for hr in heart_rates if hr < limits['heart_rate_low'] or hr > limits['heart_rate_high'])
    sys_anomalies = sum(1 for sys in systolics if sys < limits['systolic_low'] or sys > limits['systolic_high'])
    
    # Step 3: Apply weighted aggregation
    total_score = (hr_anomalies * 3) + (sys_anomalies * 2.5)
    
    # Step 4: Adjust by temperature trend
    temp_deviation = sum((t - 36.5) * 10 for t in temps)
    
    # Step 5: Use dictionary lookup for adjustment factor
    adjustment_key = 'moderate' if temp_deviation < 5 else 'high'
    adjustments = {
        'low': 0.8,
        'moderate': 1.1,
        'high': 1.3
    }
    adjusted_score = total_score * adjustments.get(adjustment_key, 1.0)
    
    # Step 6: Apply modular correction based on patient count
    n_patients = len(data)
    corrected = int(adjusted_score) % n_patients if n_patients > 0 else 0
    
    # Step 7: Inject pattern analysis (uses irrelevant function but with fixed input)
    pattern_value = analyze_pattern([3, 6, 9, 12], 7)
    
    # Step 8: Final diagnostic computation
    final_component = corrected + pattern_value
    return final_component

# Execution flow
risk_stats = evaluate_risk_level(health_data, thresholds)
encoded_flags = encode_status([p['flags'] for p in health_data])

# Critical statement
final_diagnostic = process_metrics(health_data, thresholds)

print(f"Result: {final_diagnostic}")