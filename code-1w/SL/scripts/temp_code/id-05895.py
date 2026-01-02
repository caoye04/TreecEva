def main():
    signal_readings = [0.85, 1.02, 0.77, 1.34]
    base_frequency = 440
    calibration_factor = sum(signal_readings) / len(signal_readings)
    
    adjust_gain = lambda x: x * 1.2 if x < 1.0 else x * 0.9
    calibrated_readings = [adjust_gain(x) for x in signal_readings]
    
    total_energy = sum([r ** 2 for r in calibrated_readings])
    
    def apply_calibration(factor):
        return int((factor * total_energy) + 50)

    energy_threshold = apply_calibration(calibration_factor)
    
    # Irrelevant tracking variable (minimal distraction)
    reading_count = len(signal_readings)
    
    print(f"Result: {energy_threshold}")

if __name__ == "__main__":
    main()