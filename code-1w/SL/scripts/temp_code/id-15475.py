from collections import defaultdict, Counter
import math

# Irrelevant utility function (dead code path)
def normalize_vector(v):
    norm = sum(x ** 2 for x in v) ** 0.5
    return [x / norm for x in v]

# Misleading data transformation
temp_readings = [23.5, 24.1, 22.8, 25.0, 23.9]
adjusted_readings = [x + 0.5 for x in temp_readings if x < 24.0]
aggregate_temp = sum(adjusted_readings) / len(adjusted_readings) if adjusted_readings else 0

# Decoy metrics with no impact
device_status = {'sensor_a': 'active', 'sensor_b': 'idle', 'sensor_c': 'active'}
status_count = Counter(device_status.values())
redundant_flag = status_count['active'] > 1 and len(temp_readings) % 2 == 0

# Real computational path begins
baseline = {
    'threshold': 85.0,
    'weighting': 0.7,
    'penalty_rate': 0.05,
    'boost_factor': 1.2
}

metric_data = [
    {'name': 'throughput', 'value': 92.3, 'critical': True},
    {'name': 'latency', 'value': 78.1, 'critical': True},
    {'name': 'reliability', 'value': 88.7, 'critical': False},
    {'name': 'bandwidth', 'value': 64.5, 'critical': True}
]

# Distractor: unused list comprehension
evaluated = [m['value'] * 1.1 for m in metric_data if m['name'].startswith('b')]

# Another red herring: complex but unused calculation
shadow_score = 0
for i in range(len(temp_readings)):
    shadow_score += temp_readings[i] * math.sin(i + 1)
shadow_score = round(shadow_score, 2)

# Real logic buried among noise
def calculate_metric_contribution(val, thresh, weight, boost, critical):
    if val >= thresh:
        return weight * boost if critical else weight
    else:
        penalty = (thresh - val) * baseline['penalty_rate']
        return max(0, weight - penalty)

# Misdirection via tuple unpacking
config_keys = list(baseline.keys())
config_vals = list(baseline.values())
_, weight_val, _, boost_val = config_vals  # Only two used

# Early return decoy
early_exit_mode = False
def process_chain(data):
    if early_exit_mode:
        return 0  # Never executed
    return sum(d['value'] for d in data if d['critical'])

# Unused recursive function (distractor)
def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

# Core evaluation logic hidden in complexity
def evaluate_performance(metrics, base):
    total_score = 50.0  # Base score
    threshold = base['threshold']
    weighting = base['weighting']
    boost_factor = base['boost_factor']

    # Simulated calibration offset (irrelevant but plausible)
    calibration_log = defaultdict(int)
    for m in metrics:
        key = m['name'][0]
        calibration_log[key] += 1

    # Real scoring loop
    for metric in metrics:
        raw = metric['value']
        crit = metric['critical']
        contrib = calculate_metric_contribution(raw, threshold, weighting, boost_factor, crit)
        if raw >= threshold:
            total_score += contrib
        else:
            total_score -= (threshold - raw) * 0.1

    # Final adjustment using string-derived factor (plausible distraction)
    tag = "perf_metrics_v2"
    version_digit = int(tag[-1])
    if version_digit % 2 == 0:
        total_score *= 1.05

    return int(total_score)  # Discrete final answer

# Key execution point
final_score = evaluate_performance(metric_data, baseline)
print(f"Result: {final_score}")