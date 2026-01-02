def normalize_values(data, factor=1.0):
    # Irrelevant normalization function (not used in final calculation)
    return [x / factor for x in data]

# Decoy dataset - looks important but unused
raw_metrics_decoy = [89, 92, 76, 85, 94, 88]
decoy_weights = [0.1, 0.2, 0.15, 0.25, 0.1, 0.2]

# Actual working data
performance_logs = [
    {'user': 'A', 'response_time': 120, 'accuracy': 0.88, 'load_count': 5},
    {'user': 'B', 'response_time': 95, 'accuracy': 0.93, 'load_count': 4},
    {'user': 'C', 'response_time': 110, 'accuracy': 0.85, 'load_count': 6}
]

# Distractor: complex-looking but unused transformation
transformed_logs = []
for log in performance_logs:
    transformed = {k: v * 2 if isinstance(v, int) or isinstance(v, float) else v for k, v in log.items()}
    transformed['checksum'] = sum(ord(c) for c in log['user'])
    transformed_logs.append(transformed)

# Real metric extraction
response_times = [log['response_time'] for log in performance_logs]
accuracies = [log['accuracy'] for log in performance_logs]
loads = [log['load_count'] for log in performance_logs]

# Unused sorting - red herring
sorted_by_accuracy = sorted(enumerate(accuracies), key=lambda x: x[1], reverse=True)

# Normalization using min-max scaling (only this path is relevant)
def min_max_scale(vals):
    min_val, max_val = min(vals), max(vals)
    if min_val == max_val:
        return [0.5] * len(vals)
    return [(v - min_val) / (max_val - min_val) for v in vals]

normalized_response = min_max_scale(response_times)  # lower is better
normalized_accuracy = min_max_scale([1 - a for a in accuracies])  # invert accuracy
normalized_load = min_max_scale(loads)

# Combine into single normalized vector per user
normalized_data = []
for i, (r, a, l) in enumerate(zip(normalized_response, normalized_accuracy, normalized_load)):
    score = (r * 0.6) + (a * 0.3) + (l * 0.1)  # weighted penalty score
    normalized_data.append(round(score, 6))

# Bit manipulation decoy - looks sophisticated but unused
def calculate_checksum(arr):
    result = 0
    for val in arr:
        shifted = int(val * 1000) << 2
        result ^= shifted
    return result % 100

decoy_checksum = calculate_checksum(normalized_response)

# Metric weights - only this is used
metric_weights = {'latency': 0.6, 'error': 0.3, 'load': 0.1}

# Fake aggregation functions
def aggregate_legacy(data):
    return sum(d * 0.5 for d in data) / len(data)

def compute_robustness_index(seq):
    return abs(sum(seq[i] - seq[i-1] for i in range(1, len(seq))))

# Critical function - computes final score using weighted average
# The actual answer comes from here
prev_result = None
def evaluate_performance(weights, norm_data):
    global prev_result
    base_scores = []
    for idx, penalty in enumerate(norm_data):
        adjustment = 0.0
        if idx % 2 == 0:
            adjustment += 0.05
        if penalty > 0.5:
            adjustment -= 0.02
        adjusted = max(0.0, min(1.0, penalty + adjustment))
        base_scores.append(adjusted)
    
    # Apply weights (though they sum to 1.0, values are symbolic)
    total_weight = sum(weights.values())
    final_components = [s * total_weight for s in base_scores]
    
    # Real computation: harmonic mean with adjustment
    if prev_result is None:
        inv_sum = sum(1.0 / (s + 1e-8) for s in final_components)
        h_mean = len(final_components) / inv_sum
        prev_result = round(h_mean * 10000, 0)  # scale up
    else:
        prev_result += 1
    
    return int(prev_result)

# Dead code path - never reached
if __name__ != "__main__":
    fallback_data = normalize_values([100, 200, 300], 100)
    final_score = sum(fallback_data)

# Main execution flow
intermediate_flag = False
if len(normalized_data) >= 3:
    temp_state = {}
    for i, val in enumerate(normalized_data):
        temp_state[f'entry_{i}'] = val * (i + 1)
    
    # Dictionary operations and enumerate usage
    summary_stats = {}
    for j, (idx, val) in enumerate(enumerate(normalized_data)):
        key = f'stat_{j}'
        summary_stats[key] = val ** 2 + (j * 0.1)
    
    # This is the real execution point
    final_score = evaluate_performance(metric_weights, normalized_data)

    # Additional distraction: sorting dictionary items
    sorted_stats = sorted(summary_stats.items(), key=lambda x: x[1], reverse=True)
    derived_value = sum(int(v * 10) for k, v in sorted_stats)

    # Print required output
    print(f"Target result: {final_score}")
else:
    final_score = -999
    print("Result: -999")