from collections import Counter

def analyze_patterns(sequence):
    freq = Counter(sequence)
    dominant = max(freq, key=freq.get)
    return [k for k in freq if freq[k] > 1]

def validate_entry(record):
    if not record.get('active'):
        return False
    checksum = sum(ord(c) for c in record['id']) % 17
    return checksum == record.get('token', 0)

def compute_risk_level(inputs):
    risk_factors = []
    for val in inputs:
        if val < 0:
            risk_factors.append(3)
        elif val == 0:
            risk_factors.append(1)
        else:
            risk_factors.append(min(val // 10, 5))
    adjustment = len([r for r in risk_factors if r >= 3])
    base_risk = sum(risk_factors)
    return base_risk - adjustment

def calculate_performance(flags, metrics):
    temp_result = 0
    flag_multiplier = 1
    
    # Irrelevant string processing (distractor)
    labels = ['A', 'B', 'C']
    label_map = {lbl: idx for idx, lbl in enumerate(labels)}
    label_sum = sum(len(lbl) * (idx + 1) for idx, lbl in enumerate(labels))
    
    for f in flags:
        if f == 'speed':
            flag_multiplier *= 1.5
        elif f == 'accuracy':
            flag_multiplier *= 2.0
        elif f == 'redundancy':
            flag_multiplier *= 0.8
    
    # Real computation path
    raw_total = sum(metrics)
    adjusted_total = raw_total * flag_multiplier
    
    # Dead code branch (distractor)
    if len(metrics) > 100:
        outlier_count = 0
        for m in metrics:
            if m > 500:
                outlier_count += 1

    penalty = 0
    if len(metrics) % 2 == 1:
        penalty += 5
    
    # Accumulation with conditional logic
    bonus = 0
    for i, m in enumerate(metrics):
        if i % 4 == 0 and m > 10:
            bonus += 2
    
    temp_result = adjusted_total + bonus - penalty
    
    # Final transformation
    final_value = int(temp_result // 1.7)
    return final_value

# Main execution block
raw_data = [23, 45, 67, 12, 89, 34, 56]
data_strings = ['entry_001', 'entry_002', 'entry_003']

# Unused but plausible-looking preprocessing (distractor)
processed_labels = [s.upper().replace('_', '-') for s in data_strings]
length_stats = [len(s) for s in processed_labels]

# Validate dummy records (semi-relevant but not used directly)
records = [
    {'id': 'AX1', 'active': True, 'token': 6},
    {'id': 'BX2', 'active': False, 'token': 9},
    {'id': 'CX3', 'active': True, 'token': 4}
]
valid_count = sum(1 for r in records if validate_entry(r))

# Sequence analysis with side result (distractor)
seq_pattern = [1, 2, 2, 3, 3, 3, 4, 4]
duplicates = analyze_patterns(seq_pattern)

# Risk assessment (irrelevant to final score)
risk_inputs = [-5, 0, 15, 25, -10]
risk_score = compute_risk_level(risk_inputs)

# Core variables for target calculation
bonus_flags = ['speed', 'accuracy']
raw_metrics = [10, 20, 30, 40, 50]

# Key statement
final_score = calculate_performance(bonus_flags, raw_metrics)

print(f"Target result: {final_score}")