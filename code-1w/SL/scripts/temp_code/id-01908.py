def main():
    # Simulate sensor data calibration with noise filtering
    raw_readings = [12, 15, 22, 8, 45, 16, 24, 11]
    baseline_offset = 10
    calibrated = [x - baseline_offset for x in raw_readings if x > 10]

    # Irrelevant signal smoothing (distractor)
    smoothed = []
    for i in range(len(calibrated)):
        window = calibrated[max(0, i-1):min(i+2, len(calibrated))]
        smoothed.append(sum(window) / len(window))

    # Key processing: detect anomalies using modular threshold
    anomaly_threshold = 7
    anomalies = 0
    for val in calibrated:
        if val % 5 == 0 and val > anomaly_threshold:
            anomalies += 1

    # Simulate feedback loop with state tracking
    iterations = 0
    convergence_reached = False
    feedback_loop = []
    while not convergence_reached and iterations < 6:
        score = (anomalies * 10) + (iterations ** 2)
        feedback_loop.append(score)
        if score >= 40:
            convergence_reached = True
        iterations += 1

    # Dead code path - never executed due to logic above (distractor)
    if len(feedback_loop) > 10:
        fallback = list(map(lambda x: x * 0.9, feedback_loop))
        feedback_loop = fallback

    # Aggregate performance using bitwise weighting
    def aggregate_performance(logs):
        total = 0
        weight_mask = 0b101  # Use every other bit pattern
        for idx, entry in enumerate(logs):
            if idx % 2 == 0:
                total += entry ^ 3  # XOR perturbation
            else:
                total += entry & weight_mask  # Bitwise masking
        return total + (len(logs) * 2)

    final_score = aggregate_performance(feedback_loop)
    
    # Secondary computation unrelated to final score (distractor)
    avg_calibration = sum(calibrated) / len(calibrated) if calibrated else 0
    outlier_count = len([x for x in raw_readings if x > 40])
    diagnostic_flag = (avg_calibration > 5) and (outlier_count == 1)

    # Output result as required
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()