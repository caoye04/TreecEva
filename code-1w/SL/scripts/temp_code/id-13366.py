from collections import defaultdict, Counter
import itertools

# Simulated sensor data from industrial monitoring system
temperature_readings = [23.5, 24.1, 25.0, 26.8, 27.3, 28.0, 25.7, 24.9]
humidity_readings = [45, 47, 50, 55, 58, 60, 53, 51]
pressure_readings = [1013, 1015, 1017, 1020, 1022, 1025, 1019, 1016]

# Irrelevant auxiliary data (distractor)
color_codes = ['FF0000', '00FF00', '0000FF', 'FFFF00']
status_labels = ['active', 'standby', 'maintenance', 'fault']

# Baseline thresholds (used later)
baseline = {
    'temp_avg': 25.5,
    'humidity_avg': 52,
    'pressure_trend': 10
}

# Distractor: unused function
def analyze_color_distribution(colors):
    return {c: len(c) for c in colors}

# Distractor: dead code path
if len(color_codes) > 10:
    extended_analysis = True
else:
    ignored_result = "No extended analysis required"

# Transform raw data using complex pipeline
transformation_pipeline = [
    lambda x: round(x * 1.02, 2),  # calibration adjustment
    lambda x: max(x, 0),           # safety floor
]

def apply_calibration(readings, pipeline):
    result = []
    for val in readings:
        temp = val
        for step in pipeline:
            temp = step(temp)
        result.append(temp)
    return result

transformed_temp = apply_calibration(temperature_readings, transformation_pipeline)
transformed_humid = apply_calibration([x * 1.1 for x in humidity_readings], transformation_pipeline)

# Complex data alignment using itertools
aligned_data = list(itertools.zip_longest(transformed_temp, transformed_humid, pressure_readings, fillvalue=0))

# Distractor: irrelevant aggregation
daily_summary = defaultdict(float)
for i, (t, h, p) in enumerate(aligned_data):
    daily_summary[f'day_{i//2}'] += t * 0.3 + h * 0.2

# Real processing begins: extract trends
smoothed_temps = [sum(transformed_temp[i:i+3]) / 3 
                  for i in range(len(transformed_temp) - 2)]

def compute_trend(values):
    diffs = [values[i+1] - values[i] for i in range(len(values)-1)]
    return sum(diffs) / len(diffs)

# Key derived metrics
temp_trend = compute_trend(smoothed_temps)
humidity_counter = Counter(transformed_humid)
common_humidity = humidity_counter.most_common(1)[0][1]  # most frequent count

# Distractor: unused statistical analysis
variance_proxy = sum((x - sum(transformed_temp)/len(transformed_temp))**2 
                     for x in transformed_temp) / len(transformed_temp)

# Data structure transformation
transformed_data = {
    'readings': [
        {'t': t, 'h': h, 'p': p, 'idx': i} 
        for i, (t, h, p) in enumerate(aligned_data)
    ],
    'meta': {
        'calibrated': True,
        'source': 'sensor_array_A'
    }
}

# Critical function: processes metrics for final output
def process_metrics(data, base):
    readings = data['readings']
    t_vals = [r['t'] for r in readings]
    h_vals = [r['h'] for r in readings]
    
    # Nested logic with multiple steps
    avg_temp = sum(t_vals) / len(t_vals)
    avg_humid = sum(h_vals) / len(h_vals)
    
    temp_dev = abs(avg_temp - base['temp_avg'])
    humid_dev = abs(avg_humid - base['humidity_avg'])
    
    # Multi-step weighting calculation
    weights = [0.6, 0.3, 0.1]
    recent_temps = t_vals[-3:]
    weighted_recent = sum(recent_temps[i] * weights[i] for i in range(3))
    
    # Composite score with conditional boost
    base_score = (temp_dev * 2.5) + (humid_dev * 1.8)
    if weighted_recent > base['temp_avg']:
        base_score *= 1.15
    
    # Additional correction based on pressure trend (precomputed distractor)
    pressure_change = readings[-1]['p'] - readings[0]['p']
    if pressure_change > baseline['pressure_trend']:
        adjustment = 5.0
    else:
        adjustment = -2.5  # More likely case
    
    return base_score + adjustment

# Distractor: alternative analysis path never taken
potential_models = ['linear', 'exponential', 'polynomial']
model_performance = {}
for model in potential_models:
    if model == 'linear':
        model_performance[model] = 0.85
    elif model == 'exponential':
        model_performance[model] = 0.78
    else:
        model_performance[model] = 0.91

# Anomaly detection heuristic (simple but obscured by context)
defect_pattern = [1 if x > 26.0 else 0 for x in transformed_temp]
switch_count = sum(1 for i in range(1, len(defect_pattern)) 
                   if defect_pattern[i] != defect_pattern[i-1])
anomaly_score = switch_count * 3.7

# THIS IS THE KEY STATEMENT
final_diagnostic = process_metrics(transformed_data, baseline) + anomaly_score

# Output the target result
print(f"Target result: {final_diagnostic}")