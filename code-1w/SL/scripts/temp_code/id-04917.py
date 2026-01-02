from collections import defaultdict, Counter

# Simulate sensor data with noise and redundancy
def preprocess_sensor_data(raw_data):
    filtered_data = [x for x in raw_data if x > -50 and x < 150]
    offset = sum(filtered_data) / len(filtered_data) if filtered_data else 0
    normalized = [x - offset for x in filtered_data]
    return normalized

# Analyze trends in processed data
def detect_trends(processed_data):
    trend_counter = defaultdict(int)
    for i in range(1, len(processed_data)):
        if processed_data[i] > processed_data[i-1]:
            trend_counter['up'] += 1
        elif processed_data[i] < processed_data[i-1]:
            trend_counter['down'] += 1
    return dict(trend_counter)

# Core scoring logic based on distribution and weight factors
def calculate_distribution_score(data):
    count = Counter(data)
    unique_values = len(count)
    mode_value = count.most_common(1)[0][1] if count else 0
    return (unique_values * 0.7) + (mode_value * 1.3)

# Secondary metric - not actually used in final score but looks important
def calculate_variance_metric(data):
    mean_val = sum(data) / len(data) if data else 0
    squared_diffs = [(x - mean_val) ** 2 for x in data]
    variance = sum(squared_diffs) / len(data) if data else 0
    return variance * 0.5

# Final composition of multiple metrics
def calculate_final_score(data, weights):
    # Step 1: Distribution-based score
    dist_score = calculate_distribution_score(data)
    
    # Step 2: Trend analysis score (converted to numeric heuristic)
    trends = detect_trends(data)
    trend_score = trends.get('up', 0) - trends.get('down', 0)
    
    # Step 3: Apply weights (only some are actually used)
    effective_weight = weights.get('base', 1.0)
    unused_weight = weights.get('variance_boost', 0.85)  # Distractor
    
    # Step 4: Compute auxiliary metrics that seem relevant
    aux_info = {
        'peak': max(data) if data else 0,
        'range': (max(data) - min(data)) if data else 0
    }
    
    # Step 5: Actual computation chain
    intermediate = dist_score * effective_weight
    adjustment = trend_score * 0.3
    final_score = intermediate + adjustment
    
    # Red herring computation (not used)
    theoretical_max = aux_info['range'] * unused_weight
    if theoretical_max > 100:
        final_score -= 5  # Rarely triggered, not in this case
    
    return int(final_score)

# Main execution block
if __name__ == '__main__':
    # Raw sensor readings (with outliers and noise)
    raw_readings = [23, 45, 45, 67, 89, 89, 89, 34, 23, 12, 12, 12, 90, 101, 102, 101, 90, 67, 55]
    
    # Preprocess the data
    cleaned = preprocess_sensor_data(raw_readings)
    
    # Extract key features
    feature_stats = {
        'length_after_filter': len(cleaned),
        'mean_post_filter': sum(cleaned) / len(cleaned) if cleaned else 0
    }
    
    # Weight configuration (some keys are ignored)
    config_weights = {
        'base': 1.2,
        'variance_boost': 0.85,
        'trend_multiplier': 0.3  # Used implicitly in calculate_final_score
    }
    
    # Execute main calculation
    final_score = calculate_final_score(cleaned, config_weights)
    
    # Print result as required
    print(f"Result: {final_score}")