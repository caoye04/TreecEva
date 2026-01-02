def analyze_trends(data, threshold=0.5):
    trend_list = []
    for val in data:
        if val > threshold:
            trend_list.append(1)
        else:
            trend_list.append(0)
    return trend_list

# Irrelevant helper function (decoy)
def compute_entropy(values):
    import math
    counts = {}
    for v in values:
        counts[v] = counts.get(v, 0) + 1
    total = len(values)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

# Unused transformation (dead code path)
def transform_scale(x, factor=2.5):
    return x * factor + 10

# Misleading normalization function that isn't used in final calculation
def normalize_scores(scores):
    max_val = max(scores)
    min_val = min(scores)
    if max_val == min_val:
        return [0.5 for _ in scores]
    return [(s - min_val) / (max_val - min_val) for s in scores]

# Core logic disguised among distractors
def filter_outliers(seq, limit=3):
    return [x for x in seq if abs(x) < limit]

# Heavily nested evaluation with red herrings
def evaluate_performance(metrics, base_config):
    temp_result = 0
    adjustment_factor = base_config.get('adjustment', 1.1)
    penalty_rate = base_config.get('penalty', 0.9)
    boost_flag = base_config.get('boost_enabled', False)
    decay_level = base_config.get('decay', 2)
    
    # Distractor: unused conditional branch
    if boost_flag:
        adjustment_factor *= 1.5
    else:
        dummy_cache = {f'key_{i}': i*2 for i in range(10)}  # Fake caching

    # Real computation begins
    raw_values = []
    for k, v in metrics.items():
        if k.startswith('metric_'):
            if isinstance(v, list):
                raw_values.extend([x for x in v if x > 0])
            elif isinstance(v, (int, float)):
                raw_values.append(v)
    
    # Filtering irrelevant entries
    filtered = [x for x in raw_values if x % 2 == 1]  # Only odd numbers contribute
    
    # Secondary filtering based on magnitude
    cleaned = filter_outliers(filtered, limit=50)
    
    # Accumulate result using complex conditional logic
    for val in cleaned:
        if val > 20:
            temp_result += int(val * adjustment_factor)
        elif val > 10:
            temp_result += int(val * penalty_rate)
        else:
            temp_result += val
    
    # Nested dictionary manipulation (core)
    audit_log = {}
    for step in ['init', 'filter', 'score']:
        if step == 'score':
            audit_log[step] = {"count": len(cleaned), "total": temp_result}
    
    # Final adjustment using bit manipulation (non-obvious)
    temp_result = temp_result ^ 0xAA  # XOR with hex constant
    temp_result = temp_result & 0xFFFF  # Clamp to 16 bits
    
    # Tertiary distraction: unused sorting and reversal
    sorted_cleaned = sorted(cleaned, reverse=True)
    reversed_once = sorted_cleaned[::-1]
    
    # Final score assignment
    final_score = temp_result + 100
    
    # Dead code: never accessed
    debug_snapshot = {
        'timestamp': 1678886400,
        'version': 'v2.3-alpha',
        'checksum': sum(reversed_once) * 3 % 1000
    }
    
    return final_score

# Global configuration (mixture of relevant and irrelevant keys)
baseline = {
    'adjustment': 1.2,
    'penalty': 0.8,
    'boost_enabled': False,
    'decay': 3,
    'mode': 'strict',
    'timeout': 30,
    'retries': 3,
    'cache_size': 128
}

# Complex input structure with mixed types and red herrings
metric_map = {
    'metric_a': [15, -5, 22, 33],
    'metric_b': 17,
    'metric_c': [8, 19, 41, 66],
    'aux_data': {'temp': 98, 'state': 'active'},
    'debug_mode': True,
    'metric_d': 13,
    'labels': ['x', 'y', 'z'],
    'metric_e': [-3, 7, 25, 55],
    'config_hash': 'abc123',
    'timestamp_ms': 1678886399
}

# Execution trace with decoy calls
_ = analyze_trends([0.1, 0.4, 0.7, 0.9])
_ = compute_entropy(['a', 'b', 'a', 'c'])

# Critical execution point
final_score = evaluate_performance(metric_map, baseline)

print(f"Result: {final_score}")