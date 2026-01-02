from collections import defaultdict
import math

# Simulate multi-stage thermal processing in material science
process_temperatures = [210, 240, 195, 260, 225]
pressure_levels = [32.5, 35.0, 30.8, 36.2, 33.4]
efficiency_factors = [0.88, 0.91, 0.85, 0.93, 0.89]

# Irrelevant data for distraction (distractor: dead code path)
legacy_modes = ['A', 'B', 'C']
mode_index_map = {mode: idx for idx, mode in enumerate(legacy_modes)}

# State tracker for non-critical diagnostics
status_log = defaultdict(int)
status_log['init'] = 1

# Auxiliary function that appears useful but is only partially used
apply_correction = lambda x, c: x * (1 + c / 100)

# Dummy transformation (distractor: misleading computation)
corrected_temps = []
for t in process_temperatures:
    adjusted = apply_correction(t, 2.5)  # Assumed calibration
    corrected_temps.append(round(adjusted))

# Secondary irrelevant calculation (distractor: unused physics-like formula)
stress_factor = 0
for i in range(len(pressure_levels)):
    stress_factor += pressure_levels[i] ** 1.1
stress_factor = stress_factor / len(pressure_levels)

# Core logic: compute stage weights based on efficiency and temp
stage_weights = []
for i in range(len(process_temperatures)):
    weight = process_temperatures[i] * efficiency_factors[i]
    stage_weights.append(weight)

# Normalize weights to simulate proportional contribution
total_weight = sum(stage_weights)
normalized_contributions = [w / total_weight for w in stage_weights]

# Calculate effective temperature using weighted average
effective_temperature = 0
for i in range(len(process_temperatures)):
    effective_temperature += process_temperatures[i] * normalized_contributions[i]

# Heat retention coefficient based on rounded comparison logic
retention_coeff = 0.0
if int(effective_temperature) % 5 == 0:
    retention_coeff = 0.75
elif int(effective_temperature) % 3 == 0:
    retention_coeff = 0.68
else:
    retention_coeff = 0.62

# Simulate thermal output with non-linear scaling
def calculate_thermal_output(stages):
    base_output = 0
    decay_factor = 1.0
    for stage in stages:
        # Exponential decay in contribution per stage
        contribution = stage['temp'] * stage['eff'] * decay_factor
        base_output += contribution
        decay_factor *= 0.9  # Diminishing return per stage
    
    # Apply retention and scale
    final_output = base_output * retention_coeff * 1.25
    return final_output

# Construct process stages (key structure)
process_stages = []
for i in range(5):
    stage_data = {
        'temp': process_temperatures[i],
        'pressure': pressure_levels[i],
        'eff': efficiency_factors[i],
        'index': i
    }
    process_stages.append(stage_data)

# Critical assignment point
thermal_capacity = calculate_thermal_output(process_stages)

# Print result for evaluation
print(f"Result: {thermal_capacity}")