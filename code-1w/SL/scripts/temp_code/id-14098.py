from itertools import combinations

# Simulate sensor data processing with weighted scoring
def collect_metrics(raw_readings):
    base_metrics = {}
    temp_readings = [x for x in raw_readings if x < 100]
    high_freq_noise = [x for x in raw_readings if x > 150]  # distractor

    base_metrics['avg'] = sum(temp_readings) / len(temp_readings)
    base_metrics['peak'] = max(temp_readings)
    base_metrics['stability'] = len(temp_readings) // (len(raw_readings) + 1)
    
    # Extra derived metrics (some irrelevant)
    base_metrics['noise_ratio'] = len(high_freq_noise) / len(raw_readings) if raw_readings else 0
    base_metrics['range'] = max(temp_readings) - min(temp_readings)

    return base_metrics

def normalize_values(data_dict):
    normalized = {}
    for k, v in data_dict.items():
        if k == 'noise_ratio':
            normalized[k] = round(1 - v, 3)  # invert noise
        else:
            normalized[k] = round(v / (v + 1), 3)  # standard decay norm
    # Dead code path (distractor)
    if 'dummy_flag' in data_dict:
        normalized['extra'] = 0
    return normalized

def evaluate_performance(metrics, weights):
    score = 0.0
    components = ['avg', 'peak', 'stability', 'range']  # exclude noise_ratio
    
    # Generate redundant pairs for complexity (distractor)
    pairs = list(combinations(components, 2))
    pair_contributions = []
    for a, b in pairs:
        contrib = metrics[a] * metrics[b] * 0.01  # minor side effect
        pair_contributions.append(round(contrib, 3))
    
    # Main scoring logic
    for key in components:
        weight = weights.get(key, 0.1)
        score += metrics[key] * weight
    
    # Additional adjustment based on stability threshold (relevant)
    if metrics['stability'] > 0:
        score *= 1.1
    
    return round(score, 3)

# Main execution
sensor_data = [88, 92, 95, 87, 91, 160, 170, 89, 94]
config_weights = {
    'avg': 0.4,
    'peak': 0.3,
    'stability': 0.2,
    'range': 0.1
}

raw_metrics = collect_metrics(sensor_data)
normalized_metrics = normalize_values(raw_metrics)
final_score = evaluate_performance(normalized_metrics, config_weights)

# Print result as required
print(f"Result: {final_score}")