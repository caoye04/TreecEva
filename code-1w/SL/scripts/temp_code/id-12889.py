import math

# Simulate sensor data with noise and valid readings
def generate_sensor_data():
    raw_readings = [12.5, 13.0, 11.8, 14.2, 9.7, 10.1, 13.3, 12.9]
    timestamps = list(range(len(raw_readings)))
    status_flags = [True, False, True, True, False, True, True, False]
    return list(zip(timestamps, raw_readings, status_flags))

# Filter out faulty sensor readings
def filter_valid_readings(sensor_data):
    valid_readings = []
    temp_accumulator = []
    for entry in sensor_data:
        timestamp, value, is_valid = entry
        if is_valid:
            valid_readings.append(value)
            temp_accumulator.append(value * 1.05)  # Adjusted for calibration (unused)
    return valid_readings

# Apply moving average smoothing
def smooth_data(readings):
    if len(readings) < 3:
        return readings
    smoothed = []
    for i in range(1, len(readings) - 1):
        avg = (readings[i-1] + readings[i] + readings[i+1]) / 3
        smoothed.append(round(avg, 2))
    return smoothed

# Calculate entropy of distribution (distractor function - not used in final score)
def calculate_entropy(values):
    from collections import Counter
    counts = Counter([round(v, 0) for v in values])
    total = len(values)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

# Determine outlier indices based on IQR (semi-relevant but unused)
def detect_outliers_iqr(values):
    sorted_vals = sorted(values)
    q1 = sorted_vals[len(sorted_vals)//4]
    q3 = sorted_vals[3*len(sorted_vals)//4]
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = [v for v in values if v < lower_bound or v > upper_bound]
    return outliers

# Main processing pipeline
def process_sensor_stream():
    raw_data = generate_sensor_data()
    
    # Extract valid entries
    filtered_readings = filter_valid_readings(raw_data)
    
    # Smooth the data sequence
    smoothed_readings = smooth_data(filtered_readings)
    
    # Distractor: calculate auxiliary metrics
    mean_val = sum(smoothed_readings) / len(smoothed_readings) if smoothed_readings else 0
    variance = sum((x - mean_val) ** 2 for x in smoothed_readings) / len(smoothed_readings) if smoothed_readings else 0
    std_dev = math.sqrt(variance)
    
    # Unused statistical flags
    high_variability = std_dev > 0.5
    data_range = max(smoothed_readings) - min(smoothed_readings) if smoothed_readings else 0
    
    # Generate normalized features using list comprehension
    normalized_features = [round((x - mean_val) / std_dev, 2) for x in smoothed_readings] if std_dev > 0 else [0]*len(smoothed_readings)
    
    # Feature engineering: detect rising trends (consecutive increases)
    trend_changes = []
    for i in range(1, len(smoothed_readings)):
        if smoothed_readings[i] > smoothed_readings[i-1]:
            trend_changes.append(1)
        elif smoothed_readings[i] < smoothed_readings[i-1]:
            trend_changes.append(-1)
        else:
            trend_changes.append(0)
    
    # Compute trend run lengths
    current_run = 0
    longest_positive_run = 0
    for direction in trend_changes:
        if direction == 1:
            current_run += 1
            longest_positive_run = max(longest_positive_run, current_run)
        else:
            current_run = 0
    
    # Secondary distractor: set operations to find unique pattern transitions
    transition_pairs = [(trend_changes[i], trend_changes[i+1]) for i in range(len(trend_changes)-1)]
    unique_transitions = set(transition_pairs)
    stability_index = len([t for t in trend_changes if t == 0])
    
    # Final score calculation based on feature quality and trend strength
    base_score = sum(normalized_features)
    adjustment_factor = longest_positive_run * 0.75
    penalty = len(outlier_removal_trace(filtered_readings)) * 0.2  # Use trace from helper
    
    final_score = base_score + adjustment_factor - penalty
    
    # Print intermediate debug info (irrelevant to result)
    debug_checksum = sum([hash(str(x)) % 1000 for x in raw_data]) % 100
    
    return {
        'processed_data': smoothed_readings,
        'diagnostics': {
            'mean': mean_val,
            'std': std_dev,
            'longest_run': longest_positive_run,
            'debug_key': debug_checksum
        },
        'final_score': final_score
    }

# Helper function that leaves a trace of removed outliers (used in penalty)
def outlier_removal_trace(raw_readings):
    sorted_vals = sorted(raw_readings)
    threshold = sum(sorted_vals) / len(sorted_vals) * 1.3
    removed = [x for x in raw_readings if x > threshold]
    return removed

# Final aggregation function
def calculate_final_score(processed_data_dict):
    return round(processed_data_dict['final_score'], 3)

# Execute workflow
if __name__ == "__main__":
    result_bundle = process_sensor_stream()
    final_score = calculate_final_score(result_bundle)
    print(f"Target result: {final_score}")