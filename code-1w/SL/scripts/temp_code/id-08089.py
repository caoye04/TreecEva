def main():
    # Sensor readings and calibration factors
    sensor_a = 23.5
    sensor_b = 17.8
    baseline = 42

    # Compute initial energy estimate using weighted average
    weights = [0.6, 0.4]
    raw_readings = [sensor_a, sensor_b]
    initial_energy = sum(w * r for w, r in zip(weights, raw_readings))

    # Apply environmental correction via lambda
    temp_factor = lambda t: 0.9 + 0.02 * t if t > 20 else 0.8
    corrected_energy = initial_energy * temp_factor(sensor_a)

    # Simulate system loss (fixed percentage)
    system_efficiency = 0.92
    energy_output = int(corrected_energy * system_efficiency + baseline)

    # Correction function for final calibration
    def apply_correction(val):
        adjustments = {'level_1': 0.98, 'level_2': 1.02}
        mode = 'level_1' if val < 100 else 'level_2'
        return val * adjustments[mode]

    final_adjustment = apply_correction(energy_output)
    
    print(f"Result: {energy_output}")

main()