from collections import defaultdict

# Sensor data aggregation for system diagnostics
telemetry_data = [78, 85, 90, 70, 88]
threshold = 82

efficiency_counts = defaultdict(int)
stability_index = 0
for reading in telemetry_data:
    if reading >= threshold:
        efficiency_counts['high'] += 1
    else:
        efficiency_counts['low'] += 1

# Compute derived metrics
efficiency_score = efficiency_counts['high'] * 10
stability_index = sum(telemetry_data) / len(telemetry_data)

# Calculate pressure adjustment based on distribution
pressure_adjustment = efficiency_counts['high'] * efficiency_counts['low']

# Final diagnostic rating using conditional expression
final_rating = efficiency_score if pressure_adjustment > 80 else stability_index

# Irrelevant auxiliary variable (minor distraction)
aux_offset = 5  

Result: pressure_adjustment