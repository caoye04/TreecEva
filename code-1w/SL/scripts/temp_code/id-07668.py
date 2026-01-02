def main():
    # Simulate sensor readings with noise and baseline drift
    raw_readings = [104, 98, 112, 87, 95, 103, 117, 99]
    baseline_correction = 5
    adjusted_readings = [x - baseline_correction for x in raw_readings]

    # Filter out anomalous spikes using simple threshold (simulated)
    filtered_readings = [x for x in adjusted_readings if 90 <= x <= 110]

    # Compute moving average over valid windows
    moving_averages = []
    for i in range(len(filtered_readings) - 1):
        window_avg = (filtered_readings[i] + filtered_readings[i+1]) / 2
        moving_averages.append(window_avg)

    # Calculate stability metric (inverse of variance proxy)
    mean_val = sum(moving_averages) / len(moving_averages)
    variance_proxy = sum((x - mean_val) ** 2 for x in moving_averages) / len(moving_averages)
    stability_factor = 1 / (1 + variance_proxy)  # Smoother data → higher factor

    # Dummy distraction: irrelevant computation on original data
    peak_deviation = max(raw_readings) - min(raw_readings)  # Not used later
    normalized_peaks = [round((x - min(raw_readings)) / peak_deviation, 3) for x in raw_readings]

    # Performance tiers based on filtered count
    if len(filtered_readings) > 6:
        tier_bonus = 1.2
    elif len(filtered_readings) > 4:
        tier_bonus = 1.1
    else:
        tier_bonus = 0.9

    # Simulate environmental interference penalty
    environment_flags = ['low_light', 'high_humidity']
    interference_penalty = 0.95
    if 'low_light' in environment_flags:
        interference_penalty *= 0.98
    if 'high_humidity' in environment_flags:
        interference_penalty *= 0.97

    # Final performance score calculation
    base_performance = sum(moving_averages) / len(moving_averages)
    final_score = base_performance * stability_factor * tier_bonus * interference_penalty

    # Irrelevant post-processing (dead-end)
    diagnostic_trace = [round(x * final_score / 100, 4) for x in moving_averages]
    outlier_count = len(raw_readings) - len(filtered_readings)

    # Output target result
    print(f"Result: {final_score}")

main()