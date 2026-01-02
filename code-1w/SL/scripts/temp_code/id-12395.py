from collections import defaultdict, Counter
import math

# Simulated sensor data aggregation (irrelevant but realistic)
sensor_nodes = ['temp_1', 'temp_2', 'pressure_a', 'pressure_b', 'flow_x']
raw_readings = {
    'temp_1': [23.4, 24.1, 25.0, 23.9, 24.5],
    'temp_2': [26.7, 25.8, 27.1, 26.3, 26.9],
    'pressure_a': [101.2, 102.5, 101.8, 103.1, 102.7],
    'pressure_b': [98.4, 99.1, 97.9, 98.8, 99.5],
    'flow_x': [12.1, 11.8, 12.5, 12.3, 11.9]
}

# Irrelevant statistical summary (distractor)
def compute_skew(data):
    n = len(data)
    mean_val = sum(data) / n
    variance = sum((x - mean_val)**2 for x in data) / n
    if variance == 0:
        return 0.0
    std_dev = math.sqrt(variance)
    skewness = sum((x - mean_val)**3 for x in data) / (n * std_dev**3)
    return round(skewness, 4)

# Unused anomaly detection heuristic (dead code path)
def detect_spikes(values, multiplier=2.5):
    median_val = sorted(values)[len(values)//2]
    mad = sorted([abs(x - median_val) for x in values])[len(values)//2]
    threshold = multiplier * mad
    return [i for i, x in enumerate(values) if abs(x - median_val) > threshold]

# Misleading normalization function that isn't used in main logic
def normalize_to_range(data, new_min=-1, new_max=1):
    old_min, old_max = min(data), max(data)
    if old_min == old_max:
        return [0 for _ in data]
    return [(x - old_min) / (old_max - old_min) * (new_max - new_min) + new_min for x in data]

# Core processing pipeline with relevant logic buried inside
def extract_trend_signature(readings_list):
    smoothed = []
    for i in range(2, len(readings_list)):
        avg = (readings_list[i-2] + readings_list[i-1] + readings_list[i]) / 3
        smoothed.append(avg)
    if not smoothed:
        return [0]
    return [round(x, 2) for x in smoothed]

# Distractor: complex state tracker never actually utilized
class StatefulAnalyzer:
    def __init__(self, name):
        self.name = name
        self.history = []
        self.alert_level = 0
    
    def update(self, value):
        self.history.append(value)
        if value > 100:
            self.alert_level += 1

# Real but obscured core logic
def evaluate_stability_metric(series):
    if len(series) < 2:
        return 0.0
    diffs = [abs(series[i+1] - series[i]) for i in range(len(series)-1)]
    return round(sum(diffs) / len(diffs), 3)

# Mapping of system components to critical thresholds (partially relevant)
threshold_map = defaultdict(lambda: 1.0)
threshold_map.update({
    'core_temp': 0.8,
    'pressure_diff': 1.2,
    'flow_variability': 0.5
})

# Simulated processed health features (mix of relevant and irrelevant)
health_data = {
    'core_temp': extract_trend_signature(raw_readings['temp_1'] + raw_readings['temp_2']),
    'pressure_diff': extract_trend_signature([abs(a-b) for a,b in zip(raw_readings['pressure_a'], raw_readings['pressure_b'])]),
    'flow_variability': [12.1, 11.8, 12.3, 11.9],  # Simplified flow data
    'aux_metrics': {'vibration': [0.3, 0.4, 0.3, 0.5], 'humidity': [45, 47, 46, 48]}  # Unused
}

# Secondary transformation with red herring output
transformed_diagnostics = {}
for key, values in health_data.items():
    if isinstance(values, list) and key != 'aux_metrics':
        stability_score = evaluate_stability_metric(values)
        transformed_diagnostics[key] = {
            'score': stability_score,
            'length': len(values),
            'warning': stability_score > threshold_map[key]
        }

# Decoy aggregation using set operations (irrelevant)
available_sensors = set(sensor_nodes)
active_monitoring = {s for s in available_sensors if 'temp' in s or 'pressure' in s}
disconnected = available_sensors - active_monitoring
redundant_paths = active_monitoring & {f'backup_{s}' for s in sensor_nodes}

# Critical function containing the actual answer derivation
def process_metrics(metrics, thresholds):
    # Extract only needed components
    temp_stability = metrics['core_temp']
    pressure_trend = metrics['pressure_diff']
    
    # Real computation chain begins here
    temp_variance = evaluate_stability_metric(temp_stability)
    pressure_change_rate = evaluate_stability_metric(pressure_trend)
    
    # Hidden intermediate step: composite risk index
    risk_components = []
    if temp_variance > thresholds['core_temp']:
        risk_components.append(temp_variance * 10)
    if pressure_change_rate > thresholds['pressure_diff']:
        risk_components.append(pressure_change_rate * 8)
    
    # Secret logic: XOR-based fusion of metric lengths (bit manipulation distractor)
    len_temp = len(temp_stability)
    len_pressure = len(pressure_trend)
    obfuscation_key = (len_temp ^ len_pressure) << 2  # Bitwise red herring
    
    # Actual answer calculation (non-obvious due to distractions)
    base_score = 500
    adjustment = 0
    if risk_components:
        adjustment = int(sum(risk_components) * (-1 if len(risk_components) % 2 == 0 else 1))
    
    # Final deterministic result derived from specific conditions
    final_value = base_score + adjustment - obfuscation_key
    
    # Answer is formed here through conditional arithmetic
    return final_value

# Execution point of interest
final_diagnostic = process_metrics(health_data, threshold_map)

# Print required output
print(f"Result: {final_diagnostic}")