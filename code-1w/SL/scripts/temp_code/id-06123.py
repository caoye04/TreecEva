def main():
    # Simulate sensor data processing with noise filtering and scoring
    raw_readings = [127, 85, 190, 45, 210, 60, 150]
    baseline = 100
    adjusted = [abs(x - baseline) for x in raw_readings]

    # Irrelevant transformation: color intensity simulation (distractor)
    color_intensity = [x * 0.72 for x in raw_readings if x > 80]
    avg_color = sum(color_intensity) / len(color_intensity) if color_intensity else 0

    # Focus on performance metrics
    deviations = list(filter(lambda x: x > 10, adjusted))
    squared_devs = [x ** 2 for x in deviations]

    # Bitwise normalization (simulates hardware-level adjustment)
    normalized_devs = [x & 0xFF for x in squared_devs]  # Clamp to 8-bit

    # Weighted decay factors for time-series smoothing (only some used)
    decay_weights = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
    unused_weight_sum = sum(decay_weights[:3])  # Partially unused

    # Actual weights for metrics
    weights = [0.4, 0.3, 0.2, 0.1][:len(normalized_devs)]

    # Metrics: mean, max, variance-inspired, and min impact
    mean_dev = sum(normalized_devs) / len(normalized_devs)
    max_dev = max(normalized_devs)
    variance_proxy = sum((x - mean_dev) ** 2 for x in normalized_devs) / len(normalized_devs)
    min_dev = min(normalized_devs)

    metrics = [mean_dev, max_dev, variance_proxy, min_dev]

    # Dead code path - never executed (distractor)
    if False:
        backup_score = sum(metrics) * 0.5
        print(f'Debug: {backup_score}')

    # Core aggregation function
    def aggregate_performance(mets, wts):
        sorted_mets = sorted(mets, reverse=True)
        weighted_sum = sum(w * m for w, m in zip(wts, sorted_mets[:len(wts)]))
        penalty = (max_dev >> 3)  # Right shift as coarse penalty
        return int(weighted_sum - penalty)

    final_score = aggregate_performance(metrics, weights)

    # Red herring computation: checksum for logging (not affecting score)
    log_checksum = sum(raw_readings[i] ^ i for i in range(len(raw_readings)))
    print(f"Log checksum: {log_checksum}")

    print(f"Result: {final_score}")

if __name__ == '__main__':
    main()