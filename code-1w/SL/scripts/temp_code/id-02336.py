from itertools import compress

def main():
    # Sensor data readings (simulated)
    temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9]
    pressure_readings = [101.3, 102.1, 100.7, 103.5, 101.8]

    # Threshold validation: normal operating range
    temp_normal = [22.0 <= t < 26.0 for t in temperature_readings]
    press_normal = [100.0 <= p < 105.0 for p in pressure_readings]

    # Combined validity mask using logical AND (element-wise)
    valid_readings = list(compress(temperature_readings, 
                                   [t and p for t, p in zip(temp_normal, press_normal)])
                          )

    # Calculate average of valid combined readings
    avg_temp = sum(valid_readings) / len(valid_readings) if valid_readings else 0.0

    # Performance metric based on stability (inverse of variance)
    variance = sum((t - avg_temp) ** 2 for t in valid_readings) / len(valid_readings)
    stability_score = 1 / (1 + variance)  # Smaller variance → higher score

    # External factor adjustment (unrelated but present)
    calibration_offset = 0.05  # Minor correction, not used in final logic
    device_uptime_hours = 127    # Operational metric, irrelevant to calculation

    # Final performance score with weighting
    base_score = avg_temp * 10
    final_score = base_score * stability_score

    print(f"Result: {final_score}")

    return final_score

if __name__ == "__main__":
    main()