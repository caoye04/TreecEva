from collections import defaultdict, Counter
import math

# Simulated sensor data ingestion (real and dummy)
sensor_readings = [
    {'id': 'S1', 'type': 'thermal', 'values': [23.4, 24.1, 25.0, 26.2, 25.8]},
    {'id': 'S2', 'type': 'pressure', 'values': [101.3, 102.1, 101.8, 103.0, 102.7]},
    {'id': 'S3', 'type': 'thermal', 'values': [22.9, 23.1, 24.0, 25.2, 24.8]},
    {'id': 'S4', 'type': 'humidity', 'values': [45.0, 47.2, 48.1, 46.5, 49.0]},
    {'id': 'S5', 'type': 'pressure', 'values': [100.9, 101.5, 102.3, 101.7, 102.0]}
]

# Irrelevant aggregation: total readings per sensor (unused later)
total_readings_per_sensor = {entry['id']: len(entry['values']) for entry in sensor_readings}

# Misleading intermediate: average across all sensors without type distinction (dead end)
all_values_flat = [val for entry in sensor_readings for val in entry['values']]
global_mean = sum(all_values_flat) / len(all_values_flat)
global_variance = sum((x - global_mean) ** 2 for x in all_values_flat) / len(all_values_flat)

# Relevant: group by type
sensor_data_by_type = defaultdict(list)
for entry in sensor_readings:
    sensor_data_by_type[entry['type']].append(entry['values'])

# Dead code path: unused transformation function
def transform_log_scale(data):
    return [math.log(x + 1) for x in data if x > 0]

# Unused statistical decoy: compute skewness but never used
def compute_skewness(data):
    n = len(data)
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / n
    if variance == 0:
        return 0.0
    std_dev = math.sqrt(variance)
    skew = sum(((x - mean) / std_dev) ** 3 for x in data) / n
    return skew

# Real processing begins: normalize each type's data to z-scores and flatten
def normalize_to_zscores(values_list_2d):
    flat = [val for sublist in values_list_2d for val in sublist]
    mean = sum(flat) / len(flat)
    std = math.sqrt(sum((x - mean) ** 2 for x in flat) / len(flat))
    if std == 0:
        return [0.0] * len(flat)
    return [(x - mean) / std for x in flat]

normalized_thermal = normalize_to_zscores(sensor_data_by_type['thermal'])
normalized_pressure = normalize_to_zscores(sensor_data_by_type['pressure'])

# Distractor: process humidity but it won't be used in final analysis
normalized_humidity = normalize_to_zscores(sensor_data_by_type['humidity'])
humidity_consistency_score = sum(1 for x in normalized_humidity if abs(x) < 1.0)

# Composite metric: difference in spread between thermal and pressure
thermal_mad = sum(abs(x) for x in normalized_thermal) / len(normalized_thermal)  # MAD around 0
pressure_mad = sum(abs(x) for x in normalized_pressure) / len(normalized_pressure)
spread_ratio = thermal_mad / pressure_mad if pressure_mad != 0 else float('inf')

# Simulate fault detection heuristics with lambda filters
abnormal_threshold = lambda x: abs(x) > 1.5
thermal_anomalies = list(filter(abnormal_threshold, normalized_thermal))
pressure_anomalies = list(filter(abnormal_threshold, normalized_pressure))

# Compute anomaly density per original sensor (reconstruct mapping)
anomaly_density_map = {}
cumulative_idx_t = 0
cumulative_idx_p = 0
for entry in sensor_readings:
    if entry['type'] == 'thermal':
        segment_length = len(entry['values'])
        segment_anomalies = normalized_thermal[cumulative_idx_t:cumulative_idx_t + segment_length]
        density = sum(1 for x in segment_anomalies if abs(x) > 1.5) / segment_length
        anomaly_density_map[entry['id']] = density
        cumulative_idx_t += segment_length
    elif entry['type'] == 'pressure':
        segment_length = len(entry['values'])
        segment_anomalies = normalized_pressure[cumulative_idx_p:cumulative_idx_p + segment_length]
        density = sum(1 for x in segment_anomalies if abs(x) > 1.5) / segment_length
        anomaly_density_map[entry['id']] = density
        cumulative_idx_p += segment_length

# Red herring: count transitions in dummy binary sequence (unrelated)
dummy_signal = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]
transition_count = sum(1 for i in range(1, len(dummy_signal)) if dummy_signal[i] != dummy_signal[i-1])

# Processed data structure: only this will be used in final step
processed_data = {
    'thermal_spread': thermal_mad,
    'pressure_spread': pressure_mad,
    'anomaly_ratio': len(thermal_anomalies + pressure_anomalies) / (len(normalized_thermal) + len(normalized_pressure)),
    'sensor_coverage': len([t for t in sensor_data_by_type.keys() if t in ['thermal', 'pressure']]),
    'consistency_factor': spread_ratio
}

# Decoy function that looks important but isn't called
def calculate_system_integrity(raw_data, weights=None):
    if weights is None:
        weights = {'thermal': 0.4, 'pressure': 0.6}
    score = 0.0
    for entry in raw_data:
        avg = sum(entry['values']) / len(entry['values'])
        score += avg * weights.get(entry['type'], 0.1)
    return round(score, 3)

# Core analysis function: computes diagnostic from processed features
def analyze_metrics(metrics):
    base_score = metrics['thermal_spread'] * 100
    penalty = metrics['anomaly_ratio'] * 50
    bonus = (4 - metrics['sensor_coverage']) * 10  # inverse incentive
    adjustment = math.floor(metrics['consistency_factor'] * 5)  # integer influence
    # Final formula
    result = base_score - penalty + bonus + adjustment
    return int(round(result))

# Critical execution point
final_diagnostic = analyze_metrics(processed_data)
print(f"Target result: {final_diagnostic}")