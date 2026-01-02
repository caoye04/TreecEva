from collections import defaultdict, Counter

# Simulate sensor data with noise and valid readings
def preprocess_sensor_data(raw_readings):
    filtered_data = []
    noise_count = 0
    spike_threshold = 95
    
    for reading in raw_readings:
        if reading < 0 or reading > 100:
            noise_count += 1
            continue
        if reading > spike_threshold:
            corrected = spike_threshold
        else:
            corrected = reading
        filtered_data.append(corrected)
    
    # Irrelevant statistics (distractor)
    avg_noise = noise_count / len(raw_readings) if raw_readings else 0
    redundant_calc = sum(filtered_data) * 0.01
    
    return filtered_data

def analyze_trends(data):
    trend_summary = defaultdict(int)
    up_count = 0
    down_count = 0
    
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend_summary['increasing'] += 1
            up_count += 1
        elif data[i] < data[i-1]:
            trend_summary['decreasing'] += 1
            down_count -= 1  # deliberate negative accumulation (semi-relevant)
    
    # Dead computation: this value is never used
    phantom_metric = up_count ** 2 + down_count ** 2
    
    return dict(trend_summary)

def calculate_final_score(processed_data):
    count_stats = Counter(processed_data)
    mode_value = count_stats.most_common(1)[0][1] if count_stats else 0
    total = sum(processed_data)
    length = len(processed_data) if processed_data else 1
    
    # Multiple semi-relevant calculations
    base_score = total / length
    bonus = 10 if any(x >= 90 for x in processed_data) else 0
    penalty = 5 if len([x for x in processed_data if x < 10]) > 2 else 0
    
    # Conditional expression usage
    adjustment = 7 if base_score > 50 else (-3 if mode_value > 3 else 0)
    
    # Red herring variables
    temp_factor = mode_value * 1.5
    dummy_weight = temp_factor / (base_score + 1e-5)
    
    final_score = base_score + bonus - penalty + adjustment
    return final_score

# Main execution
raw_sensor_data = [85, 92, 88, 105, -3, 87, 87, 96, 45, 12, 8, 7, 5, 91, 87, 87, 87]

processed_data = preprocess_sensor_data(raw_sensor_data)
trends = analyze_trends(processed_data)
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")