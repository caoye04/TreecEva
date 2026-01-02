from collections import defaultdict, Counter

# Simulate sensor data aggregation and anomaly detection in an IoT system
def collect_sensor_readings():
    raw_data = [
        ('sensor_a', [23.4, 24.1, 25.0, 23.8, 999.0]),
        ('sensor_b', [19.5, 19.6, 19.5, 19.7, 19.6]),
        ('sensor_c', [30.2, 30.4, 999.0, 30.5, 30.3]),
        ('sensor_d', [27.1, 27.0, 27.2, 27.1, 999.0])
    ]
    return raw_data

def clean_and_validate(data):
    cleaned = defaultdict(list)
    anomalies = defaultdict(int)
    
    for sensor_id, readings in data:
        for val in readings:
            if val == 999.0:
                anomalies[sensor_id] += 1
            elif 15.0 <= val <= 45.0:
                cleaned[sensor_id].append(val)
    
    # Irrelevant summary (distractor)
    total_anomalies = sum(anomalies.values())
    avg_per_sensor = total_anomalies / len(anomalies) if anomalies else 0
    
    return dict(cleaned), anomalies

def compute_trend_scores(cleaned_data):
    trends = {}
    volatility = {}
    
    for sensor, values in cleaned_data.items():
        if len(values) > 1:
            trend = values[-1] - values[0]
            avg = sum(values) / len(values)
            var = sum((v - avg) ** 2 for v in values) / len(values)
            volatility[sensor] = round(var, 3)
        else:
            trend = 0
            volatility[sensor] = 0.0
        trends[sensor] = round(trend, 2)
    
    # Dead computation path (distractor)
    if 'sensor_x' in trends:
        trends['sensor_x'] *= 2
    
    return trends, volatility

def calculate_final_score(trends, weights):
    base_score = 0
    debug_weights = []
    
    for sensor, trend in trends.items():
        weight = weights.get(sensor, 1.0)
        contribution = trend * weight
        base_score += contribution
        debug_weights.append(weight)
    
    # Extra processing that doesn't affect result
    normalized = base_score / (len(trends) + 0.1) if trends else 0
    ceiling_score = min(100, max(-100, round(normalized, 1)))
    
    return int(round(base_score))  # Final score based on unnormalized base

# Main execution flow
data_source = collect_sensor_readings()
processed_data, anomaly_log = clean_and_validate(data_source)
trend_analysis, variability = compute_trend_scores(processed_data)

# Weight configuration (real signal)
weights = {
    'sensor_a': 1.5,
    'sensor_b': 2.0,
    'sensor_c': 1.0,
    'sensor_d': 0.5
}

# Spurious data structure (distractor)
counter_summary = Counter()
for k, v in processed_data.items():
    counter_summary[k] = len(v)

final_score = calculate_final_score(trend_analysis, weights)
print(f"Result: {final_score}")