from collections import defaultdict
from itertools import combinations

# Simulate system performance metrics from multiple sensors
def collect_diagnostics():
    data = defaultdict(float)
    data['latency'] = 120.5
    data['throughput'] = 850.2
    data['error_rate'] = 0.034
    data['jitter'] = 7.8
    data['bandwidth_util'] = 68.9
    return data

# Apply calibration adjustments (some are red herrings)
def apply_calibration(raw_metrics):
    calibrated = {}
    temp_offset = 0.05 * raw_metrics['latency']
    jitter_factor = raw_metrics['jitter'] * 0.1
    phantom_adjustment = raw_metrics['error_rate'] * 100  # unused distractor
    
    calibrated['latency'] = raw_metrics['latency'] - temp_offset
    calibrated['throughput'] = raw_metrics['throughput'] + jitter_factor
    calibrated['error_rate'] = max(0, raw_metrics['error_rate'] - 0.01)
    calibrated['response_ratio'] = calibrated['throughput'] / (calibrated['latency'] + 1)
    return calibrated

# Compute derived health indicators
def compute_health_indicators(calib_data):
    indicators = []
    base_health = 100.0
    
    if calib_data['latency'] < 130:
        base_health += 10
    if calib_data['throughput'] > 800:
        base_health += 15
    if calib_data['error_rate'] < 0.05:
        base_health += 20
    
    # Generate unused synthetic metrics to increase cognitive load
    for pair in combinations(['latency', 'throughput', 'error_rate'], 2):
        synthetic_val = sum(calib_data[k] for k in pair if k in calib_data) % 7
        indicators.append(synthetic_val)
    
    # Actual relevant derived metric
    stability_index = calib_data['response_ratio'] * 0.7
    indicators.append(stability_index)
    
    return indicators, base_health

# Evaluate final performance score using weighted model
def evaluate_performance(metrics, weights):
    _, base_score = compute_health_indicators(metrics)
    extra_tweak = sum(w * 0.5 for w in weights)  # irrelevant adjustment
    noise_floor = 0.001 * len(weights)  # dead computation
    
    # Key logic: only stability index (last indicator) matters
    _, full_indicators = compute_health_indicators(metrics)
    raw_indicators, _ = compute_health_indicators(metrics)
    stability_component = raw_indicators[-1]
    
    # Final formula
    final = base_score + stability_component - 5.0
    return int(final)

# Main execution flow
diag_metrics = collect_diagnostics()
processed_data = apply_calibration(diag_metrics)
weights_config = [0.8, 1.2, 0.5, 1.0]  # unused except for distraction

# Critical statement
final_score = evaluate_performance(processed_data, weights_config)
print(f"Result: {final_score}")