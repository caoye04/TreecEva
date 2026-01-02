from collections import defaultdict, Counter

# Simulate sensor readings over time with some noise
def generate_sensor_data():
    return [i * 2 + (i % 3) for i in range(1, 20) if i % 5 != 0]

# Analyze data drift using moving average
def calculate_drift(data):
    moving_avg = []
    for i in range(2, len(data)):
        avg = (data[i-2] + data[i-1] + data[i]) / 3
        moving_avg.append(round(avg, 2))
    return moving_avg

# Identify anomalies based on deviation threshold
def find_anomalies(data, threshold=6.0):
    mean_val = sum(data) / len(data)
    deviations = [(x - mean_val) ** 2 for x in data]
    variance = sum(deviations) / len(deviations)
    std_dev = variance ** 0.5
    anomalies = [x for x in data if abs(x - mean_val) > threshold * std_dev]
    return anomalies

# Main evaluation logic
def evaluate_performance(sensor_logs):
    # Irrelevant preprocessing: count digit frequencies (distractor)
    digit_counter = Counter()
    for log in sensor_logs:
        for digit in str(log):
            if digit.isdigit():
                digit_counter[digit] += 1
    
    # Semi-relevant transformation: normalize logs
    normalized_logs = [x / max(sensor_logs) * 100 for x in sensor_logs]
    
    # Compute rolling drift metrics
    drift_metrics = calculate_drift(normalized_logs)
    
    # Determine stability score based on drift consistency
    stability_counter = defaultdict(int)
    for val in drift_metrics:
        bucket = int(val // 10)
        stability_counter[bucket] += 1
    
    # Extract trend from dominant bucket
    dominant_trend = max(stability_counter.keys()) if stability_counter else 0
    
    # Find anomalies (not used in final score but included to distract)
    raw_anomalies = find_anomalies(sensor_logs)
    anomaly_ratio = len(raw_anomalies) / len(sensor_logs) if sensor_logs else 0
    
    # Key computation: performance metric based on even-position sum and trend
    even_position_sum = sum(normalized_logs[i] for i in range(0, len(normalized_logs), 2))
    adjustment_factor = 0.87 if dominant_trend >= 2 else 1.15
    
    # Final score calculation
    base_score = even_position_sum * adjustment_factor
    penalty = sum(1 for x in normalized_logs if x < 10) * 1.5
    final_score = int(base_score - penalty)
    
    # Dead code path (never executed - red herring)
    if False:
        backup_score = sum(digit_counter.values()) * 2
        final_score = min(final_score, backup_score)
    
    return final_score

# Execute workflow
sensor_readings = generate_sensor_data()
data_drift = calculate_drift(sensor_readings)
anomaly_list = find_anomalies(sensor_readings, threshold=5.5)

# Critical execution point
final_score = evaluate_performance(sensor_readings)
print(f"Result: {final_score}")