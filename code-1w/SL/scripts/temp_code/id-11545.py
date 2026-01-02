from collections import defaultdict
import math

# Simulate system performance metrics over time
def analyze_system_metrics(data_points):
    raw_values = [d['value'] for d in data_points]
    timestamps = [d['ts'] for d in data_points]
    
    # Irrelevant transformation: frequency analysis (not used)
    freq_map = defaultdict(int)
    for v in raw_values:
        freq_map[v] += 1
    
    # Efficiency calculation (used)
    base_efficiency = sum(raw_values) / len(raw_values)
    
    # Misleading intermediate: peak detection (unused)
    peaks = [i for i in range(1, len(raw_values)-1)
             if raw_values[i-1] < raw_values[i] > raw_values[i+1]]
    
    # Noise filter simulation (semi-relevant)
    filtered = [v for v in raw_values if v > base_efficiency * 0.8]
    efficiency = sum(filtered) / len(filtered) if filtered else 0
    
    # Simulate error accumulation
    error_count = 0
    for d in data_points:
        if 'err' in d and d['err']:
            error_count += 1
    
    # Red herring: unused statistical moment
    variance = sum((x - efficiency)**2 for x in filtered) / len(filtered) if filtered else 0
    skewness = sum((x - efficiency)**3 for x in filtered) / (len(filtered) * (variance**1.5)) if variance > 0 else 0
    
    return efficiency, error_count

# Performance evaluation with complex logic
def evaluate_performance(eff, errs):
    # Weighted scoring with decay function
    decay_factor = math.exp(-errs * 0.1)
    base_score = eff * 10 * decay_factor
    
    # Bonus logic based on error threshold (never triggered in this input)
    if errs < 3:
        bonus = 15
    elif errs < 6:
        bonus = 5
    else:
        bonus = 0  # Distractor: obvious path
    
    # Complex adjustment using lambda (idiomatic)
    adjuster = lambda x: x * 1.1 if x < 80 else x * 1.05
    adjusted = adjuster(base_score)
    
    # Final nonlinear transformation
    final = int(adjusted + bonus + math.log(max(1, adjusted)))
    return final

# Setup realistic dataset
metrics_log = [
    {'ts': 1001, 'value': 85, 'err': False},
    {'ts': 1002, 'value': 90, 'err': False},
    {'ts': 1003, 'value': 78, 'err': True},
    {'ts': 1004, 'value': 92, 'err': False},
    {'ts': 1005, 'value': 88, 'err': False},
    {'ts': 1006, 'value': 76, 'err': True},
    {'ts': 1007, 'value': 94, 'err': False},
    {'ts': 1008, 'value': 87, 'err': False},
    {'ts': 1009, 'value': 83, 'err': True},
    {'ts': 1010, 'value': 91, 'err': False}
]

# Extract key metrics
efficiency, errors = analyze_system_metrics(metrics_log)

# Critical execution point
final_score = evaluate_performance(efficiency, errors)

# Print result for inspection
print(f"Result: {final_score}")