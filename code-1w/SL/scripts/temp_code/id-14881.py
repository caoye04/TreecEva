from itertools import compress

def main():
    # Sensor data from a solar panel array (efficiency readings in %)
    base_efficiencies = [18.2, 19.1, 17.8, 20.0, 16.5, 19.4, 18.3]
    operating_conditions = [True, True, False, True, False, True, True]  # Normal operation mask

    # Filter valid readings using condition mask
    valid_readings = list(compress(base_efficiencies, operating_conditions))

    # Baseline adjustment for temperature drift (empirical compensation)
    adjusted_readings = [r * 0.985 for r in valid_readings]

    # Calculate overall system efficiency
    total_efficiency = sum(adjusted_readings)
    reading_count = len(adjusted_readings)
    energy_output = total_efficiency / reading_count if reading_count > 0 else 0.0

    # Irrelevant auxiliary calculation (minor distraction)
    peak_efficiency = max(base_efficiencies) if base_efficiencies else 0.0
    efficiency_bands = {"low": 17.0, "optimal": 18.5, "high": 19.5}

    print(f"Result: {energy_output}")

if __name__ == "__main__":
    main()