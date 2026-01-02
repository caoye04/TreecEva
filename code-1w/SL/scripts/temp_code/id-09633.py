from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_stream = [
    {'sensor': 'temp', 'value': 72.5, 'status': 'ok'},
    {'sensor': 'pressure', 'value': 45.1, 'status': 'warning'},
    {'sensor': 'temp', 'value': 73.0, 'status': 'ok'},
    {'sensor': 'flow', 'value': 12.8, 'status': 'ok'},
    {'sensor': 'pressure', 'value': 47.3, 'status': 'critical'},
    {'sensor': 'temp', 'value': 71.9, 'status': 'ok'},
    {'sensor': 'flow', 'value': 13.1, 'status': 'ok'}
]

# Irrelevant helper function (decoy)
def calculate_efficiency(index, base):
    if index == 0:
        return 0.0
    efficiency = (base / (index + 1)) * math.sin(index)
    adjusted = efficiency * 1.5 if efficiency > 0 else efficiency * 0.5
    return round(adjusted, 3)

# Unused transformation map (dead code path)
sensor_transform_map = {
    'temp': lambda x: (x - 32) * 5/9,
    'pressure': lambda x: x * 6.894757,
    'flow': lambda x: x * 0.06309
}

# Misleading accumulator (looks important but unused in final result)
cumulative_risk_score = 0.0
risk_weights = {'ok': 0, 'warning': 10, 'error': 25, 'critical': 50}
for entry in telemetry_stream:
    cumulative_risk_score += risk_weights.get(entry['status'], 0) * 0.3

cumulative_risk_score = round(cumulative_risk_score, 4)  # Distractor variable

# Data aggregation phase
raw_observations = defaultdict(list)
status_counter = Counter()

for record in telemetry_stream:
    raw_observations[record['sensor']].append(record['value'])
    status_counter[record['status']] += 1

# Compute summary statistics (some used, some not)
summary_stats = {}
for sensor, values in raw_observations.items():
    avg = sum(values) / len(values)
    peak = max(values)
    variance = sum((v - avg) ** 2 for v in values) / len(values)
    summary_stats[sensor] = {
        'average': round(avg, 3),
        'peak': peak,
        'variance': round(variance, 4),
        'trend': 'rising' if values[-1] > values[0] else 'falling'
    }

# Secondary processing log (partially used)
performance_log = []
for sensor_type in ['temp', 'pressure', 'flow']:
    if sensor_type in summary_stats:
        stat = summary_stats[sensor_type]
        score = 100 - (stat['variance'] * 2) if stat['variance'] < 20 else 60
        performance_log.append({
            'component': sensor_type,
            'stability_score': int(score),
            'deviation_level': 'low' if stat['variance'] < 1.5 else 'high'
        })

# System state initialization
system_state = {
    'uptime_hours': 8761,
    'core_temperature': 72.8,
    'calibration_cycle': True,
    'pending_alerts': status_counter['warning'] + status_counter['critical'],
    'last_reboot_cause': 'overheat' if status_counter['critical'] > 0 else 'scheduled'
}

# Red herring: unused recursive function
def predict_failure_risk(depth, current_risk=0.0):
    if depth <= 1:
        return current_risk
    new_risk = current_risk + (1.0 / depth) * 15
    return predict_failure_risk(depth - 1, new_risk)

# Actual analysis logic chain
intermediate_flags = []
for log_entry in performance_log:
    stability = log_entry['stability_score']
    if stability < 70:
        intermediate_flags.append(1)
    else:
        intermediate_flags.append(0)

flag_sum = sum(intermediate_flags)
base_diagnostic = 1000 - (flag_sum * 125)

# Conditional expression with bit manipulation twist
adjustment_factor = 0.9 if system_state['pending_alerts'] else 1.1
bit_encoded = (flag_sum << 3) | 7  # XOR-like pattern with OR

# Final computation using conditional expression and arithmetic
final_diagnostic = base_diagnostic * adjustment_factor
final_diagnostic = int(final_diagnostic) if bit_encoded & 8 else int(final_diagnostic) + 50

# Critical output
print(f"Result: {final_diagnostic}")