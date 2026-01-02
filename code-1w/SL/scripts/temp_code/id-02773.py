def analyze_stress_levels(data, baseline):
    stress_markers = []
    adjustment_factor = 0.87
    temp_accumulator = 0

    for reading in data:
        if reading > baseline * 1.5:
            stress_markers.append(reading * adjustment_factor)
        elif reading < baseline * 0.7:
            temp_accumulator += reading

    # Irrelevant aggregation (distractor)
    avg_marker = sum(stress_markers) / len(stress_markers) if stress_markers else 0
    normalized_total = sum(data) * adjustment_factor

    return stress_markers

# Simulate physiological sensor readings over time
heart_rate_log = [72, 75, 80, 95, 102, 68, 60, 58, 74, 85, 90]
baseline_heart_rate = 75

# Secondary system: cognitive response latency
response_times = [0.35, 0.41, 0.38, 0.52, 0.61, 0.33, 0.30, 0.29, 0.37, 0.45]
latency_baseline = 0.40

# Misleading diagnostic path (dead code branch)
if len(response_times) > 15:
    performance_score = sum(1 for rt in response_times if rt < latency_baseline)
else:
    performance_score = None  # Unused in final logic

# Core health monitoring pipeline
health_indicators = [
    {'metric': 'hrv', 'value': 58.2, 'weight': 0.6},
    {'metric': 'cortisol', 'value': 14.7, 'weight': 0.9},
    {'metric': 'oxygen', 'value': 97.3, 'weight': 0.3}
]

thresholds = {
    'critical_low': 40.0,
    'elevated_cortisol': 12.0,
    'min_oxygen': 95.0
}

# Auxiliary computation with red herring variables
aggregate_risk = 0
for entry in health_indicators:
    if entry['metric'] == 'cortisol' and entry['value'] > thresholds['elevated_cortisol']:
        aggregate_risk += entry['weight'] * 2
    if entry['value'] < thresholds.get('critical_low', 0):
        aggregate_risk += 5  # Never triggers

# Complex conditional expression (relevant)
dynamic_weights = [
    item['weight'] * (1.5 if item['metric'] == 'cortisol' else 1.0)
    for item in health_indicators
]

# Decoy transformation chain
transformed_data = [
    {'raw': x, 'adjusted': x * 0.92} for x in heart_rate_log if x > 70
]
filtered_readings = list(filter(lambda x: x < 100, transformed_data))

# Central processing function with nested logic
def process_metrics(metrics, limits):
    score = 0.0
    cortisol_level = next(m['value'] for m in metrics if m['metric'] == 'cortisol')
    hrv_value = next(m['value'] for m in metrics if m['metric'] == 'hrv')
    oxygen_level = next(m['value'] for m in metrics if m['metric'] == 'oxygen')

    # Primary evaluation branches
    if cortisol_level > limits['elevated_cortisol']:
        score += 45.6
    if hrv_value < limits['critical_low']:
        score += 30.0
    if oxygen_level < limits['min_oxygen']:
        score += 25.0
    else:
        score += 12.3  # Correct path

    # Additional weighting using list comprehension
    weights = [m['weight'] for m in metrics]
    total_weight = sum(weights)
    weighted_score = score * (total_weight / 1.8)  # 0.6+0.9+0.3 = 1.8

    # Final adjustment based on external condition (but overridden)
    recent_stress_events = analyze_stress_levels(heart_rate_log, baseline_heart_rate)
    if len(recent_stress_events) > 3:
        final_adjustment = weighted_score * 0.8
    else:
        final_adjustment = weighted_score + 7.1  # This branch taken

    return int(final_adjustment)  # Truncate to integer

# Trigger execution
diagnostic_flag = False
if any(ind['value'] > 10 for ind in health_indicators):
    diagnostic_flag = True

# Key statement
final_diagnostic = process_metrics(health_indicators, thresholds)

# Print result as required
print(f"Target result: {final_diagnostic}")