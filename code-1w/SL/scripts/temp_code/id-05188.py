from collections import defaultdict, Counter

# Simulate sensor data readings over time with some noise
def generate_sensor_data():
    return [105, 110, 98, 102, 108, 115, 97, 103, 109, 112, 95, 101]

# Analyze frequency of readings for anomaly detection
def analyze_readings(data):
    freq = Counter(data)
    anomalies = []
    for val, count in freq.items():
        if count == 1 and val < 100:
            anomalies.append(val)
    return anomalies

# Track cumulative trends and suppress minor fluctuations
def smooth_trend(data, threshold=3):
    smoothed = []
    running_sum = 0
    for val in data:
        deviation = abs(val - 105)  # baseline reference
        if deviation > threshold:
            running_sum += val // 10  # coarse adjustment
        else:
            running_sum -= 1
    return running_sum  # returns aggregated trend score

# Misleading function: appears useful but not used in final calculation
def calculate_variance(data):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return variance

# Core evaluation logic with distractors
def evaluate_performance(raw_data):
    total_points = 0
    penalty_count = 0
    temp_buffer = []
    reading_log = defaultdict(int)
    
    for reading in raw_data:
        reading_log[reading] += 1
        if reading > 110:
            total_points += 2
        elif reading > 100:
            total_points += 1
        else:
            penalty_count += 1
        
        # Distractor computation - modifies buffer but unused later
        if reading % 5 == 0:
            temp_buffer.append(reading * 0.1)
    
    # Nested condition with intermediate irrelevant transformation
    adjusted_penalty = 0
    for i in range(penalty_count):
        if i % 2 == 0:
            adjusted_penalty += 3
        else:
            adjusted_penalty += 2
    
    # Secondary distractor: complex but unused structure
    summary_stats = {
        'high': len([r for r in raw_data if r > 110]),
        'medium': len([r for r in raw_data if 100 <= r <= 110]),
        'low': len([r for r in raw_data if r < 100])
    }
    
    # Key computational chain
    trend_score = smooth_trend(raw_data)
    anomaly_list = analyze_readings(raw_data)
    base_score = total_points * 5 - adjusted_penalty
    bonus = len(anomaly_list) * 4
    final_score = base_score + bonus + trend_score
    
    # Red herring: calculating something important-looking but unused
    stability_index = sum(1 for i in raw_data if 100 <= i <= 110) / len(raw_data)
    
    return final_score

# Main execution
sensor_readings = generate_sensor_data()
eval_result = evaluate_performance(sensor_readings)
final_score = eval_result
print(f"Result: {final_score}")