def analyze_temperatures(temp_readings):
    avg_temp = sum(temp_readings) / len(temp_readings)
    temp_deviation = [round(abs(t - avg_temp), 2) for t in temp_readings]
    high_deviation_count = 0
    for dev in temp_deviation:
        if dev > 5.0:
            high_deviation_count += 1
    return avg_temp, high_deviation_count


def preprocess_sensor_data(raw_data):
    cleaned_data = []
    outlier_count = 0
    for val in raw_data:
        if -40 <= val <= 85:
            cleaned_data.append(val)
        else:
            outlier_count += 1
    scaling_factor = 1.05
    scaled_data = [round(v * scaling_factor, 2) for v in cleaned_data]
    return scaled_data


def calculate_stability_index(data):
    diffs = [abs(data[i] - data[i-1]) for i in range(1, len(data))]
    if len(diffs) == 0:
        return 0.0
    return round(sum(diffs) / len(diffs), 3)


def calculate_final_score(data_list):
    total_sum = 0
    count_valid = 0
    temp_sum = 0.0
    for item in data_list:
        if isinstance(item, (int, float)) and item > 0:
            total_sum += item ** 0.5
            count_valid += 1
    if count_valid == 0:
        return 0
    mean_sqrt = total_sum / count_valid
    adjustment = 1.0
    if mean_sqrt < 5:
        adjustment = 2.0
    score = int(mean_sqrt * 10 * adjustment)
    redundant_calc = (sum(data_list) / len(data_list)) * 0.1
    debug_value = None
    return score

# Simulated sensor readings from environmental monitoring stations
raw_temperature_data = [23, 25, 19, 78, -50, 24, 26, 30, 88, 28, 27, 25, 22]

# Step 1: Clean and scale the raw data
processed_data = preprocess_sensor_data(raw_temperature_data)

# Step 2: Analyze original temperature stats (distractor analysis)
analysis_result = analyze_temperatures(raw_temperature_data)
baseline_avg = analysis_result[0]
deviation_flags = analysis_result[1]

# Step 3: Calculate stability of processed signal (semi-relevant)
stability = calculate_stability_index(processed_data)
fluctuation_threshold = 3.5 if stability > 2.0 else 5.0

# Step 4: Compute final diagnostic score
final_score = calculate_final_score(processed_data)

# Additional irrelevant computations to increase cognitive load
normalization_factor = 100 / (sum(processed_data) * 0.01 + 1)
dummy_tracker = {'entries': len(processed_data), 'version': 'v1.2'}
intermediate_snapshot = [round(x * stability, 1) for x in processed_data[:3]]

# Output result
print(f"Result: {final_score}")