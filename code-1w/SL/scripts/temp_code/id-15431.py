def preprocess_observations(raw):    
    adjusted = {}
    for k, v in raw.items():
        if v < 0: 
            adjusted[k] = 0
        else:
            adjusted[k] = v * 1.1
    return adjusted

raw_measurements = {'sector_a': 85, 'sector_b': 92, 'sector_c': -5, 'sector_d': 76}
filtered_data = preprocess_observations(raw_measurements)

stats_tracker = {"valid_count": 0, "total_sum": 0.0}
for val in filtered_data.values():
    stats_tracker["valid_count"] += 1
    stats_tracker["total_sum"] += val

baseline_offset = 5.5
normalization_factor = stats_tracker["valid_count"] * 0.9

# Simulate environmental corrections
correction_map = {}
for key in filtered_data:
    if 'a' in key:
        correction_map[key] = 1.05
    elif 'b' in key:
        correction_map[key] = 0.98
    else:
        correction_map[key] = 1.02

adjusted_readings = {}
temp_offset_store = []
for sector, reading in filtered_data.items():
    corrected = reading * correction_map[sector]
    adjusted_readings[sector] = round(corrected, 2)
    temp_offset_store.append(baseline_offset * 0.1)  # Irrelevant accumulation

# Compute efficiency with weighted contribution
weight_profile = {'sector_a': 0.3, 'sector_b': 0.4, 'sector_c': 0.1, 'sector_d': 0.2}
weighted_total = 0.0
for sec in adjusted_readings:
    weight = weight_profile[sec]
    contribution = adjusted_readings[sec] * weight
    weighted_total += contribution

# Auxiliary calculation (distraction)
avg_reading = stats_tracker["total_sum"] / len(filtered_data)
drift_compensation = avg_reading * 0.03  # Minor adjustment not used later

# Final efficiency model with threshold clamp
def calculate_harvest_efficiency(data_dict):
    efficiency_score = 0.0
    for s in data_dict:
        base_val = data_dict[s]
        if base_val > 90:
            efficiency_score += base_val * 0.6
        elif base_val > 75:
            efficiency_score += base_val * 0.5
        else:
            efficiency_score += base_val * 0.4
    if efficiency_score > 200:
        efficiency_score = efficiency_score * 0.95  # Apply bonus reduction
    return int(efficiency_score)

region_data = adjusted_readings
final_yield = calculate_harvest_efficiency(region_data)
print(f"Result: {final_yield}")