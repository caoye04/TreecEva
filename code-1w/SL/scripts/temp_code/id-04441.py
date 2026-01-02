def main():
    # Sensor data from turbine readings (temperature, pressure, rpm)
    raw_readings = [(300, 85, 1200), (310, 90, 1150), (295, 80, 1250)]

    # Filter out readings where temperature > 305 using lambda
    valid_readings = list(filter(lambda x: x[0] <= 305, raw_readings))

    # Extract rpm values and compute average
    rpms = [r[2] for r in valid_readings]
    avg_rpm = sum(rpms) / len(rpms)

    # Transform data into efficiency factors
    transformed_data = tuple(map(lambda x: (x[1] / 100) * (x[2] / avg_rpm), valid_readings))

    # Calculate final efficiency score
    def calculate_efficiency(data):
        base = 0.0
        for val in data:
            base += val ** 2
        return int(base * 10)  # Discretized energy output

    energy_output = calculate_efficiency(transformed_data)

    # Irrelevant auxiliary variable (minor distraction)
    status_flag = "NORMAL" if energy_output > 30 else "LOW"

    print(f"Result: {energy_output}")

main()