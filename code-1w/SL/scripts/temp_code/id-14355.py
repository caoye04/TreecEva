import itertools

def analyze_component(data, threshold=0.5):
    """Irrelevant analysis function (dead path)"""
    count = 0
    for x in data:
        if x > threshold:
            count += 1
    return count

def compute_entropy(values):
    """Misleading entropy computation (not used in final result)"""
    import math
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        p = v / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 6)

def extract_peaks(signal):
    """Unused signal processing function"""
    peaks = []
    for i in range(1, len(signal)-1):
        if signal[i-1] < signal[i] > signal[i+1]:
            peaks.append(signal[i])
    return peaks

def validate_bounds(x, low, high):
    """Helper to clamp values"""
    return max(low, min(high, x))

def transform_metric(m, method='linear'):
    """Apply transformation (only linear is actually used)"""
    if method == 'square':
        return m ** 2
    elif method == 'sqrt':
        return m ** 0.5
    else:
        return m  # default: linear

def evaluate_stage(scores, mode='sum'):
    """Nested evaluation with red herring modes"""
    base = 0
    multiplier = 1
    temp_result = 0
    
    for s in scores:
        if s < 0.2:
            continue  # skip low performers
        elif s > 0.8:
            multiplier = 2  # performance boost
        base += s
    
    temp_result = base * multiplier
    
    # Dead branch: never taken due to input constraints
    if mode == 'product':
        temp_result = 1
        for s in scores:
            temp_result *= s
    
    return temp_result

def evaluate_performance(metrics, weights):
    """Main evaluation logic with distractors"""
    # Irrelevant intermediate computations
    avg_metric = sum(metrics) / len(metrics)
    metric_variance = sum((x - avg_metric) ** 2 for x in metrics) / len(metrics)
    adjusted_metrics = [validate_bounds(m, 0.0, 1.0) for m in metrics]
    
    # Transform each metric (only linear used)
    transformed = [transform_metric(m, 'linear') for m in adjusted_metrics]
    
    # Weighted combination
    weighted_sum = sum(m * w for m, w in zip(transformed, weights))
    weight_total = sum(weights)
    
    normalized_score = weighted_sum / weight_total if weight_total > 0 else 0
    
    # Apply stage evaluation (with misleading multipliers)
    staged = evaluate_stage([normalized_score], mode='sum')
    
    # Additional noise variables
    peak_count = len([x for x in metrics if x > 0.75])
    penalty_factor = 0.95 if peak_count > 3 else 1.0
    
    # Final score unaffected by penalty (red herring)
    final_raw = staged  # penalty not applied
    
    # Complex rounding via itertools cycle (overkill but realistic)
    decimals = [0, 1, 2, 3, 4, 5, 6]
    cycle = itertools.cycle(decimals)
    precision_target = next(itertools.islice(cycle, 7 * len(metrics) % 7, None))
    
    final_score = round(final_raw * 1000, 0)  # Scale and round to integer
    
    # Unused data structures
    history_log = []
    for i, m in enumerate(metrics):
        history_log.append({'index': i, 'value': m})
    
    return int(final_score)

# Main execution block
if __name__ == '__main__':
    # Input data
    metrics = [0.88, 0.76, 0.91, 0.67, 0.83, 0.74, 0.95, 0.81]
    weights = [1.0, 1.2, 1.5, 0.8, 1.0, 0.9, 1.8, 1.1]
    
    # Distraction variables
    baseline_avg = sum(metrics) / len(metrics)
    ideal_count = sum(1 for m in metrics if m >= 0.9)
    entropy = compute_entropy(weights)
    
    # Key statement
    final_score = evaluate_performance(metrics, weights)
    
    # Output result
    print(f"Result: {final_score}")