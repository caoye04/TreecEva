from collections import defaultdict
from itertools import combinations

# Simulated system performance metrics (some are decoys)
def collect_metrics():
    data = defaultdict(float)
    data['latency_ms'] = 120.5
    data['throughput_ops'] = 850
    data['error_rate'] = 0.013
    data['cpu_util'] = 78.2
    data['memory_mb'] = 450
    data['cache_hit_ratio'] = 0.88
    data['network_latency'] = 45.1  # red herring
    data['disk_io'] = 1200  # irrelevant
    data['retry_count'] = 3.0
    return data

# Legacy function - unused but looks important
def calculate_legacy_score(vals):
    score = 0
    for v in vals:
        if v > 50:
            score += v * 0.3
        else:
            score += v * 0.1
    return score

# Weight assignment with misleading logic
def assign_weights(metrics):
    weights = {}
    priority_keys = ['latency_ms', 'throughput_ops', 'error_rate', 'retry_count']
    for k in metrics:
        if k in priority_keys:
            if 'ops' in k:
                weights[k] = 0.35
            elif 'latency' in k:
                weights[k] = -0.25  # inverse impact
            elif 'error' in k:
                weights[k] = -0.40
            elif 'retry' in k:
                weights[k] = -0.30
        else:
            weights[k] = 0.05  # minor weight for others (distractor)
    return weights

# Complex normalization with redundant branches
def normalize_value(key, value):
    if key == 'latency_ms':
        return max(0, 100 - (value / 2))  # higher normalized is better
    elif key == 'throughput_ops':
        return min(100, value / 10)  # cap at 100
    elif key == 'error_rate':
        return max(0, 100 - (value * 1000))  # scaled penalty
    elif key == 'retry_count':
        return max(0, 100 - (value * 10))
    elif 'util' in key:
        return min(100, value)  # direct
    elif 'ratio' in key:
        return value * 100
    else:
        return 50  # neutral default for unknowns (misleading)

# Core evaluation logic - only this matters
# But buried among distractions
def evaluate_performance(metrics, weights):
    total_score = 0.0
    base_components = 0.0
    
    # Real computation happens here, but many keys seem relevant
    for key, raw_value in metrics.items():
        norm_val = normalize_value(key, raw_value)
        weight = weights.get(key, 0.0)
        contribution = norm_val * abs(weight)  # weighted contribution
        total_score += contribution
        
        # Dead branch - looks like it does something
        if 'unused_trigger' in globals() and weight < 0:
            base_components += 1
    
    # Adjustment based on actual critical factors
    penalty_factor = 1.0
    if metrics['error_rate'] > 0.01:
        penalty_factor -= 0.1
    if metrics['latency_ms'] > 100:
        penalty_factor -= 0.05
    if metrics['retry_count'] >= 3:
        penalty_factor -= 0.08
    
    adjusted_score = total_score * penalty_factor
    
    # Red herring transformation
    final_transformations = []
    for i in range(3):
        final_transformations.append(int(adjusted_score) >> i)
    dummy_agg = sum(final_transformations) % 100
    
    # Final scaling
    final_score = round(adjusted_score + dummy_agg * 0.1, 4)
    
    # Irrelevant sorting of decoy data
    decoy_list = [dummy_agg, int(metrics['disk_io']), int(metrics['network_latency'])]
    decoy_list.sort(reverse=True)
    alternate_rank = list(combinations(decoy_list, 2))  # unused
    
    return final_score

# Unused recursive function to mislead about complexity requirements
def recursive_diagnostic(level, acc):
    if level <= 0:
        return acc
    return recursive_diagnostic(level - 1, acc + [level * 2])

# Main execution flow
if __name__ == '__main__':
    # Collect real and fake metrics
    raw_metrics = collect_metrics()
    
    # Compute weights (many assigned but only some used)
    benchmark_weights = assign_weights(raw_metrics)
    
    # Evaluate system performance - THIS IS THE KEY STATEMENT
    final_score = evaluate_performance(raw_metrics, benchmark_weights)
    
    # Print result as required
    print(f"Result: {final_score}")