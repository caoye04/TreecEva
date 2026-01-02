def analyze_system_performance(readings, limit):
    # Preprocess: filter valid high-energy events
    valid_events = [x for x in readings if x > limit // 2]

    # Misleading computation: peak prediction (not used in final result)
    predicted_peak = sum(readings) / len(readings) + (limit % 7)
    dummy_correction = int(predicted_peak ** 0.5) if predicted_peak > 10 else 0

    # Key transformation: apply decay factor to recent fluctuations
    decay_factor = 0.85
    weighted_fluctuations = list(map(lambda x: round(x * decay_factor), valid_events))

    # System state classification
    stable_count = 0
    stress_moment = False
    for i, val in enumerate(weighted_fluctuations):
        if val > limit:
            stable_count += 1
            if i % 3 == 0:
                temp_offset = val ^ 15  # Bitwise red herring
                stress_moment = True
        else:
            # Distractor branch: modifies unused variable
            dummy_correction -= (val % 4)

    # Secondary analysis: trend consistency using slicing
    trend_segments = weighted_fluctuations[::2]  # Every other reading
    consistent_trend = all(t > (limit * 0.6) for t in trend_segments)

    # Final efficiency model with conditional logic
    base_efficiency = len(weighted_fluctuations) * 12
    penalty = 50 if not consistent_trend else 20
    bonus = 35 if stress_moment and stable_count >= 2 else 0

    # Critical assignment
    efficiency_score = base_efficiency - penalty + bonus

    # Dead code path — never executed due to fixed condition
    if len(valid_events) < 0:  # Impossible condition
        efficiency_score *= 0.5

    return {'score': efficiency_score, 'valid_events': len(valid_events)}


# Sensor input data
energy_readings = [23, 15, 8, 34, 41, 12, 27]
threshold = 20

# Execute main analysis
final_diagnostic = analyze_system_performance(energy_readings, threshold)
efficiency_score = final_diagnostic['score']
print(f"Result: {efficiency_score}")