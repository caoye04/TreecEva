import math

def analyze_pattern(sequence):
    if not sequence:
        return 0
    transformed = [x ** 0.5 for x in sequence if x > 0]
    return sum(transformed) / len(transformed) if transformed else 0

def validate_entry(record):
    return record.get('status') == 'active' and record.get('version', 0) >= 2

def compute_weighted_sum(data, weights):
    # Irrelevant complex weighting (dead logic path)
    total = 0
    for k, v in data.items():
        if k in weights:
            total += v * weights[k]
    return total if total > 0 else -total

def filter_outliers(values, threshold=2):
    mean_val = sum(values) / len(values)
    std_dev = (sum((x - mean_val) ** 2 for x in values) / len(values)) ** 0.5
    return [v for v in values if abs(v - mean_val) <= threshold * std_dev]

def collect_diagnostics(logs):
    # Distractor function: collects unused diagnostics
    error_count = 0
    warnings = []
    for log in logs:
        if 'error' in log:
            error_count += 1
        elif 'warn' in log:
            warnings.append(log)
    return {'errors': error_count, 'warnings': len(warnings)}

def evaluate_performance(metrics_log, config):
    # Core relevant variables
    base_metric = metrics_log.get('base_metric', 0)
    extra_bonus = 0
    
    # Simulated preprocessing (partially relevant)
    raw_values = [v for v in metrics_log.get('values', []) if v > 0]
    filtered_values = filter_outliers(raw_values)
    
    # Bit manipulation red herring
    bit_encoded = 0
    for v in raw_values[:3]:
        bit_encoded ^= int(v) << 1
    
    # Set operation: determine unique categories
    all_categories = set(metrics_log.get('categories', []))
    required_categories = set(['A', 'B', 'C'])
    missing_cats = required_categories - all_categories
    
    if len(missing_cats) == 0:
        extra_bonus += 15
    
    # Dictionary-based threshold logic (relevant)
    thresholds = config.get('thresholds', {})
    met_thresholds = 0
    for key, thresh in thresholds.items():
        if key in metrics_log and metrics_log[key] >= thresh:
            met_thresholds += 1
    
    if met_thresholds >= 2:
        extra_bonus += 22
    
    # Conditional accumulation with early termination
    accumulator = 0
    for val in filtered_values:
        if accumulator > 100:
            break
        if val % 2 == 0:
            accumulator += int(math.log(val + 1, 2))
        else:
            accumulator -= val // 3
    
    # Complex but partially irrelevant transformation
    pattern_score = analyze_pattern(filtered_values)
    adjusted_pattern = pattern_score * 1.75 if pattern_score > 3 else pattern_score * 0.8
    
    # Final decision logic — this is where answer comes from
    base_component = base_metric * 1.5
    volatility_penalty = len(raw_values) - len(filtered_values)
    final_score = base_component + extra_bonus + accumulator - (volatility_penalty * 3)
    
    # Dead code branch (misleading)
    if adjusted_pattern > 10:
        final_score *= 1.1
    
    # Unused diagnostic collection
    diagnostics = collect_diagnostics(metrics_log.get('logs', []))
    
    return int(final_score)

# Setup input data
baseline_config = {
    'version': 3,
    'thresholds': {
        'throughput': 80,
        'latency': 95,
        'consistency': 70
    }
}

metrics_log = {
    'base_metric': 42,
    'values': [16, 25, 36, 49, 64, 81, 100],
    'categories': ['A', 'B', 'C', 'D'],
    'throughput': 85,
    'latency': 92,
    'consistency': 70,
    'logs': ['info: init', 'warn: retry', 'info: done']
}

# Execute main logic
final_score = evaluate_performance(metrics_log, baseline_config)
print(f"Result: {final_score}")