from collections import Counter, defaultdict

# Simulate sensor data with noise and valid readings
def generate_sensor_data():
    raw_data = [104, 102, 98, 95, 108, 104, 97, 110, 103, 95, 99, 101, 107, 105]
    offset = 5
    adjusted = [x - offset for x in raw_data]
    return adjusted

def analyze_trends(readings):
    trends = []
    for i in range(1, len(readings)):
        if readings[i] > readings[i-1]:
            trends.append('up')
        elif readings[i] < readings[i-1]:
            trends.append('down')
        else:
            trends.append('stable')
    trend_counts = Counter(trends)
    return trend_counts['up'] - trend_counts['down']  # net upward trend

def filter_outliers(values, threshold=100):
    upper = threshold + 8
    lower = threshold - 8
    filtered = [v for v in values if lower <= v <= upper]
    # Distractor: irrelevant transformation
    scaled = [x * 1.05 for x in filtered]
    return filtered  # scaled is unused red herring

def compute_variance(data):
    mean = sum(data) / len(data)
    squared_diffs = [(x - mean) ** 2 for x in data]
    variance = sum(squared_diffs) / len(squared_diffs)
    return variance

def calculate_final_score(dataset, limits):
    # Multiple assignment and slicing
    recent = dataset[-6:]  # last 6 readings
    historical = dataset[:6]  # first 6 readings
    
    # Distractor variables
    temp_analysis = defaultdict(int)
    for val in dataset:
        category = 'high' if val > limits['warning'] else 'normal'
        temp_analysis[category] += 1
    
    # Real computation path
    clean_data = filter_outliers(recent, threshold=limits['threshold'])
    base_score = analyze_trends(clean_data)
    
    # Conditional expression
    penalty = 5 if len(clean_data) < 4 else 0
    
    # Variance from historical baseline
    historical_var = compute_variance(historical)
    adjustment = 10 if historical_var > 20 else 3
    
    # Final calculation
    final_score = base_score * adjustment - penalty
    
    # Dead code path (never executed but looks relevant)
    if False:
        fallback = sum([x for x in dataset if x % 2 == 0])
        final_score = max(final_score, fallback)
    
    return final_score

# Main execution
sensor_readings = generate_sensor_data()
tuning_params = {
    'threshold': 100,
    'warning': 103
}
intermediate_result = compute_variance(sensor_readings)  # distractor usage
final_score = calculate_final_score(sensor_readings, tuning_params)
print(f"Result: {final_score}")