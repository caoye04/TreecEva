from collections import defaultdict

# Simulate sensor data aggregation and performance evaluation
def collect_metrics(raw_readings):
    aggregated = defaultdict(int)
    temp_cache = {}
    outlier_count = 0

    for reading in raw_readings:
        sensor_id = reading['sensor']
        value = reading['value']
        
        # Irrelevant caching (distractor)
        if sensor_id not in temp_cache:
            temp_cache[sensor_id] = []
        temp_cache[sensor_id].append(value)
        
        # Actual aggregation logic
        if value >= 0 and value <= 100:
            aggregated[sensor_id] += value
        else:
            outlier_count += 1  # Count but don't use later

    # Misleading transformation (not used in final result)
    normalized = {k: v / max(aggregated.values()) for k, v in aggregated.items()}
    return dict(aggregated)

# Analyze trend consistency (helper function)
def has_stable_trend(values):
    if len(values) < 2:
        return True
    direction = None
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            current = 'up'
        elif values[i] < values[i-1]:
            current = 'down'
        else:
            current = 'same'
        
        if direction is None:
            direction = current
        elif direction != current:
            return False  # Fluctuating trend
    return True

# Main evaluation logic
def evaluate_performance(metrics, threshold):
    total_sum = sum(metrics.values())
    count_sensors = len(metrics)
    average_load = total_sum / count_sensors if count_sensors > 0 else 0
    
    # Secondary derived metrics (some are distractions)
    adjusted_total = total_sum * 0.95  # Unused adjustment
    peak_value = max(metrics.values())
    low_performers = [k for k, v in metrics.items() if v < threshold]
    penalty_factor = len(low_performers) * 2
    
    # Simulated historical comparison (irrelevant to final score)
    historical_avg = 45.0
    deviation = abs(average_load - historical_avg)
    stability_bonus = 10 if deviation < 5 else 0
    
    # Core scoring logic
    base_score = total_sum - penalty_factor
    if peak_value > 80:
        base_score += 5
    
    # Conditional adjustment based on pattern
    readings_list = list(metrics.values())
    if has_stable_trend(readings_list):
        base_score += 8
    
    return int(base_score)

# Generate synthetic input
data_stream = [
    {'sensor': 'A', 'value': 23},
    {'sensor': 'B', 'value': 45},
    {'sensor': 'A', 'value': 34},
    {'sensor': 'C', 'value': 12},
    {'sensor': 'B', 'value': 56},
    {'sensor': 'A', 'value': 18},
    {'sensor': 'D', 'value': 67},
    {'sensor': 'C', 'value': 29},
    {'sensor': 'E', 'value': 5},
    {'sensor': 'D', 'value': 73}
]

# Execute pipeline
raw_aggregation = collect_metrics(data_stream)
base_threshold = 40
final_score = evaluate_performance(raw_aggregation, base_threshold)
print(f"Target result: {final_score}")