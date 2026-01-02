from collections import defaultdict, Counter
import math

# Simulate system performance metrics over time
def collect_metrics():
    raw_data = [
        {'cpu': 75, 'mem': 80, 'io': 30, 'net': 45},
        {'cpu': 85, 'mem': 60, 'io': 25, 'net': 55},
        {'cpu': 90, 'mem': 90, 'io': 40, 'net': 40},
        {'cpu': 65, 'mem': 70, 'io': 35, 'net': 50}
    ]
    
    # Irrelevant transformation - distractor
    processed = defaultdict(list)
    for entry in raw_data:
        for k, v in entry.items():
            processed[k].append(v * 0.9 + 5)  # Fake normalization
    
    # Another red herring: frequency analysis of rounded values
    freq_counter = Counter()
    for vals in processed.values():
        for v in vals:
            freq_counter[round(v)] += 1
    
    # Actual metric extraction (obscured)
    latest = raw_data[-1]
    avg_metrics = {k: sum(entry[k] for entry in raw_data) / len(raw_data) for k in raw_data[0]}
    peak_metrics = {k: max(entry[k] for entry in raw_data) for k in raw_data[0]}
    
    # Distractor: unused complex structure
    class MetricShadow:
        def __init__(self, name):
            self.name = name
            self.history = []
        def update(self, x):
            self.history.append(x % 100)
    
    shadow_io = MetricShadow('io')
    for i in range(5):
        shadow_io.update(1000 + i * 7)  # Dead computation path
    
    return {
        'base': latest,
        'trend': {k: avg_metrics[k] - raw_data[0][k] for k in avg_metrics},
        'peak': peak_metrics,
        'shadow': shadow_io.history  # Unused field
    }

# Weighting engine with decoy logic
def compute_weights(config=None):
    base_weights = {'cpu': 0.4, 'mem': 0.3, 'io': 0.2, 'net': 0.1}
    
    # Fake adaptive weighting - never used
    if config and 'adaptive' in config:
        temp = {}
        for k, v in base_weights.items():
            temp[k] = v * (1 + math.sin(0.1))
        return temp
    
    # Decoy weight set
    decoy_weights = {k: v * 1.5 for k, v in base_weights.items()}
    decoy_weights['gpu'] = 0.25  # Introduces irrelevant key
    
    # Actual adjustment
    adjusted = {}
    for k in base_weights:
        factor = 1.0
        if k == 'cpu':
            factor *= 0.9
        elif k == 'mem':
            factor *= 1.1
        adjusted[k] = base_weights[k] * factor
    
    # Normalize to ensure sum=1 (real operation)
    total = sum(adjusted.values())
    normalized = {k: v / total for k, v in adjusted.items()}
    
    # Return decoy under certain condition? No — this is a red herring
    return normalized  # Critical: actual weights used later

# Main evaluation with early returns and distractions
def evaluate_performance(metrics, weights):
    base = metrics['base']
    trend = metrics['trend']
    peak = metrics['peak']
    
    # Composite score components
    components = {}
    
    # Core scoring logic
    for k in weights:
        raw_val = base.get(k, 0)
        trend_impact = abs(trend[k])  # Use absolute trend deviation
        peak_ratio = raw_val / peak[k] if peak[k] > 0 else 0
        
        # Scoring formula
        if k == 'cpu':
            score = raw_val * 0.8 + 20 * peak_ratio
        elif k == 'mem':
            score = raw_val * 0.7 + 30 * (1 - trend_impact / 10)
        elif k == 'io':
            score = 50 + 10 * math.log(raw_val + 1) - trend_impact
        elif k == 'net':
            score = 40 + raw_val * 0.5
        else:
            score = 0  # Irrelevant
        
        components[k] = max(0, min(100, score))  # Clamp to [0,100]
    
    # Distractor: complex tuple unpacking with no effect
    summary_stats = [
        (k, components[k], trend[k], base[k]) for k in components
    ]
    for item in summary_stats:
        category, score_val, delta, current = item
        if score_val > 90:
            # Fake optimization path
            optimized = (score_val * 0.95) + 5
            break
    
    # Real aggregation
    weighted_sum = 0.0
    for k in weights:
        weighted_sum += components[k] * weights[k]
    
    # Final nonlinear adjustment (key step)
    if weighted_sum < 60:
        final = weighted_sum * 1.2
    else:
        final = 50 + math.sqrt(weighted_sum - 50) * 10
    
    # Dead code block - misleading intermediate
    debug_info = {}
    for k in components:
        debug_info[k] = f"{components[k]:.1f}%%"
    debug_info['total'] = f"{weighted_sum:.2f}"
    
    # THIS IS THE TARGET VARIABLE
    final_score = int(round(final))
    
    # Additional distraction: bit manipulation on score (unused)
    binary_rep = bin(final_score)[2:]
    parity = bin(final_score).count('1') % 2
    masked = final_score & 0xFF | 0x100  # Bitwise decoy
    
    return final_score

# Orchestration function with conditional execution
def main():
    # Collect metrics
    metrics = collect_metrics()
    
    # Compute weights
    weights = compute_weights({'adaptive': False})  # adaptive=False so fake path not taken
    
    # Evaluate performance
    final_score = evaluate_performance(metrics, weights)
    
    # Print result as required
    print(f"Result: {final_score}")
    
    # Debug prints that are commented out (dead hints)
    # print(f"Components: {components}")
    # print(f"Weights used: {weights}")
    
    return final_score

if __name__ == "__main__":
    main()