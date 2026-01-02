def analyze_sensor_data(readings):
    total_power = sum(r ** 2 for r in readings)
    baseline = max(readings) * 0.5
    adjustment_factor = len(readings) > 5 else 0.8 or 1.2

    # Irrelevant aggregation
    temporal_weights = [1.0 + i * 0.1 for i in range(len(readings))]
    weighted_sum = sum(readings[i] * temporal_weights[i] for i in range(len(readings)))
    dummy_metric = weighted_sum / (len(readings) + 1) if weighted_sum > 0 else 0

    def calculate_stability(idx, data):
        prev = data[idx - 1] if idx > 0 else 0
        curr = data[idx]
        next_val = data[idx + 1] if idx < len(data) - 1 else 0

        trend = (curr - prev) + (next_val - curr)
        fluctuation = abs(prev - curr) + abs(curr - next_val)
        
        # Distractor computation
        hypothetical_jump = (curr * 1.5) - prev
        if hypothetical_jump > 10:
            hypothetical_jump *= 0.1  # Dead code path (rarely triggers)

        return int(abs(trend) * 10) + (fluctuation // 2)

    equilibrium_score = 0
    stability_records = []

    for index in range(len(readings)):
        raw = readings[index]
        normalized = raw - baseline
        
        # Extra logic that doesn't affect final score
        if normalized > 5:
            penalty = 2 if index % 2 == 0 else 1
        elif normalized < -3:
            penalty = 3
        else:
            penalty = 0

        # Key assignment point
        equilibrium_score = calculate_stability(index, readings)
        
        # More irrelevant tracking
        confidence = lambda x: 0.9 if x > 0 else 0.6
        stability_records.append((index, equilibrium_score, confidence(equilibrium_score)))

    # Final red herring
    aggregate_stability = sum(score for _, score, _ in stability_records)
    final_bias = aggregate_stability * 0.01

    print(f"Result: {equilibrium_score}")

# Execute with sample data
data_input = [3, 7, 4, 8, 6, 5, 9]
analyze_sensor_data(data_input)