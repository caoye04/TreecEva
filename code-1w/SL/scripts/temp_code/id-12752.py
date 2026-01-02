import math

# System calibration constants (irrelevant to final result)
def calibrate_sensor(x):
    return (x ** 2 + 3 * x + 1) % 7

sensor_offsets = [calibrate_sensor(i) for i in range(8)]
adjusted_readings = [(s + 0.5) * 1.2 for s in sensor_offsets]
baseline_noise = sum(adjusted_readings) / len(adjusted_readings)

# Decoy function - looks important but unused in critical path
def legacy_power_model(voltage, current, harmonics=0.04):
    if voltage < 1.0:
        return 0
    efficiency = 0.87 - harmonics
    return (voltage * current) * efficiency

# Real computation chain begins
processor_load = 784  # Measured in MIPS units
overclock_factor = 1.18

# Simulated dynamic adjustment (distraction)
dynamic_scaling = True
if dynamic_scaling:
    processor_load = int(processor_load * overclock_factor)
    temp_threshold = 95
    if processor_load > 900:
        processor_load = 900  # Throttle to prevent overheating

cooling_efficiency = 0.83
ambient_compensation = 22.5

# Irrelevant environmental simulation
humidity_levels = [60 + 5 * math.sin(i / 2) for i in range(10)]
humidity_impact = max(humidity_levels) - min(humidity_levels)

# Distractor: unused fault tolerance matrix
fault_matrix = {
    'node_a': {'status': 1, 'retries': 3},
    'node_b': {'status': 0, 'retries': 0},
    'node_c': {'status': 1, 'retries': 1}
}
active_nodes = sum(1 for v in fault_matrix.values() if v['status'] == 1)

# Core calculation dependencies
modulation_index = (processor_load % 113) / 100.0
heat_dissipation = math.exp(-cooling_efficiency * 0.4)

# Conditional expression with red herring variables
stability_factor = 1.05 if humidity_impact > 8 else 0.95
feedback_gain = modulation_index * (1 + (ambient_compensation / 100))

# Secondary decoy calculation (never used)
theoretical_bandwidth = 0
for i in range(1, 6):
    theoretical_bandwidth += (i * processor_load) // (i + 2)

# Critical function that computes the answer
def calculate_thermal_output(load, efficiency):
    base_heat = load * 0.73
    adjusted_effort = base_heat * (1 - efficiency)
    
    # Nested logic with intermediate distractors
    if adjusted_effort > 200:
        safety_margin = 15.0
        stress_level = math.log(adjusted_effort)
        if stress_level > 5.2:
            recovery_damping = 0.88
            adjusted_effort *= recovery_damping
    else:
        safety_margin = 5.0
        stress_level = 0
        recovery_damping = 1.0
    
    # Final composite formula
    non_linear_correction = math.sqrt(adjusted_effort) * feedback_gain
    final_output = adjusted_effort + non_linear_correction - safety_margin
    
    # Dead code branch - looks like it modifies something but doesn't affect output
    if final_output < 0:
        print("Negative output detected")  # Unreachable due to input constraints
    
    return final_output

# Key statement
thermal_capacity = calculate_thermal_output(processor_load, cooling_efficiency)

# Output result as required
print(f"Result: {thermal_capacity}")