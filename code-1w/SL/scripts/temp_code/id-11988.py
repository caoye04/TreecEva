from itertools import cycle

# Simulate multi-stage industrial processing with quality control
raw_input_batch = 4860
contamination_level = 0.04
initial_purity = 1 - contamination_level

# Stage 1: Mechanical preprocessing
grind_efficiency = 0.92
preprocessed_material = raw_input_batch * initial_purity * grind_efficiency

# Misleading intermediate calculation (distractor) - energy consumption not used later
total_energy_used = raw_input_batch * 2.3 + 175
energy_per_unit = total_energy_used / raw_input_batch if raw_input_batch > 0 else 0

# Stage 2: Chemical treatment with yield loss
chemical_reaction_yield = 0.88
treated_material = preprocessed_material * chemical_reaction_yield

# Quality sampling and batch adjustment (semi-relevant)
sample_count = 12
defect_rate = sum([0.05, 0.03, 0.06, 0.04, 0.05]) / sample_count
adjusted_for_defects = treated_material * (1 - defect_rate)

# Stage 3: Crystallization and drying
thermal_loss_rate = 0.07
dried_crystals = adjusted_for_defects * (1 - thermal_loss_rate)

# Packaging inefficiency (distractor - unused path)
packaging_error_margin = 0.012
theoretical_final_units = int(dried_crystals // 100)  # per 100g unit
actual_packaged = theoretical_final_units * (1 - packaging_error_margin)

# Environmental efficiency factor based on temperature cycles (relevant)
temperature_fluctuations = [22.1, 23.5, 21.9, 24.0, 22.8]
avg_temp_deviation = abs(sum(temperature_fluctuations) / len(temperature_fluctuations) - 22.5)
efficiency_factor = 0.96 - (avg_temp_deviation * 0.02)

# Final output calibration using sensor drift correction (distractor)
sensor_readings = ['23.1', '22.8', '23.5', '24.2']
raw_offsets = [float(x) - 23.0 for x in sensor_readings]
mean_offset = sum(raw_offsets) / len(raw_offsets)
adjusted_readings = [round(float(x) - mean_offset, 2) for x in sensor_readings]
final_drift_correction = abs(mean_offset) < 0.5  # boolean, not used

# Primary output stream
net_output = dried_crystals

# Key statement
final_yield = net_output * efficiency_factor

# Auxiliary string processing (distractor)
process_log = "Stage1_Complete;Stage2_Optimal;Stage3_Stable"
status_flags = process_log.split(';')
cleaned_flags = [flag.replace('_', '').lower() for flag in status_flags]
normalized_status = '_'.join(sorted(set([f[:6] for f in cleaned_flags])))
warning_count = len([c for c in cycle('AB') if c == 'A']) if 'unstable' in normalized_status else 0  # infinite cycle avoided via condition

# Output result
print(f"Result: {final_yield}")