from collections import defaultdict, Counter
import itertools

# Simulated health monitoring system with sensor fusion logic
def analyze_risk_level(vital_signs, baseline):
    risk_counter = defaultdict(int)
    for metric, (current, normal) in zip(vital_signs.keys(), vital_signs.values()):
        deviation = abs(current - normal)
        if deviation > 0.2 * normal:
            risk_counter[metric] += 1
    return sum(risk_counter.values())

# Irrelevant helper: dead code path
def deprecated_normalization(data):
    return [x / max(data) for x in data]

# Sensor calibration routine (partially relevant)
def calibrate_sensors(raw_readings):
    calibrated = {}
    for sensor_id, readings in raw_readings.items():
        offset = sum(readings[:3]) / 3 - 1.0  # Baseline adjustment
        calibrated[sensor_id] = [round(x - offset, 3) for x in readings]
    return calibrated

# Data alignment function using slicing
def align_time_series(data, ref_key='ECG'):
    min_len = min(len(v) for v in data.values())
    trimmed = {k: v[-min_len:] for k, v in data.items()}  # Slicing to common length
    return {k: v for k, v in trimmed.items() if k != 'debug_trace'}  # Exclude debug

# Main processing pipeline
def compute_stability_index(ts_data):
    stability = {}
    for metric, values in ts_data.items():
        diffs = [abs(a - b) for a, b in itertools.pairwise(values)]
        stability[metric] = round(sum(diffs) / len(diffs), 4) if diffs else 0.0
    return stability

# Secondary scoring (distractor)
def calculate_efficiency_ratio(stability, weights):
    total_weight = sum(weights.values())
    efficiency = sum(stability.get(k, 0) * w for k, w in weights.items()) / total_weight
    return round(efficiency, 4)

# Core logic disguised among distractors
def derive_anomaly_flags(stability, thresholds):
    flags = []
    for metric, value in stability.items():
        if value > thresholds.get(metric, 0.5):
            flags.append(hash(metric) % 100)  # Non-linear flag encoding
    return flags

# Final aggregation with decoy parameters
def process_metrics(sensor_data, config_map, mode='primary', scale_factor=1.87):
    # Step 1: Calibrate raw inputs
    calibrated = calibrate_sensors(sensor_data)
    
    # Step 2: Align time-series across sensors
    aligned = align_time_series(calibrated)
    
    # Step 3: Compute stability per metric
    stability_index = compute_stability_index(aligned)
    
    # Step 4: Generate anomaly flags (key step)
    thresholds = {k: v['anomaly_threshold'] for k, v in config_map.items()}
    anomalies = derive_anomaly_flags(stability_index, thresholds)
    
    # Step 5: Risk analysis on baseline deviation (red herring)
    baseline_vitals = {k: (aligned[k][0], config_map[k]['normal_range'][1]) for k in aligned}
    risk_level = analyze_risk_level(baseline_vitals, {'HR': 70})
    
    # Step 6: Efficiency calculation (dead-end computation)
    weights = {k: v['weight'] for k, v in config_map.items()}
    _efficiency = calculate_efficiency_ratio(stability_index, weights)  # Unused
    
    # Step 7: Hidden logic path - sum of squared anomaly hashes mod 10000
    if len(anomalies) >= 3:
        secret_bias = sum(x**2 for x in anomalies[:3]) % 5000
    else:
        secret_bias = len(anomalies) * 100
    
    # Step 8: Final score computed from multiple paths
    base_score = sum(stability_index.values()) * 100
    adjustment = config_map.get('RR', {}).get('weight', 1) * risk_level
    final_score = int(base_score - adjustment + secret_bias)
    
    # Debug print that mimics importance (distraction)
    debug_info = {"base": base_score, "adj": adjustment, "bias": secret_bias}
    
    return final_score

# --- Simulation Setup ---
if __name__ == "__main__":
    # Real sensor inputs
    raw_health_data = {
        'HR': [1.05, 1.08, 1.07, 1.12, 1.18, 1.15],
        'RR': [0.98, 0.95, 0.97, 1.02, 1.05, 1.03],
        'SpO2': [1.01, 1.03, 1.02, 1.04, 1.06, 1.05],
        'ECG': [0.92, 0.89, 0.93, 0.97, 1.02, 1.00],
        'debug_trace': [0, 0, 0]  # Will be filtered out
    }
    
    # Configuration map with mixed relevance
    threshold_map = {
        'HR': {'anomaly_threshold': 0.04, 'weight': 2, 'normal_range': (60, 80)},
        'RR': {'anomaly_threshold': 0.03, 'weight': 3, 'normal_range': (12, 20)},
        'SpO2': {'anomaly_threshold': 0.05, 'weight': 1, 'normal_range': (95, 100)},
        'ECG': {'anomaly_threshold': 0.035, 'weight': 4, 'normal_range': (0.9, 1.1)}
    }
    
    # Trigger main computation
    final_score = process_metrics(raw_health_data, threshold_map)
    
    # Output result as required
    print(f"Result: {final_score}")