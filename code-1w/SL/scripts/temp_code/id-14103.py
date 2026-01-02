from collections import defaultdict, Counter

# Simulate sensor readings with some noise and redundancy
def get_sensor_readings():
    raw_readings = [
        ('temp', 23.5), ('humidity', 45.2), ('temp', 24.1), ('pressure', 1013.25),
        ('humidity', 46.0), ('temp', 23.9), ('pressure', 1012.8), ('temp', 24.0)
    ]
    return raw_readings

def preprocess_readings(readings):
    # Group by type using defaultdict
    grouped = defaultdict(list)
    for sensor_type, value in readings:
        grouped[sensor_type].append(value)
    
    processed = {}
    for stype, values in grouped.items():
        avg_val = sum(values) / len(values)
        processed[stype] = round(avg_val, 2)
    
    # Misleading computation: entropy-like measure (not used later)
    total_points = sum(len(v) for v in grouped.values())
    entropy = 0
    for v in grouped.values():
        p = len(v) / total_points
        if p > 0:
            import math
            entropy -= p * math.log(p)
    
    # Dead code path: never accessed
    if entropy < 0:
        processed['entropy'] = entropy
        
    return processed

def analyze_stability(metrics):
    # Assess variation across metrics using min/max spread
    all_vals = list(metrics.values())
    spread = max(all_vals) - min(all_vals)
    
    # Extra distraction: normalize to 0-1 scale (unused)
    normalized = [(v - min(all_vals)) / (spread + 1e-8) for v in all_vals]
    
    # Stability threshold based on empirical observation
    stable = spread < 100
    return stable, spread

def compute_reliability_index(metrics, stability_flag, spread):
    base_index = 0
    if 'temp' in metrics:
        base_index += 25
    if 'humidity' in metrics:
        base_index += 20
    if 'pressure' in metrics:
        base_index += 30
    
    # Adjustment factors (some irrelevant)
    adjustment = 0
    if stability_flag:
        adjustment += 15
    if spread < 50:
        adjustment += 10  # unreachable due to data
    if len(metrics) >= 3:
        adjustment += 5
    
    reliability = base_index + adjustment
    
    # Unused diagnostic trace
    debug_info = f'Reliability breakdown: base={base_index}, adj={adjustment}'
    
    return reliability

def calculate_final_score(data_dict):
    # Extract relevant metric values
    temp_val = data_dict.get('temp', 0)
    humidity_val = data_dict.get('humidity', 0)
    pressure_val = data_dict.get('pressure', 0)
    
    # Composite scoring with weighted contributions
    temperature_score = temp_val * 1.2
    humidity_score = (100 - abs(humidity_val - 50)) * 0.8  # ideal at 50%
    pressure_score = (1020 - abs(pressure_val - 1013)) * 0.5  # ideal at 1013
    
    preliminary_score = temperature_score + humidity_score + pressure_score
    
    # Apply non-linear boost if all sensors agree within range
    values_in_range = 0
    if 23 <= temp_val <= 25:
        values_in_range += 1
    if 40 <= humidity_val <= 60:
        values_in_range += 1
    if 1010 <= pressure_val <= 1020:
        values_in_range += 1
    
    consensus_multiplier = 1.0
    if values_in_range == 3:
        consensus_multiplier = 1.15
    elif values_in_range == 2:
        consensus_multiplier = 1.05
    
    boosted_score = preliminary_score * consensus_multiplier
    
    # Final adjustment based on reliability index
    is_stable, spread_val = analyze_stability(data_dict)
    reliability = compute_reliability_index(data_dict, is_stable, spread_val)
    final_adjustment = reliability / 100.0
    
    final_score = boosted_score + final_adjustment
    
    # Several intermediate variables not directly affecting logic
    avg_metric = sum(data_dict.values()) / len(data_dict)
    metric_variance = sum((v - avg_metric) ** 2 for v in data_dict.values()) / len(data_dict)
    quality_flag = metric_variance < 50
    
    return round(final_score, 2)

# Main execution flow
if __name__ == '__main__':
    readings = get_sensor_readings()
    processed_data = preprocess_readings(readings)
    final_score = calculate_final_score(processed_data)
    print(f"Result: {final_score}")