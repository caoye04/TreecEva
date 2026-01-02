def sensor_network_analysis():
    raw_readings = [14.2, 18.9, 22.1, 7.3, 31.5, 25.8, 19.0, 11.7, 42.3, 38.6]
    calibration_offset = 1.8
    sensitivity_factor = 0.87
    noise_floor = 5.0
    peak_threshold = 35.0
    baseline_reference = 20.0

    # Irrelevant signal smoothing (distractor)
    smoothed = []
    for i in range(len(raw_readings)):
        if i == 0 or i == len(raw_readings) - 1:
            smoothed.append(raw_readings[i])
        else:
            smoothed.append((raw_readings[i-1] + raw_readings[i] + raw_readings[i+1]) / 3)

    # Apply calibration (red herring - not used later)
    calibrated = [v + calibration_offset for v in raw_readings]

    # Real processing begins: filter based on dynamic threshold
    def dynamic_noise_gate(x):
        return x > noise_floor * 1.5

    filtered_data = [v for v in raw_readings if dynamic_noise_gate(v)]

    # Decoy transformation chain (dead path)
    transformed_chain = list(map(lambda x: (x + 2.5) ** 0.5 * sensitivity_factor, raw_readings))
    normalized = [round((x - min(raw_readings)) / (max(raw_readings) - min(raw_readings)), 4) for x in raw_readings]
    zipped_pairs = list(zip(normalized, raw_readings))

    # Unused recursive function (decoy)
    def recursive_dampen(val, depth=0):
        if depth >= 3 or val < 10:
            return val
        return recursive_dampen(val * 0.75, depth + 1)

    # Threshold function that will be passed as callable
    def threshold_func(x):
        return x > baseline_reference

    # Secondary distractor: enumerate with filtering (irrelevant result)
    indexed_high = []
    for idx, val in enumerate(smoothed):
        if val > peak_threshold:
            indexed_high.append((idx, val))

    # Core logic disguised among distractions
    def count_fluctuations(data):
        count = 0
        for i in range(1, len(data)):
            if (data[i] > baseline_reference) != (data[i-1] > baseline_reference):
                count += 1
        return count

    fluctuation_score = count_fluctuations(filtered_data)  # distraction but looks important

    # Actual computation path
    def process_readings(data, condition):
        subset = [x for x in data if condition(x)]
        if not subset:
            return 0
        avg = sum(subset) / len(subset)
        variance = sum((x - avg) ** 2 for x in subset) / len(subset)
        return round(avg * (variance ** 0.5), 4)

    # Critical execution point
    final_diagnostic = process_readings(filtered_data, threshold_func)
    
    # Print required output
    print(f"Result: {final_diagnostic}")

sensor_network_analysis()