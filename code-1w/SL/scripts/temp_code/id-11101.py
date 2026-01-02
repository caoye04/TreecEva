import itertools

# Sensor simulation and diagnostic system with noise filtering and calibration
raw_readings = [107, 214, 153, 98, 241, 188, 73, 162, 134, 89, 205, 142]
noise_floor = 75
saturation_limit = 250
calibration_factor = 0.87
redundant_offset = 42  # Unused red herring
phantom_threshold = 199  # Misleading threshold for irrelevant logic

# Decoy statistical counters (distractors)
decoys = {'count_high': 0, 'sum_decoy': 0, 'flagged': False}
temp_snapshot = []

# Simulated environmental interference (irrelevant transformation)
environment_log = ['storm', 'clear', 'windy', 'fog', 'sunny']
impact_weights = {'storm': 0.6, 'windy': 0.8, 'fog': 0.7, 'clear': 1.0, 'sunny': 1.1}
weighted_impact = sum(impact_weights.get(log, 0.5) for log in environment_log)  # Dead-end computation

# Irrelevant string processing using required python feature
status_message = "System nominal: all sensors online"
status_tokens = status_message.upper().replace(':', '').split()
nominal_count = len([t for t in status_tokens if 'NOMINAL' in t])  # Red herring

# Real signal path begins: filter valid readings
valid_readings = [r for r in raw_readings if noise_floor < r < saturation_limit]

# Introduce distracting but unused list comprehension
_ = [x * 2 + 1 for x in range(len(valid_readings)) if x % 2 == 0]  # Unused

# Apply masking via bitwise operation (relevant preprocessing)
masked_readings = [v ^ 85 for v in valid_readings]  # Signal obfuscation

# Unrelated tuple unpacking distraction
data_point = (112, 'inactive', 3.14159)
reading_id, mode_flag, _ = data_point  # Partially used, mostly decoy

# Filter out phantom-like values (actually does nothing due to threshold)
filtered_data = [m for m in masked_readings if m <= phantom_threshold or m == 42]  # Includes logic that seems important

# Secondary distraction: attempt to normalize using unused method
normalization_cycle = list(itertools.accumulate([1, -1, 1, -1], lambda x, y: abs(x + y)))  # Complex but irrelevant

# Conditional trap: this block never executes due to data
if any(d > 200 for d in filtered_data):
    decoys['flagged'] = True
    temp_snapshot.extend([d * 1.1 for d in filtered_data])
else:
    temp_snapshot = [d * 0.98 for d in filtered_data]  # Actually used branch

# Real processing function with recursion (core concept)
def process_readings(data, factor, index=0):
    if index >= len(data):
        return 0
    # Recursive summation with calibration
    calibrated_value = round(data[index] * factor, 6)
    return calibrated_value + process_readings(data, factor, index + 1)

# Another distraction: min/max analysis on decoy data
extreme_values = (min(raw_readings), max(raw_readings))
spread = extreme_values[1] - extreme_values[0]
midpoint_guess = sum(extreme_values) / 2  # Unused analytics

# Key assignment - target of the query
final_diagnostic = process_readings(filtered_data, calibration_factor)

# Print required output
print(f"Result: {final_diagnostic}")