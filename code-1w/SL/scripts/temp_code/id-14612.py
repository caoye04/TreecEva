from collections import defaultdict

# Simulate environmental sensor readings over days
def simulate_readings(days):
    data = defaultdict(float)
    for i in range(days):
        data[f'day_{i}'] = (i * 1.5 + 7) % 100
    return data

# Analyze trend stability with irrelevant smoothing
def smooth_data(raw_data, factor=0.3):
    smoothed = {}
    prev = 0
    for k, v in raw_data.items():
        smoothed[k] = prev * factor + v * (1 - factor)
        prev = smoothed[k]
    return smoothed  # Not actually used in final logic

# Determine quality category based on threshold bands
def categorize_conditions(readings, limits):
    categories = []
    temp_score = 0
    for val in readings.values():
        if val > limits['high']:
            categories.append('critical')
            temp_score -= 1
        elif val > limits['moderate']:
            categories.append('elevated')
            temp_score += 2
        else:
            categories.append('normal')
            temp_score += 3
    # Distraction: temp_score computed but not directly used
    return categories

# Core calculation: assess harvest yield from pattern density
def calculate_harvest_quality(env_data, criteria):
    count_normal = 0
    total_days = len(env_data)
    
    # Extract values in order
    values = [env_data[key] for key in sorted(env_data.keys())]
    
    # Compute moving average (distraction - not used)
    window = 3
    moving_averages = []
    for i in range(len(values) - window + 1):
        moving_averages.append(sum(values[i:i+window]) / window)
    
    # Actual logic: count how many days fall below moderate threshold
    normal_threshold = criteria['moderate']
    for val in values:
        if val <= normal_threshold:
            count_normal += 1
    
    # Bonus if consistent early performance (first third)
    early_period = values[:len(values)//3]
    if all(v <= normal_threshold for v in early_period):
        count_normal += 2
    
    # Hidden penalty: if any single day exceeds 90
    if any(v > 90 for v in values):
        count_normal -= 1
    
    # Final yield formula: base + bonus - penalty, scaled
    base_yield = 85
    adjustment = (count_normal - 5) * 3
    final_yield = base_yield + adjustment
    
    return int(final_yield)

# Irrelevant helper: format report string
def generate_summary(data_list):
    summary = ""
    for idx, item in enumerate(data_list):
        summary += f"[Item {idx}] Value={item:.1f}; "
    return summary  # Dead code path

# Main execution flow
if __name__ == "__main__":
    # Simulate 8 days of environmental conditions
    sensor_data = simulate_readings(8)
    
    # Apply smoothing (computation with no downstream use)
    filtered_readings = smooth_data(sensor_data)
    
    # Define agricultural thresholds
    thresholds = {
        'high': 75,
        'moderate': 50
    }
    
    # Categorize each day (produces side info, not used in math)
    status_labels = categorize_conditions(sensor_data, thresholds)
    
    # Generate unused textual summary
    report_text = generate_summary(list(sensor_data.values()))
    
    # Critical statement: compute final harvest yield
    final_yield = calculate_harvest_quality(sensor_data, thresholds)
    
    # Output result
    print(f"Result: {final_yield}")