def analyze_system_performance(readings, thresholds):
    total_samples = len(readings)
    threshold_map = dict(zip(range(len(thresholds)), thresholds))
    valid_count = 0
    temp_buffer = []
    outlier_detected = False

    for i, (value, is_active) in enumerate(zip(readings, [v > 0 for v in readings])):
        if i == 0:
            running_avg = value
            continue

        adjusted_index = i % 4 if i > 2 else i
        temp_buffer.append(value * (0.9 + adjusted_index * 0.05))

        if value > threshold_map.get(i % len(thresholds), 100):
            valid_count += 1
        elif value < 10:
            outlier_detected = True

    filtered_values = [v for v in temp_buffer if v > 15]
    convergence = sum(filtered_values) / len(filtered_values) if filtered_values else 0

    spike_count = 0
    for j in range(1, len(readings)):
        if readings[j] - readings[j-1] > 20:
            spike_count += 1

    stability_factor = 1 if not outlier_detected and spike_count < 3 else 0.5

    # Irrelevant diagnostic trace
    debug_state = 'STABLE' if convergence > 40 else 'FLUCTUATING'
    _ = [f'Diagnostic: {debug_state} at level {convergence:.1f}' for _ in range(2)]

    def compute_rating(conv, stab):
        base_rating = conv * 2.5
        penalty = 10 if stab < 1 else 0
        bonus = 5 if len(temp_buffer) > 6 else 0  # Depends on temp_buffer from outer scope
        return int(base_rating + (bonus - penalty) * stab)

    final_score = compute_rating(convergence, stability_factor)
    
    # Dead code branch - never executed due to logic above
    if False and len(readings) == 0:
        final_score = -1

    return final_score

# Simulated sensor readings and thresholds
data_stream = [23, 45, 12, 67, 89, 34, 78, 10]
cutoff_levels = [30, 50, 20, 90]

result = analyze_system_performance(data_stream, cutoff_levels)
print(f"Result: {result}")