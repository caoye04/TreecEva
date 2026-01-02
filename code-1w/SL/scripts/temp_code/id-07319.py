def analyze_signal_strength(readings):
    filtered_readings = [x for x in readings if x > 0]
    base_energy = sum(filtered_readings) / len(filtered_readings) if filtered_readings else 0

    # Misleading transformation (not used in final result)
    inverted_map = [1.0 / (1 + x) for x in filtered_readings]
    avg_inversion = sum(inverted_map) / len(inverted_map) if inverted_map else 0

    # Key processing steps
    squared_readings = [x ** 2 for x in filtered_readings]
    normalized = [x / base_energy for x in squared_readings if base_energy != 0]

    # Simulate frequency weighting
    weights = []
    for i, val in enumerate(normalized):
        weight = val * (0.9 ** i)  # Exponential decay
        if i % 2 == 0:
            weight += 0.05  # Boost even indices
        weights.append(round(weight, 4))

    # Secondary distraction: unused cluster analysis
    clusters = set()
    temp_cluster = []
    for w in weights:
        if w > 0.5:
            temp_cluster.append(w)
        else:
            if temp_cluster:
                clusters.add(len(temp_cluster))
                temp_cluster = []
    if temp_cluster:
        clusters.add(len(temp_cluster))

    # Destructuring with partial use
    first_weight, *middle_weights, last_weight = weights
    extremities = (first_weight, last_weight)

    # Core logic chain
    adjustment = len(middle_weights) % 4
    correction_factor = (sum(extremities) + adjustment) / 3

    # Final computation
    cumulative = 0
    final_weights = []
    for w in weights:
        cumulative += w * 0.8
        final_weights.append(round(cumulative, 4))

    threshold_balance = final_weights[-1] * correction_factor

    # Dead code path - never executed due to prior filtering
    outlier_flags = []
    for r in readings:
        if r < -100:
            outlier_flags.append(True)

    return threshold_balance

# Input data
sensor_data = [1.2, 2.5, -0.3, 3.1, 0.8, 2.9, -1.0, 1.7]
result = analyze_signal_strength(sensor_data)
print(f"Result: {result}")