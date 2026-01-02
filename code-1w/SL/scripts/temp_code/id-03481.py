from collections import defaultdict

# Simulated sensor data with noise and redundant entries
data = {
    'temperature': [23.5, 24.1, 22.9, 25.0, 23.8],
    'humidity': [45, 47, 50, 44, 46],
    'pressure': [1013, 1015, 1012, 1014, 1016]
}

# Irrelevant auxiliary data (distractor)
aux_data = defaultdict(int)
for key in data:
    aux_data[key + '_count'] += len(data[key])
aux_data['dummy_flag'] = 1

# Weight configuration for scoring (only some are actually used)
weights = {
    'temp_w': 0.4,
    'humid_w': 0.3,
    'press_w': 0.2,
    'bonus_w': 0.1  # Not used in final calculation
}

# Misleading intermediate computation (dead path)
temp_avg_raw = sum(data['temperature']) / len(data['temperature'])
humid_avg_raw = sum(data['humidity']) / len(data['humidity'])
press_avg_raw = sum(data['pressure']) / len(data['pressure'])

# Simulated calibration offset (unused)
calibration = {
    'temp_offset': -0.2,
    'humid_offset': 1.0
}

def normalize(lst):
    min_val, max_val = min(lst), max(lst)
    if max_val == min_val:
        return [0.5 for _ in lst]
    return [(x - min_val) / (max_val - min_val) for x in lst]

def calculate_final_score(sensor_data, weight_map):
    # Normalize relevant sensor streams
    norm_temp = normalize(sensor_data['temperature'])
    norm_humid = normalize(sensor_data['humidity'])
    norm_press = normalize(sensor_data['pressure'])
    
    # Compute average normalized values
    avg_temp = sum(norm_temp) / len(norm_temp)
    avg_humid = sum(norm_humid) / len(norm_humid)
    avg_press = sum(norm_press) / len(norm_press)
    
    # Apply only three weights; bonus_w is ignored
    weighted_temp = avg_temp * weight_map['temp_w']
    weighted_humid = avg_humid * weight_map['humid_w']
    weighted_press = avg_press * weight_map['press_w']
    
    # Aggregate score (this is the actual answer path)
    total = weighted_temp + weighted_humid + weighted_press
    
    # Dead logic: unreachable under normal conditions (mild red herring)
    if False:
        total += 10  # never executed
    
    return round(total, 4)

# Key statement
final_score = calculate_final_score(data, weights)

# Print result as required
print(f"Result: {final_score}")