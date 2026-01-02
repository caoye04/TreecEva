from itertools import cycle

# Simulate sensor data processing with calibration and noise filtering
def process_sensor_flux(raw_readings, calibration_factor):
    base_value = sum(r ** 0.5 for r in raw_readings if r > 0) * calibration_factor
    noise_floor = 0.78
    adjusted_base = int(base_value - noise_floor)

    # Irrelevant intermediate: signal harmonics (not used in final result)
    harmonics = [adjusted_base * (1.5 ** i) % 100 for i in range(3)]
    avg_harmonic = sum(harmonics) / len(harmonics)

    # Cycle simulation for device pulsing behavior
    thresholds = [5, 7, adjusted_base // 10]
    threshold = max(thresholds)
    cycle_source = cycle([1, 0, 1, 1])
    cycle_count = 0
    for _ in range(adjusted_base % 20):
        cycle_count += next(cycle_source)

    # Bitwise masking for hardware register alignment (semi-relevant)
    masked_cycle = cycle_count ^ 3 & 7
    base_multiplier = (masked_cycle + 2) * 1.5
    cycle_multiplier = (masked_cycle + 4) * 2.25

    # Dead code: temperature compensation (never applied)
    temp_ratio = 1.0
    if base_value > 30:
        temp_offset = 0.15
        temp_ratio = 1 - temp_offset

    # Key statement
    final_flux = adjusted_base * (cycle_multiplier if cycle_count > threshold else base_multiplier)
    
    # Extra red herring variables
    derived_energy = final_flux * 0.01 + 5.5
    normalized_output = round(derived_energy, 2)

    print(f"Result: {final_flux}")
    return final_flux

raw_data = [16, 25, 9, 0, 36, -4, 49]
calib = 1.8
result = process_sensor_flux(raw_data, calib)