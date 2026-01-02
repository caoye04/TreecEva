def analyze_temperatures(temp_readings):
    avg_temp = sum(temp_readings) / len(temp_readings)
    temp_deviation = [round(abs(t - avg_temp), 2) for t in temp_readings]
    high_stress_count = sum(1 for t in temp_readings if t > 30)
    return avg_temp, temp_deviation, high_stress_count


def normalize_values(raw_scores):
    max_val = max(raw_scores)
    min_val = min(raw_scores)
    normalized = [(x - min_val) / (max_val - min_val) * 100 for x in raw_scores]
    adjusted = [n + 10 for n in normalized]  # adjustment factor
    return adjusted


def calculate_rating(data_dict):
    ratings = []
    for key, values in data_dict.items():
        if 'temp' in key:
            mean, _, stress_events = analyze_temperatures(values)
            score = 100 - stress_events * 2.5
            ratings.append(score)
        elif 'sensor' in key:
            norm_vals = normalize_values(values)
            sensor_score = sum(norm_vals) / len(norm_vals)
            ratings.append(sensor_score / 10)
    
    # Irrelevant aggregation
    cumulative_total = 0
    for i, r in enumerate(ratings):
        cumulative_total += r * (i + 1)
    
    # Dummy logic with zip and enumerate
    indices = list(range(len(ratings)))
    paired = list(zip(indices, ratings))
    weight_map = {idx: 1.0 + 0.1 * idx for idx, _ in paired}
    
    final_rating = sum(ratings[i] * weight_map[i] for i in range(len(ratings)))
    return int(round(final_rating))

# Main execution block
raw_temperature_data = [25, 32, 35, 27, 29, 40, 31]
sensor_input_log = [150, 200, 175, 300, 225]

# Preprocessing with distractor steps
processed_data = {}
processed_data['temp_weekly'] = [t for t in raw_temperature_data if t >= 25]
processed_data['sensor_readings'] = [s for s in sensor_input_log]

# Dead code path - not affecting final result
if len(processed_data['sensor_readings']) > 10:
    processed_data['auxiliary'] = [0] * 5
else:
    debug_info = {'status': 'normal', 'bypassed': True}

# Another irrelevant dictionary operation
lookup_table = {i: chr(65 + i) for i in range(10)}
for k in lookup_table:
    lookup_table[k] = ord(lookup_table[k]) * 2

# Critical computation chain
baseline_shift = 5
scaling_factor = 1.0
interim_result = [x + baseline_shift for x in processed_data['temp_weekly']]

# Final rating calculation
final_score = calculate_rating(processed_data)
print(f"Result: {final_score}")