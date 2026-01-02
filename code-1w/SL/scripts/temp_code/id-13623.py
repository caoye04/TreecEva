def analyze_sensor_data(data, min_val, max_val):
    count_valid = 0
    sum_filtered = 0
    temp_results = []
    outlier_count = 0

    for i, val in enumerate(data):
        if min_val <= val <= max_val:
            count_valid += 1
            sum_filtered += val
            temp_results.append(val * 0.9 + 5)
        else:
            outlier_count += 1
            temp_results.append(None)

    avg_valid = sum_filtered / count_valid if count_valid > 0 else 0
    return avg_valid, temp_results, outlier_count


def calculate_rating(readings, threshold):
    adjusted_values = []
    penalty_points = 0
    base_multiplier = 1.0

    high_freq_map = {}
    for idx, temp in enumerate(readings):
        adjusted = temp * 1.1 if temp < threshold else temp * 0.85
n        adjusted_values.append(round(adjusted, 2))

        band = int(temp // 5)
        high_freq_map[band] = high_freq_map.get(band, 0) + 1

    # Misleading aggregation
    dummy_sum = sum([v for v in high_freq_map.values() if v > 1])
    dummy_avg = dummy_sum / len(high_freq_map) if high_freq_map else 0

    # Real logic starts here
    above_threshold = [t for t in readings if t > threshold]
    below_or_equal = [t for t in readings if t <= threshold]

    score_a = len(above_threshold) * 3
    score_b = len(below_or_equal) * 2

    extreme_high = len([t for t in above_threshold if t > threshold + 10])
    penalty_points += extreme_high * 2

    # Use of zip and enumerate in a semi-relevant way
    stability_score = 0
    for i, (curr, next_val) in enumerate(zip(adjusted_values, adjusted_values[1:])):
        diff = abs(next_val - curr)
        if diff > 3:
            stability_score += 1

    final_rating = score_a + score_b - penalty_points - stability_score

    # Dead code - never used
    debug_info = {'iterations': i + 1, 'last_diff': diff, 'base': base_multiplier}

    scaling_factor = 1.5 if stability_score < 5 else 1.1
    final_score = int((final_rating * scaling_factor))

    return final_score

# Main execution
sensor_logs = [23.5, 26.1, 24.8, 28.3, 22.0, 30.2, 27.4, 25.0, 29.6]
temperature_readings = [int(x) for x in sensor_logs]  # Simulated discretization

# Irrelevant preprocessing
normalized = [round((t - min(sensor_logs)) / (max(sensor_logs) - min(sensor_logs)), 3) for t in sensor_logs]
duplicate_check = {k: v for k, v in enumerate(zip(sensor_logs, normalized))}

avg_temp, _, outliers = analyze_sensor_data(sensor_logs, 20, 35)

# Key statement
final_score = calculate_rating(temperature_readings, threshold=25)

print(f"Result: {final_score}")