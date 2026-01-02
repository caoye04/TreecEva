from collections import defaultdict
import math

# Simulate sensor data aggregation and performance scoring in an industrial control system
def collect_sensor_data(units):
    data = defaultdict(list)
    for unit in units:
        if unit['type'] == 'thermal':
            data['temperature'].append(unit['reading'] * 0.85)
        elif unit['type'] == 'pressure':
            data['pressure'].append(unit['reading'] + 5)
    return data

def normalize_readings(raw_data):
    normalized = {}
    temp_vals = raw_data.get('temperature', [])
    pressure_vals = raw_data.get('pressure', [])
    
    avg_temp = sum(temp_vals) / len(temp_vals) if temp_vals else 0
    avg_pressure = sum(pressure_vals) / len(pressure_vals) if pressure_vals else 0
    
    normalized['temp_norm'] = round(avg_temp / 100, 4) if avg_temp else 0
    normalized['press_norm'] = round(math.log(avg_pressure + 1), 4) if avg_pressure > 0 else 0
    
    # Distractor: irrelevant humidity normalization
    humidity_fake = [65, 70, 68]
    avg_humid = sum(humidity_fake) / len(humidity_fake)
    normalized['humid_dummy'] = avg_humid * 0.1  # Not used later
    
    return normalized

def calculate_efficiency_index(norm_data):
    base_index = 1.0
    if norm_data['temp_norm'] > 0.5:
        base_index *= 0.9
    elif norm_data['temp_norm'] < 0.3:
        base_index *= 1.1
    else:
        base_index *= 1.05

    if norm_data['press_norm'] > 0.7:
        base_index *= 1.15
    
    # Distractor: unused efficiency branches
    if norm_data.get('humid_dummy', 0) > 6.5:
        base_index *= 0.95  # Never reached due to logic
    
    return round(base_index, 4)

def evaluate_performance(metrics, weights):
    weighted_sum = 0.0
    total_weight = sum(weights.values())
    for key, value in metrics.items():
        if key in weights:
            weighted_sum += value * weights[key]
    
    # Final adjustment using efficiency index
    efficiency = calculate_efficiency_index(metrics)
    final_score = int(weighted_sum * efficiency * 100)
    
    # Dead code: redundant check with no impact
    if final_score < 0:
        final_score = 0  # Not triggered
    
    return final_score

# Main execution
units = [
    {'type': 'thermal', 'reading': 60},
    {'type': 'thermal', 'reading': 55},
    {'type': 'pressure', 'reading': 20},
    {'type': 'pressure', 'reading': 25}
]

raw_data = collect_sensor_data(units)
normalized_metrics = normalize_readings(raw_data)

weights = {
    'temp_norm': 0.4,
    'press_norm': 0.6
}

final_score = evaluate_performance(normalized_metrics, weights)
print(f"Result: {final_score}")