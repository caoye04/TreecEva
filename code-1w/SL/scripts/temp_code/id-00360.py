def preprocess_sensor_array(raw_readings):
    # Irrelevant preprocessing: normalize light and humidity (not used later)
    normalized_light = [max(0.0, min(1.0, x / 1000)) for x in raw_readings['light']]
    humidity_ratio = sum(raw_readings['humidity']) / len(raw_readings['humidity']) if raw_readings['humidity'] else 0
    return normalized_light  # Dead end return


def calculate_gradient(elevations, temps):
    # Core logic: compute average rate of temperature change per 100m elevation
    paired_data = list(zip(elevations, temps))
    gradient_sum = 0.0
    valid_intervals = 0
    
    for i in range(1, len(paired_data)):
        delta_elev = paired_data[i][0] - paired_data[i-1][0]
        delta_temp = paired_data[i][1] - paired_data[i-1][1]
        if delta_elev != 0:
            gradient_sum += delta_temp / (delta_elev / 100)  # °C per 100m
            valid_intervals += 1
    
    return round(gradient_sum / valid_intervals, 4) if valid_intervals else 0.0

# Simulated environmental sensor data
data_packet = {
    'elevation': [100, 250, 400, 550, 700],
    'temperature': [23.5, 21.2, 19.8, 17.3, 15.9],
    'light': [890, 950, 1100, 1080, 1020],
    'humidity': [65, 68, 72, 75, 70]
}

# Distractor: unused derived metrics
elevation_deltas = [data_packet['elevation'][i] - data_packet['elevation'][i-1] for i in range(1, len(data_packet['elevation']))]
temp_differences = [round(data_packet['temperature'][i] - data_packet['temperature'][i-1], 2) for i in range(1, len(data_packet['temperature']))]

# Red herring computation: thermal index using irrelevant formula
thermal_index = 0
for i, t in enumerate(data_packet['temperature']):
    thermal_index += t * (i + 1)  # Weighted sum with position (unused later)

# Slicing distraction: extract middle segment of data
mid_elev = data_packet['elevation'][1:-1]
mid_temp = data_packet['temperature'][1:-1]

# Dictionary manipulation: add redundant processed fields
data_packet['status'] = 'processed'
data_packet['metrics'] = {}
data_packet['metrics']['avg_temp'] = sum(data_packet['temperature']) / len(data_packet['temperature'])
data_packet['metrics']['total_ascent'] = sum(abs(data_packet['elevation'][i] - data_packet['elevation'][i-1]) for i in range(1, len(data_packet['elevation'])))

# Critical assignment
thermal_gradient = calculate_gradient(data_packet['elevation'], data_packet['temperature'])

# More distractors: tuple unpacking with unused values
extremes = (min(data_packet['temperature']), max(data_packet['temperature']))
lowest_temp, highest_temp = extremes

# Linear search for threshold (dead code path)
transition_level = -1
for i, elev in enumerate(data_packet['elevation']):
    if elev > 500:
        transition_level = i
        break

# Unused helper function
def adjust_for_pressure(temp, elev):
    return temp + (elev / 100) * 0.1  # Hypothetical correction

# Final output
print(f"Result: {thermal_gradient}")