from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_stream = [
    {'sensor': 'temp', 'value': 45, 'status': 'ok'},
    {'sensor': 'pressure', 'value': 102, 'status': 'ok'},
    {'sensor': 'temp', 'value': 50, 'status': 'warning'},
    {'sensor': 'flow', 'value': 75, 'status': 'ok'},
    {'sensor': 'temp', 'value': 60, 'status': 'critical'},
    {'sensor': 'pressure', 'value': 95, 'status': 'ok'},
    {'sensor': 'flow', 'value': 80, 'status': 'ok'}
]

# Irrelevant helper: counts status occurrences but not used in final logic
def count_status_events(data):
    counter = defaultdict(int)
    for event in data:
        counter[event['status']] += 1
    return counter

# Misleading preprocessing: computes averages but some are unused
sensor_avg = defaultdict(float)
sensor_count = defaultdict(int)
for entry in telemetry_stream:
    sensor = entry['sensor']
    sensor_avg[sensor] += entry['value']
    sensor_count[sensor] += 1

for s in sensor_avg:
    sensor_avg[s] /= sensor_count[s]

# Unused transformation: applies logarithmic scaling (distractor)
log_scaled = {s: math.log(v + 1) for s, v in sensor_avg.items()}

# Relevant metric data for evaluation
metric_data = {
    'temp': 60,
    'pressure': 102,
    'flow': 75
}

# Thresholds for performance bands
thresholds = {
    'temp': {'green': 55, 'yellow': 65},
    'pressure': {'green': 100, 'yellow': 110},
    'flow': {'green': 70, 'yellow': 85}
}

# Secondary distractor: frequency analysis of values (unused)
all_values = [e['value'] for e in telemetry_stream]
value_freq = Counter(all_values)
frequent_outliers = [v for v, cnt in value_freq.items() if cnt == 1 and v > 55]

# Bitwise diagnostic (red herring)
diag_flag = 0
for v in frequent_outliers:
    diag_flag ^= (v & 7) << 2

# Core evaluation logic with nested conditions
def evaluate_metric(value, green_thresh, yellow_thresh):
    if value <= green_thresh:
        return 10
    elif value <= yellow_thresh:
        return 7
    else:
        return 3

# Helper to check dominance (not actually used but looks relevant)
def is_dominant_sensor(data, target_sensor):
    totals = defaultdict(int)
    for e in data:
        totals[e['sensor']] += e['value']
    max_sensor = max(totals, key=totals.get)
    return max_sensor == target_sensor

# Main evaluation function
def evaluate_performance(metrics, limits):
    score = 0
    contributions = []
    
    # Real scoring logic
    for sensor, value in metrics.items():
        green = limits[sensor]['green']
        yellow = limits[sensor]['yellow']
        pts = evaluate_metric(value, green, yellow)
        contributions.append(pts)
        
        # Complex conditional weight (only some branches matter)
        base_weight = 1
        if sensor == 'temp' and value > green:
            base_weight += 1
        elif sensor == 'pressure' and value < green:
            base_weight += 0.5
        
        adjusted_pts = pts * base_weight
        score += adjusted_pts
    
    # Final nonlinear adjustment
    if sum(contributions) >= 20:
        score = int(score * 1.1)
    else:
        score = int(score * 0.95)
    
    return score

# Dead code path: simulates fallback mechanism (never triggered)
backup_weights = {'temp': 1.2, 'pressure': 1.0, 'flow': 0.9}
use_backup = False

# Critical execution point
final_score = evaluate_performance(metric_data, thresholds)

# Print result as required
print(f"Result: {final_score}")