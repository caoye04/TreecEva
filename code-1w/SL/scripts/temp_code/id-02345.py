from collections import defaultdict

# Simulate sensor data aggregation and performance evaluation
def collect_metrics(raw_readings):
    aggregated = defaultdict(int)
    temp_cache = []
    outlier_count = 0

    for reading in raw_readings:
        sensor_id = reading['sensor']
        value = reading['value']
        
        # Filter obvious outliers (distraction: not used later)
        if abs(value) > 1000:
            outlier_count += 1
            continue
            
        # Only process valid sensors
        if sensor_id in ['A1', 'B2', 'C3']:
            aggregated[sensor_id] += value
            temp_cache.append(value * 0.95)  # Scaled cache - semi-relevant

    # Dead code path - misleading
    if outlier_count == 0:
        backup_flag = True
        temp_cache = [x + 10 for x in temp_cache]  # Never actually used

    return dict(aggregated)


def calculate_baseline(metrics):
    total = sum(metrics.values())
    count = len(metrics)
    average = total / count if count else 0
    
    # Extra computations to increase cognitive load
    squared_sum = sum(x ** 2 for x in metrics.values())
    variance_proxy = squared_sum / count - average ** 2 if count else 0
    
    # This normalization is unused but looks important
    normalized_avg = average * (1 + variance_proxy * 0.01) if variance_proxy > 0 else average
    
    return average


def evaluate_performance(data, threshold):
    # Apply threshold filtering
    passed_sensors = [val for val in data.values() if val >= threshold]
    bonus_factor = 1.0
    
    # Conditional bonus logic with red herring variables
    if len(passed_sensors) >= 2:
        ratio = len(passed_sensors) / len(data)
        if ratio >= 0.66:
            adjustment = ratio * 100
            # Bitwise trick that doesn't affect result
            masked_adj = int(adjustment) & 255
            bonus_factor = 1.25
    else:
        penalty_counter = 0
        for v in data.values():
            if v < threshold * 0.8:
                penalty_counter += 1
        # Computed but unused
        penalty_rate = penalty_counter / len(data)

    base_score = sum(passed_sensors)
    final_score = int(base_score * bonus_factor)
    
    # Critical print statement - required format
    print(f"Result: {final_score}")
    return final_score

# Main execution
if __name__ == "__main__":
    readings = [
        {'sensor': 'A1', 'value': 120},
        {'sensor': 'B2', 'value': 180},
        {'sensor': 'C3', 'value': 90},
        {'sensor': 'D4', 'value': 200},  # Invalid sensor
        {'sensor': 'A1', 'value': 80},
        {'sensor': 'B2', 'value': 150},
        {'sensor': 'C3', 'value': 110},
        {'sensor': 'A1', 'value': -50},  # Will be filtered as outlier
    ]
    
    metric_data = collect_metrics(readings)
    base_threshold = calculate_baseline(metric_data)
    final_score = evaluate_performance(metric_data, base_threshold)