from collections import defaultdict
from itertools import combinations

# Simulated sensor readings and calibration data
temperature_readings = [23.5, 24.1, 22.9, 25.0, 23.8]
humidity_readings = [45, 47, 50, 44, 46]
pressure_readings = [1013, 1015, 1012, 1016, 1014]

# Irrelevant auxiliary data (distractor)
baseline_offsets = defaultdict(float)
for i in range(5):
    baseline_offsets[f'temp_{i}'] = temperature_readings[i] * 0.01

# Data aggregation with noise filtering
filtered_data = []
for t, h, p in zip(temperature_readings, humidity_readings, pressure_readings):
    if t > 23.0 and h < 50:
        filtered_data.append({'temp': t, 'humid': h, 'press': p})

# Weighted scoring setup
weights = {'temp': 0.5, 'humid': 0.3, 'press': 0.2}
base_thresholds = {'temp': 24.0, 'humid': 46, 'press': 1014}

# Misleading transformation (dead-end path)
transformed_scores = []
for entry in filtered_data:
    temp_dev = abs(entry['temp'] - base_thresholds['temp'])
    humid_dev = abs(entry['humid'] - base_thresholds['humid'])
    press_dev = abs(entry['press'] - base_thresholds['press'])
    score = (temp_dev * 2 + humid_dev * 1.5 + press_dev * 1) / 4.5
    transformed_scores.append(score)

# Actual processing: compute normalized deviations
results = []
for entry in filtered_data:
    norm_temp = (entry['temp'] - 20) / 5
    norm_humid = (entry['humid'] - 30) / 20
    norm_press = (entry['press'] - 1000) / 50
    results.append({'norm_temp': norm_temp, 'norm_humid': norm_humid, 'norm_press': norm_press})

# Red herring: unused combinatorial analysis
unused_pairs = list(combinations(results, 2))
complexity_factor = len(unused_pairs) * 0.1  # Not used later

# Core logic for final score calculation
def calculate_final_score(data_list, weight_dict):
    total_score = 0.0
    for record in data_list:
        # Apply weights to normalized values
        weighted_sum = (
            record['norm_temp'] * weight_dict['temp'] +
            record['norm_humid'] * weight_dict['humid'] +
            record['norm_press'] * weight_dict['press']
        )
        total_score += weighted_sum
    return int(total_score * 10)  # Discretize result

# Final computation
final_score = calculate_final_score(results, weights)

# Print result as required
print(f"Target result: {final_score}")