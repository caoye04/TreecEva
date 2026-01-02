from collections import defaultdict

# Simulate sensor data processing with noise filtering and threshold evaluation
def evaluate_performance(sensor_data, config):
    raw_readings = [x for x in sensor_data if x > 0]
    filtered_readings = [x for x in raw_readings if x < 1000]
    
    # Misleading intermediate computation (not used in final score)
    outlier_count = 0
    temp_buffer = []
    for val in sensor_data:
        if val > 1000:
            outlier_count += 1
            temp_buffer.append(val)
    
    # Actual processing begins: categorize readings
    category_counts = defaultdict(int)
    cumulative_sum = 0
    for reading in filtered_readings:
        if reading >= config['high']:
            category_counts['high'] += 1
            cumulative_sum += reading * 0.8
        elif reading >= config['medium']:
            category_counts['medium'] += 1
            cumulative_sum += reading * 0.5
        else:
            category_counts['low'] += 1
            cumulative_sum += reading * 0.2

    # Red herring: unused statistical calculation
    average_raw = sum(sensor_data) / len(sensor_data) if sensor_data else 0
    variance_proxy = sum((x - average_raw) ** 2 for x in sensor_data) / len(sensor_data) if sensor_data else 0

    # Weighted scoring logic
    base_score = cumulative_sum * 0.9
    bonus = 0
    if category_counts['high'] > 3:
        bonus += 50
    elif category_counts['medium'] > 5:
        bonus += 30
    
    # Final adjustments
    adjustment_factor = 1.0
    if len(filtered_readings) > 8:
        adjustment_factor = 1.1
    
    final_score = int((base_score + bonus) * adjustment_factor)
    
    # Dead code path - never reached due to prior filtering
    invalid_flag = False
    for v in sensor_data:
        if v == -999:
            invalid_flag = True
            break
    
    return final_score

# Input data and configuration
sensor_input = [150, -5, 200, 1001, 350, 400, 750, 800, 950, 60, 45, 30, 1200]
thresholds = {
    'low': 100,
    'medium': 300,
    'high': 600
}

# Execute main logic
data = [x for x in sensor_input]
final_score = evaluate_performance(data, thresholds)
print(f"Result: {final_score}")