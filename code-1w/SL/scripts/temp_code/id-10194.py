from collections import defaultdict, Counter
import math

# Simulated sensor data aggregation (real and decoy)
sensor_readings = [
    [1.2, 0.9, 1.3, 1.1, 0.8],
    [2.4, 2.6, 2.3, 2.5, 2.7],
    [0.5, 0.7, 0.6, 0.8, 0.9],
    [3.1, 3.3, 3.0, 3.2, 3.4]
]

# Irrelevant auxiliary data (distractor)
aux_logs = [
    {'event': 'calibration', 'value': 0.01},
    {'event': 'reset', 'value': 0.0},
    {'event': 'debug', 'value': 0.05}
]

# Real health metrics indexed by system component
health_data = {
    'core_temp': [78.3, 79.1, 77.5, 78.9, 79.0],
    'voltage_rails': [3.28, 3.31, 3.29, 3.33, 3.30],
    'fan_speed': [1420, 1450, 1410, 1460, 1440],
    'power_draw': [86.4, 87.1, 85.9, 87.5, 88.0]
}

# Thresholds for anomaly detection (used in logic)
thresholds = defaultdict(lambda: (0, 100))
thresholds['core_temp'] = (75.0, 80.0)
thresholds['voltage_rails'] = (3.25, 3.40)
thresholds['fan_speed'] = (1400, 1500)
thresholds['power_draw'] = (85.0, 88.5)

# Decoy transformation (never used but looks relevant)
def transform_signal(data, factor=1.05):
    return [x * factor for x in data]

# Unused recursive function (red herring)
def calculate_entropy(seq, depth=0):
    if depth > 3 or len(seq) == 0:
        return 0.0
    p = Counter(seq)
    return sum(- (count/len(seq)) * math.log2(count/len(seq)) for count in p.values())

# Bit manipulation decoy (simulates checksum but unused)
def compute_checksum(arr):
    chk = 0
    for val in arr:
        chk ^= int(val * 100) & 0xFF
    return chk << 1

# Real processing pipeline
smoothing_factor = 0.85
anomaly_weights = {'core_temp': 2.0, 'voltage_rails': 1.5, 'fan_speed': 1.0, 'power_draw': 1.8}

# Intermediate diagnostic states (some are distractions)
baseline_shift = {}
for key, values in health_data.items():
    baseline_shift[key] = sum(values[:2]) / 2 - sum(values[-2:]) / 2

# Simulate historical drift (unused in final logic)
historical_drift = {}
for key in health_data:
    historical_drift[key] = (health_data[key][-1] - health_data[key][0]) / len(health_data[key])

# Core metric processor (key logic)
def evaluate_stability(metric, readings, limits):
    avg = sum(readings) / len(readings)
    deviation = abs(avg - ((limits[0] + limits[1]) / 2))
    tolerance = (limits[1] - limits[0]) / 2
    return deviation <= tolerance

# Secondary validator (looks important, only partially used)
def validate_consistency(series, window=3):
    trends = []
    for i in range(len(series) - window + 1):
        sub = series[i:i+window]
        trend = 'up' if sub[-1] > sub[0] else 'down' if sub[-1] < sub[0] else 'stable'
        trends.append(trend)
    return Counter(trends).get('stable', 0)

# Main processing function with lambda abstraction
aggregation_rule = lambda x, w: sum(a*b for a, b in zip(x, w)) / sum(w) if sum(w) > 0 else 0

def process_metrics(metrics, bounds):
    scores = []
    # Critical evaluation path
    for name, data in metrics.items():
        low, high = bounds[name]
        avg_val = sum(data) / len(data)
        in_bounds = 1 if low <= avg_val <= high else 0
        fluctuation = max(data) - min(data)
        stability_score = 1 if fluctuation < (high - low) * 0.25 else 0
        # Only in_bounds is actually used in final calculation
        scores.append(in_bounds * anomaly_weights.get(name, 1.0))
    
    # Dead code branch - never executed due to prior logic
    extreme_outliers = []
    for d in sensor_readings:
        if max(d) > 3.0:
            extreme_outliers.append(compute_checksum(d))  # unreachable in practice
    
    # Final weighted aggregation using only the in-bounds status
    final_score = aggregation_rule(scores, list(anomaly_weights.values()))
    
    # Diagnostic override simulation (looks complex but bypassed)
    override_flag = False
    for log in aux_logs:
        if log['value'] > 0.04:
            override_flag = True
    # This condition is never met; override ignored
    if override_flag and final_score < 1.5:
        final_score *= 1.2
    
    # Key result computation
    diagnostic_code = int(round(final_score * 100))
    return diagnostic_code

# Execution point of interest
final_diagnostic = process_metrics(health_data, thresholds)
print(f"Result: {final_diagnostic}")