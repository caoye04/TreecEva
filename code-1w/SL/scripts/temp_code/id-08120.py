def analyze_temperature_patterns(data, threshold=30):
    high_temp_days = []
    temp_sum = 0
    count = 0
    for i, temp in enumerate(data):
        if temp > threshold:
            high_temp_days.append(i)
        temp_sum += temp
        count += 1
    
    avg_temp = temp_sum / count if count else 0
    return high_temp_days, avg_temp


def transform_readings(raw_readings):
    scaled = [round(x * 1.8 + 32, 2) for x in raw_readings]  # to Fahrenheit
    reversed_slice = scaled[::-1]
    mid_segment = reversed_slice[2:7]
    offset_correction = sum(mid_segment) / len(mid_segment)
    corrected = [val - offset_correction for val in scaled]
    return corrected


def calculate_adjusted_score(metrics):
    base = sum(metrics)
    penalty = 0
    for i, val in enumerate(metrics):
        if i % 2 == 0 and val > 50:
            penalty += 5
    adjustment_factor = 0.9 if len(metrics) > 6 else 1.0
    return int((base - penalty) * adjustment_factor)

# Simulated sensor data (Celsius)
sensor_log = [22.3, 31.5, 28.0, 33.1, 25.7, 36.8, 29.4, 26.9]

# Irrelevant processing branch
dummy_aggregates = {}
total_energy_est = 0
for idx, val in enumerate(sensor_log):
    energy_approx = val ** 2 * 0.05
    total_energy_est += energy_approx
    if idx not in [0, 2, 4]:
        dummy_aggregates[f'entry_{idx}'] = energy_approx

# Main processing chain
processed_data = transform_readings(sensor_log)
outlier_indices, mean_temp = analyze_temperature_patterns(processed_data, threshold=85)

# Dummy filtering (no effect on result)
filtered_metrics = [x for x in processed_data if x > 70]
placeholder_dict = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
side_calculation = sum([v**2 for k, v in placeholder_dict.items()])  # unused

final_score = calculate_adjusted_score(processed_data)
print(f'Result: {final_score}')