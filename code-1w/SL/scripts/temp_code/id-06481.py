from itertools import combinations

def analyze_patterns(sequence):
    count = 0
    for i in range(len(sequence)):
        if sequence[i].startswith('A') and len(sequence[i]) > 3:
            count += 1
    return count

def compute_risk_level(items):
    risk = 0
    for item in items:
        if 'critical' in item or 'high' in item:
            risk += 1
    return risk * 2

def calculate_final_score(data):
    pattern_count = analyze_patterns(data)
    risk_factor = compute_risk_level(data)
    base_value = len([x for x in data if 'alert' in x])
    adjustment = 0
    
    # Generate all 2-element combinations to check for duplicate alerts
    for pair in combinations(data, 2):
        if 'alert' in pair[0] and 'alert' in pair[1]:
            adjustment -= 1
    
    final_score = (pattern_count * 3) + (base_value * 2) - risk_factor + adjustment
    return final_score

# Input data
log_entries = [
    'Alert: A12_failure',
    'Error: B2_overflow',
    'Warning: A3_critical',
    'Info: normal_operation',
    'Alert: timeout_A4',
    'Status: idle'
]

final_score = calculate_final_score(log_entries)
print(f"Target result: {final_score}")