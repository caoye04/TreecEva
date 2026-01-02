def analyze_performance(metrics, thresholds):
    alert_flags = set()
    performance_log = []
    
    for idx, (name, value) in enumerate(metrics.items()):
        if value < thresholds.get(name, 0):
            alert_flags.add(f'low_{name}')
            performance_log.append((idx, name, value))

    return alert_flags, performance_log


def adjust_weights(raw_weights, boost_factor):
    adjusted = {}
    temp_sum = 0
    
    for k, v in raw_weights.items():
        temp_val = v * boost_factor if v > 0.1 else v
n        adjusted[k] = round(temp_val, 4)
        temp_sum += adjusted[k]
    
    normalization_factor = 1.0 / temp_sum if temp_sum != 0 else 1
    normalized = {k: v * normalization_factor for k, v in adjusted.items()}
    
    # Distractor: irrelevant computation
    squared_deltas = [abs(v - 0.5)**2 for v in normalized.values()]
    mean_square_dev = sum(squared_deltas) / len(squared_deltas) if squared_deltas else 0
    
    return normalized


def calculate_final_score(data_points, weights, config):
    base_total = 0
    penalty = 0
    bonus = 0
    
    # Real logic begins
    sorted_points = sorted(data_points.values())
    median_value = sorted_points[len(sorted_points)//2]
    
    for key, val in data_points.items():
        if val >= median_value:
            bonus += weights.get(key, 0.1)
        else:
            penalty += 0.5 * weights.get(key, 0.1)

    # Core calculation
    for i, (k, v) in enumerate(zip(data_points.keys(), weights.values())):
        base_total += data_points.get(k, 0) * v

    # Secondary adjustment based on config
    if config['scaling_enabled']:
        scale_factor = config['scale_factor']
        base_total *= scale_factor

    # Final composition
    intermediate = base_total + (bonus * 10) - (penalty * 5)
    final_score = int(round(intermediate - 17.8))  # deterministic integer result
    
    # Distractor variables
    debug_info = {"intermediate": intermediate, "adjustments": (bonus, penalty)}
    temp_result = (intermediate * 2) % 100
    
    return final_score

# Main execution block
if __name__ == "__main__":
    metrics = {'latency': 0.08, 'throughput': 0.92, 'accuracy': 0.97, 'coverage': 0.85}
    thresholds = {'latency': 0.1, 'accuracy': 0.95, 'coverage': 0.8}
    raw_weights = {'latency': 0.2, 'throughput': 0.3, 'accuracy': 0.4, 'coverage': 0.1}
    config = {'scaling_enabled': True, 'scale_factor': 1.2}
    
    # Irrelevant preprocessing
    valid_keys = set(metrics.keys()) & set(thresholds.keys())
    filtered_metrics = {k: metrics[k] for k in valid_keys}
    
    # Call analysis (semi-relevant but not used directly)
    alerts, logs = analyze_performance(filtered_metrics, thresholds)
    
    # Weight adjustment with side effects (partially relevant)
    adjusted_weights = adjust_weights(raw_weights, boost_factor=1.1)
    
    # Critical statement
    final_score = calculate_final_score(metrics, adjusted_weights, config)
    
    # Output result
    print(f"Result: {final_score}")