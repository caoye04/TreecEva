from collections import defaultdict

# Simulate sensor data processing with noise filtering and threshold evaluation
def collect_sensor_data():
    raw_readings = [105, 110, 98, 120, 150, 89, 95, 130, 142, 138]
    timestamps = list(range(10))
    sensor_data = [(t, v) for t, v in zip(timestamps, raw_readings)]
    return sensor_data

def filter_outliers(data, factor=1.5):
    values = [v for _, v in data]
    q1 = sorted(values)[len(values)//4]
    q3 = sorted(values)[3*len(values)//4]
    iqr = q3 - q1
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    filtered = [item for item in data if lower_bound <= item[1] <= upper_bound]
    # Dead code - not used later
    outlier_count = len(data) - len(filtered)
    return filtered

def calculate_trend_score(filtered_data):
    if len(filtered_data) < 2:
        return 0
    diffs = [filtered_data[i+1][1] - filtered_data[i][1] for i in range(len(filtered_data)-1)]
    trend_sum = sum(1 for d in diffs if d > 0) - sum(1 for d in diffs if d < 0)
    return trend_sum

def count_critical_events(raw_data, limit):
    # Irrelevant function - not used in final computation
    counter = 0
    for _, value in raw_data:
        if value > limit:
            counter += 1
    return counter

def evaluate_performance(data, thresholds):
    # Step 1: Filter noisy data
    clean_data = filter_outliers(data)
    
    # Step 2: Compute base metrics
    base_values = [v for _, v in clean_data]
    avg_value = sum(base_values) / len(base_values)
    
    # Step 3: Apply multiple threshold checks using defaultdict
    category_counts = defaultdict(int)
    for _, v in clean_data:
        if v < thresholds['low']:
            category_counts['low'] += 1
        elif v < thresholds['medium']:
            category_counts['medium'] += 1
        else:
            category_counts['high'] += 1
    
    # Step 4: Calculate stability metric (unused distractor)
    stability = sum(1 for i in range(1, len(base_values)) if abs(base_values[i] - base_values[i-1]) < 10)
    
    # Step 5: Compute trend influence (actually used)
    trend_influence = calculate_trend_score(clean_data)
    
    # Step 6: Weighted scoring
    score = 0
    score += category_counts['high'] * 3
    score += category_counts['medium'] * 1
    score += trend_influence * 2
    
    # Irrelevant transformation
    temp_shift = [v * 0.95 for v in base_values]
    adjusted_avg = sum(temp_shift) / len(temp_shift) if temp_shift else 0
    
    # Final score calculation
    final_score = int(score + avg_value // 10)
    
    return final_score

# Main execution block
sensor_input = collect_sensor_data()
dummy_thresholds = {'low': 100, 'medium': 130, 'high': float('inf')}
final_score = evaluate_performance(sensor_input, dummy_thresholds)
print(f"Result: {final_score}")