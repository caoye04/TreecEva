import itertools

# Simulate time-series sensor data for structural load analysis
def analyze_structural_loads(sensor_readings):
    base_threshold = 42.5
    spike_count = 0
    filtered_peaks = []
    cumulative_drift = 0.0

    # Process each window of readings
    for i, window in enumerate(itertools.batched(sensor_readings, 5)):
        if len(window) < 5:
            break

        # Misleading statistical distraction
        mean_val = sum(window) / len(window)
        variance_proxy = sum((x - mean_val) ** 2 for x in window) / len(window)
        cumulative_drift += variance_proxy * 0.03  # Irrelevant to final result

        # Identify significant peaks above threshold
        peaks = [x for x in window if x > base_threshold + 5]
        if peaks:
            spike_count += 1
            filtered_peaks.extend(peaks)

    # Red herring: unused complex calculation
    temporal_gradient = sum(
        abs(sensor_readings[i+1] - sensor_readings[i])
        for i in range(len(sensor_readings)-1)
    ) / len(sensor_readings)

    # Key derived values
    net_flow = sum(filtered_peaks) - spike_count * 10
    peak_moment = max(filtered_peaks) if filtered_peaks else 0
    base_moment = min(filtered_peaks) if filtered_peaks else 0

    # Correction factor based on pattern density
    pattern_density = len(filtered_peaks) / spike_count if spike_count else 0
    correction_factor = int(pattern_density > 2) + 1  # Either 1 or 2

    # Dead code path - never executed due to logic above
    if len(filtered_peaks) == 0 and False:
        fallback_value = 999
        net_flow = -1

    # Critical statement
    equilibrium_score = net_flow + (peak_moment - base_moment) * correction_factor

    # Print result as required
    print(f"Result: {equilibrium_score}")

    return equilibrium_score

# Input data with embedded patterns
readings = [
    40.1, 43.2, 48.5, 41.0, 44.3,
    46.7, 52.1, 49.3, 45.0, 53.4,
    42.8, 47.6, 54.2, 50.1, 46.9,
    45.5, 43.7, 48.9, 51.2, 55.8,
    44.0, 46.1, 49.7, 53.0, 47.4
]

# Execute function
equilibrium_score = analyze_structural_loads(readings)