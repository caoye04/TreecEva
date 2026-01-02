from collections import defaultdict
from itertools import combinations

# Simulate sensor data aggregation across processing units
data_streams = [12, 15, 22, 18, 25, 30, 20, 14]
processing_efficiencies = []
temperature_fluctuations = [-1.2, 0.5, 2.1, -0.3, 1.8, 0.9, -2.0, 1.1]

# Auxiliary tracking for system diagnostics (mostly irrelevant)
diagnostic_log = defaultdict(int)
calibration_offset = 0
for i in range(len(data_streams)):
    if data_streams[i] > 20:
        diagnostic_log['high_load'] += 1
    elif data_streams[i] < 15:
        diagnostic_log['low_signal'] += 1
    calibration_offset += abs(temperature_fluctuations[i])

calibration_offset = round(calibration_offset, 1)

# Generate synthetic efficiency scores based on windowed averaging
window_size = 3
for start in range(len(data_streams) - window_size + 1):
    window = data_streams[start:start + window_size]
    avg_load = sum(window) / window_size
    stability_penalty = 0
    for j in range(window_size - 1):
        stability_penalty += abs(window[j] - window[j + 1])
    efficiency_score = avg_load - (stability_penalty * 0.5)
    processing_efficiencies.append(round(efficiency_score, 2))

# Extra computation: analyze all 2-element load patterns (distractor)
valid_pairs_count = 0
for pair in combinations(data_streams, 2):
    if abs(pair[0] - pair[1]) <= 10 and (pair[0] + pair[1]) % 2 == 0:
        valid_pairs_count += 1

# Misleading intermediate calculation
baseline_reference = sum(data_streams) // len(data_streams)
adjusted_baseline = baseline_reference * 0.9

# Key statement
peak_efficiency = max(processing_efficiencies)

# Dead code path - never executed but looks relevant
if False:
    fallback_mode = True
    peak_efficiency *= 0.8

# Print result for evaluation
print(f"Result: {peak_efficiency}")