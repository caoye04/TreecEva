from itertools import combinations

# Simulate sensor array efficiency metrics
def calculate_efficiency(readings):
    base = sum(r ** 2 for r in readings) / len(readings)
    adjustment = len([r for r in readings if r > 5]) * 0.1
    return base + adjustment

def generate_metrics(raw_data):
    temp_trend = [raw_data[i+1] - raw_data[i] for i in range(len(raw_data)-1)]
    trend_strength = sum(abs(t) for t in temp_trend)
    
    # Distractor: unused computation
    redundant_calc = [t * 1.5 for t in temp_trend if t > 0]
    ignored_result = max(redundant_calc) if redundant_calc else 0
    
    efficiency = calculate_efficiency(raw_data)
    stability = 10 - (max(raw_data) - min(raw_data)) * 0.5
    response_time = len(raw_data) / (sum(raw_data) / 10)
    
    return {
        'efficiency': efficiency,
        'stability': stability,
        'response_time': response_time,
        'trend_strength': trend_strength
    }

def apply_calibration(metrics, mode='standard'):
    calibrated = {}
    for k, v in metrics.items():
        if k == 'efficiency':
            calibrated[k] = v * 1.15
        elif k == 'stability':
            calibrated[k] = v * 1.05
        elif k == 'response_time':
            calibrated[k] = max(v * 0.9, 1.0)
        else:
            calibrated[k] = v * 0.8  # generic adjustment
    
    # Dead code path (not taken unless mode=='debug')
    if mode == 'debug':
        print("Debug mode active")  # unreachable in normal execution
    
    return calibrated

def compute_reliability_index(calibrated):
    keys = ['efficiency', 'stability', 'response_time']
    values = [calibrated[k] for k in keys]
    
    # Generate all pairwise interactions as features
    interaction_sum = 0
    for a, b in combinations(values, 2):
        interaction_sum += a * b * 0.01
    
    base_index = sum(values) / len(values)
    return base_index + interaction_sum

def evaluate_performance(metrics, weights):
    calibrated = apply_calibration(metrics, mode='standard')
    reliability = compute_reliability_index(calibrated)
    
    # Weighted aggregation
    weighted_sum = 0
    total_weight = 0
    for key, weight in weights.items():
        if key in calibrated:
            weighted_sum += calibrated[key] * weight
            total_weight += weight
    
    if total_weight == 0:
        return 0
    
    final_component = weighted_sum / total_weight
    
    # Final scoring with nonlinear boost
    final_score = final_component * (1 + reliability / 100)
    
    # Irrelevant tracking variable
    tracking_log = f'Score computed: {final_score:.2f}'
    
    return final_score

# Main execution
sensor_readings = [4, 6, 5, 7, 5, 6, 4]
metrics = generate_metrics(sensor_readings)
benchmark_weights = {
    'efficiency': 3.0,
    'stability': 2.5,
    'response_time': 2.0,
    'trend_strength': 1.0  # included but downweighted
}
final_score = evaluate_performance(metrics, benchmark_weights)
print(f"Result: {final_score}")