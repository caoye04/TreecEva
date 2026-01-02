def main():
    base_signal = 145.6
    noise_floor = 23.4
    calibration_factor = 0.88

    # Signal processing pipeline
    filtered_signal = (base_signal - noise_floor) * calibration_factor

    # Define dynamic adjustment function
    adaptive_gain = lambda x: x * 1.2 if x < 100 else x * 0.9

    adjusted_level = adaptive_gain(filtered_signal)

    # Environmental compensation
    temperature_drift = 3.2
    compensated_value = adjusted_level - temperature_drift

    # Final non-linear correction
    def final_adjustment():
        nonlocal compensated_value
        if compensated_value > 120:
            compensated_value *= 0.95
        else:
            compensated_value += 10
        return compensated_value

    energy_threshold = final_adjustment()
    print(f"Result: {energy_threshold}")

if __name__ == "__main__":
    main()