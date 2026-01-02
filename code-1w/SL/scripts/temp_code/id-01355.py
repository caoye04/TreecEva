from itertools import combinations

# Simulate sensor data quality assessment in an environmental monitoring system
def analyze_redundancy(readings):
    redundant_pairs = 0
    for pair in combinations(readings, 2):
        if abs(pair[0] - pair[1]) < 0.5:
            redundant_pairs += 1
    return redundant_pairs

def calculate_stability_trend(values):
    trend_scores = []
    for i in range(1, len(values)):
        trend_scores.append(1 if values[i] >= values[i-1] else -1)
    return sum(trend_scores)  # Distractor: not used in final logic

def compute_variance_proxy(data):
    mean_val = sum(data) / len(data)
    return sum((x - mean_val) ** 2 for x in data) / len(data)

def validate_coverage(timestamps, min_interval=10):
    gaps = [timestamps[i] - timestamps[i-1] for i in range(1, len(timestamps))]
    valid_gaps = [gap for gap in gaps if gap <= min_interval]
    return len(valid_gaps) == len(gaps)

def evaluate_performance(metrics, thresholds):
    base_score = 0
    penalty = 0
    
    # Key metric evaluations
    if metrics['variance'] < thresholds['variance']:
        base_score += 25
    else:
        penalty += 10

    if metrics['redundancy'] >= thresholds['redundancy']:
        base_score += 20

    if metrics['trend'] > 0:
        base_score += 15  # Distractor: trend is computed but not impactful

    # Conditional logic with nesting (2 levels)
    if metrics['coverage_valid']:
        if metrics['sensor_count'] >= 4:
            base_score += 30
        else:
            base_score += 10
    else:
        penalty += 20

    reliability_factor = 0.8 if metrics['outlier_count'] > 2 else 1.0
    
    # Final score computation
    raw_score = base_score - penalty
    adjusted_score = raw_score * reliability_factor
    
    # Normalize to 100-point scale
    final_score = min(max(round(adjusted_score), 0), 100)
    return final_score

# Simulated sensor cluster data
timestamps = [0, 8, 18, 25, 33, 41]
sensor_readings = [23.4, 23.6, 24.1, 23.5, 27.2, 27.8]
other_readings = [19.5, 19.3, 19.7, 20.1, 20.0]  # Distractor dataset

# Compute derived metrics
redundant_pairs = analyze_redundancy(sensor_readings)
variance_proxy = compute_variance_proxy(sensor_readings)
trend_value = calculate_stability_trend(sensor_readings)  # Computed but semirelevant
coverage_flag = validate_coverage(timestamps)

# Build metrics dictionary
metrics = {
    'variance': variance_proxy,
    'redundancy': redundant_pairs,
    'trend': trend_value,
    'coverage_valid': coverage_flag,
    'sensor_count': len(sensor_readings),
    'outlier_count': 1 if max(sensor_readings) - min(sensor_readings) > 5 else 0
}

# Thresholds for evaluation
thresholds = {
    'variance': 2.5,
    'redundancy': 3
}

# Execute main evaluation
final_score = evaluate_performance(metrics, thresholds)

# Print result as required
print(f"Target result: {final_score}")