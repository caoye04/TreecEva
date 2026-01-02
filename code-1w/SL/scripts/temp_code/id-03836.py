import math

# Simulated system performance analyzer with distractors
def analyze_component_health(reading):
    if reading < 0.2:
        return 'CRITICAL'
    elif reading < 0.5:
        return 'WARNING'
    else:
        return 'OK'

# Irrelevant helper - dead code path
def deprecated_normalization(x):
    return (x - 0.5) * 2  # Unused in final logic

# Distractor function dealing with unrelated unit conversion
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

# Unused statistical function to mislead reasoning
def compute_z_score(value, mean=0, std=1):
    return (value - mean) / std

# Core processing pipeline
baseline_metrics = {
    'threshold_a': 0.67,
    'weight_x': 0.3,
    'weight_y': 0.7,
    'decay_factor': 0.9,
    'history_limit': 5
}

# Fake sensor array - mostly irrelevant
temp_sensors = [0.45, 0.67, 0.33, 0.89]
humidity_readings = [0.51, 0.62, 0.44]

# Actual data log used in computation
data_log = [
    {'time': 0, 'event': 'init', 'metric_a': 0.72, 'metric_b': 0.68},
    {'time': 1, 'event': 'update', 'metric_a': 0.75, 'metric_b': 0.64},
    {'time': 2, 'event': 'update', 'metric_a': 0.70, 'metric_b': 0.71},
    {'time': 3, 'event': 'update', 'metric_a': 0.78, 'metric_b': 0.66},
    {'time': 4, 'event': 'final', 'metric_a': 0.74, 'metric_b': 0.69}
]

# Decoy accumulator variables
aggregate_sum = 0.0
temp_cache = []
status_flags = []

# Complex evaluation with multiple concepts
evaluate_performance = lambda log, base: (
    sum(
        (entry['metric_a'] * base['weight_x'] + 
         entry['metric_b'] * base['weight_y']) * 
        (base['decay_factor'] ** i)
        for i, entry in enumerate(reversed(log))
        if entry['event'] != 'init'
    ) * 100
)

# Secondary distraction: string-based health summary
health_summary = ""
for entry in data_log:
    a_status = analyze_component_health(entry['metric_a'])
    b_status = analyze_component_health(entry['metric_b'])
    if a_status != 'OK' or b_status != 'OK':
        status_flags.append((entry['time'], a_status, b_status))

# Build irrelevant cache
for val in temp_sensors:
    temp_cache.append(deprecated_normalization(val))

# More red herrings: character counting in event labels
event_chars = 0
for record in data_log:
    event_chars += len(record['event'])

# Unused sorting operation
sorted_log = sorted(data_log, key=lambda x: x['metric_a'], reverse=True)

# Core result computation - depends on weighted, decayed sum
final_score = evaluate_performance(data_log, baseline_metrics)

# Additional distraction: conditional modification that never triggers
if len(status_flags) > 10:
    final_score *= 0.8

# Print required output
print(f"Result: {final_score}")