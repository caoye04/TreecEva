def main():
    # Sensor readings in arbitrary units
    sensor_a = 17
    sensor_b = 23
    calibration_factor = 0.85

    # Derived measurements
    combined_signal = (sensor_a + sensor_b) * calibration_factor
    
    # Efficiency calculation using lambda
    efficiency_curve = lambda x: 0.5 + (x / 100) ** 0.5
    efficiency = efficiency_curve(combined_signal)

    # Power transformation
    raw_power = combined_signal * 1.2
    energy_output = raw_power * efficiency

    # Secondary calculations (distractor variables)
    peak_load = sensor_a * sensor_b / 10
    system_margin = peak_load - raw_power  # Not used in main path

    # Final adjustment step
    final_adjustment = lambda: energy_output * 0.95
    energy_output = final_adjustment()  # Key assignment point

    print(f"Result: {energy_output}")

if __name__ == "__main__":
    main()