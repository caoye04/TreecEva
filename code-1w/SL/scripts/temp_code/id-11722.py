def calculate_performance(data):
    base_multiplier = 1.5
    penalty_factor = 0.9
    bonus_threshold = 85
    temp_offset = 0.0  # Irrelevant offset for distraction

    # Preprocess: extract valid results above threshold using list comprehension
    valid_results = [entry['score'] for entry in data if entry['active'] and entry['score'] >= 70]

    if not valid_results:
        return 0

    # Compute average of valid results
    raw_average = sum(valid_results) / len(valid_results)

    # Apply conditional bonus based on performance
    performance_bonus = 1.1 if raw_average >= bonus_threshold else 1.0

    # Simulate calibration adjustment (partially irrelevant)
    calibration_readings = [0.98, 1.02, 0.99]
    avg_calibration = sum(calibration_readings) / len(calibration_readings)
    adjusted_average = raw_average * avg_calibration  # Minor real effect

    # Complex conditional expression to determine scaling
    scaling_factor = base_multiplier if adjusted_average > 80 \
        else (base_multiplier * 0.8 if adjusted_average > 70 else base_multiplier * 0.6)

    # Secondary distraction: compute unused efficiency metric
    total_ops = sum([entry.get('ops', 0) for entry in data])
    total_time = sum([entry.get('time', 1) for entry in data])
    efficiency_ratio = total_ops / total_time if total_time > 0 else 0  # Not used

    # Final score computation
    final_score = adjusted_average * scaling_factor * performance_bonus
    final_score -= temp_offset  # No effect

    return int(final_score)  # Deterministic integer result

# Benchmark data input
benchmark_data = [
    {'score': 88, 'active': True, 'ops': 450, 'time': 5},
    {'score': 76, 'active': True, 'ops': 320, 'time': 4},
    {'score': 65, 'active': False, 'ops': 200, 'time': 2},  # Inactive, excluded
    {'score': 91, 'active': True, 'ops': 510, 'time': 6},
    {'score': 73, 'active': True, 'ops': 380, 'time': 5},
    {'score': 82, 'active': True, 'ops': 400, 'time': 4}
]

# Key execution point
final_score = calculate_performance(benchmark_data)
print(f"Target result: {final_score}")