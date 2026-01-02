import itertools

# Sensor readings in microvolts from a neural monitoring device
clean_readings = [34.2, 45.1, 12.8, 76.3, 23.9, 67.4, 55.0, 89.6]
offset = 1.5
adjusted_readings = [x + offset for x in clean_readings]

# Filter out readings below baseline threshold
temperature_factor = 0.88
baseline_adjusted = [x * temperature_factor for x in adjusted_readings]
filtered_readings = [x for x in baseline_adjusted if x > 40.0]

# Irrelevant distraction: counting valid hours (not used in final result)
valid_hours = 0
for hour in range(8):
    if hour < len(filtered_readings):
        valid_hours += 1

# Core computation step
event_markers = list(itertools.compress(clean_readings, [r > 40 for r in clean_readings]))
energy_threshold = max(filtered_readings)

print(f"Result: {energy_threshold}")