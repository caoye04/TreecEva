import math

# Simulated sensor data from environmental monitoring stations
temperature_logs = [23.4, 24.1, 19.5, 22.8, 25.0, 26.3, 21.7, 18.9, 20.2, 24.4]
humidity_logs = [45, 48, 55, 60, 52, 47, 58, 62, 50, 46]
pressure_logs = [1013, 1015, 1012, 1009, 1016, 1018, 1014, 1011, 1010, 1017]

# Irrelevant backup data (distractor)
backup_timestamps = [1623456789, 1623456849, 1623456909, 1623456969, 1623457029,
                      1623457089, 1623457149, 1623457209, 1623457269, 1623457329]

# Misleading intermediate variables (red herring)
calibration_offset = 0.78
adjusted_temperatures = [t + calibration_offset for t in temperature_logs]
dummy_adjustment = sum(adjusted_temperatures) * 0.01  # Unused later

# Data transformation with set operations
stable_conditions = set()
for i in range(len(temperature_logs)):
    if 20 <= temperature_logs[i] <= 25 and 45 <= humidity_logs[i] <= 55:
        stable_conditions.add(i)

fluctuating_conditions = set(range(len(temperature_logs))) - stable_conditions

# Complex conditional filtering and aggregation
high_pressure_indices = {i for i, p in enumerate(pressure_logs) if p > 1014}
valid_diagnostic_set = stable_conditions & high_pressure_indices

# Multiple data structure manipulations
log_summary = []
for idx in sorted(valid_diagnostic_set):
    temp_factor = math.log(temperature_logs[idx] + 10)
    humid_factor = humidity_logs[idx] / 100
    pressure_ratio = pressure_logs[idx] / 1013.25
    composite_score = (temp_factor * 0.4) + (humid_factor * 0.3) + (pressure_ratio * 0.3)
    log_summary.append(composite_score)

# Decoy function - looks important but unused
def compute_stability_index(data_list):
    mean_val = sum(data_list) / len(data_list)
    variance = sum((x - mean_val) ** 2 for x in data_list) / len(data_list)
    return 1 / (1 + variance)

# Another decoy: dead code path
if len(log_summary) > 10:
    scaled_values = [x * 1.5 for x in log_summary]
    normalized = [x / max(scaled_values) for x in scaled_values]
else:
    # This block runs, but some operations are irrelevant
    temp_normalization = [x / 25.0 for x in temperature_logs]
    dummy_set = {round(t, 1) for t in temp_normalization}  # Not used

# Real processing begins here — nested logic with distractions
baseline_reference = 0.95
processed_logs = []
for score in log_summary:
    adjusted_score = score * baseline_reference
    if adjusted_score < 0.85:
        category = 'LOW'
    elif adjusted_score > 0.92:
        category = 'HIGH'
    else:
        category = 'MEDIUM'
    
    # Bit manipulation for encoding (actual use)
    encoded_flag = (len(category) << 2) ^ int(adjusted_score * 100)
    processed_logs.append((adjusted_score, encoded_flag, category))

# Secondary transformation: extract numeric components
extracted_flags = [flag for _, flag, _ in processed_logs]
flag_median = sorted(extracted_flags)[len(extracted_flags) // 2] if extracted_flags else 0

# Final analysis function with red herrings inside
def analyze_readings(log_entries):
    if not log_entries:
        return -1
    
    # Irrelevant aggregation
    total_encoded = sum(flag for _, flag, _ in log_entries)
    avg_encoded = total_encoded / len(log_entries)
    
    # Decoy statistical measure
    category_map = {'LOW': 1, 'MEDIUM': 2, 'HIGH': 3}
    category_vals = [category_map[cat] for _, _, cat in log_entries]
    mode_category = max(set(category_vals), key=category_vals.count)  # Unused
    
    # Core calculation — depends on prior filtering
    significant_entries = [score for score, flag, cat in log_entries if cat == 'HIGH']
    if not significant_entries:
        return round(avg_encoded / 100, 6)
    
    # Actual answer path
    base_value = sum(significant_entries) * 1000
    adjustment = flag_median % 7  # Depends on earlier bit ops
    final_value = base_value + adjustment
    
    # Dead code branch (misleading)
    if base_value < 50:
        final_value -= 20  # Never reached
    
    return int(final_value)

# Execution point of interest
final_diagnostic = analyze_readings(processed_logs)
print(f"Target result: {final_diagnostic}")