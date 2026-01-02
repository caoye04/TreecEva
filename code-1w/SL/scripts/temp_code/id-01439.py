from collections import defaultdict

# Simulate time-series load monitoring across multiple server clusters
def analyze_cluster_load():
    raw_metrics = [12.5, 18.3, 9.8, 22.1, 15.7, 25.6, 19.4, 23.9, 27.2, 20.1]
    threshold = 10.0
    peak_capacity = 0.0
    historical_peaks = defaultdict(float)
    temp_buffer = []
    scaling_factor = 1.25
    adjustment_history = []

    for i, reading in enumerate(raw_metrics):
        # Apply dynamic scaling based on time index (simulated learning rate decay)
        if i % 3 == 0:
            adjusted_reading = reading * scaling_factor
        else:
            adjusted_reading = reading * (scaling_factor - 0.15)

        # Simulate noise filtering
        if adjusted_reading < threshold:
            continue

        # Track rolling statistics (some are distractions)
        temp_buffer.append(adjusted_reading)
        if len(temp_buffer) > 3:
            temp_buffer.pop(0)

        # Compute moving average (semi-relevant, not used in final result)
        moving_avg = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
        adjustment_history.append(moving_avg)

        # Core logic: track peak system capacity
        current_load = adjusted_reading * 0.85  # Simulate efficiency loss

        # Critical update point
        peak_capacity = max(peak_capacity, current_load)

        # Record historical data (distractor)
        historical_peaks[f'hour_{i}'] = current_load + (i * 0.01)

    # Irrelevant post-processing (dead code path with side effect that doesn't affect answer)
    if len(adjustment_history) > 5:
        smoothed_peak = sum(adjustment_history[-3:]) / 3
        peak_capacity = round(smoothed_peak * 1.1, 2)  # This does NOT override the real peak

    # Final output
    print(f"Result: {peak_capacity}")

    return peak_capacity

analyze_cluster_load()