def analyze_production_cycle(data, thresholds):
    total_output = 0
    idle_count = 0
    peak_flag = False
    temp_buffer = []
    cumulative_noise = 0  # Distractor: not used in final result

    for i, (output, duration, status) in enumerate(data):
        if output < 0:
            continue  # Skip invalid negative outputs

        adjusted_output = output * 0.95  # Simulate loss factor
        if duration <= 0:
            continue

        if status == 'active':
            total_output += adjusted_output
            temp_buffer.append(duration)
        elif status == 'idle':
            idle_count += 1
            cumulative_noise += len(str(duration))  # Red herring computation

        if output > thresholds['peak'] and not peak_flag:
            peak_flag = True

    # Compute active_duration from temp_buffer using zip for alignment with dummy weights
    weights = [1.0] * len(temp_buffer)
    active_duration = sum(d * w for d, w in zip(temp_buffer, weights))

    # Dummy statistical check (irrelevant to main logic)
    avg_temp = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
    fluctuation = max(temp_buffer) - min(temp_buffer) if temp_buffer else 0

    # Key computation point
    efficiency_score = total_output / active_duration if active_duration > 0 else 0

    # Post-processing distraction
    if idle_count > 3:
        efficiency_score *= 0.9
    if peak_flag:
        efficiency_score += 0.5  # This branch is never taken due to data

    # Final adjustment unrelated to core path
    scaling_factor = 1 + (idle_count * 0.01)
    efficiency_score *= scaling_factor

    print(f"Result: {efficiency_score}")
    return efficiency_score

# Input data
production_data = [
    (100, 10, 'active'),
    (-5, 5, 'active'),         # Invalid output, skipped
    (200, 20, 'active'),
    (0, 15, 'idle'),
    (150, 0, 'active'),       # Zero duration, skipped
    (300, 30, 'active')
]
thresholds = {'peak': 250}

result = analyze_production_cycle(production_data, thresholds)