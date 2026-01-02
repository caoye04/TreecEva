from collections import defaultdict
import itertools

# Simulated system metrics from a distributed network node
def get_raw_metrics():
    return {
        'latency_ms': 142,
        'packet_loss': 0.037,
        'throughput_mbps': 89,
        'retries': 5,
        'jitter_ms': 4.2,
        'uptime_hours': 973,
        'active_connections': 211
    }

# Misleading auxiliary function (dead code path - never used)
def compute_health_legacy(data):
    score = 0
    for k, v in data.items():
        if 'loss' in k:
            score -= v * 100
        elif 'throughput' in k:
            score += v / 10
    return max(score, 10)

# Unused but plausible-looking transformation
def normalize_metrics(metrics):
    normalized = {}
    scales = {
        'latency_ms': 0.01,
        'packet_loss': 100,
        'throughput_mbps': 0.1,
        'jitter_ms': 0.1
    }
    for k, v in metrics.items():
        if k in scales:
            normalized[k + '_norm'] = round(v * scales[k], 3)
        else:
            normalized[k] = v
    return normalized  # Never actually used

# Core evaluation logic with relevant computation
def evaluate_performance(metrics, weights):
    base_score = 100.0
    
    # Component adjustments
    if metrics['latency_ms'] < 150:
        base_score += 12
    else:
        base_score -= 8
        
    if metrics['packet_loss'] < 0.05:
        base_score += 10 * (1 - metrics['packet_loss'] * 20)  # scaled bonus
    else:
        base_score -= 15
        
    if metrics['throughput_mbps'] > 80:
        base_score += 8
    
    # Penalty for excessive retries
    base_score -= min(metrics['retries'], 10) * 2
    
    # Jitter consideration
    if metrics['jitter_ms'] < 5.0:
        base_score += 5
    else:
        base_score -= 10
    
    # Uptime bonus (non-linear)
    uptime_bonus = min(metrics['uptime_hours'] // 100, 10) * 1.5
    base_score += uptime_bonus
    
    # Active connections scaling (saturating)
    conn_bonus = min(metrics['active_connections'] / 25, 8)
    base_score += conn_bonus
    
    # Weighted adjustment using distractor structure
    total_weight = sum(weights.values())
    weighted_adjustment = 0
    
    # This loop looks important but only some keys matter
    for key, weight in weights.items():
        if key == 'latency_ms':
            weighted_adjustment += weight * (150 - metrics['latency_ms']) * 0.1
        elif key == 'packet_loss':
            weighted_adjustment += weight * (0.05 - metrics['packet_loss']) * 50
    
    base_score += weighted_adjustment
    
    return round(base_score, 4)

# Secondary decoy function that processes similar data
def analyze_stability_trace(trace_data):
    counter = defaultdict(int)
    for event in trace_data:
        counter[event['type']] += 1
    
    # Complex but unused calculation
    sequences = list(itertools.combinations(sorted(counter.keys()), 2))
    risk_score = 0
    for a, b in sequences:
        if a == 'ERROR' and b == 'TIMEOUT':
            risk_score += counter[a] * counter[b] * 1.5
    return risk_score

# Distractor variables
system_log = [
    {'timestamp': '2023-01-01T00:01:00', 'type': 'INFO', 'payload': 12},
    {'timestamp': '2023-01-01T00:02:00', 'type': 'ERROR', 'payload': 3},
    {'timestamp': '2023-01-01T00:03:00', 'type': 'WARNING', 'payload': 7}
]

# Real execution flow starts here
raw_data = get_raw_metrics()

# Irrelevant transformation (not used in final path)
dummy_normalized = normalize_metrics(raw_data)

# Weight configuration — only latency and packet_loss are actually used
weights_config = {
    'latency_ms': 1.8,
    'packet_loss': 2.2,
    'throughput_mbps': 1.0,  # Unused in logic
    'jitter_ms': 1.5         # Unused in logic
}

# Simulate trace analysis (distractor call)
trace_risk = analyze_stability_trace(system_log)

# Key statement: this is where the answer is determined
final_score = evaluate_performance(raw_data, weights_config)

# Additional red herring: post-processing that doesn't affect result
temp_adj = final_score * 0.98
if temp_adj > 95:
    temp_adj -= 5

# Output the target result
Result: {final_score}