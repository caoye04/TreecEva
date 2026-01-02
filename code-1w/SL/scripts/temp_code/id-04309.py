from collections import defaultdict, Counter
import math

# Simulate system performance metrics over time
def collect_metrics():
    raw_data = [
        (1, {'cpu': 70, 'memory': 60, 'latency': 20, 'requests': 100}),
        (2, {'cpu': 85, 'memory': 75, 'latency': 35, 'requests': 120}),
        (3, {'cpu': 90, 'memory': 80, 'latency': 50, 'requests': 90}),
        (4, {'cpu': 60, 'memory': 50, 'latency': 15, 'requests': 110})
    ]
    
    # Irrelevant aggregation - red herring
    request_counter = Counter()
    for _, data in raw_data:
        category = 'high' if data['requests'] > 100 else 'low'
        request_counter[category] += 1
    
    # Actual useful transformation
    metrics = {}
    for timestamp, values in raw_data:
        metrics[timestamp] = {
            'efficiency': (values['cpu'] + values['memory']) / 2,
            'responsiveness': 100 - values['latency'],
            'load': values['requests']
        }
    
    # Dead code path - never used
    def deprecated_normalization(x):
        return x / (1 + abs(x))
    
    return metrics

# Weighting system with decoy components
def load_weights():
    # Complex structure with unused fields
    config = defaultdict(lambda: 0)
    config['efficiency'] = 0.4
    config['responsiveness'] = 0.35
    config['load'] = 0.25
    config['deprecated_metric'] = -0.1  # Unused
    config['dummy_flag'] = True         # Misleading
    config['version'] = 'legacy'        # Irrelevant
    
    # Lambda for dynamic adjustment (only one used)
    adjust = lambda w, f: w * 1.1 if f else w * 0.9
    adjusted = {}
    for k, v in config.items():
        if isinstance(v, float) and k != 'deprecated_metric':
            factor = k in ['efficiency', 'responsiveness']
            adjusted[k] = adjust(v, factor)  # Only efficiency and responsiveness get boosted
        else:
            adjusted[k] = v
    
    # Return only relevant weights
    return {k: adjusted[k] for k in ['efficiency', 'responsiveness', 'load']}

# Recursive scoring with distractors
def recursive_boost(value, depth):
    if depth <= 0 or value < 10:
        return value
    return 1.05 * recursive_boost(value - 5, depth - 1)  # Diminishing returns

def calculate_risk_penalty(responsiveness):
    # Unused risk model
    baseline = 100
    diff = baseline - responsiveness
    if diff > 40:
        return 0.8
    elif diff > 20:
        return 0.9
    else:
        return 1.0  # No penalty

# Core evaluation logic
def evaluate_performance(metrics, weights):
    scores = []
    
    # Enumerate with zip to align timestamps and indices (overkill but realistic)
    for i, (ts, m) in enumerate(zip(range(1, len(metrics)+1), [metrics[t] for t in sorted(metrics)])):
        base = 0
        norm_factor = sum(weights.values())
        
        # Weighted sum
        base += m['efficiency'] * weights['efficiency']
        base += m['responsiveness'] * weights['responsiveness']
        base += m['load'] * weights['load'] * 0.1  # Scale down load contribution
        
        # Conditional boost based on trend (misleading history check)
        if i > 0 and m['responsiveness'] > 80:
            base *= 1.02
        
        # Apply recursive boost only if high efficiency
        if m['efficiency'] > 75:
            base = recursive_boost(base, 2)
        
        scores.append(base)
    
    # Final aggregation with irrelevant operations
    avg = sum(scores) / len(scores)
    peak = max(scores)
    stability = avg / peak  # Closer to 1 is more stable
    
    # Decoy calculation
    volatility = math.sqrt(sum((s - avg)**2 for s in scores) / len(scores)) if len(scores) > 1 else 0
    
    # The real final score
    final_score = int(round(avg * stability))
    
    # Unused normalization chain
    def deep_normalize(x):
        for _ in range(3):
            x = x / (1 + math.exp(-x * 0.01))
        return x
    
    return final_score

# Irrelevant utility function (dead code)
def generate_report(data):
    return "Performance Report:\n" + "\n".join([f"- {k}: {v}" for k, v in data.items()])

# Main execution flow
if __name__ == "__main__":
    # Collect metrics
    metrics = collect_metrics()
    
    # Load weighting scheme
    weights = load_weights()
    
    # Compute final performance score
    final_score = evaluate_performance(metrics, weights)
    
    # Print result as required
    print(f"Target result: {final_score}")