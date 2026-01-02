def analyze_system_status(temperatures, thresholds, mode='safe'):
    # Irrelevant helper function (dead code path)
    def legacy_calibrate(x):
        return (x + 32) * 5/9

    # Distractor variables
    baseline_offset = 273.15
    emergency_triggered = False
    system_log = []

    # Real processing begins
    calibrated_temps = [t + 0.5 for t in temperatures if t > 0]  # Simulate sensor offset

    # Misleading intermediate transformation
    normalized = [(t - min(calibrated_temps)) / (max(calibrated_temps) - min(calibrated_temps)) for t in calibrated_temps]
    
    # Masked filtering logic with red herring condition
    alerts = 0
    for i, temp in enumerate(calibrated_temps):
        if temp > thresholds[i % len(thresholds)] and mode == 'aggressive':
            alerts += 1
            emergency_triggered = True

    # Actual relevant data path
    valid_indices = [i for i in range(len(calibrated_temps)) if calibrated_temps[i] < 95.0]
    filtered_data = [calibrated_temps[i] for i in valid_indices]

    # Decoy aggregation
    average_with_padding = sum(filtered_data + [0] * (10 - len(filtered_data))) / 10

    # Core logic hidden among distractions
    calibration_factor = sum([i * 0.1 for i in range(len(filtered_data))]) or 1.0

    def process_readings(data, factor):
        # Bit manipulation as obfuscation layer
        encoded = 0
        for d in data:
            encoded ^= int(d * 10) & 0xFF
        
        # Real calculation buried here
        base_score = sum(map(lambda x: (x ** 2) % 7, data))
        adjustment = (encoded & 15) - 8
        return int(base_score * factor) + adjustment

    # Unused but plausible-looking diagnostic call
    preliminary_diag = process_readings(calibrated_temps[:3], 0.5)

    final_diagnostic = process_readings(filtered_data, calibration_factor)

    # Redundant print to mislead about output importance
    # print(f"Legacy normalized: {normalized}")
    # print(f"System log entries: {len(system_log)}")
    
    # Critical output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Entry point with seeded behavior
if __name__ == "__main__":
    temps = [96.1, 88.3, 72.4, 99.0, 85.6, 60.2, 91.8, 102.0]
    threshold_values = [90.0, 92.0, 88.0]
    result = analyze_system_status(temps, threshold_values, mode='safe')
