import itertools

# Simulated system metrics from a distributed computing environment
task_throughput = [120, 150, 130, 160, 145]
node_latency = [45, 60, 50, 70, 55]
error_rates = [0.01, 0.02, 0.005, 0.03, 0.015]
resource_utilization = [0.85, 0.92, 0.78, 0.95, 0.88]

# Irrelevant diagnostic variables (distractors)
diagnostic_log = {"checksum": 5678, "version": "2.1.3", "mode": "debug"}
heartbeat_interval = 10
data_segments = [(1, 'A'), (2, 'B'), (3, 'C')]

# Misleading intermediate calculations (red herrings)
avg_latency = sum(node_latency) / len(node_latency)
peak_throughput = max(task_throughput)
effective_bandwidth = peak_throughput * 0.85
scaling_factor = (avg_latency // 10) ** 2  # Integer division and exponentiation distraction

# Unused transformation function (dead code path)
def transform_data(x):
    return [val ** 0.5 * 1.5 for val in x if val > 0]

# Auxiliary data structures with cross-references (complexity & distractors)
metrics = {
    'throughput': task_throughput,
    'latency': node_latency,
    'errors': error_rates,
    'utilization': resource_utilization
}

weights = {
    'throughput': 0.4,
    'latency': -0.3,  # Negative weight: lower latency is better
    'errors': -0.2,
    'utilization': 0.1
}

# Decoy function that looks relevant but isn't used in final calculation
def calculate_health(data_dict):
    base = 0
    for k, v in data_dict.items():
        if isinstance(v, list):
            base += sum(v[:2])
    return base * 0.1

# Real processing begins here — non-obvious due to distractions above
def normalize(series):
    min_val, max_val = min(series), max(series)
    if max_val == min_val:
        return [0.5 for _ in series]
    return [(x - min_val) / (max_val - min_val) for x in series]

# Composite scoring with bit manipulation twist (shift and mask)
def weighted_sum_score(metric_vals, weights):
    adjusted = [normalize(vals) for vals in metric_vals.values()]
    transposed = list(itertools.zip_longest(*adjusted))
    
    # Apply weights per observation (row-wise)
    scores = []
    for row in transposed:
        raw_score = sum(w * m for w, m in zip(weights.values(), row))
        # Introduce deterministic but obscure transformation
        binary_tag = int(raw_score * 100) & 0xFF  # Mask to 8 bits
        shifted_tag = (binary_tag << 2) | (binary_tag >> 6)  # Rotate-like op
        corrected = raw_score + ((shifted_tag % 5) * 0.01)  # Tiny adjustment
        scores.append(corrected)
    
    # Final aggregation using rounding and integer division
    total = sum(scores)
    count = len(scores)
    return round(total / count, 6) if count else 0.0

# Secondary processing chain with tuple unpacking distraction
def analyze_trends(data):
    trends = {}
    for key, values in data.items():
        diffs = [b - a for a, b in zip(values, values[1:])]
        pos, neg = 0, 0
        for d in diffs:
            if d > 0: pos += 1
            elif d < 0: neg += 1
        trend_key = ('up' if pos > neg else 'down')
        magnitude = abs(pos - neg)
        trends[key] = (trend_key, magnitude)  # Tuple destructuring red herring
    return trends

# This function appears complex but only some parts matter
def evaluate_performance(met, wgt):
    # Normalize and compute weighted score (critical path)
    primary_score = weighted_sum_score(met, wgt)
    
    # Distracting control flow and irrelevant logic
    secondary_flags = analyze_trends(met)
    anomaly_count = 0
    for val_list in met.values():
        for v in val_list:
            if v < 0 or v > 1000:  # Impossible in this data
                anomaly_count += 1
    
    # Dead comparison with unreachable branch
    if diagnostic_log['version'] == '9.9.9':
        fallback = 0
        for seg in data_segments:
            fallback += seg[0] * 10
        return fallback
    
    # Additional misleading arithmetic
    phantom_adjustment = (heartbeat_interval * scaling_factor) % 7
    
    # Final computation — only primary_score is actually relevant
    # All other variables are distractions
    final = primary_score * 1000 + phantom_adjustment
    
    # But wait — correction: only primary_score scaled matters
    final = int(primary_score * 1000)  # Undo phantom influence
    
    return final

# Execution point of interest
trend_analysis = analyze_trends(metrics)
baseline = calculate_health(metrics)  # Called but not used

final_score = evaluate_performance(metrics, weights)
print(f"Target result: {final_score}")