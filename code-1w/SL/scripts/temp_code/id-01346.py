from collections import defaultdict

# Simulate sensor data aggregation over time
sensor_data = [18.2, 19.1, 17.8, 20.3, 16.9, 18.7, 19.5]
data_counts = defaultdict(int)
for reading in sensor_data:
    data_counts[round(reading)] += 1

# Environmental compensation factor based on rounded trends
compensation_factor = sum(k * v for k, v in data_counts.items() if v > 1) or 1.0
temperature_baseline = max(sensor_data) - min(sensor_data)

# Phantom subsystem: vibration analysis (irrelevant to final result)
vibration_samples = [0.02, 0.05, 0.01, 0.03]
rms_vibration = sum(x**2 for x in vibration_samples)**0.5
alert_threshold = 0.04
vibration_alert = rms_vibration > alert_threshold

# Core system load simulation
processor_load = sum(sensor_data) / len(sensor_data)
overload_margin = processor_load * 0.15 if processor_load > 18.5 else 0
adjusted_load = processor_load + overload_margin

# Efficiency model with conditional expression
base_efficiency = 0.88
age_degradation = 0.07
system_age = 6
efficiency_factor = base_efficiency - (age_degradation if system_age > 5 else 0)
efficiency_factor = efficiency_factor * (0.9 if vibration_alert else 1.0)  # No impact since alert is False

# Secondary calculation: power fluctuation tracking (distractor)
power_readings = [processor_load * (1 + (i % 3) * 0.05) for i in range(5)]
fluctuation_index = max(power_readings) - min(power_readings)

# Key function using combined state
processed_units = int(sum(data_counts.keys()))
unit_ratio = processed_units / (compensation_factor + 1e-5)

# Thermal model core
def calculate_thermal_output(load, efficiency):
    base_output = load * 12.5
    adjusted_output = base_output / efficiency
    penalty_factor = 1.2 if adjusted_output > 240 else 1.0
    return adjusted_output * penalty_factor

# Critical assignment point
thermal_capacity = calculate_thermal_output(processor_load, efficiency_factor)

# Final print statement required
print(f"Result: {thermal_capacity}")