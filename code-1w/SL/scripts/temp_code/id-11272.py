import math

def analyze_metrics(entries):
    totals = [e['value'] for e in entries]
    avg = sum(totals) / len(totals)
    variance = sum((x - avg) ** 2 for x in totals) / len(totals)
    std_dev = math.sqrt(variance)
    return avg, std_dev

# Simulate system health checks with irrelevant transformations
def transform_readings(readings):
    temp_offset = 273.15
    kelvin_vals = [r + temp_offset for r in readings]
    normalized = [(k - 273.15) / 100 for k in kelvin_vals]  # back to scaled Celsius
    noise_filter = [n for n in normalized if n > 0.1]
    return noise_filter  # not actually used later

# Auxiliary function for data calibration (partial red herring)
def calibrate_sensors(data_map):
    calibrated = {}
    adjustment_factor = 0.98
    for key, val in data_map.items():
        if val > 50:
            calibrated[key] = val * adjustment_factor
        else:
            calibrated[key] = val + 2
    checksum = sum(calibrated.values()) % 17  # irrelevant computation
    return calibrated

# Core logic obscured by auxiliary distractions
def calculate_performance(logs):
    base_points = 0
    penalty_count = 0
    bonus_tracker = []

    for record in logs:
        timestamp = record['ts']
        metric = record['metric']
        status = record['status']

        # Real logic begins
        if metric > 85:
            base_points += 3
            if status == 'stable':
                base_points += 2
        elif metric > 60:
            base_points += 1
            if 'recovery' in record:
                bonus_tracker.append(record['recovery'])
        else:
            penalty_count += 1

        # Distractor: tracking unused diagnostics
        debug_info = {'time': timestamp, 'impact': abs(metric - 70)}
        diagnostic_log = []
        diagnostic_log.append(debug_info)  # dead storage

    # Bonus logic
    extra_credit = 0
    if len(bonus_tracker) >= 2:
        extra_credit = sum([int(b * 0.1) for b in bonus_tracker])  # minor boost

    # Final score calculation — only this matters
    raw_score = base_points * 10 - penalty_count * 5 + extra_credit
    scaling_factor = 1.05
    final_score = int(raw_score * scaling_factor)

    # Irrelevant floating point residue
    residual_error = raw_score * 0.001
    correction_term = math.sin(residual_error)

    return final_score

# Input data with meaningful structure
benchmark_data = [
    {'ts': 1001, 'metric': 92, 'status': 'stable'},
    {'ts': 1002, 'metric': 68, 'status': 'active', 'recovery': 15},
    {'ts': 1003, 'metric': 45, 'status': 'lagging'},
    {'ts': 1004, 'metric': 88, 'status': 'stable', 'recovery': 8},
    {'ts': 1005, 'metric': 73, 'status': 'active', 'recovery': 12}
]

sensor_inputs = [22.5, 36.8, 41.0, 55.3]
data_registry = {'sensor_a': 67, 'sensor_b': 91, 'sensor_c': 44}

# Execute distractor functions
_ = transform_readings(sensor_inputs)
_ = calibrate_sensors(data_registry)
(avg_val, std_dev) = analyze_metrics(benchmark_data)

# Critical execution point
final_score = calculate_performance(benchmark_data)

print(f"Result: {final_score}")