from collections import defaultdict, Counter
import itertools

# Simulate system performance metrics from multiple sensors
def collect_diagnostics():
    return {
        'cpu_load': [0.78, 0.82, 0.75, 0.91, 0.67],
        'mem_usage': [0.64, 0.71, 0.78, 0.81, 0.85],
        'disk_io': [120, 135, 110, 145, 150],
        'net_latency_ms': [23, 45, 31, 29, 56]
    }

def analyze_trends(data):
    trends = {}
    for key, values in data.items():
        avg = sum(values) / len(values)
        peak = max(values)
        volatility = sum(abs(values[i+1] - values[i]) for i in range(len(values)-1))
        trends[key] = {'avg': avg, 'peak': peak, 'volatility': volatility}
    return trends

def calculate_health_index(trend_data):
    # Irrelevant helper (distractor)
    def smooth(x):
        return (x * 0.9) + 0.1

    health = 100.0
    if trend_data['cpu_load']['avg'] > 0.8:
        health -= 15
    if trend_data['mem_usage']['peak'] > 0.8:
        health -= 10
    if trend_data['disk_io']['volatility'] > 50:
        health -= 8
    
    # Dead code path - never executed due to logic above
    if False and trend_data['net_latency_ms']['avg'] > 40:
        health -= 12
        
    # Decoy transformation
    temp_scores = []
    for val in [health, health+5, health-3]:
        temp_scores.append(val * 1.05)
    
    return health  # Final health index before weighting

# Unused function - red herring
def predict_failure_risk(health_index):
    return "LOW" if health_index > 60 else "HIGH"

# Complex weighting with distractors
def apply_weights(raw_metrics, custom_weights=None):
    base_weights = defaultdict(float)
    base_weights.update({'cpu_load': 0.4, 'mem_usage': 0.3, 'disk_io': 0.2, 'network': 0.1})
    
    # Misleading weight adjustment
    adjustment_factor = 1.0
    for i in range(2):  # Useless loop
        adjustment_factor *= 0.99
    
    # Apply actual weights only on relevant components
    adjusted = {}
    for k, v in raw_metrics.items():
        key = k.replace('_usage', '').replace('_load', '').replace('_io', '')
        if key in base_weights:
            adjusted[k] = v['avg'] * base_weights[key]
    
    return dict(adjusted)

# Core evaluation logic
def evaluate_performance(metrics, weights):
    # Extract base scores
    scores = {}
    for k, v in metrics.items():
        scores[k] = v['avg'] * 100 if 'avg' in v else 0
    
    # Dummy aggregation using itertools
    all_pairs = list(itertools.combinations(scores.keys(), 2))
    pair_impact = 0
    for a, b in all_pairs:
        pair_impact += abs(scores[a] - scores[b]) * 0.01  # Minor noise
    
    # Main calculation chain
    raw_total = sum(scores.values())
    normalized = raw_total / len(scores)
    volatility_penalty = sum(v.get('volatility', 0) for v in metrics.values()) * 0.05
    
    # Critical distraction: irrelevant counter usage
    log_counter = Counter()
    for key in metrics.keys():
        log_counter['processed'] += 1
        log_counter['total_keys'] += len(key)
    
    # Final score computation
    preliminary = normalized - volatility_penalty
    
    # Additional decoy logic
    shadow_score = 0
    for val in [preliminary * x for x in [0.95, 1.0, 1.05]]:
        if val > 50:
            shadow_score += val * 0.1
    
    final_score = int(preliminary) + 5  # Key assignment point
    
    # Unused conditional expression (red herring)
    status = 'PASS' if final_score > 60 else 'FAIL'
    debug_info = f'Score={final_score}' if False else None
    
    return final_score

# Execution flow
if __name__ == '__main__':
    # Collect raw diagnostics
    raw_data = collect_diagnostics()
    
    # Analyze temporal trends
    trends = analyze_trends(raw_data)
    
    # Compute base health (unused in final path)
    health_index = calculate_health_index(trends)
    
    # Prepare weights (partially unused)
    weights = {'cpu': 0.4, 'memory': 0.3}  # Mismatched keys - distractor
    applied_weights = apply_weights(trends, weights)
    
    # Evaluate final performance score
    final_score = evaluate_performance(trends, applied_weights)
    
    print(f"Result: {final_score}")