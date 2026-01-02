from collections import defaultdict

# Simulate sensor data aggregation and performance evaluation
def collect_metrics(raw_readings):
    aggregated = defaultdict(int)
    temp_buffer = []
    outlier_count = 0

    for reading in raw_readings:
        if reading < 0 or reading > 1000:  # Invalid range
            outlier_count += 1
            continue
        category = 'low' if reading < 250 else 'high' if reading > 750 else 'normal'
        aggregated[category] += reading
        temp_buffer.append(reading * 0.1)  # unused transformation

    # Irrelevant smoothing pass
    smoothed = [temp_buffer[i] + temp_buffer[i-1]*0.5 for i in range(1, len(temp_buffer))] if temp_buffer else []
    return aggregated, outlier_count, smoothed

def calculate_baseline(ref_data):
    total = 0
    count = 0
    dummy_tracker = []
    for val in ref_data:
        if val % 2 == 0:
            total += val ** 0.5
            count += 1
        else:
            dummy_tracker.append(val * 2)  # dead code path
    return total / count if count else 0

def filter_anomalies(data_map, limit):
    cleaned = {}
    anomaly_log = []
    for k, v in data_map.items():
        if v > limit:
            cleaned[k] = v * 0.9
        else:
            anomaly_log.append(f"Low-{k}")
    return cleaned

def evaluate_performance(metrics, threshold):
    score = 0
    adjustment = 1.0
    
    if metrics.get('low', 0) > threshold:
        score += 10
        adjustment *= 1.1
    else:
        adjustment *= 0.95

    if metrics.get('normal', 0) > threshold * 3:
        score += 25
        adjustment -= 0.05
    
    high_val = metrics.get('high', 0)
    if high_val > 0 and high_val < threshold * 2:
        score += 15
    elif high_val >= threshold * 2:
        score += 5

    consistency_bonus = 0
    values = list(metrics.values())
    if len(values) > 1:
        variance = sum((x - sum(values)/len(values))**2 for x in values) / len(values)
        if variance < threshold:
            consistency_bonus = 8
    
    score += consistency_bonus
    final_raw = int(score * adjustment)
    
    # Red herring computation
    debug_snapshot = {"score": score, "adj": adjustment, "bonus": consistency_bonus}
    serialization_key = ''.join([chr(97 + (v % 26)) for v in [score, adjustment*100, consistency_bonus]])
    
    return final_raw

# Main execution
raw_sensor_data = [120, 300, 800, 450, 900, 200, 700, 100, 600]
base_threshold = 500

aggregated_metrics, _, _ = collect_metrics(raw_sensor_data)
cleaned_metrics = filter_anomalies(aggregated_metrics, base_threshold)
baseline = calculate_baseline(raw_sensor_data)
final_score = evaluate_performance(cleaned_metrics, base_threshold)

print(f"Result: {final_score}")