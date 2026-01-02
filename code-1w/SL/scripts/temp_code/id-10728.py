def calculate_final_score(raw_data, limits):
    # Initialize tracking variables
    temp_sum = 0
    outlier_count = 0
    normalized_values = []
    
    # Preprocess: filter and normalize data
    for i, value in enumerate(raw_data):
        if value < limits['min']:
            adjusted = limits['min']
            outlier_count += 1
        elif value > limits['max']:
            adjusted = limits['max']
            outlier_count += 1
        else:
            adjusted = value
        
        temp_sum += adjusted
        normalized_values.append(adjusted)
    
    # Compute baseline statistics (some are red herrings)
    avg_normalized = temp_sum / len(normalized_values) if normalized_values else 0
    squared_deviations = [(x - avg_normalized) ** 2 for x in normalized_values]
    variance_estimate = sum(squared_deviations) / len(squared_deviations) if squared_deviations else 0
    std_deviation = variance_estimate ** 0.5
    
    # Secondary processing: apply weighting using index position
    weighted_sum = 0
    for idx, val in enumerate(normalized_values):
        weight = 1 + (idx * 0.1)  # Emphasis on later elements
        weighted_sum += val * weight
    
    # Distractor: unused transformation chain
    shifted_data = [x * 0.95 for x in raw_data]
    capped_data = [min(x, 100) for x in shifted_data]
    ignored_total = sum(capped_data)
    
    # Key slicing operation: use only last 4 normalized values
    recent_segment = normalized_values[-4:]
    recent_avg = sum(recent_segment) / len(recent_segment) if recent_segment else 0
    
    # Combine metrics with threshold penalties
    penalty_factor = 1 - (outlier_count * 0.05)  # Max 20% penalty
    if penalty_factor < 0.8:
        penalty_factor = 0.8
    
    stability_score = 1 / (std_deviation + 1)  # Higher if stable
    
    # Final score computation
    base_component = avg_normalized * 0.6
    trend_component = recent_avg * 0.4
    dynamic_adjustment = stability_score * 10
    
    final_score = (base_component + trend_component + dynamic_adjustment) * penalty_factor
    
    return final_score

# Main execution context
sensor_readings = [85, 92, 95, 103, 45, 88, 90, 150, 97]
config_thresholds = {'min': 50, 'max': 120}

# Irrelevant helper function (dead code path)
def analyze_pattern(seq):
    runs = 0
    for a, b in zip(seq, seq[1:]):
        if b > a:
            runs += 1
    return runs

# Unused intermediate transformations
doubled_readings = [x * 2 for x in sensor_readings]
halved_readings = [x // 2 for x in doubled_readings]
sorted_pairs = list(zip(sensor_readings, halved_readings))

# Actual critical computation
final_score = calculate_final_score(sensor_readings, config_thresholds)

Result: {final_score}