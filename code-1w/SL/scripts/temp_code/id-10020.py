import math

# Simulated sensor readings over time
time_series_data = [102, 95, 110, 90, 120, 85, 130, 75, 140, 60]

# Noise floor and calibration offsets (some are red herrings)
calibration_factor = 1.05
noise_floor = 50
offset_x = 2.3
offset_y = -1.7
offset_z = 0.9

# Threshold configuration for signal classification
threshold_map = {
    'low': 80,
    'medium': 100,
    'high': 120
}

# Auxiliary diagnostic counters (mostly unused later)
diagnostic_count_a = 0
diagnostic_count_b = 0
diagnostic_count_c = 0

# Step 1: Filter out values below noise floor (but expressed indirectly)
valid_range_mask = [x > noise_floor for x in time_series_data]
filtered_data = [time_series_data[i] for i in range(len(time_series_data)) if valid_range_mask[i]]

# Misleading transformation using irrelevant offsets
temp_shifted = [x + offset_x - offset_y for x in filtered_data]  # Not used in final logic
diagnostic_count_a = sum(1 for x in temp_shifted if x > 100)  # Distractor counter

# Step 2: Apply effective calibration (only this matters)
calibrated_readings = [x * calibration_factor for x in filtered_data]

# Step 3: Classify each reading based on dynamic thresholds
def classify_signal(value, thresholds):
    if value < thresholds['medium']:
        return 'normal'
    elif value < thresholds['high']:
        return 'elevated'
    else:
        return 'critical'

# Step 4: Count transitions between states (extra complexity)
state_sequence = [classify_signal(x, threshold_map) for x in calibrated_readings]
transition_count = 0
for i in range(1, len(state_sequence)):
    if state_sequence[i] != state_sequence[i-1]:
        transition_count += 1

# Step 5: Compute weighted impact score (semi-relevant computation)
impact_weights = {'normal': 1, 'elevated': 2, 'critical': 4}
raw_impact_score = sum(impact_weights[state] for state in state_sequence)

# Step 6: Normalize score by number of transitions (distractor calculation)
normalized_diagnostic = raw_impact_score / (transition_count + 1) if transition_count > 0 else raw_impact_score
diagnostic_count_c = int(normalized_diagnostic)  # Another dead-end variable

# Step 7: Actual core logic — find max calibrated value above high threshold
above_high = [x for x in calibrated_readings if x >= threshold_map['high']]
peak_value = max(above_high) if above_high else 0

# Step 8: Final output depends only on peak_value and map scaling
scaling_factor = len(threshold_map)  # 3 categories
final_output = int(peak_value // scaling_factor * 2)

# Output result
print(f"Result: {final_output}")