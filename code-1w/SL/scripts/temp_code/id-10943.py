from collections import defaultdict, Counter

# Simulate system performance metrics over time
def collect_metrics():
    raw_data = [
        {'cpu': 75, 'mem': 80, 'latency_ms': 45, 'req_per_sec': 230},
        {'cpu': 60, 'mem': 60, 'latency_ms': 30, 'req_per_sec': 300},
        {'cpu': 90, 'mem': 95, 'latency_ms': 120, 'req_per_sec': 150},
        {'cpu': 45, 'mem': 50, 'latency_ms': 25, 'req_per_sec': 400}
    ]

    # Irrelevant transformation: normalize names (distraction)
    renamed = [{k.replace('_ms', '').upper(): v for k, v in item.items()} for item in raw_data]

    aggregated = defaultdict(float)
    counts = defaultdict(int)
    
    # Real aggregation logic
    for entry in raw_data:
        for k, v in entry.items():
            aggregated[k] += v
            counts[k] += 1
    
    avg_metrics = {k: aggregated[k] / counts[k] for k in aggregated}
    
    # Dead code path: never used (distractor)
    def analyze_trend(data):
        return sum(d['req_per_sec'] for d in data) / len(data)

    # Misleading intermediate calculation (red herring)
    peak_load = max(d['req_per_sec'] for d in raw_data)
    efficiency_ratio = (avg_metrics['req_per_sec'] / peak_load) * 100

    return avg_metrics

# Weighting system for evaluation
def apply_weights(metrics):
    # Base weights
    weights = {'cpu': 0.2, 'mem': 0.2, 'latency_ms': 0.4, 'req_per_sec': 0.35}
    
    # Adjust weights based on policy (real logic)
    if metrics['latency_ms'] > 50:
        weights['latency_ms'] += 0.2
        weights['req_per_sec'] -= 0.1
    else:
        weights['cpu'] -= 0.05

    # Normalize weights to sum to 1.0 (important correction)
    total = sum(weights.values())
    normalized = {k: v / total for k, v in weights.items()}
    
    # Use of zip and enumerate: real but subtle use
    adjustments = [0.1, -0.05, 0.15, -0.1]
    keys = list(normalized.keys())
    for i, (k, w) in enumerate(zip(keys, normalized.values())):
        if i % 2 == 0 and metrics[keys[i]] > 70:
            normalized[k] = w + adjustments[i] if i < len(adjustments) else w

    return normalized

# Final scoring logic
def evaluate_performance(metrics, weights):
    score = 0.0
    
    # Scoring each dimension
    for k in metrics:
        val = metrics[k]
        w = weights[k]
        
        if k == 'latency_ms':
            # Inverse scoring: lower latency = higher score
            contribution = (100 - min(val, 100)) * w
        elif k == 'req_per_sec':
            # Throughput bonus up to cap
            contribution = min(val / 4, 100) * w
        else:
            # CPU and MEM: lower usage is better, but not penalized beyond threshold
            base = 100 - val
            penalty = 20 if val > 85 else 0
            contribution = (base - penalty) * w
        
        score += contribution
    
    # Apply non-linear scaling (critical step)
    if score > 60:
        score = score * 0.9 + 10
    else:
        score = score * 0.8
    
    # Redundant transformation (distractor)
    final_map = {i: round(score - i*0.5) for i in range(5)}
    fallback_score = sum(final_map.values()) / 5
    
    # Never updated or used (decoy)
    debug_trace = []
    for _ in range(3):
        debug_trace.append('checkpoint')
    
    return score

# Orchestration function with unused branching (misdirection)
def main_flow(mode='production'):
    metrics = collect_metrics()
    
    # Unused conditional path (dead code branch)
    if mode == 'debug':
        print("Debug mode active")
        return None
    
    weights = apply_weights(metrics)
    final_score = evaluate_performance(metrics, weights)
    
    # Additional distraction: character frequency count from metric names (irrelevant)
    all_keys = ''.join(metrics.keys())
    freq = Counter(all_keys)
    rare_chars = [ch for ch, cnt in freq.items() if cnt == 1]
    
    # Case conversion chain (no effect on result)
    temp_labels = [k.title().swapcase() for k in metrics.keys()]
    temp_labels = [lbl.replace('Ms', 'Milliseconds') for lbl in temp_labels]
    
    return final_score

# Execute
result = main_flow('production')
Target result: {result}