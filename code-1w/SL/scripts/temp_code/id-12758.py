def calculate_final_score(log):
    total_entries = len(log)
    valid_count = 0
    temp_sum = 0
    outlier_threshold = 100
    penalty_factor = 0.1

    # Misleading pre-scan for outliers (not actually used in final logic)
    high_values = [v for v in log.values() if v > outlier_threshold]
    adjustment_offset = len(high_values) * 2

    # Actual processing: count valid entries and sum values above threshold
    min_valid_score = 50
    for key, value in log.items():
        if isinstance(key, str) and len(key) > 2 and value >= min_valid_score:
            valid_count += 1
            temp_sum += value

    # Red herring: unused transformation map
    transform_map = {i: i**2 for i in range(valid_count + 1) if i % 2 == 0}
    dummy_aggregate = sum(transform_map.values()) / (valid_count + 1) if valid_count else 0

    # Core calculation with distractor variables
    base_score = temp_sum / valid_count if valid_count else 0
    bonus = 10 if valid_count >= 3 else 0
    debug_trace = f'Score computed with {valid_count} entries'

    # Final score computation
    final_score = base_score + bonus - penalty_factor * adjustment_offset
    return int(final_score)

# Simulated dataset from sensor readings
sensor_data = {
    'sensor_A1': 45,
    'sensor_B2': 78,
    'sensor_C3': 120,
    'sensor_D4': 65,
    'err_001': 30,  # invalid name pattern
    'sensor_E5': 200,
    999: 55,         # invalid key type
    'sensor_F6': 40  # below min threshold
}

# Extraneous data structure manipulation
backup_copy = sensor_data.copy()
sorted_keys = sorted([k for k in sensor_data.keys() if isinstance(k, str)], reverse=True)
shifted_values = [(v + 5) % 100 for v in sensor_data.values()]

# Key execution point
final_score = calculate_final_score(sensor_data)

# Irrelevant conditional block (dead code path)
if False:
    final_score *= 2

print(f"Result: {final_score}")