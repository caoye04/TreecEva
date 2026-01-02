from collections import defaultdict

# Simulate system performance metrics over time
def collect_metrics():
    data = [120, 85, 90, 110, 95]
    timestamps = [1, 2, 3, 4, 5]
    
    # Misleading intermediate processing
    temp_buffer = []
    for x in data:
        temp_buffer.append(x * 0.95 + 5)  # Distractor transformation
    
    metrics = defaultdict(float)
    metrics['avg_response'] = sum(data) / len(data)
    metrics['peak_load'] = max(data)
    metrics['stability'] = sum(abs(data[i] - data[i-1]) for i in range(1, len(data)))
    metrics['consistency'] = len([x for x in data if x > 90])
    
    # Irrelevant health checks
    system_health = {'cpu': 0.78, 'memory': 0.65, 'disk': 0.3}
    for k, v in system_health.items():
        if v > 0.8:
            print(f'Warning: High {k} usage')  # Dead code path (never triggers)

    return metrics

# Weighting logic with red herring parameters
def apply_weights(m, w):
    weighted_sum = 0.0
    total_weight = 0.0
    
    # Real weighting
    for key in w:
        if key in m:
            weighted_sum += m[key] * w[key]
            total_weight += w[key]
    
    # Fake normalization branch (not used)
    debug_mode = False
    if debug_mode:
        baseline = 100
        weighted_sum = (weighted_sum / total_weight) / baseline
    
    return weighted_sum / total_weight if total_weight > 0 else 0

# Secondary metric adjustment (partially relevant)
def adjust_for_reliability(raw, count):
    adjustment_factor = 1.0
    if count < 3:
        adjustment_factor = 0.8
    elif count > 5:
        adjustment_factor = 1.15
    return raw * adjustment_factor

# Main evaluation function
def evaluate_performance(metrics, weights):
    base = apply_weights(metrics, weights)
    
    # Introduce side computation that looks important but isn't used directly
    synthetic_index = (metrics['peak_load'] ** 0.5) * (metrics['consistency'] / 10)
    outlier_check = metrics['stability'] > 40
    
    # Actual use of secondary logic
    adjusted = adjust_for_reliability(base, metrics['consistency'])
    
    # Final nonlinear calibration
    if base > 100:
        final = adjusted * 0.92
    else:
        final = adjusted * 1.03
    
    # Unused diagnostic trace
    diagnostics = {
        'input_base': base,
        'adjusted': adjusted,
        'synthetic_index': synthetic_index,
        'outlier_flag': outlier_check
    }
    
    return int(round(final))  # Discretize result

# Execution flow
if __name__ == '__main__':
    # Collect observed behavior
    collected = collect_metrics()
    
    # Define importance weights (some keys don't exist in metrics - intentional)
    weights = {
        'avg_response': 0.4,
        'peak_load': 0.1,
        'stability': 0.3,
        'consistency': 0.2,
        'downtime': 0.05  # Irrelevant - not in metrics
    }
    
    # Compute final score
    final_score = evaluate_performance(collected, weights)
    
    # Print result as required
    print(f"Result: {final_score}")