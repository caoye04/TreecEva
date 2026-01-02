import itertools

def main():
    # Simulate sensor array readings with noise filtering
    raw_readings = [105, 98, 112, 95, 108, 118, 93, 101]
    filtered = [x for x in raw_readings if 90 <= x <= 120]
    baseline = sum(filtered) / len(filtered)

    # Irrelevant temperature calibration (distractor)
    temp_offset = 2.5
    calibrated_temps = [t - temp_offset + 0.1 for t in raw_readings[:4]]
    avg_calibrated = sum(calibrated_temps) / len(calibrated_temps)

    # Signal quality metrics
    signal_strengths = [abs(r - baseline) for r in filtered]
    stability_score = sum(1 for s in signal_strengths if s < 15)

    # Data transformation pipeline
    shifted = [int((x - baseline) * 2) for x in filtered]
    squared_residuals = [s ** 2 for s in shifted]
    mse = sum(squared_residuals) / len(squared_residuals)
    rmse = mse ** 0.5

    # Weighted feedback model (key computation path)
    feedback_weights = [0.8, 0.6, 0.9, 0.7, 0.5]
    activation_levels = [abs(shifted[i]) / 20.0 for i in range(len(shifted)) if i < 5]
    normalized_results = []

    for val in activation_levels:
        if val > 0.7:
            normalized_results.append(val * 1.2)
        elif val > 0.4:
            normalized_results.append(val * 1.1)
        else:
            normalized_results.append(val * 0.9)

    # Auxiliary debug trace (semi-relevant but not used directly)
    debug_snapshot = list(itertools.accumulate(normalized_results, lambda a, b: a + b * 0.5))

    # Core aggregation logic
    def aggregate_performance(weights, norms):
        weighted_sum = 0
        weight_total = 0
        for w, n in zip(weights, norms):
            weighted_sum += w * n * 100
            weight_total += w
        return int(weighted_sum / weight_total) if weight_total > 0 else 0

    final_score = aggregate_performance(feedback_weights, normalized_results)

    # Dead code branch (distractor)
    if rmse < 0:
        fallback = sum(calibrated_temps) // len(calibrated_temps)
        final_score = fallback

    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()