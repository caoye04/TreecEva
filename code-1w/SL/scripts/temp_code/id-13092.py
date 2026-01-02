def analyze_temperature_profiles(raw_temps):
    # Filter valid temperature ranges (in Kelvin)
    valid_temps = [t for t in raw_temps if 273 <= t <= 373]
    temp_variance = sum((t - sum(valid_temps)/len(valid_temps))**2 for t in valid_temps) / len(valid_temps) if valid_temps else 0
    return valid_temps, temp_variance


def compute_pressure_adjustment(base_pressure, altitude):
    # Simulate pressure decay with altitude (simplified)
    adjustment_factor = 1 - (altitude / 10000)
    adjusted_pressure = base_pressure * adjustment_factor
    return adjusted_pressure


def calculate_reaction_efficiency(temps, pressure):
    if not temps:
        return 0.0
    avg_temp = sum(temps) / len(temps)
    efficiency = (avg_temp * pressure) / 10000
    # Artificial dampening factor
    dampen = len(temps) > 5
    efficiency *= 0.9 if dampen else 1.0
    return efficiency


def calculate_optimal_yield(data):
    raw_temperatures = data['temperatures']
    altitude = data['altitude_km']
    base_pressure = data['base_pressure_kpa']
    impurities = data['impurities']

    # Step 1: Process temperature profiles
    filtered_temps, variance = analyze_temperature_profiles(raw_temperatures)

    # Irrelevant computation: impurity analysis (not used later)
    impurity_set = set(impurities)
    secondary_impurities = {x for x in impurity_set if 'S' in x}
    high_risk_count = len([x for x in impurities if 'H2S' in x])  # dead-end calculation

    # Step 2: Adjust pressure for altitude
    corrected_pressure = compute_pressure_adjustment(base_pressure, altitude)

    # Step 3: Calculate efficiency from thermal and pressure data
    efficiency = calculate_reaction_efficiency(filtered_temps, corrected_pressure)

    # Step 4: Apply correction factors based on sensor count (distractor)
    sensor_readings = data['sensors']
    active_sensors = [s for s in sensor_readings if s > 0]
    redundancy_factor = len(active_sensors) / len(sensor_readings) if sensor_readings else 1

    # Step 5: Compute preliminary yield
    preliminary_yield = efficiency * redundancy_factor * 100

    # Step 6: Normalize using set difference (semi-relevant)
    expected_sensors = {1, 2, 3, 4, 5}
    active_sensor_set = set(active_sensors)
    missing_sensors = expected_sensors - active_sensor_set
    missing_penalty = 0.95 ** len(missing_sensors)  # small penalty

    # Step 7: Final yield calculation
    final_yield = preliminary_yield * missing_penalty

    # Distractor: unused health metrics
    system_health = sum(1 for s in active_sensors if s > 2) / len(expected_sensors)
    calibration_offset = 0.05 * len(variance.__repr__())  # meaningless but plausible

    return final_yield

# Input data
input_data = {
    'temperatures': [280, 295, 310, 305, 290, 315, 320],
    'altitude_km': 1200,
    'base_pressure_kpa': 101.3,
    'impurities': ['CO', 'H2S', 'SO2', 'CO'],
    'sensors': [3, 1, 0, 4, 2]
}

# Execution point of interest
processed_data = input_data
final_yield = calculate_optimal_yield(processed_data)
print(f"Result: {final_yield}")