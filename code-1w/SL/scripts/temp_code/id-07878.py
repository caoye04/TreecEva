def analyze_system_performance(input_data):
    base_rating = 0
    efficiency_factor = 1.0
    transient_load = 0
    calibration_offset = 0.023
    
    # Process sensor readings and compute system rating
    for i, reading in enumerate(input_data):
        if i % 2 == 0:
            base_rating += reading ** 2
        else:
            transient_load += reading  # Not used in final result

    # Misleading intermediate calculation (dead computation)
    avg_reading = sum(input_data) / len(input_data)
    noise_floor = avg_reading * 0.05
    adjusted_load = transient_load - noise_floor  # Distractor

    # Efficiency logic with conditional modulation
    thresholds = [10, 20, 30]
    for idx, thresh in enumerate(thresholds):
        if base_rating > thresh:
            efficiency_factor *= (1 + 0.1 * (idx + 1))

    # Red herring: complex-looking but irrelevant list transformation
    metadata_pairs = [('a', 2), ('b', 4), ('c', 6)]
    scale_map = {k: v * 3 for k, v in metadata_pairs}
    scaling_factor = len(scale_map)  # Unused

    # Key assignment point
    thermal_capacity = base_rating * efficiency_factor

    # Additional distraction: zipping unrelated sequences
    indices = list(range(len(input_data)))
    for pos, val in zip(indices, input_data):
        if val < 5:
            thermal_capacity -= pos * 0.1  # Minor adjustment, still deterministic

    return thermal_capacity

# Simulate execution
sensor_readings = [3, 4, 2, 5]
result = analyze_system_performance(sensor_readings)
print(f"Result: {result}")