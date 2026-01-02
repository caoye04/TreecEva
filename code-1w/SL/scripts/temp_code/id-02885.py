from itertools import combinations

# Simulate sensor data from a thermal regulation system
temperature_readings = [23.4, 25.1, 24.8, 26.3, 22.9, 25.6, 24.2, 23.8]
humidity_readings = [45, 47, 50, 44, 52, 46, 48, 51]

# Irrelevant auxiliary data (distractor)
pressure_readings = [101.3, 102.1, 100.9, 101.8, 103.2, 101.5, 102.0, 100.7]
dummy_indices = [i ** 2 for i in range(8) if i % 3 != 0]

# Preprocess: normalize temperature and filter stable zones
normalized_temps = [(t - min(temperature_readings)) / (max(temperature_readings) - min(temperature_readings)) for t in temperature_readings]
stable_zone_mask = [1 if 24 <= t <= 25 else 0 for t in temperature_readings]

# Extract paired environmental states
environmental_states = list(zip(normalized_temps, humidity_readings, stable_zone_mask))

# Distractor function that is defined but not used
def analyze_pressure_trend(data):
    return sum((data[i+1] - data[i]) for i in range(len(data)-1))

# Real processing: find all pairs of readings where humidity variation is significant
significant_pairs = []
for pair in combinations(range(len(humidity_readings)), 2):
    diff = abs(humidity_readings[pair[0]] - humidity_readings[pair[1]])
    if diff >= 5:
        significant_pairs.append(pair)

# Count overlapping stability and high-variance humidity
overlap_count = 0
for idx1, idx2 in significant_pairs:
    if stable_zone_mask[idx1] and stable_zone_mask[idx2]:
        overlap_count += 1

# Simulated processed data structure
processed_data = {
    'avg_normalized_temp': sum(normalized_temps) / len(normalized_temps),
    'high_var_pairs': len(significant_pairs),
    'overlap_stable': overlap_count,
    'base_entropy': 0.5 * len(significant_pairs) + 0.1 * len(normalized_temps)
}

# Auxiliary computation with red herring variables
baseline_effort = sum(pressure_readings) / len(pressure_readings)  # Unused
scaling_factor = 2 if processed_data['avg_normalized_temp'] > 0.5 else 1.5

# Core efficiency calculation
overlap_ratio = processed_data['overlap_stable'] / max(processed_data['high_var_pairs'], 1)
efficiency_score = 0

if processed_data['base_entropy'] > 10:
    adjustment = (processed_data['avg_normalized_temp'] + overlap_ratio) * scaling_factor
    efficiency_score = adjustment * 100
else:
    efficiency_score = processed_data['base_entropy'] * 10

efficiency_score = calculate_efficiency(processed_data)

# Final result printing
print(f"Result: {efficiency_score}")

# Helper function definition after usage (minor distraction)
def calculate_efficiency(data):
    base = data['avg_normalized_temp'] * 50
    bonus = data['overlap_stable'] * 3.5
    penalty = data['high_var_pairs'] * 0.8 if data['high_var_pairs'] > 10 else 0
    return base + bonus - penalty