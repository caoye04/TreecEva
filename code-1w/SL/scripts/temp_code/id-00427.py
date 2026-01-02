def analyze_growth_patterns(data, thresholds):
    results = []
    for i, reading in enumerate(data):
        if reading > thresholds[i % len(thresholds)]:
            results.append((i, reading * 1.2))
        else:
            results.append((i, reading * 0.85))
    return results

# Simulate environmental sensor readings over time
sensor_readings = [34, 56, 78, 23, 67, 89, 12, 45]
alert_levels = [40, 60, 75, 30]

# Irrelevant transformation - red herring
transformed_data = list(map(lambda x: x ** 0.5 * 2.1, sensor_readings))
dummy_calc = sum([x for x in transformed_data if x > 10]) / len(transformed_data)

# Analyze only relevant growth triggers
active_responses = analyze_growth_patterns(sensor_readings, alert_levels)

# Track state across phases
phase_tracker = {}
for idx, val in active_responses:
    phase = idx // 2
    if phase not in phase_tracker:
        phase_tracker[phase] = []
    phase_tracker[phase].append(val)

# Compute phase aggregates (some are unused later)
phase_averages = {p: sum(vals)/len(vals) for p, vals in phase_tracker.items()}
phase_peaks = {p: max(vals) for p, vals in phase_tracker.items()}

# Introduce irrelevant set operations for distraction
unique_values = set(round(v, 1) for sublist in phase_tracker.values() for v in sublist)
baseline_set = {round(x * 0.95, 1) for x in sensor_readings}
overlap_count = len(unique_values & baseline_set)  # Not used

# Define complex conditions based on response patterns
conditions = []
magnitude_shift = 0
for i in range(len(active_responses) - 1):
    current_val = active_responses[i][1]
    next_val = active_responses[i+1][1]
    change = (next_val - current_val) / current_val
    magnitude_shift += abs(change)
    if change > 0.15:
        conditions.append('growth')
    elif change < -0.15:
        conditions.append('decay')
    else:
        conditions.append('stable')

# Add dummy smoothing filter (irrelevant)
smoothed_conditions = []
for c, (idx, val) in zip(conditions, active_responses[:-1]):
    smoothed_conditions.append(c if val > 50 else 'stable')

# Stress factors from external simulation (misleading data)
stress_factors = [0.98, 1.02, 0.89, 1.15, 0.93, 1.07, 0.85]
stress_flags = ['high' if s < 0.9 or s > 1.1 else 'normal' for s in stress_factors]

# Core yield model - depends only on condition sequence and one stress factor
valid_pairs = list(zip(conditions, stress_factors[:len(conditions)]))

# Real logic begins here
buffer_zone = []
for cond, stress in valid_pairs:
    if cond == 'growth':
        buffer_zone.append(150 * stress)
    elif cond == 'decay':
        buffer_zone.append(40 * stress)
    else:
        buffer_zone.append(90 * stress)

# Final calculation uses only last three values
trimmed_buffer = buffer_zone[-3:]

# Secondary adjustment based on trend direction
multiplier = 1.1 if conditions[-3:] == ['growth', 'stable', 'growth'] else 0.9

# Key statement
final_yield = round(sum(trimmed_buffer) * multiplier, 3)

print(f"Result: {final_yield}")