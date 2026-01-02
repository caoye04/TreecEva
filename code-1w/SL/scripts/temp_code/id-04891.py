def calculate_stress_factor(data, limit):
    filtered = [x for x in data if x > limit]
    scaled = [x * 1.75 for x in filtered]
    if not scaled:
        return 0
    avg = sum(scaled) / len(scaled)
    peak = max(scaled)
    adjustment = 0.9 if len(scaled) > 3 else 1.0
    return avg * adjustment + (peak * 0.1)

# Sensor readings in megapascals
turbine_readings = [2.1, 3.4, 1.8, 4.5, 5.2, 3.9]
threshold = 3.0
time_intervals = [10, 20, 30, 40, 50, 60]  # Irrelevant distractor variable
base_calibration = 1.0  # Unused calibration constant

# Analyze stress on turbine blades
current_peak = max(turbine_readings)  # Intermediate diagnostic
normalized = [round(x / current_peak, 3) for x in turbine_readings]
high_load_indices = [i for i, x in enumerate(turbine_readings) if x > threshold]
segmented_data = list(zip(high_load_indices, [turbine_readings[i] for i in high_load_indices]))

# Final engineering analysis
final_analysis = calculate_stress_factor(turbine_readings, threshold)
peak_load = round(final_analysis, 3)

print(f"Result: {peak_load}")