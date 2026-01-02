def analyze_trends(raw_values):
    # Irrelevant trend analysis (dead code path)
    moving_avg = [sum(raw_values[i:i+3]) / 3 for i in range(len(raw_values) - 2)]
    volatility = sum((moving_avg[i+1] - moving_avg[i]) ** 2 for i in range(len(moving_avg) - 1))
    return volatility  # Unused return

def preprocess_inputs(data_list):
    # Distractor: complex preprocessing that isn't used in final calculation
    normalized = [(x - min(data_list)) / (max(data_list) - min(data_list)) for x in data_list]
    encoded = [int(n * 100) for n in normalized]
    return encoded

def transform_metrics(x, y, z):
    # Real computation buried in irrelevant operations
    temp_a = (x ^ y) & 0xFF  # Bit manipulation red herring
    temp_b = (z >> 2) + (z << 1)  # Shift distraction
    result = (x * 3) + (y * 2) + z  # Actual relevant logic
    checksum = sum(int(d) for d in str(result)) * 2  # Misleading side effect
    return result  # Only this matters

def filter_outliers(values):
    mean_val = sum(values) / len(values)
    std_dev = (sum((v - mean_val) ** 2 for v in values) / len(values)) ** 0.5
    return [v for v in values if abs(v - mean_val) <= 2 * std_dev]  # Unused filtering

def evaluate_performance(metrics):
    # Core logic hidden among distractions
    base = metrics['alpha']
    bonus = metrics['gamma'] if metrics['beta'] > 50 else 0
    
    # Conditional expression (required Python feature)
    adjustment = 1.5 if 'delta' in metrics and metrics['delta'] < 0 else 0.8
    
    # Real calculation
    raw_score = transform_metrics(base, metrics['beta'], bonus)
    
    # Slicing operation (required Python feature)
    history_window = list(metrics.values())[1:4]
    historical_boost = sum(history_window) // 4
    
    # Dictionary mutation distraction
    metrics['temp_debug'] = raw_score * 0.1
    metrics['last_updated'] = 'irrelevant_timestamp'
    
    # Final computation
    final_score = int((raw_score * adjustment) + historical_boost)
    
    # Dead code path
    if final_score < 0:
        final_score = abs(final_score)
        audit_log = {'recovered': True, 'source': 'negative_correction'}
        return None  # Never reached
    
    return final_score

# Main execution flow
if __name__ == '__main__':
    # Input data setup
    sensor_readings = [127, 201, 98, 155, 240, 73]
    processed_data = preprocess_inputs(sensor_readings)  # Unused
    trends = analyze_trends(sensor_readings)  # Unused
    
    # Actual input dictionary
    metric_data = {
        'alpha': 42,
        'beta': 68,
        'gamma': 25,
        'delta': 12,
        'epsilon': 88
    }
    
    # Filtered version not used directly
    filtered_metrics = filter_outliers(list(metric_data.values()))
    
    # Key assignment
    final_score = evaluate_performance(metric_data)
    
    # Output result
    print(f"Result: {final_score}")