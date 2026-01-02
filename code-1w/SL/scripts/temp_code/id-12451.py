import math

def analyze_component_health(sensor_data, weights):
    # Irrelevant health computation (dead path)
    total = 0
    for k, v in sensor_data.items():
        if 'temp' in k:
            total += v * weights.get(k, 1.0)
    return total / len(sensor_data) if sensor_data else 0

def compute_entropy(values):
    # Distractor: computes entropy but not used in main logic
    total = sum(values)
    entropy = 0
    for v in values:
        prob = v / total
        if prob > 0:
            entropy -= prob * math.log(prob)
    return entropy

def extract_key_indicators(log_entry):
    # Extracts relevant indicators but adds noise
    features = {}
    for key, val in log_entry.items():
        if key.startswith('metric_'):
            features[key] = val ** 2  # Distortion
    features['timestamp_norm'] = abs(hash(log_entry.get('timestamp', '')) % 1000)
    return features

def adjust_for_bias(data_dict, correction_factor=0.92):
    # Misleading adjustment function (not actually affecting final result)
    adjusted = {}
    for k, v in data_dict.items():
        adjusted[k] = v * correction_factor if isinstance(v, (int, float)) else v
    return adjusted

def validate_stability(readings):
    # Unused validation logic (red herring)
    if len(readings) < 3:
        return False
    variance = sum((x - sum(readings)/len(readings))**2 for x in readings) / len(readings)
    return variance < 5.0

def evaluate_performance(log, threshold):
    # Core logic buried among distractions
    processed = {}
    for k, v in log.items():
        if k == 'metric_A':
            processed[k] = v * 1.5
        elif k == 'metric_B':
            processed[k] = v + 10
        elif k == 'metric_C':
            processed[k] = max(v, threshold)
    
    # Actual answer computation
    base = processed.get('metric_A', 0) + processed.get('metric_B', 0)
    bonus = 50 if processed.get('metric_C', 0) > threshold else 25
    penalty = 0
    if 'metric_D' in log and log['metric_D'] > 80:
        penalty = 20  # Not triggered
    
    intermediate = base * 1.1
    final_score = int(intermediate + bonus - penalty)
    
    # Dead code path with decoy variables
    temp_result = intermediate * 0.5
    temp_result = math.ceil(temp_result) if temp_result > 100 else temp_result
    
    return final_score

# Main execution with multiple irrelevant variables
if __name__ == '__main__':
    metrics_log = {
        'metric_A': 60,
        'metric_B': 40,
        'metric_C': 75,
        'metric_D': 70,
        'timestamp': '2023-10-05T08:23:11',
        'sensor_X_temp': 45,
        'sensor_Y_temp': 47,
        'status_flag': 0b1010
    }

    config_weights = {
        'sensor_X_temp': 1.1,
        'sensor_Y_temp': 0.9
    }

    # Irrelevant data structures
    historical_metrics = [
        {'metric_A': 55, 'metric_B': 42, 'timestamp': '2023-10-04'},
        {'metric_A': 62, 'metric_B': 38, 'timestamp': '2023-10-03'}
    ]

    summary_stats = {
        'avg_latency': 120.5,
        'peak_usage': 87.2,
        'entropy_level': compute_entropy([55, 62, 42, 38])
    }

    # Trigger core logic
    base_threshold = 70
    final_score = evaluate_performance(metrics_log, base_threshold)
    
    # Print required result
    print(f"Result: {final_score}")
