def analyze_temperature_readings(raw_readings):
    cleaned_readings = []
    outlier_count = 0
    for reading in raw_readings:
        if -50 <= reading <= 150:
            cleaned_readings.append(reading)
        else:
            outlier_count += 1
    average_temp = sum(cleaned_readings) / len(cleaned_readings) if cleaned_readings else 0
    adjusted_avg = round(average_temp, 2)
    return cleaned_readings, adjusted_avg


def filter_by_variance(data, mean_val):
    variance_threshold = 25.0
    low_variance = []
    high_variance = []
    temp_sum = 0
    for val in data:
        temp_sum += (val - mean_val) ** 2
    variance = temp_sum / len(data) if data else 0
    for val in data:
        if abs(val - mean_val) < variance_threshold:
            low_variance.append(val)
        else:
            high_variance.append(val)
    return low_variance, set(high_variance), variance


def calculate_optimal_yield(values, exclusion_zone):
    base_yield = 0
    penalty = 0
    bonus = 0
    for v in values:
        if v in exclusion_zone:
            penalty += 3
        elif v > 85:
            base_yield += v * 0.8
            bonus += 1
        else:
            base_yield += v * 0.6
    final_yield = int(base_yield - penalty + bonus)
    return final_yield

# Main execution block
sensor_data = [95, 102, -60, 88, 155, 76, 91, 84, 103, 79, 82, -45, 90]
processed_data, avg_temp = analyze_temperature_readings(sensor_data)
low_var, high_var_set, observed_variance = filter_by_variance(processed_data, avg_temp)

# Simulate calibration offset
offset_correction = 0
for i in range(len(processed_data)):
    if processed_data[i] > avg_temp:
        offset_correction += 0.1
    else:
        offset_correction -= 0.05

threshold_set = {x for x in high_var_set if x > 90}
calibration_flag = len(threshold_set) > 2
temp_diagnostic = f"Calibration needed: {calibration_flag}"

# Dummy structure to increase cognitive load
stats_summary = {
    "count": len(processed_data),
    "mean": avg_temp,
    "variance": observed_variance,
    "outliers_removed": 3,
    "high_energy_count": len([x for x in processed_data if x > 90])
}

scaling_factor = 1.0
if stats_summary["variance"] > 20:
    scaling_factor = 0.95

# Modify threshold set with irrelevant logic
if calibration_flag:
    threshold_set.add(105)
else:
    threshold_set.discard(105)

intermediate_score = sum(threshold_set) / len(threshold_set) if threshold_set else 0

final_yield = calculate_optimal_yield(processed_data, threshold_set)
print(f"Result: {final_yield}")