def main():
    # Simulate sensor readings with noise and calibration
    raw_readings = [12, 15, 10, 8, 20, 14, 16]
    calibrated = list(map(lambda x: (x * 1.05) - 0.25, raw_readings))

    # Apply moving average filter (window size 3)
    smoothed = []
    for i in range(2, len(calibrated)):
        window_avg = (calibrated[i-2] + calibrated[i-1] + calibrated[i]) / 3
        smoothed.append(round(window_avg, 2))

    # Threshold detection for anomalies
    threshold = 13.5
    anomalies = []
    anomaly_count = 0
    for val in smoothed:
        if val > threshold:
            anomalies.append(val)
            anomaly_count += 1

    # Simulate feedback loop with adjustment factors
    adjustments = [0.9, 1.1, 0.95, 1.05, 1.0]
    feedback_loop = []
    temp_sum = 0
    for i, a in enumerate(anomalies):
        adjusted = a * adjustments[i % len(adjustments)]
        temp_sum += adjusted
        if i % 2 == 0:
            temp_sum -= 0.5  # correction factor
        feedback_loop.append(round(temp_sum, 2))

    # Dead code - irrelevant tracking (distractor)
    debug_trace = []
    cumulative_delta = 0
    for x in feedback_loop:
        delta = x - threshold
        if delta > 1:
            cumulative_delta += delta * 0.1
        debug_trace.append((x, delta, cumulative_delta))

    # Aggregation function using lambda and conditional logic
    aggregate_performance = lambda data: sum(x for x in data if x > 12.0) * 0.85

    # Key computation point
    final_score = aggregate_performance(feedback_loop)

    # Irrelevant secondary calculation (distractor)
    baseline = len(smoothed) * threshold * 0.75
    offset_adjustment = baseline * 0.15 if len(anomalies) > 2 else baseline * 0.05

    # Output result
    print(f"Result: {final_score}")

main()