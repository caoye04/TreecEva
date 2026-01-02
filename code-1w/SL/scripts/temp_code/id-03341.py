from collections import defaultdict

# Simulate sensor data aggregation over time
def aggregate_sensor_readings(readings):
    aggregated = defaultdict(int)
    temp_cache = {}
    for sensor, value in readings:
        if sensor not in temp_cache:
            temp_cache[sensor] = 0
        temp_cache[sensor] += value % 97
        aggregated[sensor] += value // 3
    return dict(aggregated)

# Determine system state based on load profile
def evaluate_system_stability(load_profile):
    total_load = sum(load_profile)
    peak_load = max(load_profile) if load_profile else 0
    avg_load = total_load / len(load_profile) if load_profile else 0
    fluctuation_score = (peak_load - avg_load) * len(load_profile)
    return fluctuation_score < 150 and total_load > 50

# Main calculation function
def calculate_thermal_output(load_sequence, efficiency_ratio):
    base_heat = 0
    transient_spike = 0
    for i, load in enumerate(load_sequence):
        if i % 3 == 0:
            base_heat += load * 1.2
        elif i % 5 == 0:
            transient_spike += load * 0.5
        else:
            base_heat += load * 0.8
    adjusted_heat = base_heat * (1 - efficiency_ratio)
    penalty_factor = 1.1 if transient_spike > 20 else 1.0
    final_output = adjusted_heat * penalty_factor
    return int(final_output)

# Simulated input data
processor_readings = [
    ('cpu', 45), ('gpu', 60), ('cpu', 55), ('ram', 30),
    ('gpu', 70), ('cpu', 40), ('ram', 35), ('gpu', 65)
]

# Aggregating sensor values (distraction step - not directly used)
aggregated_data = aggregate_sensor_readings(processor_readings)
system_status = evaluate_system_stability([45, 55, 40, 70, 65])

# Core variables for thermal computation
processor_load = [45, 55, 40, 70, 65]
efficiency_factor = 0.15

# Red herring: unused intermediate calculations
idle_cycles = sum(100 - load for load in processor_load)
power_reserves = [load * 0.25 for load in processor_load if load > 50]
buffer_consumption = idle_cycles * 0.01

# Key statement
thermal_capacity = calculate_thermal_output(processor_load, efficiency_factor)

# Irrelevant conditional (dead code path)
if len(power_reserves) > 10:
    buffer_consumption *= 2

Result: {thermal_capacity}