import math

# Simulated sensor fusion system for environmental monitoring
sensors = ['temp', 'humidity', 'pressure', 'co2', 'voc']
raw_readings = [23.4, 45.2, 1013.25, 415, 87]
weights = {'temp': 0.2, 'humidity': 0.15, 'pressure': 0.1, 'co2': 0.25, 'voc': 0.3}

# Irrelevant calibration constants (distractor)
calibration_offsets = {'temp': 0.5, 'humidity': 1.2, 'pressure': -2.1, 'co2': 5, 'voc': 3}
offset_keys = list(calibration_offsets.keys())
adjusted_offsets = {k: v * 1.1 for k, v in calibration_offsets.items() if v > 1}  # Dead path

# Misleading preprocessing with unused transformation
transformed = {}
for i, s in enumerate(sensors):
    transformed[s] = raw_readings[i] + (calibration_offsets[s] * 0.1)

# Actual processing begins here
baseline = dict(zip(sensors, [22.0, 40.0, 1010.0, 400, 50]))
deviations = {}
for s in sensors:
    idx = sensors.index(s)
    deviations[s] = abs(raw_readings[idx] - baseline[s])

# Complex weighting with lambda-based dynamic adjustment
adjustment_factor = lambda x: math.log(x + 1) if x > 1 else x * 0.9
weighted_deviation = 0
for s in sensors:
    base_weight = weights[s]
    adjusted_weight = base_weight * adjustment_factor(deviations[s])
    weighted_deviation += adjusted_weight * deviations[s]

# Red herring: Unused recursive function for alternate calculation
def recursive_impact(value, depth):
    if depth <= 0 or value < 1:
        return value
    return value * 0.8 + recursive_impact(value * 0.3, depth - 1)

# Another distraction: building unused composite score
composite = 0
for i in range(len(sensors)):
    s = sensors[i]
    if deviations[s] > 5:
        composite += raw_readings[i] * weights[s] * 0.7

# Threshold logic with dictionary mapping (critical path)
thresh_specs = {
    'temp': {'warn': 3.0, 'crit': 5.0},
    'humidity': {'warn': 10.0, 'crit': 20.0},
    'pressure': {'warn': 5.0, 'crit': 10.0},
    'co2': {'warn': 50.0, 'crit': 100.0},
    'voc': {'warn': 30.0, 'crit': 60.0}
}

alert_levels = {}
for s in sensors:
    dev = deviations[s]
    spec = thresh_specs[s]
    if dev >= spec['crit']:
        alert_levels[s] = 2
    elif dev >= spec['warn']:
        alert_levels[s] = 1
    else:
        alert_levels[s] = 0

# Distractor: string-based status map with no impact
status_names = {0: 'normal', 1: 'elevated', 2: 'critical'}
status_summary = [status_names[alert_levels[s]] for s in sensors]

# Real processing pipeline
processed_data = []
for i, s in enumerate(sensors):
    processed_data.append({
        'sensor': s,
        'value': raw_readings[i],
        'deviation': deviations[s],
        'weight': weights[s],
        'alert': alert_levels[s]
    })

# Threshold map construction - relevant
threshold_map = {}
total_warn = 0
total_crit = 0
for s in sensors:
    warn_val = thresh_specs[s]['warn']
    crit_val = thresh_specs[s]['crit']
    total_warn += warn_val * weights[s]
    total_crit += crit_val * weights[s]
threshold_map['combined_warn'] = total_warn
threshold_map['combined_crit'] = total_crit

# Decoy data structure (irrelevant)
summary_stats = {
    'max_dev': max(deviations.values()),
    'weighted_avg': sum(deviations[s] * weights[s] for s in sensors),
    'high_alert_count': sum(1 for v in alert_levels.values() if v == 2)
}

# Core analysis function
def analyze_readings(data_list, thresholds):
    comp_score = 0
    alert_score = 0
    for item in data_list:
        d = item['deviation']
        w = item['weight']
        a = item['alert']
        comp_score += d * w
        alert_score += a * w * 10
    
    # Secondary adjustment based on threshold comparison
    if comp_score >= thresholds['combined_crit']:
        level_modifier = 3.0
    elif comp_score >= thresholds['combined_warn']:
        level_modifier = 1.8
    else:
        level_modifier = 0.7
    
    # Final diagnostic calculation
    base_diagnostic = comp_score * level_modifier
    penalty = 0
    for item in data_list:
        if item['alert'] == 2:
            penalty += item['weight'] * 15
    
    # Apply penalty and scale
    final_value = base_diagnostic - penalty
    final_value *= (1 + alert_score / 100)
    
    # Dead code branch - never executed due to logic
    if False and 'temp' in [x['sensor'] for x in data_list]:
        temp_item = next(x for x in data_list if x['sensor'] == 'temp')
        if temp_item['value'] > 30:
            final_value *= 1.2
    
    return int(final_value)

# Critical execution point
final_diagnostic = analyze_readings(processed_data, threshold_map)
print(f"Result: {final_diagnostic}")