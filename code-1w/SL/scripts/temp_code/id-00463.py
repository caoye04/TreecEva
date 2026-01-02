from collections import defaultdict
import math

# Simulate sensor data with noise and metadata
data_stream = [
    {'value': 12, 'type': 'temp', 'status': 'ok'},
    {'value': 8, 'type': 'temp', 'status': 'ok'},
    {'value': 15, 'type': 'temp', 'status': 'ok'},
    {'value': 30, 'type': 'pressure', 'status': 'warning'},
    {'value': 25, 'type': 'pressure', 'status': 'ok'}
]

# Misleading counters (distractor variables)
error_count = 0
redundant_sum = 0
ignored_flags = []

# Data aggregation by type
aggregated = defaultdict(list)
for entry in data_stream:
    aggregated[entry['type']].append(entry['value'])

# Compute averages per type
averages = {}
for k, v in aggregated.items():
    averages[k] = sum(v) / len(v)

# Intermediate transformation using lambda (relevant)
scale_fn = lambda x: x * 1.8 + 32 if x < 20 else x
scaled_averages = {k: scale_fn(v) for k, v in averages.items()}

# Extract temperature-related values
raw_temps = [d['value'] for d in data_stream if d['type'] == 'temp']
valid_temps = list(filter(lambda x: x > 0, raw_temps))  # sanity filter

# Distractor: complex but unused computation on pressure
pressure_status_map = {'ok': 1, 'warning': -1, 'critical': -2}
pressure_score = 0
for d in data_stream:
    if d['type'] == 'pressure':
        pressure_score += d['value'] * pressure_status_map.get(d['status'], 0)
        redundant_sum += d['value'] ** 2  # dead computation

# Real processing begins: normalize valid temperatures
mean_temp = sum(valid_temps) / len(valid_temps)
deviations = [(t - mean_temp) ** 2 for t in valid_temps]
rms_deviation = math.sqrt(sum(deviations) / len(deviations))

# Processed data structure (key input)
processed_data = {
    'base': mean_temp,
    'variation': rms_deviation,
    'count': len(valid_temps),
    'scale_adjust': scaled_averages['temp']
}

# Calculation function (uses only some fields)
def calculate_rating(data):
    base_weight = 2.5
    var_weight = 1.2
    # Only uses base and variation; others are distractions
    score = base_weight * data['base'] - var_weight * data['variation']
    return int(score)

# Final computation step
final_score = calculate_rating(processed_data)
print(f"Result: {final_score}")