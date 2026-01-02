from collections import defaultdict, Counter

# Simulate sensor data aggregation and anomaly filtering
def collect_sensor_readings():
    raw_readings = [
        ('temp', 23.5), ('humidity', 45), ('temp', 24.1),
        ('pressure', 1013), ('humidity', 47), ('temp', 22.9),
        ('light', 300), ('pressure', 1012), ('temp', 24.0)
    ]
    
    aggregated = defaultdict(list)
    for sensor, value in raw_readings:
        aggregated[sensor].append(value)
    
    return aggregated

# Misleading function - appears useful but not used in final computation
def compute_rolling_average(data, window=2):
    result = []
    for i in range(len(data)):
        if i < window - 1:
            result.append(None)
        else:
            result.append(sum(data[i - window + 1:i + 1]) / window)
    return result

# Core processing pipeline
def filter_outliers_and_normalize(data_dict):
    cleaned = {}
    stats_summary = {}  # distractor: collected but not fully used
    
    for sensor_type, values in data_dict.items():
        mean_val = sum(values) / len(values)
        variance = sum((x - mean_val) ** 2 for x in values) / len(values)
        std_dev = variance ** 0.5
        
        # Filter values within 1.5 std dev
        filtered = [v for v in values if abs(v - mean_val) <= 1.5 * std_dev]
        
        # Normalize to zero mean
        normalized = [round(v - mean_val, 2) for v in filtered]
        
        cleaned[sensor_type] = normalized
        stats_summary[sensor_type] = {
            'original_count': len(values),
            'filtered_count': len(filtered),
            'mean': round(mean_val, 2),
            'std_dev': round(std_dev, 2)
        }
        
    # Dead code path (misleading branch)
    if 'co2' in cleaned:
        cleaned['co2'] = [x * 1.1 for x in cleaned['co2']]
    
    return cleaned

# Secondary transformation with red herring variables
def extract_temp_trends(temp_data):
    trend_changes = 0
    prev = temp_data[0]
    direction = 0
    
    for curr in temp_data[1:]:
        if curr > prev:
            if direction == -1:
                trend_changes += 1
            direction = 1
        elif curr < prev:
            if direction == 1:
                trend_changes += 1
            direction = -1
        prev = curr
    
    # Computed but unused in final logic
    smoothness_score = len(temp_data) / (trend_changes + 1) if trend_changes > 0 else float('inf')
    return trend_changes  # only this matters

# Main scoring logic
def calculate_final_score(data):
    base_weight = {'temp': 1.2, 'humidity': 0.8, 'pressure': 0.9, 'light': 0.5}
    signal_quality = {}
    total_influence = 0.0
    
    for sensor, readings in data.items():
        if not readings:
            signal_quality[sensor] = 0.0
            continue
        
        magnitude = sum(abs(r) for r in readings)
        penalty_factor = 1.0
        
        # Apply length-based adjustment (real logic)
        if len(readings) < 3:
            penalty_factor = 0.6
        
        quality = magnitude * penalty_factor
        signal_quality[sensor] = quality
        total_influence += quality * base_weight.get(sensor, 0.4)
    
    # Distractor computations
    avg_influence = total_influence / len(signal_quality) if signal_quality else 0
    completeness_ratio = len([v for v in signal_quality.values() if v > 0]) / len(base_weight)
    stability_hint = extract_temp_trends(data.get('temp', [0]))
    
    # Final formula combines multiple factors
    final_score = int(
        total_influence * 0.7 + 
        avg_influence * 0.2 + 
        completeness_ratio * 10 + 
        stability_hint * 2
    )
    
    # Irrelevant normalization step (no effect on integer cast above)
    normalized_final = round(final_score / 1.0, 4)
    
    return final_score

# Execution flow
if __name__ == '__main__':
    raw_data = collect_sensor_readings()
    processed_data = filter_outliers_and_normalize(raw_data)
    
    # Critical execution point
    final_score = calculate_final_score(processed_data)
    
    print(f"Result: {final_score}")