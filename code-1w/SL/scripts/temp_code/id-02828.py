def analyze_efficiency(data, threshold=0.75):
    # Irrelevant helper function (dead code path)
    return sum(1 for x in data if x > threshold) / len(data)

# Distractor variables (seem relevant but unused in final computation)
baseline = [0.6, 0.8, 0.9, 0.7, 0.5]
system_load = {'cpu': 0.45, 'memory': 0.67, 'disk': 0.33}

def normalize(values):
    max_val = max(values)
    return [v / max_val for v in values]

def calculate_entropy(probs):
    from math import log
    return -sum(p * log(p) for p in probs if p > 0)

# Unused lambda – red herring
assess_risk = lambda x: 'high' if x > 0.8 else 'low'

# Core data with mixed relevance
metrics = {
    'latency': 0.12,
    'throughput': 850,
    'error_rate': 0.004,
    'retries': 3,
    'timeout_count': 2
}

weights = {
    'latency': 0.3,
    'throughput': 0.4,
    'error_rate': 0.2,
    'retries': 0.1
    # Note: timeout_count has no weight – subtle distractor
}

# Complex preprocessing with partial relevance
preprocess = lambda m: {
    k: (
        1/v if k == 'latency' else 
        v/1000 if k == 'throughput' else 
        max(0, 1 - v*100) if k == 'error_rate' else 
        max(0, 5 - v) / 5
    )
    for k, v in m.items() if k in ['latency', 'throughput', 'error_rate', 'retries']
}

# Secondary transformation – looks important but only some output matters
transformed = preprocess(metrics)

# Simulate system health – irrelevant calculation
health_index = sum(1 for k in ['cpu', 'memory', 'disk'] if system_load[k] < 0.7)

# Decoy scoring function that's defined but not used
def compute_rank(score_map):
    return sorted(score_map.items(), key=lambda x: x[1], reverse=True)[0][0]

# Real evaluation logic buried among distractions
def evaluate_performance(m, w):
    normalized = preprocess(m)
    
    # Hidden conditional manipulation
    if normalized['latency'] < 0.7:
        w = {k: v * 1.2 if k == 'throughput' else v for k, v in w.items()}
    
    # Additional interference: fake aggregation
    avg_metric = sum(normalized.values()) / len(normalized)
    entropy_proxy = calculate_entropy(normalize(list(normalized.values())))
    
    # Actual weighted score – the real answer source
    raw_score = sum(normalized[metric] * w[metric] for metric in w)
    
    # Final adjustment based on retries (already partially normalized)
    penalty = 0.1 * (5 - normalized['retries'])
    adjusted_score = raw_score - penalty
    
    # This line determines the answer
    final_raw = adjusted_score * 100
    
    # Dead branch – never executed due to fixed input
    if metrics.get('timeout_count', 0) > 5:
        final_raw *= 0.8  # unreachable
    
    return int(final_raw)

# Execution point of interest
final_score = evaluate_performance(metrics, weights)

# Print result as required
print(f"Result: {final_score}")