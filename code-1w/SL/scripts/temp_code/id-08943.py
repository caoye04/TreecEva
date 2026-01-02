def process_readings(data, thresholds):
    cumulative_score = 0
    penalty_offset = 0
    temp_log = []
    
    for i, (sensor_id, reading) in enumerate(data):
        if sensor_id not in thresholds:
            continue
        base_threshold = thresholds[sensor_id]
        deviation = abs(reading - base_threshold)
        
        # Irrelevant string processing (distractor)
        status_msg = f"Sensor {sensor_id} reading {reading}".upper().replace(" ", "_")
        temp_log.append(len(status_msg))
        
        if deviation > base_threshold * 0.2:
            if reading > base_threshold:
                cumulative_score += int(deviation // 2)
            else:
                penalty_offset += 1
        
    aggregate = sum(temp_log[:len(temp_log)//2 + 1]) if temp_log else 0
    final_value = cumulative_score - penalty_offset
    return final_value

# Sensor calibration data
raw_data = [
    ('A1', 45), ('B2', 67), ('A1', 52), ('C3', 89), ('B2', 63),
    ('D4', 101), ('A1', 48), ('E5', 33), ('C3', 85), ('F6', 110)
]

# Threshold configuration (per sensor)
threshold_map = {
    'A1': 50,
    'B2': 65,
    'C3': 80,
    'D4': 100,
    'E5': 30
}

# Filtering logic with zip and enumerate (mixed relevance)
valid_sensors = set(threshold_map.keys())
filtered_pairs = []
for idx, (sid, val) in enumerate(raw_data):
    if sid in valid_sensors:
        filtered_pairs.append((sid, val))

# Dead code path - irrelevant filtering (distractor)
duplicate_check = dict()
for sensor, value in filtered_pairs:
    if sensor in duplicate_check:
        duplicate_check[sensor] += 1
    else:
        duplicate_check[sensor] = 1

# Character frequency distraction (irrelevant to result)
log_tag = "CALIBRATION_DIAGNOSTIC"
char_count = {c: log_tag.count(c) for c in set(log_tag)}
special_sum = sum(v for k, v in char_count.items() if k in 'AEIOU')

# Actual processing pipeline
intermediate_stats = []
for tag, val in filtered_pairs:
    zipped_tmp = list(zip([val]*3, [tag]*3))
    intermediate_stats.append(len(zipped_tmp))

# Key computation step
final_diagnostic = process_readings(filtered_data=filtered_pairs, threshold_map=threshold_map)

# Print result
print(f"Result: {final_diagnostic}")