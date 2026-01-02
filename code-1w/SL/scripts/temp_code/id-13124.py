def main():
    temperature = 23.5
    humidity = 68
    pressure = 1013.25

    # Initial energy level calculation based on environmental factors
    base_energy = temperature * 4.2 + (100 - humidity) * 0.8
    adjustment_factor = 1.0 if temperature > 20 else 0.9
    energy_level = base_energy * adjustment_factor

    baseline = 100.0
    calibration_offset = 5.5  # minor offset, not directly used in final logic

    # Conditional correction using lambda and ternary logic
    apply_correction = lambda condition, val: val * 1.15 if condition else val * 0.85
    final_adjustment = apply_correction(energy_level > baseline, energy_level)

    # Secondary derived value, not impacting result
    perceived_warmth = temperature + 0.5 * (humidity / 100)

    energy_threshold = int(final_adjustment)  # final discrete threshold

    # Print result for evaluation
    print(f"Result: {energy_threshold}")

if __name__ == "__main__":
    main()