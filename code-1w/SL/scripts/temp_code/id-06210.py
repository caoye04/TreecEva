from collections import defaultdict

# System thermal diagnostics for processor cores
core_logs = [
    [72, 75, 79, 74],
    [68, 70, 73, 71],
    [80, 85, 82, 84]
]

# Extract peak temperature from each core's log
load_temperatures = [max(log) for log in core_logs]

# Baseline safety thresholds per core (in degrees Celsius)
safety_thresholds = [85, 85, 90, 88]

# Calculate average threshold across all cores
avg_safety_rating = sum(safety_thresholds) / len(safety_thresholds)

# Operational rating is the minimum safe threshold minus average deviation
deviations = [abs(t - avg_safety_rating) for t in safety_thresholds]
avg_deviation = sum(deviations) / len(deviations)
operational_ratings = [thr - avg_deviation for thr in safety_thresholds]

# Key statement: compute thermal safety margin
thermal_margin = min(operational_ratings) - max(load_temperatures)

# Irrelevant helper: count occurrences above nominal
nominal_temp = 75
temp_counter = defaultdict(int)
for temp in load_temperatures:
    temp_counter['high' if temp > nominal_temp else 'normal'] += 1

print(f"Result: {thermal_margin}")