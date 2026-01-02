from collections import defaultdict
import math

# Simulate sensor data aggregation and performance scoring in an autonomous drone system
def collect_diagnostics():
    diagnostics = defaultdict(lambda: 0)
    diagnostics['voltage'] = 12.4
    diagnostics['current_draw'] = 3.8
    diagnostics['temperature'] = 67
    diagnostics['packet_loss'] = 0.04
    diagnostics['uptime'] = 1420
    return diagnostics

def preprocess_metrics(raw):
    processed = {}
    # Relevant transformations
    processed['power_efficiency'] = raw['voltage'] * raw['current_draw']
    processed['thermal_stress'] = max(0, raw['temperature'] - 50) / 50
    processed['signal_integrity'] = 1 - raw['packet_loss']
    processed['lifespan_utilization'] = min(1, raw['uptime'] / 3600)
    
    # Distractor computations (not used later)
    processed['apparent_power'] = raw['voltage'] * raw['current_draw'] * 1.1
    processed['reactive_power'] = processed['apparent_power'] * 0.3
    processed['phase_angle'] = math.atan(processed['reactive_power'] / processed['power_efficiency'])
    
    return processed

def calculate_health_index(data):
    # This function is defined but not used — red herring
    base = 100
    for key in ['thermal_stress', 'packet_loss']:
        if key in data:
            base -= data[key] * 10
    return base

def apply_calibration(values, mode='standard'):
    calibrated = {}
    # Only some keys are actually used later
    calibration_map = {
        'power_efficiency': lambda x: x * 0.88,
        'thermal_stress': lambda x: min(1, x * 1.1),
        'signal_integrity': lambda x: x ** 0.95,
        'lifespan_utilization': lambda x: x,
        'phase_angle': lambda x: math.degrees(x)  # distractor
    }
    for k, v in values.items():
        if k in calibration_map:
            calibrated[k] = calibration_map[k](v)
        else:
            calibrated[k] = v
    return calibrated

def aggregate_risk_factors(calib):
    risk = 0.0
    # Bitwise simulation of fault flags (for show)
    fault_code = 0
    if calib['thermal_stress'] > 0.3:
        fault_code |= 1  # bit 0
    if 1 - calib['signal_integrity'] > 0.1:
        fault_code |= 2  # bit 1
    if fault_code & 1 and fault_code & 2:
        risk += 0.1
    # Actual risk logic (simplified)
    risk += calib['thermal_stress'] * 0.3
    risk += (1 - calib['signal_integrity']) * 0.4
    return risk, fault_code

def evaluate_performance(metrics, weights):
    score = 0.0
    weight_sum = sum(weights.values())
    for k, w in weights.items():
        if k in metrics:
            score += metrics[k] * (w / weight_sum)
    # Additional adjustment based on risk
    risk_level, _ = aggregate_risk_factors(metrics)
    score *= (1 - risk_level)  # performance penalty
    return int(score * 100)  # scale to integer

# Main execution flow
raw_data = collect_diagnostics()
base_metrics = preprocess_metrics(raw_data)
# Dead code path — misleading function call
health_status = {'code': 0, 'level': 'nominal'}  # unused structure

# Calibrate relevant metrics
calibrated_metrics = apply_calibration(base_metrics)

# Define weighting scheme for final evaluation
weights = {
    'power_efficiency': 0.4,
    'thermal_stress': 0.3,
    'signal_integrity': 0.3,
    'lifespan_utilization': 0.1  # over-defined; not all used proportionally
}

# Introduce irrelevant set operations (distractor)
data_keys = set(base_metrics.keys())
expected_keys = {'power_efficiency', 'thermal_stress', 'signal_integrity', 'lifespan_utilization'}
missing = expected_keys - data_keys
extra = data_keys - expected_keys
consistency_check = len(missing) == 0

# Lambda for dynamic threshold (semi-relevant)
is_stable = lambda x: 1 if x['thermal_stress'] < 0.5 and x['signal_integrity'] > 0.9 else 0.8
stability_bonus = is_stable(calibrated_metrics)

# Final scoring
final_score = evaluate_performance(calibrated_metrics, weights)
final_score = int(final_score * stability_bonus)  # apply bonus

print(f"Result: {final_score}")