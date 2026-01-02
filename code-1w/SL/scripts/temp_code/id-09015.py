def main():
    # Simulate sensor data processing with performance scoring
    raw_readings = [145, 172, 138, 161, 153]
    baseline = 150
    deviation_threshold = 10

    # Irrelevant transformation (distractor)
    normalized = list(map(lambda x: (x - baseline) / baseline, raw_readings))

    # Compute actual metrics of interest
    deviations = [abs(x - baseline) for x in raw_readings]
    high_deviation_count = sum(1 for d in deviations if d > deviation_threshold)
    avg_deviation = sum(deviations) / len(deviations)

    # Secondary metrics (some used, some not)
    peak_reading = max(raw_readings)
    stability_ratio = (len(raw_readings) - high_deviation_count) / len(raw_readings)
    fluctuation_index = sum(abs(a - b) for a, b in zip(raw_readings, raw_readings[1:]))

    # Unused distractor variables
    dummy_correction = sum((x - baseline) ** 2 for x in raw_readings) / 100
    calibration_offset = sum(normalized) * 0.5

    # Weighted metric evaluation
    metrics = {
        'stability': stability_ratio,
        'precision': 1 - (avg_deviation / baseline),
        'consistency': 1 - (high_deviation_count / len(raw_readings))
    }

    weights = {
        'stability': 0.4,
        'precision': 0.35,
        'consistency': 0.25
    }

    def evaluate_performance(mets, wts):
        score = 0.0
        for key in mets:
            score += mets[key] * wts[key]
        return int(score * 100)  # Convert to integer percentage

    final_score = evaluate_performance(metrics, weights)

    # Dead code path (distractor)
    if dummy_correction < 0:
        final_score += 10

    # Print result as required
    print(f"Result: {final_score}")

main()