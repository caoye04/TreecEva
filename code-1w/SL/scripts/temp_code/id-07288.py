from collections import defaultdict

# Simulate sensor data aggregation and performance evaluation
def collect_metrics(raw_readings):
    aggregated = defaultdict(float)
    counts = defaultdict(int)
    
    for sensor_id, value in raw_readings:
        if value < 0:  # Invalid reading
            continue
        aggregated[sensor_id] += value
        counts[sensor_id] += 1

    avg_metrics = {}
    for sid in aggregated:
        avg_metrics[sid] = aggregated[sid] / counts[sid]
    
    return avg_metrics

def filter_outliers(data, threshold=50.0):
    # Misleading: this function is called but not impactful due to data range
    filtered = {}
    for k, v in data.items():
        if v <= threshold:
            filtered[k] = v
    return filtered if filtered else data  # Return original if all filtered

def compute_variance(values):
    # Dead code path - never actually used in final computation
    mean = sum(values) / len(values)
    return sum((x - mean) ** 2 for x in values) / len(values)

def evaluate_performance(metrics, base):
    score = 0
    penalty_adjustment = 0.0
    
    # Irrelevant intermediate calculation (distractor)
    temp_vals = [v * 1.05 for v in metrics.values() if v > base]
    if len(temp_vals) > 2:
        penalty_adjustment = sum(temp_vals) * 0.01
    
    for val in metrics.values():
        if val > base:
            score += 1
        elif val < base * 0.8:
            score -= 2
    
    # Key logic step: score adjusted by fixed rule
    modifier = len(metrics) // 4
    score += modifier
    
    # Final assignment - target execution point
    final_score = int(score - penalty_adjustment)
    return final_score

# Main execution
if __name__ == '__main__':
    raw_sensor_data = [
        ('A1', 23.1), ('B2', 45.6), ('A1', 21.9), ('C3', 67.3),
        ('B2', 47.2), ('D4', 12.5), ('C3', 66.8), ('D4', 13.1),
        ('E5', 89.0), ('E5', 87.4), ('F6', 5.2), ('F6', 6.1)
    ]
    base_threshold = 40.0
    
    # Extraneous pre-processing (some distraction)
    valid_only = [item for item in raw_sensor_data if item[1] >= 0]
    processed_readings = collect_metrics(valid_only)
    
    cleaned_data = filter_outliers(processed_readings, 50.0)
    
    # Unused statistical computation (distractor)
    all_values = list(processed_readings.values())
    variance_proxy = sum((v - 40) ** 2 for v in all_values) / len(all_values)
    
    # Critical statement
    final_score = evaluate_performance(processed_readings, base_threshold)
    
    print(f"Result: {final_score}")