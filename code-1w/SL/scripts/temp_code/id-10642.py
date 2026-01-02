def analyze_system_efficiency(readings, threshold=75.0, min_duration=3):
    # Simulate sensor data processing for thermal system monitoring
    durations = [len(segment) for segment in readings]
    baseline_avg = sum(durations) / len(durations)

    # Extract temperature values from readings (timestamp, temp, pressure)
    temperatures = [entry[1] for reading in readings for entry in reading]
    pressures = [entry[2] for reading in readings for entry in reading]

    # Misleading computation: average pressure (not used in final result)
    avg_pressure = sum(pressures) / len(pressures)
    pressure_variance = sum((p - avg_pressure) ** 2 for p in pressures) / len(pressures)

    # Filter temperatures above threshold with sufficient duration
    temp_duration_map = []
    for reading in readings:
        high_temp_entries = [temp for _, temp, _ in reading if temp > threshold]
        temp_duration_map.append((len(high_temp_entries), sum(high_temp_entries)))

    # Only consider segments that exceed minimum duration
    valid_segments = [seg for seg in temp_duration_map if seg[0] >= min_duration]

    # Compute thermal load as sum of temps per valid segment
    thermal_loads = [segment[1] for segment in valid_segments]

    # Apply correction factor using lambda (idiomatic python)
    correction_factor = lambda x: 1.1 if x > 80 else 0.95
    corrected_loads = [load * correction_factor(load) for load in temperatures[:len(thermal_loads)]]

    # Final filtered loads based on corrected values above dynamic threshold
    dynamic_threshold = sum(temperatures) / len(temperatures) * 0.9
    thermal_loads_filtered = [
        corrected_loads[i] for i in range(len(thermal_loads))
        if i < len(corrected_loads) and corrected_loads[i] > dynamic_threshold
    ]

    # Key assignment point
    peak_capacity = max(thermal_loads_filtered)

    # Dead code path - never executed but adds distraction
    if False:
        fallback = sum(thermal_loads) / len(thermal_loads)
        peak_capacity = fallback if fallback > 0 else 0

    # Irrelevant slicing operation (distractor)
    tail_slice = temperatures[-5:-2]
    slice_avg = sum(tail_slice) / len(tail_slice) if tail_slice else 0

    return peak_capacity

# Simulated sensor data: list of operational periods, each with (time, temp, pressure)
data_log = [
    [(0, 70.1, 101.3), (1, 72.3, 102.1), (2, 74.0, 101.8), (3, 76.5, 103.0)],
    [(0, 80.2, 105.6), (1, 82.1, 106.3), (2, 85.4, 107.0), (3, 88.9, 108.1), (4, 90.1, 109.0)],
    [(0, 60.5, 99.8), (1, 65.3, 100.2), (2, 68.9, 101.0)],
    [(0, 79.8, 104.5), (1, 83.2, 105.8), (2, 87.5, 106.9), (3, 89.0, 107.5), (4, 91.2, 108.3)]
]

result = analyze_system_efficiency(data_log)
print(f"Target result: {result}")