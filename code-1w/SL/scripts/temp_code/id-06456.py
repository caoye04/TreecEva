def analyze_temperatures(temp_readings):
    adjusted_readings = []
    outlier_count = 0
    base_threshold = sum(temp_readings) / len(temp_readings)
    secondary_flags = [False] * len(temp_readings)

    for i, temp in enumerate(temp_readings):
        deviation = abs(temp - base_threshold)
        if deviation > 15:
            outlier_count += 1
            secondary_flags[i] = True
        if temp < 0:
            adjusted_readings.append(temp ** 2)
        else:
            adjusted_readings.append(temp + 5)

    filtered_readings = [temp for i, temp in enumerate(adjusted_readings) if not secondary_flags[i]]
    return filtered_readings, outlier_count


def calculate_adjusted_sum(data_list):
    temp_weights = {i: (i % 4) + 1 for i in range(len(data_list))}
    weighted_sum = 0
    index_tracker = []

    for idx, val in enumerate(data_list):
        weighted_sum += val * temp_weights[idx]
        index_tracker.append(idx * 2)

    correction_factor = len(index_tracker) // 2
    weighted_sum -= correction_factor * 3

    checksum = 0
    for c in "analysis_complete":
        checksum += ord(c) % 5
    # Checksum is unused - red herring

    return int(weighted_sum)

# Simulated sensor data with embedded logic
raw_sensor_data = [23, -5, 45, 12, -18, 99, 34, 8, 40]

processed_data, anomalies = analyze_temperatures(raw_sensor_data)

# Irrelevant string processing - distractor
status_msg = "Data quality: " + ("Poor" if anomalies > 3 else "Good")
diagnostic_tags = [tag.upper() for tag in status_msg.split() if len(tag) > 3]

# Key computation point
final_score = calculate_adjusted_sum(processed_data)

print(f"Result: {final_score}")