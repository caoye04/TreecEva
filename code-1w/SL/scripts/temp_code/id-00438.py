def normalize_string(s):
    # Irrelevant utility function for string processing
    return s.strip().lower().replace(' ', '_')

# Decoy data structures
user_preferences = {
    'theme': 'dark',
    'notifications': True,
    'timeout': 30,
    'language': 'en'
}

temporary_buffer = [0] * 15  # Unused buffer array (red herring)

for i in range(len(temporary_buffer)):
    if i % 2 == 0:
        temporary_buffer[i] = i ** 2  # Distractor computation

# Real data for evaluation
metrics = [
    {'name': 'response_time', 'value': 120, 'weight': 0.25},
    {'name': 'accuracy', 'value': 0.94, 'weight': 0.35},
    {'name': 'throughput', 'value': 85, 'weight': 0.20},
    {'name': 'error_rate', 'value': 0.03, 'weight': 0.20}
]

baseline = {
    'response_time': 100,
    'accuracy': 0.90,
    'throughput': 80,
    'error_rate': 0.05
}

# Misleading intermediate scoring
raw_total = 0
for m in metrics:
    raw_total += m['value'] * m['weight']

adjustment_factor = 1.0
if raw_total > 90:
    adjustment_factor = 0.95
elif raw_total < 70:
    adjustment_factor = 1.1

# Dead code path - never executed due to logic above
if adjustment_factor == 1.05:
    raw_total *= 1.05

# Core evaluation logic buried among distractions
def calculate_deviation_score(metric_name, current_val, base_val):
    if metric_name in ['accuracy', 'throughput', 'response_time']:
        return (current_val - base_val) / base_val
    else:
        return (base_val - current_val) / base_val  # Inverted for error rate

def extract_key_indicators(data_list):
    # Complex unpacking and filtering
    keys = []
    values = []
    weights = []
    for item in data_list:
        name = normalize_string(item['name'])
        keys.append(name)
        values.append(item['value'])
        weights.append(item['weight'])
    return keys, values, weights

def evaluate_performance(met, base):
    total_adjusted = 0.0
    deviations = {}
    
    # Heavily nested logic with mixed concerns
    for entry in met:
        name = entry['name']
        current = entry['value']
        weight = entry['weight']
        base_val = base[name]
        
        dev = calculate_deviation_score(name, current, base_val)
        deviations[name] = dev
        
        # Non-linear transformation
        impact = weight * (1 + dev)
        
        # Conditional amplification
        if dev > 0.05:
            impact *= 1.1
        elif dev < -0.05:
            impact *= 0.9
            
        total_adjusted += impact
    
    # Final aggregation with scaling
    score = (total_adjusted / len(met)) * 100
    
    # Additional distraction: string-based switch
    mode_flag = 'standard'
    if score > 105:
        mode_flag = 'high_performance'
    elif score < 95:
        mode_flag = 'needs_improvement'
    
    # Irrelevant dictionary update
    user_preferences['last_mode'] = mode_flag
    
    return int(score)  # Truncate to integer

# Key execution point
keys_extracted, vals, ws = extract_key_indicators(metrics)

# Dummy loop with string operations (distraction)
decoded_labels = []
for k in keys_extracted:
    label = k.replace('_', ' ').title()
    if 'time' in label:
        label = label.upper()
    decoded_labels.append(label)

# Critical statement
final_score = evaluate_performance(metrics, baseline)

# Print result as required
print(f"Result: {final_score}")