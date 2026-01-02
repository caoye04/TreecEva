import math

# Simulated system performance metrics (some are red herrings)
def get_system_metrics():
    raw_data = {
        'latency_ms': 142.5,
        'throughput_ops': 890,
        'error_rate': 0.0032,
        'cpu_load': 78.3,
        'memory_mb': 4210,
        'disk_iops': 230,
        'network_kbps': 987,
        'cache_hit_ratio': 0.88,
        'retry_count': 6,
        'timeout_events': 2
    }
    return raw_data

# Irrelevant transformation - distractor
def transform_data(data):
    transformed = {}
    for k, v in data.items():
        if 'rate' in k:
            transformed[k] = round(100 * (1 - v), 2)
        elif 'count' in k or 'events' in k:
            transformed[k] = max(0, v - 1)
        else:
            transformed[k] = v * 0.95
    return transformed

# Decoy scoring function - never actually used
def compute_health_score(metrics):
    score = 0
    score += min(metrics.get('latency_ms', 0) / 10, 20)
    score += min(metrics.get('throughput_ops', 0) / 50, 15)
    score += 10 if metrics.get('error_rate', 0) < 0.01 else 5
    return round(score, 2)

# Core logic: weight mapping using dictionary and lambda functions
def define_weights():
    # Weight adjustment based on deployment type (only some weights matter)
    base_weights = {
        'latency_ms': lambda w: w * 1.8,
        'throughput_ops': lambda w: w * 1.5,
        'error_rate': lambda w: w * 2.0,
        'cache_hit_ratio': lambda w: w * 1.2
    }
    configured = {}
    for key, func in base_weights.items():
        if 'ops' in key or 'ratio' in key:
            configured[key] = func(0.25)
        else:
            configured[key] = func(0.20)
    # Unused entries - red herring
    configured['dummy_entry'] = 0.0
    configured['placeholder'] = None
    return configured

# Data normalization function with early returns
def normalize(value, min_val, max_val):
    if value <= min_val:
        return 0.0
    if value >= max_val:
        return 1.0
    return (value - min_val) / (max_val - min_val)

# Main evaluation logic with nested conditions and irrelevant branches
def evaluate_performance(metrics, weights):
    score_components = {}
    
    # Real evaluation path
    latency_norm = normalize(metrics['latency_ms'], 50, 200)
    throughput_norm = normalize(metrics['throughput_ops'], 500, 1000)
    error_norm = 1 - normalize(metrics['error_rate'], 0.001, 0.01)
    cache_norm = normalize(metrics['cache_hit_ratio'], 0.7, 0.95)
    
    score_components['latency'] = (1 - latency_norm) * weights['latency_ms']
    score_components['throughput'] = throughput_norm * weights['throughput_ops']
    score_components['error'] = error_norm * weights['error_rate']
    score_components['cache'] = cache_norm * weights['cache_hit_ratio']
    
    # Dead branch - misleading
    if metrics.get('cpu_load', 0) > 90:
        score_components['throttled'] = -5.0
    else:
        score_components['throttled'] = 0.0  # Never affects final score
    
    # Complex aggregation with unused intermediate values
    temp_vals = []
    for k, v in score_components.items():
        if v != 0:
            temp_vals.append(v * 0.95)  # Distractor scaling
    
    # Actual final computation
    raw_total = sum(score_components[k] for k in ['latency', 'throughput', 'error', 'cache'])
    
    # Bonus logic based on combinatorics of thresholds
    bonus = 0
    met_targets = 0
    if metrics['latency_ms'] <= 150:
        met_targets += 1
    if metrics['throughput_ops'] >= 850:
        met_targets += 1
    if metrics['error_rate'] <= 0.005:
        met_targets += 1
    if metrics['cache_hit_ratio'] >= 0.85:
        met_targets += 1
    
    # Combinatoric bonus: 2^n for n targets met above threshold
    if met_targets >= 3:
        bonus = int(math.pow(2, met_targets - 2))
    
    # Final weighted score with bonus
    final_raw = raw_total * 100 + bonus
    
    # Redundant transformation - looks important but isn't
    audit_trace = []
    for key in sorted(weights.keys()):
        if isinstance(weights[key], float):
            audit_trace.append(f'{key}:{round(weights[key], 3)}')
    
    # Key assignment point
    final_score = round(final_raw, 2)
    
    # Unrelated cleanup - distractor
    del audit_trace
    temp_vals.clear()
    
    return final_score

# Orchestration with irrelevant setup
if __name__ == '__main__':
    # Fetch real data
    metrics = get_system_metrics()
    
    # Transform but don't use - red herring
    distorted = transform_data(metrics)
    _ = compute_health_score(distorted)  # Unused result
    
    # Define actual weights
    weights = define_weights()
    
    # Execute main logic
    final_score = evaluate_performance(metrics, weights)
    
    # Print result as required
    print(f"Result: {final_score}")