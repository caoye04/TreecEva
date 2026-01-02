from collections import defaultdict, Counter
import math

# Simulated sensor data with noise and irrelevant tags
data = [
    {'type': 'temp', 'value': 25.3, 'sensor_id': 'S001', 'calib': 0.98},
    {'type': 'temp', 'value': 26.1, 'sensor_id': 'S002', 'calib': 1.02},
    {'type': 'pressure', 'value': 101.3, 'sensor_id': 'P001'},
    {'type': 'temp', 'value': 24.8, 'sensor_id': 'S003', 'calib': 0.99},
    {'type': 'humidity', 'value': 45.0, 'sensor_id': 'H001'},
    {'type': 'temp', 'value': 27.5, 'sensor_id': 'S001', 'calib': 0.98},
]

# Irrelevant statistical counters (distractors)
counts = defaultdict(int)
sensor_stats = defaultdict(list)
noise_floor = 0.05

for entry in data:
    counts[entry['type']] += 1
    if 'calib' in entry:
        calibrated = entry['value'] * entry['calib']
        sensor_stats[entry['sensor_id']].append(calibrated)
    else:
        sensor_stats[entry['sensor_id']].append(entry['value'])

# Dead code path: unused function for alternate processing
def legacy_transform(x):
    return x * 1.05 if x < 30 else x * 0.95

# Unused transformation matrix (red herring)
transform_matrix = [
    [1.0, -0.1, 0.05],
    [0.1, 1.0, -0.05],
    [-0.05, 0.1, 1.0]
]

# Weight configuration for relevant calculation
weights = {
    'temp': 0.6,
    'pressure': 0.3,
    'humidity': 0.1
}

# Decoy normalization function not used in final path
def normalize readings(reading_list):
    mean_val = sum(reading_list) / len(reading_list)
    return [r / mean_val for r in reading_list]

# Core logic hidden among distractions
def extract_temperature_readings(data_entries):
    temps = []
    for entry in data_entries:
        if entry['type'] == 'temp':
            if 'calib' in entry:
                temps.append(entry['value'] * entry['calib'])
            else:
                temps.append(entry['value'])
    return sorted(temps, reverse=True)[:3]  # Top 3 calibrated temperatures

# Secondary metric with misleading intermediate result
avg_pressure = sum(e['value'] for e in data if e['type'] == 'pressure') / counts['pressure'] if counts['pressure'] > 0 else 0

# Unused bit manipulation demo (distractor)
status_flag = 0b101010
status_flag ^= 0b111100
status_flag >>= 2

# Main processing function buried in complexity
def process_results(sensor_data, weight_map):
    # Extract and sort temperature values (main signal)
    temp_vals = extract_temperature_readings(sensor_data)
    
    # Compute weighted components
    temp_component = sum(temp_vals) * weight_map['temp']
    pressure_component = avg_pressure * weight_map['pressure']
    humidity_component = 50.0 * weight_map['humidity']  # Fixed reference
    
    # Composite score with case conversion red herring
    mode_flag = 'ACTIVE'.lower()
    if mode_flag == 'active':
        scaling_factor = 1.1
    else:
        scaling_factor = 0.9
    
    # Final aggregation
    raw_score = temp_component + pressure_component + humidity_component
    final_normalized = raw_score * scaling_factor
    
    # Apply artificial floor/ceiling (not actually binding here)
    final_clamped = max(10.0, min(final_normalized, 1000.0))
    
    # Key assignment: this is the target variable
    final_score = int(round(final_clamped))
    
    return final_score

# Execute main logic
result_temps = extract_temperature_readings(data)
sorted_sensors = sorted(sensor_stats.keys())  # Unused sorting operation
letter_codes = [s[:1].upper() for s in sorted_sensors]  # Case conversion distractor

temp_contrib = sum(result_temps) * weights['temp']

# Critical execution point
final_score = process_results(data, weights)

print(f"Result: {final_score}")