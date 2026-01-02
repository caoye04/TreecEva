from collections import defaultdict, Counter

# Simulated system performance metrics with noise data
def get_raw_metrics():
    return {
        'latency': [120, 135, 110, 145, 98, 200, 105],
        'throughput': [850, 870, 830, 900, 880, 400, 860],
        'error_rate': [0.002, 0.003, 0.001, 0.004, 0.002, 0.05, 0.001],
        'memory_usage': [75, 80, 70, 85, 78, 95, 72]
    }

# Irrelevant helper - looks important but unused in final calculation
def analyze_trends(data):
    trends = {}
    for key, values in data.items():
        trend = 'increasing' if values[-1] > values[0] else 'decreasing'
        trends[key] = trend
    return trends

# Decoy function that appears related but is not used
def calculate_avg_response_time(logs):
    total = 0
    count = 0
    for entry in logs:
        if 'response' in entry and entry['valid']:
            total += entry['response']
            count += 1
    return total / count if count else 0

# Core processing pipeline
def preprocess_metrics(raw):
    cleaned = defaultdict(list)
    for key, values in raw.items():
        # Remove outliers (values beyond 1.5 * IQR)
        sorted_vals = sorted(values)
        q1, q3 = sorted_vals[1], sorted_vals[-2]
        iqr = q3 - q1
        lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
        for v in values:
            if lower <= v <= upper:
                cleaned[key].append(v)
    return dict(cleaned)

# Secondary transformation with distractor variables
def normalize_series(series, min_val=0, max_val=100):
    actual_min, actual_max = min(series), max(series)
    normalized = []
    for x in series:
        norm_x = (x - actual_min) / (actual_max - actual_min) * (max_val - min_val) + min_val
        normalized.append(round(norm_x, 3))
    return normalized

# Weight assignment with misleading defaults
def assign_weights(criteria, custom=None):
    default_weights = {
        'latency': 0.3,
        'throughput': 0.4,
        'error_rate': 0.2,
        'memory_usage': 0.1
    }
    # Dead code path - custom is never passed
    if custom and all(k in custom for k in criteria):
        return {k: custom[k] for k in criteria}
    return {k: default_weights[k] for k in criteria}

# Scoring engine with red herring logic
def compute_dimension_score(values, direction='lower_is_better'):
    base = sum(values) / len(values)
    volatility = (max(values) - min(values)) / base  # distraction metric
    adjustment = 1 - volatility * 0.1
    
    if direction == 'lower_is_better':
        return base * adjustment
    else:
        return (100 - base) * adjustment  # inverted logic for throughput

# Main evaluation with tuple unpacking and slicing distraction
def evaluate_performance(metrics, weights):
    scores = {}
    
    # Preprocess and normalize each metric
    processed = preprocess_metrics(metrics)
    
    # Extract recent samples (last 3) - slicing use
    recent_slices = {}
    for k, v in processed.items():
        if len(v) >= 3:
            recent_slices[k] = v[-3:]  # distractor: not used in final score
    
    # Normalize full series
    normalized = {}
    for k, v in processed.items():
        if k == 'throughput':
            normalized[k] = normalize_series(v, 0, 100)
        else:
            # latency, error_rate, memory_usage: lower is better
            rev_v = [max(v) + min(v) - x for x in v]  # invert temporarily
            normalized[k] = normalize_series(rev_v, 0, 100)
    
    # Compute individual scores using enumerate and zip
    directions = ['lower_is_better', 'higher_is_better', 'lower_is_better', 'lower_is_better']
    keys_in_order = ['latency', 'throughput', 'error_rate', 'memory_usage']
    
    temp_results = []
    for i, key in enumerate(keys_in_order):
        direction = directions[i]
        vals = normalized[key]
        raw_score = compute_dimension_score(vals, direction)
        temp_results.append((key, raw_score))
    
    # Final weighted aggregation
    weighted_sum = 0.0
    total_weight = 0.0
    score_map = dict(temp_results)
    
    for metric, (weight_idx, w) in zip(keys_in_order, enumerate(weights.values())):
        # Use zip and enumerate together in non-trivial way
        actual_weight = w
        metric_score = score_map[metric]
        weighted_sum += actual_weight * metric_score
        total_weight += actual_weight
    
    final_raw = weighted_sum / total_weight
    
    # Apply final nonlinear transformation
    penalty_factor = 1.0
    if any(compute_dimension_score(normalized[k]) > 90 for k in normalized):  # fake condition
        penalty_factor = 0.95
    
    # Critical execution point
    final_score = int(round(final_raw * penalty_factor))
    
    # Dead code - unreachable
    if False:
        backup = sum(len(v) for v in metrics.values())
        final_score = backup % 100
    
    return final_score

# Auxiliary data - looks like it might be used
log_data = [
    {'timestamp': '2023-01-01T10:00', 'response': 115, 'valid': True},
    {'timestamp': '2023-01-01T10:01', 'response': 140, 'valid': True},
    {'timestamp': '2023-01-01T10:02', 'response': 250, 'valid': False}
]

# Unused counter - creates false importance
usage_counter = Counter()
for m in ['latency', 'throughput', 'latency', 'error_rate']:
    usage_counter[m] += 1

# Primary execution flow
def main():
    raw_metrics = get_raw_metrics()
    
    # Distractor: analysis that isn't used
    trends = analyze_trends(raw_metrics)
    
    # Process and evaluate
    weights = assign_weights(raw_metrics.keys())
    final_score = evaluate_performance(raw_metrics, weights)
    
    # Print result as required
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()