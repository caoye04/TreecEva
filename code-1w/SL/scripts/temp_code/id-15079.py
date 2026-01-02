from collections import defaultdict, Counter

# Simulate sensor data with noise and redundant readings
def generate_noisy_data():
    raw_readings = [23.1, 24.5, 24.5, 25.0, 26.3, 24.5, 27.8, 23.1, 25.0, 28.2]
    timestamps = list(range(10))
    status_flags = ['OK', 'OK', 'ERROR', 'OK', 'OK', 'OK', 'WARNING', 'OK', 'OK', 'OK']
    
    data = []
    for i in range(len(raw_readings)):
        entry = {
            'time': timestamps[i],
            'value': raw_readings[i],
            'flag': status_flags[i]
        }
        data.append(entry)
    return data

def analyze_trends(readings):
    # Extract values and compute moving differences (distractor logic)
    values = [r['value'] for r in readings]
    diffs = [values[i+1] - values[i] for i in range(len(values)-1)]
    avg_diff = sum(diffs) / len(diffs) if diffs else 0
    
    # Count flag occurrences (semi-relevant)
    flag_count = Counter([r['flag'] for r in readings])
    error_count = flag_count.get('ERROR', 0)
    warning_count = flag_count.get('WARNING', 0)
    
    # Distractor: Compute trend-based prediction (not used later)
    predicted_next = readings[-1]['value'] + avg_diff if readings else 0
    
    # Return only relevant stats
    return {'error_count': error_count, 'warning_count': warning_count}

def filter_valid_entries(readings):
    # Remove entries marked as ERROR (actual preprocessing)
    valid_entries = [r for r in readings if r['flag'] != 'ERROR']
    filtered_values = [v['value'] for v in valid_entries]
    
    # Extra slicing and processing (some irrelevant)
    mid_window = filtered_values[1:-1] if len(filtered_values) > 2 else filtered_values
    smoothed = [round((mid_window[i-1] + mid_window[i] + mid_window[i+1]) / 3, 2)
                for i in range(1, len(mid_window)-1)] if len(mid_window) > 2 else mid_window
    
    # Return both original and processed (only original slice is used later)
    return filtered_values

def calculate_stability_metric(values):
    if not values:
        return 0.0
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    return round((1 / (1 + variance)) * 100, 2)  # Stability percentage

def detect_outliers(values, threshold=2.0):
    if len(values) < 2:
        return []
    mean_val = sum(values) / len(values)
    std_dev = (sum((x - mean_val) ** 2 for x in values) / len(values)) ** 0.5
    outliers = [v for v in values if abs(v - mean_val) > threshold * std_dev]
    return outliers  # Not used, distractor

def calculate_final_score(data, thresholds):
    # Step 1: Analyze error/warning counts
    trend_stats = analyze_trends(data)
    errors = trend_stats['error_count']
    warnings = trend_stats['warning_count']
    
    # Step 2: Get clean data
    clean_values = filter_valid_entries(data)
    
    # Step 3: Calculate core metrics
    stability = calculate_stability_metric(clean_values)
    base_score = sum(clean_values)
    
    # Step 4: Apply penalty logic
    penalty = 0
    if errors > 0:
        penalty += thresholds['error_penalty'] * errors
    if warnings > 0:
        penalty += thresholds['warning_penalty'] * warnings
    
    # Step 5: Outlier detection (distractor - result unused)
    _ = detect_outliers(clean_values)
    
    # Step 6: Aggregate final score
    final_score = base_score + stability - penalty
    
    # Irrelevant transformations (distractors)
    final_score_normalized = final_score / (1 + abs(final_score) * 0.01)
    final_score_clipped = max(10, min(90, final_score))
    
    return int(round(final_score))  # Actual output used

# Main execution
if __name__ == '__main__':
    # Setup configuration
    config_thresholds = {
        'error_penalty': 15,
        'warning_penalty': 5
    }
    
    # Generate input
    sensor_data = generate_noisy_data()
    
    # Key computation
    final_score = calculate_final_score(sensor_data, config_thresholds)
    
    # Output result
    print(f"Result: {final_score}")