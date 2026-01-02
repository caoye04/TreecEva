import itertools

# Simulated system performance metrics (some relevant, some distractors)
metrics = {
    'latency': 120,           # milliseconds
    'throughput': 850,        # requests/sec
    'error_rate': 0.04,       # percentage
    'cpu_load': 78.5,         # percent usage (distractor)
    'memory_usage': 62,       # MB (distractor)
    'concurrent_users': 490,  # active connections
    'bandwidth': 95,          # Mbps (distractor)
    'cache_hit_ratio': 0.88,  # important for scoring
    'retry_count': 3,         # operational noise
    'availability': 0.995     # SLA metric
}

# Weight configuration: only some keys contribute to final score
weights = {
    'latency': -0.2,              # negative impact
    'throughput': 0.15,
    'error_rate': -0.25,
    'concurrent_users': 0.1,
    'cache_hit_ratio': 0.2,
    'availability': 0.3             # high importance
    # Note: cpu_load, memory_usage, bandwidth, retry_count are NOT in weights → irrelevant
}

# Irrelevant transformation pipeline (dead code path)
def transform_metrics_raw(data):
    return {k: v * 1.05 for k, v in data.items() if isinstance(v, (int, float))}

def normalize_log_scale(val):
    import math
    return math.log(val + 1)

# Decoy scoring function (never called)
def legacy_evaluate(m):
    score = 0
    for k, v in m.items():
        if 'usage' in k:
            score -= v * 0.1
        elif 'rate' in k or 'error' in k:
            score -= v * 5
        else:
            score += v * 0.01
    return round(score, 2)

# Real evaluation logic
def calculate_dimensional_score(value, max_val=1000, reverse=False):
    normalized = min(value / max_val, 1.0)
    return (1 - normalized) if reverse else normalized

def evaluate_performance(met, wgt):
    score = 0.0
    components_used = []
    
    # Real logic: iterate only over weighted keys
    for key, weight in wgt.items():
        if key not in met:
            continue
        
        val = met[key]
        
        # Special handling per metric type
        if key == 'latency':
            # Inverse scoring: lower latency = higher score
            base = calculate_dimensional_score(val, max_val=200, reverse=True)
        elif key == 'error_rate' or key == 'availability':
            base = val if key == 'availability' else (1 - val)
        elif key == 'cache_hit_ratio':
            base = val
        else:
            base = calculate_dimensional_score(val)
        
        contribution = base * abs(weight)
        if weight < 0:
            contribution = -contribution
        
        score += contribution
        components_used.append((key, contribution))
    
    # Apply non-linear adjustment based on concurrent user load
    if 'concurrent_users' in met and met['concurrent_users'] > 400:
        boost_factor = 1 + (min(met['concurrent_users'], 1000) - 400) / 2000
        score *= boost_factor
    
    # Red herring: attempt to correlate with unrelated metrics (no effect)
    suspicious_correlation = None
    for pair in itertools.combinations(['cpu_load', 'memory_usage', 'bandwidth'], 2):
        x, y = met.get(pair[0], 0), met.get(pair[1], 0)
        if x > 0 and y > 0:
            corr = (x * y) / 10000
            suspicious_correlation = corr if not suspicious_correlation else max(suspicious_correlation, corr)
    
    # Final clamping and rounding
    score = max(-100, min(score, 100))
    return round(score, 4)

# Secondary distraction: sort metrics by name for no functional reason
sorted_keys = sorted(metrics.keys())
displacement_map = {k: i for i, k in enumerate(sorted_keys)}

# Dummy list processing using conditional expressions
flags = ["high" if v > 50 and isinstance(v, (int, float)) else "low" for k, v in metrics.items() if 'usage' in k or 'load' in k]

# Actual execution point
baseline = sum(v for k, v in metrics.items() if 'count' in k or 'retry' in k)  # minor red herring

# Critical statement
final_score = evaluate_performance(metrics, weights)

# Print result as required
print(f"Result: {final_score}")