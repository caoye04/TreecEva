from collections import defaultdict, Counter

# Simulate sensor data with timestamps and types
timestamps = list(range(100, 200, 3))
sensor_types = ['temp', 'pressure', 'humidity', 'temp', 'flow']
raw_data = [(t, sensor_types[t % len(sensor_types)], (t * 1.5 + t % 7) / 10) for t in timestamps]

# Misleading preprocessing: irrelevant aggregation
misleading_aggregate = sum(d[2] * 0.1 for d in raw_data if 'p' in d[1])
offset_map = defaultdict(float)
for t, s_type, value in raw_data:
    offset_map[s_type] += value * 0.01

# Relevant filtering and transformation
filtered_data = [entry for entry in raw_data if entry[2] > 12.0 and entry[1] != 'flow']
sliced_data = filtered_data[::2]  # Take every second valid reading

daily_groups = defaultdict(list)
for t, s_type, value in sliced_data:
    day_bucket = t // 150
    daily_groups[day_bucket].append(value)

# Secondary distraction: unused statistical computation
temp_values = [v for t, s_type, v in raw_data if s_type == 'temp']
mean_temp = sum(temp_values) / len(temp_values)
variance_proxy = sum((v - mean_temp) ** 2 for v in temp_values) / len(temp_values)

# Core processing function
def process_readings(data_list):
    result = defaultdict(list)
    for t, s_type, val in data_list:
        normalized = val - (t % 10) * 0.1
        result[s_type].append(round(normalized, 3))
    return result

processed_data = process_readings(sliced_data)

# Distractor: complex but unused structure
compression_state = {}
for k, v_list in processed_data.items():
    compression_state[k] = {
        'window': len(v_list) // 2,
        'peak': max(v_list),
        'entropy_like': len(set(map(lambda x: int(x), v_list)))
    }

# Auxiliary scoring (partially relevant)
def calculate_bias_correction(values, base_factor=0.85):
    if len(values) < 3:
        return 0.0
    sorted_vals = sorted(values)
    trimmed = sorted_vals[1:-1]  # Remove outliers
    return (sum(trimmed) / len(trimmed)) * 0.15 * base_factor

# Main scoring logic
def compute_final_score(data_dict):
    score = 0.0
    bonus_tracker = defaultdict(int)
    
    for s_type, readings in data_dict.items():
        base_sum = sum(readings)
        if s_type == 'temp':
            correction = calculate_bias_correction(readings)
            score += base_sum * 1.2 + correction
        elif s_type == 'humidity':
            mid_values = readings[1:-1] if len(readings) > 2 else readings
            score += sum(mid_values) * 0.85
        else:  # pressure
            avg_val = sum(readings) / len(readings)
            count_bonus = len(readings) // 3
            bonus_tracker['pressure'] += count_bonus
            score += avg_val * 2.1
    
    # Final adjustment using bonus (only pressure contributes)
    total_bonus = sum(bonus_tracker.values()) * 10
    final_adjustment = total_bonus if total_bonus > 5 else 5
    return int(score) + final_adjustment

final_score = compute_final_score(processed_data)
print(f"Result: {final_score}")