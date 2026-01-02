from itertools import combinations

# Simulate sensor data from agricultural zones
temperature_readings = [22, 25, 19, 24, 23]
humidity_levels = [60, 65, 58, 70, 63]
soil_nutrients = [88, 92, 85, 90, 87]

# Irrelevant auxiliary data (distractor)
wind_speeds = [12, 15, 10, 14, 13]  
dummy_flags = [True, False, True, False, True]

# Process valid growth windows
valid_windows = []
for i in range(len(temperature_readings)):
    if temperature_readings[i] >= 20 and humidity_levels[i] > 60:
        valid_windows.append(i)

# Accumulate nutrient trends (semi-relevant)
nutrient_trend = 0
for idx in valid_windows:
    nutrient_trend += soil_nutrients[idx] - 85

# Generate interaction effects between sensors (distraction via combinatorics)
interaction_pairs = list(combinations(range(len(valid_windows)), 2))
complexity_score = len(interaction_pairs) * 2  # Unused metric

# Simulate daily yield accumulation
yield_progress = []
current_base = 100
for day in valid_windows:
    adjustment = (temperature_readings[day] - 20) * 1.5
    humidity_factor = humidity_levels[day] / 100
    current_base *= (1 + adjustment / 100)
    current_base += humidity_factor * 5
    yield_progress.append(round(current_base, 2))

# Log efficiency per valid window
efficiency_log = {}
for i, day in enumerate(valid_windows):
    efficiency_log[day] = round(yield_progress[i] / (soil_nutrients[day] + 1), 3)

# Collect multi-source data
collected_data = []
for d in valid_windows:
    entry = {
        'day': d,
        'temp': temperature_readings[d],
        'humid': humidity_levels[d],
        'nutrient': soil_nutrients[d]
    }
    collected_data.append(entry)

# Misleading dead-end calculation (distractor)
avg_wind_in_window = sum(wind_speeds[i] for i in valid_windows) / len(valid_windows) if valid_windows else 0
turbulence_index = avg_wind_in_window ** 1.1  # Not used later

# Core computation function
def harvest_results(data_entries, efficiency_map):
    total_yield = 0.0
    for entry in data_entries:
        day = entry['day']
        base_yield = entry['nutrient'] * 0.75
        if day in efficiency_map:
            base_yield *= efficiency_map[day] * 1.2
        total_yield += base_yield
    return round(total_yield, 4)

# Final computation step
efficiency_correction = 0.0
for val in efficiency_log.values():
    efficiency_correction += val * 0.01  # Minor unused adjustment

final_yield = harvest_results(collected_data, efficiency_log)
print(f"Result: {final_yield}")