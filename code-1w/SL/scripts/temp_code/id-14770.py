def calculate_thermal_output(sequence):
    base_factor = 1.5
    adjustment = 0.8
    transient_loss = 0.12
    cumulative_stress = 0
    thermal_capacity = 0

    for step in sequence:
        if step['type'] == 'heating':
            thermal_capacity += base_factor * step['duration']
        elif step['type'] == 'cooling':
            thermal_capacity -= adjustment * step['duration']

        # Irrelevant stress accumulation (distractor)
        cumulative_stress += step.get('pressure', 0) * transient_loss

    # Secondary pass: frequency correction (only applies to long steps)
    duration_corrections = [s['duration'] // 10 for s in sequence if s['duration'] > 15]
    correction_factor = sum([c ** 0.5 for c in duration_corrections]) * 0.3
    thermal_capacity += correction_factor

    # Dead code path - never alters thermal_capacity
    if len(sequence) > 100:
        outlier = max(sequence, key=lambda x: x['duration'])
        thermal_capacity *= 0.95

    # Destructuring irrelevant metrics
    summary_stats = [s['duration'] for s in sequence]
    avg_duration = sum(summary_stats) / len(summary_stats) if summary_stats else 0
    long_steps = [s for s in sequence if s['duration'] > avg_duration]

    # Actual result modification happens here
    efficiency_ratio = len(long_steps) / len(sequence) if sequence else 0
    thermal_capacity *= (1 + efficiency_ratio * 0.25)

    return thermal_capacity

# Experimental process data
process_sequence = [
    {'type': 'heating', 'duration': 12, 'pressure': 4},
    {'type': 'heating', 'duration': 18, 'pressure': 6},
    {'type': 'cooling', 'duration': 5, 'pressure': 3},
    {'type': 'heating', 'duration': 22, 'pressure': 7},
    {'type': 'cooling', 'duration': 8, 'pressure': 5},
    {'type': 'heating', 'duration': 14, 'pressure': 4}
]

# Red herring computation
baseline_score = sum(s['duration'] for s in process_sequence) * 0.1
offset_value = max(s['pressure'] for s in process_sequence) - min(s['pressure'] for s in process_sequence)

thermal_capacity = calculate_thermal_output(process_sequence)
Result: {thermal_capacity}