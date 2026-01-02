def analyze_readings(readings):
    processed = []
    for r in readings:
        if r < 0:
            processed.append(abs(r) * 1.5)
        elif r > 100:
            processed.append(100)
        else:
            processed.append(r / 2.0)
    return processed

# Irrelevant helper (distractor)
def normalize_string(s):
    return s.upper().replace(' ', '_')

# Unused function (dead code path)
def legacy_calibrate(x):
    return (x + 10) % 7

# Primary data
raw_values = [120, -5, 60, 200, 45]

# Distractor variables
auxiliary_log = ['event_1', 'event_2']
dummy_counter = 0

# Real processing begins
adjusted_readings = analyze_readings(raw_values)

# Simulate sensor confidence scores (partly irrelevant)
confidence_scores = []
for val in raw_values:
    if val > 150:
        score = 0.6
    elif val < 0:
        score = 0.4
    else:
        score = 0.8
    confidence_scores.append(score)
    dummy_counter += 1  # Used only in distractor

# Compute average confidence (misleading intermediate result)
avg_confidence = sum(confidence_scores) / len(confidence_scores)
warning_flag = avg_confidence < 0.65  # Looks important, not used later

# Focus on critical health thresholds
threshold_set = {40, 60, 75, 100}
baseline_metrics = {x: round(y) for x, y in enumerate(adjusted_readings)}

# Conditional expression with lambda (required feature)
filter_func = lambda x: x >= 40
filtered_metrics = list(filter(filter_func, adjusted_readings))

# Set operations (required feature): find overlap between rounded values and thresholds
rounded_diagnostics = {round(x) for x in filtered_metrics}
common_elements = rounded_diagnostics & threshold_set  # Intersection

# Secondary distractor: string-based status map (irrelevant)
status_map = {key: ('HIGH' if val > 75 else 'NORMAL') for key, val in baseline_metrics.items()}

# Core logic disguised among distractions
severity_weights = []
for x in common_elements:
    if x in threshold_set:
        if x < 50:
            severity_weights.append(x * 0.5)
        elif x < 80:
            severity_weights.append(x * 1.2)
        else:
            severity_weights.append(x * 1.8)

# Final aggregation
aggregated_risk = sum(severity_weights)

# Key transformation using conditional expression
primary_index = len(common_elements) if warning_flag else len(filtered_metrics)

# Critical assignment hidden among noise
scaling_factor = 3 if primary_index > 2 else 2

# Final diagnostic computation (answer point)
final_diagnostic = aggregated_risk * scaling_factor

# Print result as required
print(f"Result: {final_diagnostic}")