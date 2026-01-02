import math

def analyze_pattern(sequence):
    return sum(1 for i in range(len(sequence)-1) if sequence[i] < sequence[i+1])

def dummy_transform(x):
    # Irrelevant transformation used in dead code path
    return (x ** 2 + 3*x + 1) % 100

def compute_entropy(values):
    total = sum(values)
    probabilities = [v / total for v in values if v > 0]
    return -sum(p * math.log2(p) for p in probabilities)

data_log = [
    {'timestamp': 1000, 'ops': 50, 'errors': 2, 'mode': 'A'},
    {'timestamp': 1001, 'ops': 60, 'errors': 1, 'mode': 'B'},
    {'timestamp': 1002, 'ops': 55, 'errors': 0, 'mode': 'A'},
    {'timestamp': 1003, 'ops': 70, 'errors': 3, 'mode': 'C'},
    {'timestamp': 1004, 'ops': 65, 'errors': 1, 'mode': 'B'}
]

# Distractor variables (irrelevant computations)
baseline_ops = 55
peak_window = max([entry['ops'] for entry in data_log]) - min([entry['ops'] for entry in data_log])
error_rate_sequence = [entry['errors'] for entry in data_log]
trend_analysis = analyze_pattern([entry['ops'] for entry in data_log])

config = {
    'threshold': 58,
    'weight_a': 0.6,
    'weight_b': 0.4,
    'debug_mode': False,
    'version': '2.1-alpha'
}

# Unused function - red herring
def deprecated_normalization(arr):
    mean_val = sum(arr) / len(arr)
    return [(x - mean_val) / mean_val for x in arr]

# Decoy metrics with misleading intermediate results
aggregate_metrics = []
for log in data_log:
    raw_metric = log['ops'] * (1 + log['errors'])
    adjusted = raw_metric * 0.9 if log['mode'] == 'C' else raw_metric * 1.1
n    aggregate_metrics.append(adjusted)

# Real computation begins here — deeply nested and mixed with distractions
intermediate_scores = []
for entry in data_log:
    base = entry['ops']
    penalty = entry['errors'] * 5
    mode_bonus = {'A': 3, 'B': 5, 'C': 2}.get(entry['mode'], 0)
    score = base - penalty + mode_bonus
    intermediate_scores.append(score)

# Conditional expression usage (required python feature)
score_summary = {
    'high_perf': len([s for s in intermediate_scores if s > config['threshold']]),
    'low_perf': len([s for s in intermediate_scores if s <= config['threshold']])
}

scaling_factor = config['weight_a'] if score_summary['high_perf'] >= 3 else config['weight_b']

# Complex data transformation with tuple unpacking and filtering
filtered_with_index = [
    (i, s) for i, s in enumerate(intermediate_scores) if s > baseline_ops
]
indices, filtered_scores = zip(*filtered_with_index) if filtered_with_index else ([], [])

# Key distractor: irrelevant combinatorics calculation
from itertools import combinations
fake_correlation = sum(1 for a, b in combinations(filtered_scores, 2) if abs(a-b) < 5) if filtered_scores else 0

# Core logic buried among noise
weighted_total = sum(
    s * (0.8 if i in (1,3) else 0.7) for i, s in enumerate(intermediate_scores)
)

# Bit manipulation decoy (irrelevant)
bitmask = 0
for val in [len(data_log), baseline_ops, peak_window]:
    bitmask ^= (val << 1) | 1

# Main processing function with control flow and nesting
def process_metrics(logs, cfg):
    ops_list = [entry['ops'] for entry in logs]
    err_list = [entry['errors'] for entry in logs]
    
    avg_ops = sum(ops_list) / len(ops_list)
    total_err = sum(err_list)
    
    # Nested conditionals with conditional expressions
    stability = 'high' if avg_ops > 55 else 'low'
    severity = 'critical' if total_err > 4 else 'moderate'
    
    correction_factor = 1.25 if stability == 'high' and severity != 'critical' else 0.85
    
    # Multiple assignment and destructuring
    first, *middle, last = ops_list
    span = last - first
    
    # Real efficiency score computation (non-obvious due to distractions)
    raw_efficiency = avg_ops - (total_err * 4.2)
    bonus = 10 if trend_analysis > 2 else 5
    efficiency_score = (raw_efficiency * correction_factor) + bonus
    
    # Dead code path — looks important but unused
    diagnostics = []
    for entry in logs:
        if entry['mode'] == 'Z':  # Never true
            diagnostics.append('anomaly')
    
    final_data = {
        'efficiency_score': efficiency_score,
        'span': span,
        'diagnostics': diagnostics
    }
    
    return final_data

# Execution point of interest
final_output = process_metrics(data_log, config)
efficiency_score = final_output['efficiency_score']

print(f"Result: {efficiency_score}")