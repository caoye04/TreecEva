def normalize_values(entries):
    total = sum(entries.values())
    normalized = {k: v / total for k, v in entries.items()}
    return normalized

# Simulate sensor data aggregation and weighted evaluation
data_map = {
    'sensor_a': 45,
    'sensor_b': 67,
    'sensor_c': 23,
    'sensor_d': 89,
    'sensor_e': 12
}

weights = {
    'sensor_a': 0.15,
    'sensor_b': 0.25,
    'sensor_c': 0.10,
    'sensor_d': 0.30,
    'sensor_e': 0.20
}

# Irrelevant transformation - string mapping (distractor)
sensor_labels = {k: k.upper().replace('_', '') for k in data_map.keys()}
dummy_conversion = {k: v.lower() for k, v in sensor_labels.items() if 'A' in v}

# Preprocessing step with side effect on data structure
adjusted_data = {}
for key, value in data_map.items():
    if value > 50:
        adjusted_data[key] = value * 0.9
    else:
        adjusted_data[key] = value * 1.1

# Normalization of adjusted values (used in computation)
norm_adjusted = normalize_values(adjusted_data)

# Additional irrelevant list processing (dead code path)
outlier_flags = []
for val in data_map.values():
    if val < 20 or val > 80:
        outlier_flags.append(True)
    else:
        outlier_flags.append(False)

# Unused helper function simulating diagnostic check
def diagnose_sensors(raw, adj):
    diffs = [abs(raw[k] - adj[k]) for k in raw]
    return sum(diffs) > 10

# Key computation chain
weighted_sum = 0.0
total_influence = 0.0

for sensor, base_value in adjusted_data.items():
    normalized_contribution = norm_adjusted[sensor]
    weight_factor = weights[sensor]
    
    # Intermediate metric not directly used later
    temp_impact_score = normalized_contribution * weight_factor * 100
    
    weighted_sum += base_value * weight_factor
    total_influence += weight_factor

# Secondary adjustment based on distribution skew
skew_metric = (max(norm_adjusted.values()) - min(norm_adjusted.values())) * 10
adjustment_penalty = 0.0
if skew_metric > 5.0:
    adjustment_penalty = skew_metric * 0.5

# Final scoring logic
efficiency_ratio = weighted_sum / total_influence
raw_offset = abs(data_map['sensor_a'] - data_map['sensor_c'])

# Critical statement
final_score = int(efficiency_ratio - adjustment_penalty + raw_offset // 4)

# Print result as required
print(f"Result: {final_score}")