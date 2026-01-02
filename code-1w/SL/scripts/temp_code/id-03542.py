import math

def collect_sensor_data():
    # Simulated sensor readings (some relevant, some red herrings)
    raw_data = {
        'temp_f': [72.1, 73.5, 71.8, 74.2, 75.0],
        'pressure_psi': [14.7, 14.6, 14.8, 14.5, 14.9],
        'humidity_pct': [45, 47, 46, 48, 44],
        'vibration_g': [0.12, 0.15, 0.11, 0.13, 0.16],
        'co2_ppm': [420, 435, 415, 450, 425],
        'light_lux': [300, 310, 295, 320, 305]  # Irrelevant for analysis
    }
    return raw_data

def filter_outliers(values, threshold=2.0):
    mean_val = sum(values) / len(values)
    std_dev = (sum((x - mean_val) ** 2 for x in values) / len(values)) ** 0.5
    return [v for v in values if abs(v - mean_val) <= threshold * std_dev]

def normalize_readings(data_list):
    min_val, max_val = min(data_list), max(data_list)
    if max_val == min_val:
        return [0.5 for _ in data_list]
    return [(x - min_val) / (max_val - min_val) for x in data_list]

def calculate_entropy(values):
    # Red herring function — looks important but unused in final logic
    value_counts = {}
    for v in values:
        bin_val = int(v * 10) // 1
        value_counts[bin_val] = value_counts.get(bin_val, 0) + 1
    total = len(values)
    return -sum((count / total) * math.log(count / total) for count in value_counts.values())

def smooth_signal(signal):
    # Unused smoothing function — distractor
    smoothed = [signal[0]]
    for i in range(1, len(signal) - 1):
        smoothed.append(sum(signal[i-1:i+2]) / 3)
    smoothed.append(signal[-1])
    return smoothed

def extract_trend(values):
    # Calculates trend slope using linear regression
    n = len(values)
    if n < 2:
        return 0.0
    sum_x, sum_y = sum(range(n)), sum(values)
    sum_xy = sum(i * values[i] for i in range(n))
    sum_x2 = sum(i * i for i in range(n))
    denominator = n * sum_x2 - sum_x * sum_x
    if denominator == 0:
        return 0.0
    return (n * sum_xy - sum_x * sum_y) / denominator

def compute_checksum(data_dict):
    # Decoy checksum — looks like integrity check but irrelevant
    chk = 0
    for key, vals in data_dict.items():
        chk ^= hash(key) % 100
        chk ^= int(sum(vals)) % 50
    return chk

def aggregate_metrics(filtered_data):
    # Process only relevant sensors
    metrics = {}
    for sensor, readings in filtered_data.items():
        if sensor in ['temp_f', 'pressure_psi', 'humidity_pct']:
            clean = filter_outliers(readings)
            normalized = normalize_readings(clean)
            trend = extract_trend(normalized)
            metrics[sensor] = {
                'mean': sum(clean) / len(clean),
                'trend': trend,
                'range': max(clean) - min(clean)
            }
        else:
            # Other sensors are ignored
            pass
    return metrics

def evaluate_stability(metric):
    # Stability score based on trend and range
    trend_weight = abs(metric['trend']) * 100
    range_penalty = metric['range'] * 0.5
    return 1.0 / (1.0 + trend_weight + range_penalty)

def analyze_readings(metrics, thresholds):
    # Final diagnostic computation
    stability_scores = []
    for sensor, m in metrics.items():
        score = evaluate_stability(m)
        stability_scores.append(score)
    
    # Core answer calculation
    base_score = sum(stability_scores) / len(stability_scores)
    adjustment_factor = 1.0
    if 'temp_f' in metrics and metrics['temp_f']['mean'] > 73.0:
        adjustment_factor += 0.1
    if 'pressure_psi' in metrics and metrics['pressure_psi']['trend'] < 0:
        adjustment_factor -= 0.05
    
    # Actual answer derivation
    final_index = int(base_score * 1000 * adjustment_factor)
    diagnostic_code = (final_index ^ 0xABC) + 17  # Bitwise manipulation
    return diagnostic_code

# Main execution flow
sensor_data = collect_sensor_data()

# Irrelevant transformation chain (dead path)
dummy_copy = {k: [x * 1.001 for x in v] for k, v in sensor_data.items()}
dummy_checksum = compute_checksum(dummy_copy)
entropy_check = {k: calculate_entropy(v) for k, v in sensor_data.items() if k != 'light_lux'}

# Real processing begins
processed_data = {}
for key, values in sensor_data.items():
    if key in ['temp_f', 'pressure_psi', 'humidity_pct', 'vibration_g']:
        filtered = filter_outliers(values)
        processed_data[key] = filtered

# Thresholds for decision logic (only partially used)
thresholds = {
    'temp_f': (70.0, 75.0),
    'pressure_psi': (14.5, 15.0),
    'stability_threshold': 0.85
}

# Additional distraction: unused clustering attempt
if 'vibration_g' in processed_data:
    vib_mean = sum(processed_data['vibration_g']) / len(processed_data['vibration_g'])
    high_vib = [v for v in processed_data['vibration_g'] if v > vib_mean]
    low_vib = [v for v in processed_data['vibration_g'] if v <= vib_mean]
    cluster_ratio = len(high_vib) / len(low_vib) if len(low_vib) > 0 else 0.0

# Critical assignment point
final_diagnostic = analyze_readings(processed_data, thresholds)

# Output result
print(f"Result: {final_diagnostic}")