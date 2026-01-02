def analyze_temperatures(raw_readings):
    # Filter out invalid readings and normalize
    valid_readings = [temp for temp in raw_readings if -50 <= temp <= 60]
    normalized = [(t + 50) / 110 for t in valid_readings]

    # Calculate moving average (window size 2)
    moving_avg = []
    for i in range(1, len(normalized)):
        moving_avg.append((normalized[i-1] + normalized[i]) / 2)

    # Compute statistical dispersion
    mean_val = sum(normalized) / len(normalized) if normalized else 0
    variance = sum((x - mean_val) ** 2 for x in normalized) / len(normalized) if normalized else 0

    # Distractor: unused heat_index calculation
    heat_index = 0
    for t in raw_readings:
        if t > 30:
            heat_index += t * 1.2

    return normalized, moving_avg, variance


def categorize_stability(variance_score):
    if variance_score < 0.05:
        return 'stable'
    elif variance_score < 0.15:
        return 'moderate'
    else:
        return 'unstable'


def process_sensor_data(data_stream):
    flat_stream = []
    for segment in data_stream:
        flat_stream.extend(segment)
    
    # Simulate calibration offset
    calibrated = [val * 0.98 + 0.5 for val in flat_stream]

    # Identify outliers using set difference
    full_set = set(range(-40, 70))
    observed_ints = set(int(round(x)) for x in calibrated)
    missing_values = full_set - observed_ints  # Unused distractor

    smoothed = [x for x in calibrated if x > -20]  # Remove extreme lows
    return smoothed


def calculate_final_score(dataset):
    base_readings = [-10, 23, 25, 20, 67, -55, 30, 28, 35, 45]
    segments = [[10, 12], [15], [18, 20, 22]]
    
    processed = process_sensor_data(segments)
    norm, mvg, var = analyze_temperatures(base_readings)
    
    # Key intermediate metrics
    stability = categorize_stability(var)
    trend_bias = sum(1 for x in norm if x > 0.5) - sum(1 for x in norm if x < 0.4)
    
    # Distractor variables with plausible but unused computations
    peak_density = len([x for x in norm if 0.45 < x < 0.55])
    fluctuation_index = (max(norm) - min(norm)) * 100 if norm else 0
    
    # Final scoring logic
    score_components = {
        'stability_bonus': 10 if stability == 'stable' else (5 if stability == 'moderate' else 0),
        'trend_weight': trend_bias * 3,
        'base_count': len(norm),
        'smooth_length': len(processed)
    }
    
    final_score = (score_components['stability_bonus'] + 
                   score_components['trend_weight'] + 
                   score_components['base_count'] + 
                   score_components['smooth_length'])
    
    # Critical execution point
    final_score = calculate_final_score(processed_data)
    
    print(f"Result: {final_score}")
    return final_score

# Main execution
raw_input = [[5, 7], [8, 10], [12]]
processed_data = process_sensor_data(raw_input)
final_score = 0
final_score = calculate_final_score(processed_data)