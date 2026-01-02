from collections import defaultdict

# Simulate sensor data aggregation and performance scoring
def collect_sensor_readings():
    raw_data = [120, 150, 130, 180, 90, 200, 170]
    offset = 25
    adjusted = [x - offset for x in raw_data]
    return adjusted

def normalize_readings(data):
    min_val, max_val = min(data), max(data)
    if max_val == min_val:
        return [0.5] * len(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

def calculate_trend(scores):
    trend = 0
    for i in range(1, len(scores)):
        trend += scores[i] - scores[i-1]
    return trend  # Irrelevant for final score, just distraction

def evaluate_performance(weights, values):
    weighted_sum = sum(w * v for w, v in zip(weights, values))
    penalty = 0.1 * len([v for v in values if v < 0.2])  # Penalize low readings
    adjustment_factor = lambda x: 0.95 if x > 0 else 1.0
    trend = calculate_trend(values)
    adjusted = weighted_sum * adjustment_factor(trend)
    return int(round(adjusted * 100))

def main():
    # Step 1: Collect and preprocess sensor data
    sensor_readings = collect_sensor_readings()  # [95, 125, 105, 155, 65, 175, 145]
    
    # Step 2: Normalize data for scoring
    normalized_data = normalize_readings(sensor_readings)  # Scales to [0,1]
    
    # Step 3: Define metric importance (weights)
    metric_weights = [0.2, 0.1, 0.15, 0.25, 0.1, 0.1, 0.1]
    
    # Step 4: Track historical anomalies (distraction - not used)
    anomaly_tracker = defaultdict(int)
    for val in sensor_readings:
        if val > 150:
            anomaly_tracker['high'] += 1
        elif val < 100:
            anomaly_tracker['low'] += 1
    
    # Step 5: Compute trend (unused in final logic - red herring)
    raw_trend = calculate_trend(normalized_data)
    
    # Step 6: Final performance evaluation
    final_score = evaluate_performance(metric_weights, normalized_data)
    
    # Output result
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()