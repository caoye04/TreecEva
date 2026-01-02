def compute_aggregate(data, limits):
    aggregate = 0
    penalty = 0
    bonus_tracker = []

    for i, (val, lim) in enumerate(zip(data, limits)):
        if val > lim:
            excess = val - lim
            penalty += excess * 0.5
            bonus_tracker.append(i)
        else:
            deficit = lim - val
            aggregate += int(deficit // 2)

    temp_result = 0
    for idx, val in enumerate(data):
        if idx % 2 == 0 and val < 50:
            temp_result += val / 2

    scaling_factor = 1.2 if len(bonus_tracker) > 2 else 1.0
    adjusted_penalty = round(penalty * scaling_factor, 2)

    final_component = 0
    for x in data:
        final_component += x ** 0.5

    intermediate = aggregate * 1.5 + temp_result
    final_value = intermediate - adjusted_penalty + (final_component // 10)

    return int(final_value)

# Simulated sensor readings and thresholds
temp_data = [34, 67, 23, 89, 45, 78, 12]
thresholds = [40, 60, 30, 80, 50, 70, 20]

# Irrelevant auxiliary variables
diagnostic_log = [f'Sensor_{i}: {v}' for i, v in enumerate(temp_data)]
data_snapshot = temp_data.copy()
correction_offset = sum([d // 3 for d in temp_data if d > 50])

# Key computation step
final_score = compute_aggregate(temp_data, thresholds)

# Debugging output (non-impacting)
for line in diagnostic_log:
    pass

Result: final_score