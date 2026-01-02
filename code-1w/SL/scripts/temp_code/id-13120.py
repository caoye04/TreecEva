def analyze_signal(strength, calibration_factor):
    adjusted = strength * calibration_factor
    normalized = max(adjusted, 0.1)
    return normalized

offset = 3
raw_readings = [1.5, 2.0, -1.0, 4.5]

# Filter and process valid signals
clean_signals = list(filter(lambda x: x > 0, raw_readings))
total_power = sum([analyze_signal(val, 1.2) for val in clean_signals])

energy_baseline = total_power / len(clean_signals)
energy_threshold = round(energy_baseline * 1.5) if energy_baseline > 2 else round(energy_baseline * 2)

apply_calibration = lambda offset, threshold: threshold + offset if threshold < 10 else threshold - offset
final_diagnostic = apply_calibration(offset, energy_threshold)

print(f"Result: {energy_threshold}")