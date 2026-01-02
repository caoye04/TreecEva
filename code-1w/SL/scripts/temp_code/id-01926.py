from collections import defaultdict, Counter
import math

# Simulated sensor telemetry data over time
log_data = [
    {'sensor': 'temp', 'value': 45.2, 'status': 'active', 'time': 1},
    {'sensor': 'pressure', 'value': 101.3, 'status': 'active', 'time': 1},
    {'sensor': 'temp', 'value': 47.8, 'status': 'active', 'time': 2},
    {'sensor': 'flow', 'value': 12.1, 'status': 'active', 'time': 2},
    {'sensor': 'pressure', 'value': 99.7, 'status': 'active', 'time': 3},
    {'sensor': 'temp', 'value': 53.1, 'status': 'active', 'time': 3},
    {'sensor': 'flow', 'value': 11.9, 'status': 'degraded', 'time': 3},
    {'sensor': 'temp', 'value': 56.3, 'status': 'active', 'time': 4},
    {'sensor': 'pressure', 'value': 102.1, 'status': 'active', 'time': 4},
    {'sensor': 'flow', 'value': 0.0, 'status': 'failed', 'time': 4},  # Sensor failure
]

# Thresholds for anomaly detection
thresholds = {
    'temp_high': 55.0,
    'temp_low': 35.0,
    'pressure_high': 103.0,
    'pressure_low': 95.0,
    'flow_min': 1.0
}

# Irrelevant baseline model (distractor)
def legacy_calibrate(x):
    return (x * 0.98) + 0.5

# Unused fault injection table (red herring)
fault_matrix = [[0 for _ in range(5)] for _ in range(5)]
for i in range(5):
    for j in range(5):
        fault_matrix[i][j] = (i ** 2 + j * 3) % 7

# Decoy function that appears useful but isn't used
def compute_entropy(values):
    counts = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

# Misleading intermediate aggregation (unused)
temp_snapshot = []
for entry in log_data:
    if entry['sensor'] == 'temp':
        temp_snapshot.append(entry['value'])
snapshot_avg = sum(temp_snapshot) / len(temp_snapshot) if temp_snapshot else 0

# Real processing begins here
def extract_series(data, sensor_type):
    return [entry['value'] for entry in data if entry['sensor'] == sensor_type]

def count_failures(data, sensor_type):
    return sum(1 for entry in data if entry['sensor'] == sensor_type and entry['status'] == 'failed')

def analyze_trend(values):
    if len(values) < 2:
        return 0
    return sum(1 for i in range(1, len(values)) if values[i] > values[i-1])

def validate_pressure_stability(pressure_vals, threshold_window=2.0):
    return max(pressure_vals) - min(pressure_vals) <= threshold_window

# Heavily nested diagnostic engine with distractors
def process_metrics(data, limits):
    # Group data by sensor using defaultdict (relevant)
    grouped = defaultdict(list)
    status_log = defaultdict(list)
    for record in data:
        grouped[record['sensor']].append(record['value'])
        status_log[record['sensor']].append(record['status'])
    
    # Spurious transformation (distraction)
    transformed = {}
    for k, v in grouped.items():
        transformed[k] = [x + math.sin(i) for i, x in enumerate(v)]
    
    # Fake normalization layer (dead code path)
    normalized = {}
    base_ref = {'temp': 40, 'pressure': 100, 'flow': 10}
    for k, vals in grouped.items():
        offset = base_ref.get(k, 0)
        normalized[k] = [max(0, (x - offset) * 1.1) for x in vals]
    
    # Begin actual diagnosis
    diagnostics = []
    
    # Temperature analysis
    temp_vals = grouped['temp']
    temp_high_count = sum(1 for v in temp_vals if v > limits['temp_high'])
    temp_trend = analyze_trend(temp_vals)
    temp_alert = temp_high_count > 0 and temp_trend >= 2
    diagnostics.append(30 if temp_alert else 0)
    
    # Pressure analysis
    pressure_vals = grouped['pressure']
    pressure_stable = validate_pressure_stability(pressure_vals)
    pressure_outliers = sum(1 for v in pressure_vals if v < limits['pressure_low'] or v > limits['pressure_high'])
    pressure_score = 20 if not pressure_stable or pressure_outliers > 0 else 0
    diagnostics.append(pressure_score)
    
    # Flow analysis with status dependency
    flow_vals = extract_series(data, 'flow')
    flow_failures = count_failures(data, 'flow')
    flow_valid = [v for v in flow_vals if v >= limits['flow_min']]
    flow_ratio = len(flow_valid) / len(flow_vals) if flow_vals else 0
    
    # Complex conditional expression (key step)
    flow_diagnostic = 50 if flow_failures > 0 else (10 if flow_ratio < 0.5 else 0)
    diagnostics.append(flow_diagnostic)
    
    # Hidden dependency: correlation between rising temp and pressure deviation
    zipped_readings = list(zip(temp_vals[:len(pressure_vals)], pressure_vals))
    correlated_spikes = 0
    for t, p in zipped_readings:
        high_temp = t > limits['temp_high']
        unstable_pressure = p < limits['pressure_low'] or p > limits['pressure_high']
        if high_temp and unstable_pressure:
            correlated_spikes += 1
    
    # Critical interference: this block looks important but is unused
    safety_audit = []
    for i, (t, p) in enumerate(zipped_readings):
        risk_factor = (t - 40) * (abs(p - 101.3) / 10)
        adjusted_risk = risk_factor * (0.95 ** i)
        safety_audit.append(adjusted_risk)
    
    # Final scoring logic (actual answer source)
    base_risk = sum(diagnostics)
    multiplier = 1.0
    if correlated_spikes >= 1:
        multiplier = 1.8  # Amplifies due to correlated failure risk
    final_risk = base_risk * multiplier
    
    # One last red herring: bit manipulation on unrelated metric
    debug_flag = 0
    for val in temp_vals:
        debug_flag ^= int(val) & 0xF
    debug_flag = (debug_flag << 2) | (debug_flag >> 2)
    
    # The true result
    final_diagnostic = int(round(final_risk))
    return final_diagnostic

# Execution point of interest
final_diagnostic = process_metrics(log_data, thresholds)
print(f"Result: {final_diagnostic}")