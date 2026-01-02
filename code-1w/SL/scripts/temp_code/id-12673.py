import math

def analyze_metrics(raw_values, thresholds):
    normalized = [max(0.0, min(1.0, v / 100.0)) for v in raw_values]
    
    # Irrelevant transformation (distractor)
    squared_deltas = [(x - 0.5)**2 for x in normalized]
    entropy_proxy = -sum(p * math.log(p + 1e-9) for p in normalized)
    
    # Relevant filtering
    passed = [n for n in normalized if n >= thresholds['min_accept']]
    
    # Semi-relevant statistic (not used later but plausible)
    avg_deviation = sum(abs(x - 0.5) for x in normalized) / len(normalized)

    return passed

def calculate_complexity_index(items):
    if len(items) == 0:
        return 0.0
    log_component = math.log(len(items) + 1)
    inverse_density = 1.0 / (sum(items) + 0.1)
    return log_component * inverse_density * 10.0

def calculate_rating(data_list):
    base_weight = 0.85
    
    # Dummy clustering attempt (dead code path)
    clusters = {}
    for i, val in enumerate(data_list):
        key = int(val * 10) // 2
        if key not in clusters:
            clusters[key] = []
        clusters[key].append(val)
    
    # Unused cluster metric
    cluster_count = len(clusters)
    balance_metric = len(set(clusters.keys())) / (max(clusters.keys()) + 1)
    
    complexity = calculate_complexity_index(data_list)
    
    # Core logic: efficiency depends on both size and complexity
    size_factor = len(data_list) * 0.5
    efficiency = size_factor + (10.0 - complexity)
    
    return efficiency

# Main execution
sensor_readings = [88, 72, 94, 65, 103, 85, 77, 91, 68]
config_thresholds = {'min_accept': 0.7, 'saturation': 0.95}

# Intermediate processing with side calculations
aggregate_stats = {
    'total_sensors': len(sensor_readings),
    'peak_value': max(sensor_readings),
    'baseline_adjust': sum(sensor_readings) / len(sensor_readings)
}

# Distractor: time-series smoothing (unused)
smoothed = []
for i in range(len(sensor_readings)):
    window = sensor_readings[max(0, i-1):i+2]
    smoothed.append(sum(window) / len(window))

processed_data = analyze_metrics(sensor_readings, config_thresholds)
efficiency_score = calculate_rating(processed_data)

# Final computation point
final_rating = calculate_rating(processed_data)
print(f"Result: {efficiency_score}")