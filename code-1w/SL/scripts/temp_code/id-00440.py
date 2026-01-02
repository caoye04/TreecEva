import math

def preprocess_inputs(raw_values):
    # Irrelevant preprocessing (dead path)
    if len(raw_values) == 0:
        return [0]
    filtered = [x for x in raw_values if x > 0]
    normalized = [(x - min(filtered)) / (max(filtered) - min(filtered) + 1e-8) for x in filtered]
    return normalized

def generate_synthetic_metrics(n):
    # Distractor: generates unused synthetic data
    return [math.sin(i * 0.5) + math.cos(i * 0.3) for i in range(n)]

def compute_entropy(data):
    # Misleading function: looks important but not used in final result
    total = sum(data)
    if total == 0:
        return 0.0
    probs = [x / total for x in data]
    return -sum(p * math.log2(p) for p in probs if p > 0)

def validate_thresholds(config, limits):
    # Dead logic branch with red herring variables
    checks = []
    for k, v in config.items():
        if k in limits:
            checks.append(v <= limits[k])
    return all(checks)

def accumulate_weighted_sum(entries, weights):
    # Partially relevant but ultimately bypassed in key logic
    if len(entries) != len(weights):
        weights = weights[:len(entries)]
    return sum(e * w for e, w in zip(entries, weights))

def evaluate_performance(metrics, cache):
    # Core logic embedded within distractions
    base = cache.get('reference', 1.0)
    adjustment = 0.0
    
    # Conditional expression (required feature)
    scaling_factor = 2.5 if sum(metrics) > 10 else 1.8
    
    # Lambda for dynamic filtering (required feature)
    outlier_filter = lambda x: x < (base * 1.5)
    filtered_metrics = [m for m in metrics if outlier_filter(m)]
    
    # Accumulation with conditional modification
    temp_sum = 0
    for val in filtered_metrics:
        if val > base:
            temp_sum += val * scaling_factor
        elif val == base:
            temp_sum += val
        else:
            temp_sum += val * 0.7
    
    # Red herring: complex bit manipulation (irrelevant to result)
    decoy_value = int.from_bytes(b'perf', 'big')
    decoy_value ^= 0xFF
    decoy_value >>= 2
    decoy_value += len(filtered_metrics) ** 2
    
    # Key intermediate transformation
    raw_score = temp_sum / (base + 1e-6)
    
    # Multiple nested conditions (3 levels deep)
    if raw_score > 15:
        if scaling_factor == 2.5:
            adjustment = 2.0 if len(filtered_metrics) % 2 == 0 else 1.5
        else:
            adjustment = 1.0
    elif raw_score > 8:
        if base < 2:
            adjustment = 0.8
        else:
            adjustment = 0.5
    else:
        adjustment = 0.2
    
    # Final computation
    final_score = raw_score + adjustment
    
    # Unused container with cross-reference distraction
    log_entry = {
        'input_size': len(metrics),
        'filtered_count': len(filtered_metrics),
        'decoy_checksum': decoy_value,
        'computed_at': 'simulated_timestamp'
    }
    
    return final_score

# Main execution flow
if __name__ == '__main__':
    # Real input data
    sensor_readings = [3.2, 4.1, 1.8, 5.7, 2.3, 6.4, 0.9, 3.3]
    
    # Irrelevant synthetic generation (distractor)
    fake_data = generate_synthetic_metrics(10)
    
    # Preprocessing that isn't used
    processed = preprocess_inputs(sensor_readings)
    
    # Cache setup - only this matters
    baseline_cache = {'reference': 3.0, 'version': 'v2.1'}
    
    # Metric transformation chain
    transformed = [math.sqrt(x * 1.5) for x in sensor_readings]
    amplified = [t * 1.3 for t in transformed]
    metric_data = [a + 0.5 for a in amplified]
    
    # Validation call with unused return
    config = {'tolerance': 0.1, 'window': 5}
    limits = {'tolerance': 0.15, 'window': 10, 'depth': 3}
    _ = validate_thresholds(config, limits)
    
    # Weighted sum with unused result
    weights = [0.1, 0.2, 0.3, 0.4, 0.5]
    _ = accumulate_weighted_sum(transformed, weights)
    
    # Critical statement
    final_score = evaluate_performance(metric_data, baseline_cache)
    
    # Output result as required
    print(f"Result: {final_score}")