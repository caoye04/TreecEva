from collections import defaultdict, Counter
import math

# Simulated system diagnostics (irrelevant to final result)
def analyze_diagnostics(logs):
    error_count = defaultdict(int)
    for log in logs:
        if 'ERROR' in log:
            error_count[log.split()[0]] += 1
    return dict(error_count)

def compute_fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

# Unused transformation chain
def transform_data(data_list):
    temp_result = []
    for item in data_list:
        temp_result.append({
            'orig': item,
            'squared': item ** 2,
            'log_val': math.log(item) if item > 0 else 0
        })
    # Dead processing branch
    processed = [x['squared'] for x in temp_result if x['orig'] > 5]
    normalized = [p / sum(processed) for p in processed]
    return normalized

# Core business logic with distractors
def evaluate_efficiency(records):
    efficiency_map = {}
    total_records = len(records)
    valid_count = 0
    
    for r in records:
        key = r['type']
        val = r['value']
        if val > 0:
            # Red herring computation
            inverse = 1 / val
            efficiency_map[key] = efficiency_map.get(key, 0) + math.sqrt(val) * 0.1
            valid_count += 1
    
    # Misleading normalization
    for k in efficiency_map:
        efficiency_map[k] = round(efficiency_map[k] / (valid_count + 1e-8), 3)
    
    return efficiency_map

# Key function that affects final answer
def calculate_weighted_average(values, weights):
    if len(values) != len(weights):
        return -1
    total = 0.0
    weight_sum = 0.0
    for i in range(len(values)):
        total += values[i] * weights[i]
        weight_sum += weights[i]
    return round(total / weight_sum, 6) if weight_sum > 0 else 0

# Central processing with multiple distractions
def process_performance(metric_log, adjustment_rules):
    # Real data used in computation
    base_metrics = [m['score'] for m in metric_log if m['active']]
    modifiers = [adjustment_rules.get(m['category'], 1.0) for m in metric_log if m['active']]
    
    # Irrelevant grouping
    category_counter = Counter([m['category'] for m in metric_log])
    type_breakdown = defaultdict(list)
    for m in metric_log:
        type_breakdown[m['type']].append(m['score'])
    
    # Fake recursive smoothing (never called)
    def smooth_recursive(arr, depth=0):
        if depth >= 3 or len(arr) < 2:
            return arr
        smoothed = [(arr[i] + arr[i+1]) / 2 for i in range(len(arr)-1)]
        return smooth_recursive(smoothed, depth+1)
    
    # Distractor variables
    peak_value = max(base_metrics) if base_metrics else 0
    decay_factor = 0.95 ** len(base_metrics)
    baseline_shift = sum(1 for m in metric_log if not m['active']) * 0.05
    
    # Actual critical computation path
    raw_average = sum(base_metrics) / len(base_metrics) if base_metrics else 0
    adjusted_scores = [s * modifiers[i] for i, s in enumerate(base_metrics)]
    
    # Secondary adjustment using weighted average
    time_weights = [0.8 ** i for i in range(len(adjusted_scores))]  # exponential decay
    reversed_adjusted = adjusted_scores[::-1]
    time_weighted_avg = calculate_weighted_average(reversed_adjusted, time_weights)
    
    # Final transformation
    stability_penalty = abs(len(base_metrics) - category_counter['core']) * 0.01
    final_value = (time_weighted_avg * 1.05) - stability_penalty + baseline_shift
    
    # This is the actual answer variable
    final_score = int(round(final_value * 100))
    
    # Dead code branches
    if False:
        backup = compute_fibonacci(10)
        fallback = transform_data([5, 10, 15])
    
    return final_score

# Input data with mixed relevance
metrics = [
    {'score': 0.72, 'category': 'core', 'type': 'primary', 'active': True},
    {'score': 0.68, 'category': 'aux', 'type': 'secondary', 'active': True},
    {'score': 0.81, 'category': 'core', 'type': 'primary', 'active': True},
    {'score': 0.59, 'category': 'aux', 'type': 'secondary', 'active': True},
    {'score': 0.75, 'category': 'core', 'type': 'primary', 'active': True},
    {'score': 0.00, 'category': 'debug', 'type': 'test', 'active': False},  # inactive
    {'score': 0.64, 'category': 'aux', 'type': 'secondary', 'active': True}
]

adjustments = {
    'core': 1.05,
    'aux': 0.95,
    'debug': 0.1
}

# Execute main logic
diag_logs = ["INFO: OK", "ERROR: TIMEOUT", "WARNING: SLOW"]
diag_analysis = analyze_diagnostics(diag_logs)  # unused

# Critical execution point
final_score = process_performance(metrics, adjustments)

print(f"Result: {final_score}")