import itertools

def analyze_trend(data, threshold=0.5):
    """Determine trend direction based on moving average crossover."""
    short_avg = sum(data[-3:]) / 3
    long_avg = sum(data[-6:]) / 6
    return 1 if short_avg > long_avg + threshold else -1

def compute_risk_adjusted_return(returns, volatility, risk_free_rate=0.02):
    """Compute Sharpe ratio as a measure of risk-adjusted performance."""
    avg_return = sum(returns) / len(returns)
    excess_return = avg_return - risk_free_rate
    sharpe_ratio = excess_return / (volatility + 1e-8)
    return sharpe_ratio

def filter_outliers(values, factor=1.5):
    """Remove outliers using IQR method."""
    sorted_vals = sorted(values)
    q1, q3 = sorted_vals[len(sorted_vals)//4], sorted_vals[3*len(sorted_vals)//4]
    iqr = q3 - q1
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    return [v for v in values if lower_bound <= v <= upper_bound]

def evaluate_performance(metrics, weights):
    # Normalize metrics to [0,1] range for fair weighting
    normalized = {}
    for k, v in metrics.items():
        if k == 'response_time':
            normalized[k] = max(0, min(1, (1 - v / 100)))  # Lower is better
        elif k == 'accuracy':
            normalized[k] = max(0, min(1, v))
        elif k == 'throughput':
            normalized[k] = max(0, min(1, v / 200))
    
    weighted_sum = 0.0
    total_weight = 0.0
    for metric_name, weight in weights.items():
        if metric_name in normalized:
            weighted_sum += normalized[metric_name] * weight
            total_weight += weight
    
    # Dummy tracking variables (distractors)
    adjustment_factor = 1.0
    if total_weight < 0.5:
        adjustment_factor = 2.0  # Never reached due to fixed weights
    
    final_value = weighted_sum / (total_weight + 1e-9)
    
    # Additional red herring: unused transformation chain
    temp_data = [final_value * 2, final_value ** 2, abs(final_value - 0.5)]
    processed = list(itertools.accumulate(temp_data, lambda x, y: x + y * 0.1))
    smoothed = processed[::-1][0]  # Not used
    
    # Irrelevant dictionary operations
    metadata_log = {}
    metadata_log['version'] = '2.1'
    metadata_log['timestamp'] = '2023-11-05'
    metadata_log['nodes'] = ['A', 'B', 'C']
    node_slice = metadata_log['nodes'][1:3]  # Unused
    
    # Actual result
    return int(round(final_value * 100))

# Simulated system metrics (real inputs)
metrics = {
    'accuracy': 0.92,
    'response_time': 45,
    'throughput': 180
}

weights = {
    'accuracy': 0.5,
    'response_time': 0.3,
    'throughput': 0.2
}

# Historical data for trend analysis (distractor)
historical_load = [120, 135, 130, 140, 145, 150, 160, 155, 165, 170]
trend_direction = analyze_trend(historical_load)

# Return series for financial metric (semi-relevant distractor)
return_series = [0.03, 0.02, -0.01, 0.04, 0.02]
volatility = 0.015
risk_adjusted_perf = compute_risk_adjusted_return(return_series, volatility)

# Outlier filtering on dummy data (irrelevant block)
sensor_readings = [23.1, 22.9, 23.0, 23.2, 24.5, 23.1, 22.8, 26.0, 23.0]
cleaned_readings = filter_outliers(sensor_readings)

# Core evaluation call
final_score = evaluate_performance(metrics, weights)

# Output result as required
print(f"Result: {final_score}")