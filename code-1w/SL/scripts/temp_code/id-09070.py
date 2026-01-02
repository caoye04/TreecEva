from collections import defaultdict, Counter
import math

# Simulated sensor data ingestion pipeline
def fetch_sensor_data():
    raw_data = [
        (1, 'temp', 23.5), (2, 'pressure', 101.3), (3, 'humidity', 45.2),
        (1, 'temp', 24.1), (4, 'vibration', 0.7), (2, 'pressure', 102.0),
        (5, 'temp', 19.8), (3, 'humidity', 47.1), (4, 'vibration', 1.2),
        (1, 'temp', 22.9), (2, 'pressure', 100.8), (5, 'temp', 20.3)
    ]
    return raw_data

# Redundant parsing function - never used but looks important
def parse_legacy_format(data):
    parsed = []
    for entry in data:
        if entry[0] % 2 == 0:
            parsed.append((entry[1], entry[2] * 1.05))
    return parsed

# Core transformation logic
def group_by_sensor(raw_data):
    grouped = defaultdict(list)
    for sensor_id, sensor_type, reading in raw_data:
        grouped[sensor_type].append(reading)
    return grouped

# Secondary processing with distractor logic
def filter_anomalies(grouped_data):
    filtered = {}
    thresholds = {'temp': (20, 30), 'humidity': (30, 60), 'pressure': (95, 105)}
    
    # Distractor: unused anomaly tracking
    anomaly_log = defaultdict(int)
    total_anomalies = 0
    
    for s_type, readings in grouped_data.items():
        low, high = thresholds.get(s_type, (float('-inf'), float('inf')))
        valid_readings = []
        for r in readings:
            if low <= r <= high:
                valid_readings.append(r)
            else:
                anomaly_log[s_type] += 1
                total_anomalies += 1
        filtered[s_type] = valid_readings
    
    # Dead code path: this modification does nothing
    if total_anomalies > 100:
        for k in filtered:
            filtered[k] = [x * 0.95 for x in filtered[k]]
    
    return filtered

# Irrelevant utility - looks like it's part of analysis
def compute_entropy(values):
    counts = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

# Real processing step disguised among noise
def calculate_stability_metric(readings):
    if not readings:
        return 0.0
    mean_val = sum(readings) / len(readings)
    variance = sum((x - mean_val) ** 2 for x in readings) / len(readings)
    return round(math.sqrt(variance), 3)

# Another decoy function that computes but doesn't influence final result
def predict_next_value(series):
    if len(series) < 3:
        return series[-1] if series else 0
    trend = (series[-1] - series[0]) / (len(series) - 1)
    return round(series[-1] + trend, 2)

# Main processing chain
def process_logs(raw_data):
    grouped = group_by_sensor(raw_data)
    cleaned = filter_anomalies(grouped)
    
    processed = {}
    # Real computation mixed with irrelevant calls
    for sensor_type, readings in cleaned.items():
        stability = calculate_stability_metric(readings)
        entropy = compute_entropy([round(x) for x in readings])  # Computed but unused
        next_pred = predict_next_value(readings)  # Computed but unused
        
        processed[sensor_type] = {
            'readings_count': len(readings),
            'stability': stability,
            'forecast': next_pred  # Stored but only stability matters later
        }
    
    return processed

# Final diagnostic using only specific fields
def analyze_readings(processed_logs):
    weights = {'temp': 0.4, 'humidity': 0.3, 'pressure': 0.3}
    score_components = {}
    
    for sensor_type, data in processed_logs.items():
        if sensor_type in weights:
            # Only stability is used in calculation
            stability = data['stability']
            weight = weights[sensor_type]
            contribution = (1 / (1 + stability)) * weight  # Inverse relationship
            score_components[sensor_type] = round(contribution, 4)
    
    # Distractor: unused aggregation
    total_forecast = sum(d['forecast'] for d in processed_logs.values())
    reading_sum = sum(d['readings_count'] for d in processed_logs.values())
    
    if reading_sum > 100:
        adjustment = total_forecast / 100
    else:
        adjustment = 0  # Never applied
    
    final_score = sum(score_components.values())
    return int(round(final_score * 10000))  # Scale to integer

# Execution flow
if __name__ == "__main__":
    # Initial data acquisition
    sensor_data = fetch_sensor_data()
    
    # Parsing (distractor call - result ignored)
    legacy_parsed = parse_legacy_format(sensor_data)
    
    # Actual processing pipeline
    processed_logs = process_logs(sensor_data)
    
    # Critical statement containing the answer
    final_diagnostic = analyze_readings(processed_logs)
    
    print(f"Result: {final_diagnostic}")