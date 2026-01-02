import itertools

def analyze_trend(data):
    """Irrelevant function: analyzes trend but not used in final computation"""
    positive_count = sum(1 for x in data if x > 0)
    negative_count = sum(1 for x in data if x < 0)
    return 'increasing' if positive_count > negative_count else 'decreasing'

def preprocess_inputs(raw_values):
    """Distractor function: performs normalization but result is discarded"""
    min_val = min(raw_values)
    max_val = max(raw_values)
    normalized = [(x - min_val) / (max_val - min_val) for x in raw_values]
    thresholded = [1 if x > 0.5 else 0 for x in normalized]
    return thresholded

def compute_entropy(values):
    """Dead-end calculation: entropy computed but never used"""
    from math import log2
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    total = len(values)
    entropy = -sum((count / total) * log2(count / total) for count in freq_map.values())
    return round(entropy, 4)

def filter_outliers(seq, factor=1.5):
    """Red herring: used to create filtered_data, which is defined but unused"""
    sorted_seq = sorted(seq)
    q1, q3 = sorted_seq[len(sorted_seq)//4], sorted_seq[3*len(sorted_seq)//4]
    iqr = q3 - q1
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    filtered = [x for x in seq if lower_bound <= x <= upper_bound]
    return filtered

def evaluate_performance(metrics, weights):
    """Core function: computes weighted harmonic mean of non-zero metrics"""
    # Remove zero-valued metrics and corresponding weights
    paired = [(m, w) for m, w in zip(metrics, weights) if m != 0]
    if not paired:
        return 0.0
    
    # Compute weighted harmonic mean
    weighted_inv_sum = sum(w / m for m, w in paired)
    total_weight = sum(w for _, w in paired)
    
    intermediate_result = total_weight / weighted_inv_sum
    
    # Apply adjustment based on metric consistency
    deviations = [abs(m - sum(metrics)/len(metrics)) for m in metrics if m != 0]
    avg_deviation = sum(deviations) / len(deviations) if deviations else 0
    consistency_bonus = 1 + max(0, 0.1 - avg_deviation)  # Bonus decreases with deviation
    
    adjusted_score = intermediate_result * consistency_bonus
    
    # Additional logic: if more than half metrics above median, add flat boost
    median_metric = sorted(m for m in metrics if m != 0)[len([m for m in metrics if m != 0])//2]
    above_median = sum(1 for m in metrics if m > median_metric)
    if above_median > len(metrics) // 2:
        adjusted_score += 5.0
    
    return adjusted_score

# Main execution block
if __name__ == '__main__':
    # Input data
    raw_sensor_data = [120, 150, 90, 180, 210, 60, 140]
    config_weights = [0.2, 0.3, 0.1, 0.25, 0.15, 0.05, 0.1]

    # Irrelevant preprocessing chain
    binary_flags = preprocess_inputs(raw_sensor_data)
    entropy_value = compute_entropy(binary_flags)
    trend_direction = analyze_trend(raw_sensor_data)
    filtered_data = filter_outliers(raw_sensor_data, factor=2.0)  # Defined but unused

    # Generate combinations as distraction (itertools usage)
    combo_list = list(itertools.combinations(raw_sensor_data, 3))
    large_combos = [c for c in combo_list if sum(c) > 400]
    combo_count = len(large_combos)

    # Simulate historical baseline comparison (unused)
    historical_avg = sum(raw_sensor_data) / len(raw_sensor_data)
    deviation_from_history = [x - historical_avg for x in raw_sensor_data]
    significant_devs = [abs(d) > 50 for d in deviation_from_history].count(True)

    # Core metric transformation
    transformed_metrics = [max(10, min(x, 200)) for x in raw_sensor_data]  # Clipping to range

    # Introduce a decoy assignment that looks important
    performance_snapshot = {
        'timestamp': 1234567890,
        'raw_mean': historical_avg,
        'adjusted_metrics': transformed_metrics.copy(),
        'weight_distribution': config_weights[:],
        'entropy': entropy_value
    }

    # Key computation path
    final_score = evaluate_performance(transformed_metrics, config_weights)

    # Print result as required
    print(f"Result: {final_score}")