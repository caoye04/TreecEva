import math

# Simulated sensor data with timestamps and readings
data_log = [
    {'time': 100, 'temp': 23.5, 'active': True, 'count': 4},
    {'time': 105, 'temp': 24.1, 'active': True, 'count': 6},
    {'time': 110, 'temp': 22.8, 'active': False, 'count': 2},
    {'time': 115, 'temp': 25.3, 'active': True, 'count': 8},
    {'time': 120, 'temp': 24.9, 'active': True, 'count': 7}
]

# Irrelevant baseline constants for distraction
temp_threshold = 25.0
penalty_factor = 0.85
baseline_offset = 12.7

# Helper lambda to compute weighted contribution
weighted_contribution = lambda x, w: x * w

# Tracking variables (some are distractions)
cumulative_drift = 0.0
dropped_samples = 0
valid_entries = 0
summed_weights = 0.0
adjusted_total = 0.0
aux_counter = 0  # dead variable, not used in final logic

# Secondary structure for red herring processing
status_map = {}
for entry in data_log:
    key = "high" if entry['temp'] > temp_threshold else "low"
    status_map[entry['time']] = key

# Main processing with nested logic
aggregated_temp = 0.0
activity_flags = []
effective_count = 0

for record in data_log:
    # Irrelevant drift simulation
    cumulative_drift += abs(record['temp'] - 24.0) * 0.01
    
    if record['active']:
        valid_entries += 1
        aggregated_temp += record['temp']
        activity_flags.append(True)
        
        # Weighted contribution based on count
        weight = record['count'] / 10.0
        contribution = weighted_contribution(record['temp'], weight)
        adjusted_total += contribution
        summed_weights += weight
    else:
        dropped_samples += 1

# Dead code path - never executed due to data, but looks relevant
if len(activity_flags) > 10:
    aux_counter = math.floor(cumulative_drift * 2)

# Compute efficiency score using non-obvious formula
average_active_temp = aggregated_temp / valid_entries if valid_entries > 0 else 0
normalization_scale = math.log(summed_weights + 2)  # shift by 2 to avoid log(0)

# Final metric calculation
raw_efficiency = adjusted_total * normalization_scale
penalty_applied = raw_efficiency * penalty_factor if dropped_samples > 0 else raw_efficiency

# Key derived variable
intermediate_bias = (average_active_temp - 24.0) ** 2
efficiency_score = int(raw_efficiency - intermediate_bias * 10)

# Another red herring: character counting in status keys (unused)
char_count = sum(len(k) for k in status_map.values())

# Final processing function that encapsulates the result
def process_metrics(log):
    return efficiency_score

final_output = process_metrics(data_log)
print(f"Result: {efficiency_score}")