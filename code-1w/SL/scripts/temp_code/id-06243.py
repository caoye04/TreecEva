def main():
    # Simulate sensor readings with noise and valid data
    raw_readings = [102, 105, 98, 110, 103, 97, 108, 101]
    calibration_factor = 0.97
    adjusted_readings = [x * calibration_factor for x in raw_readings]

    # Filter out potential outliers using a lambda
    valid_range = lambda x: 99 <= x <= 107
    filtered_readings = [x for x in adjusted_readings if valid_range(x)]

    # Misleading computation: temperature compensation (not used in final score)
    base_temp = 23.5
    temp_drift = 0.18
    compensated_values = [x - (base_temp * temp_drift) for x in raw_readings]  # Irrelevant

    # Statistical summary (some values will be used, others not)
    mean_val = sum(filtered_readings) / len(filtered_readings)
    variance_proxy = sum((x - mean_val) ** 2 for x in filtered_readings) / len(filtered_readings)
    stability_index = 1 / (1 + variance_proxy)  # Measure of consistency

    # Data grouping by threshold (using dictionary operations)
    group_data = {'stable': [], 'variable': []}
    threshold = mean_val - 2
    for val in filtered_readings:
        key = 'stable' if val >= threshold else 'variable'
        group_data[key].append(val)

    # Dead code path: unused classification
    def classify_noise(level):
        if level < 0.5:
            return 'low'
        elif level < 1.0:
            return 'medium'
        else:
            return 'high'

    noise_category = classify_noise(variance_proxy)  # Computed but unused

    # Secondary distraction: peak detection
    peaks = [i for i in range(1, len(raw_readings)-1)
             if raw_readings[i] > raw_readings[i-1] and raw_readings[i] > raw_readings[i+1]]
    peak_count_analysis = len(peaks)  # Not used

    # Core logic: calculate final score based on group sizes and stability
    def calculate_final(data_dict):
        stable_size = len(data_dict['stable'])
        variable_size = len(data_dict['variable'])
        ratio = stable_size / (stable_size + variable_size) if (stable_size + variable_size) > 0 else 0
        return int(ratio * 100 * stability_index)  # Integer score

    final_score = calculate_final(group_data)

    # Print result as required
    print(f"Result: {final_score}")

if __name__ == '__main__':
    main()