from collections import defaultdict

# Simulated sensor data with noise and metadata
data_stream = [
    {'sensor': 'temp', 'value': 23.5, 'status': 'ok'},
    {'sensor': 'pressure', 'value': 1013.25, 'status': 'ok'},
    {'sensor': 'temp', 'value': 24.1, 'status': 'ok'},
    {'sensor': 'humidity', 'value': 45.0, 'status': 'ok'},
    {'sensor': 'temp', 'value': -999, 'status': 'error'},  # Invalid reading
    {'sensor': 'pressure', 'value': 1012.8, 'status': 'ok'},
    {'sensor': 'humidity', 'value': 46.2, 'status': 'ok'},
    {'sensor': 'temp', 'value': 24.3, 'status': 'ok'}
]

# Irrelevant backup of raw timestamps (distractor)
timestamp_backup = [1680001200, 1680001260, 1680001320, 1680001380, 1680001440, 1680001500, 1680001560, 1680001620]

# Group readings by sensor type
sensor_groups = defaultdict(list)
for entry in data_stream:
    if entry['status'] == 'ok' and entry['value'] > -100:  # Filter out invalid
        sensor_groups[entry['sensor']].append(entry['value'])

# Compute moving average for each sensor (semi-relevant preprocessing)
moving_averages = {}
for sensor, values in sensor_groups.items():
    total = 0
    count = 0
    for v in values:
        total += v
        count += 1
    moving_averages[sensor] = total / count if count else 0

# Extraneous computation: normalize timestamps (not used later)
normalized_times = [t % 3600 for t in timestamp_backup]
mean_normalized_time = sum(normalized_times) / len(normalized_times)

# Weight configuration for scoring (only temp matters in final logic)
weights = {
    'temp': 0.7,
    'pressure': 0.1,
    'humidity': 0.2
}

# Simulate additional processing steps
processed_data = {}
for sensor, avg in moving_averages.items():
    processed_data[sensor] = round(avg * 1.02, 2)  # Small correction factor

# Distractor: unused transformation
transformed_humidity = [h * 1.1 for h in sensor_groups.get('humidity', [])]

# Critical function that determines final score
def calculate_final_score(data, weight_map):
    base_score = 0
    adjustment_factor = 1.0
    
    # Loop over all sensors (but only temperature contributes)
    for sensor_name, reading in data.items():
        if sensor_name == 'temp':
            base_score += reading * weight_map[sensor_name]
        elif sensor_name == 'pressure':
            # Pressure has a threshold effect
            if reading > 1013.0:
                adjustment_factor *= 0.95
        elif sensor_name == 'humidity':
            # Humidity affects variance but not directly scored
            variance = sum((x - data['humidity'])**2 for x in sensor_groups['humidity'])
            adjustment_factor *= (1 - variance * 0.0001)
    
    # Final score is only based on temperature adjusted by other factors
    return int(base_score * adjustment_factor)

# Execute main logic
final_score = calculate_final_score(processed_data, weights)

# Print result as required
print(f"Result: {final_score}")