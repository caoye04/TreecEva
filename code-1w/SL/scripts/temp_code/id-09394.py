from collections import defaultdict, Counter
import math

# Simulated sensor array data (temperature, pressure, humidity)
sensor_logs = [
    ('A7', [23.4, 101.3, 45]), ('B2', [25.1, 102.0, 47]), ('A7', [24.0, 101.8, 46]),
    ('C5', [22.8, 100.9, 44]), ('B2', [25.3, 102.2, 48]), ('D1', [26.5, 103.1, 50]),
    ('C5', [23.0, 101.0, 45]), ('A7', [24.2, 101.9, 47]), ('E9', [21.9, 100.5, 43])
]

# Irrelevant mapping - red herring
sensor_locations = {'A7': 'North Wing', 'B2': 'South Wing', 'C5': 'East Tower', 'D1': 'West Tower', 'E9': 'Roof Access'}
location_temperatures = defaultdict(float)

# Misleading aggregation path
for sensor_id, readings in sensor_logs:
    location_temperatures[sensor_locations[sensor_id]] += readings[0]

# Decoy function - never called
def compute_wind_chill(temp, wind_speed):
    return 13.12 + 0.6215*temp - 11.37*(wind_speed**0.16) + 0.3965*temp*(wind_speed**0.16)

# Another decoy: dead code path with complex logic
def analyze_turbulence(data_stream):
    turbulence_score = 0
    for entry in data_stream:
        if entry[1] > 102.0:
            turbulence_score += (entry[1] - 102.0) * 3
        elif entry[2] > 47:
            turbulence_score -= 1
    return max(turbulence_score, 0)

# Unused but plausible-looking transformation
normalized_logs = []
for sid, vals in sensor_logs:
    normalized_vals = [round(v / (sum(vals) * 0.01), 2) for v in vals]
    normalized_logs.append((sid, normalized_vals))

# Real processing begins: group by sensor
raw_groups = defaultdict(list)
for sensor_id, readings in sensor_logs:
    raw_groups[sensor_id].append(readings)

# Compute average readings per sensor
average_readings = {}
for sensor_id, records in raw_groups.items():
    temp_avg = sum(r[0] for r in records) / len(records)
    press_avg = sum(r[1] for r in records) / len(records)
    humid_avg = sum(r[2] for r in records) / len(records)
    average_readings[sensor_id] = [temp_avg, press_avg, humid_avg]

# Filtering criteria: only sensors with avg temp > 24.0
filtered_sensors = {k: v for k, v in average_readings.items() if v[0] > 24.0}
filtered_data = list(filtered_sensors.values())

# Red herring: bit manipulation with no effect
obfuscation_key = 0b110101
scrambled = (len(filtered_sensors) << 2) ^ obfuscation_key
baseline_offset = int(math.sqrt(scrambled * 3))  # Distractor calculation

# Fake calibration chain
historical_bias = [0.15, -0.08, 0.22]
calibration_cycle = 0
while calibration_cycle < 3:
    historical_bias = [b * 0.9 for b in historical_bias]
    calibration_cycle += 1

# Actual calibration factor used
calibration_factor = 1.08

# Core processing function
def process_readings(data, calib):
    total_score = 0.0
    for entry in data:
        temp, pressure, humidity = entry
        # Primary computation
        adjusted_temp = temp * calib
        pressure_ratio = pressure / 101.3
        humidity_index = (humidity - 40) / 10
        
        # Composite diagnostic formula
        score_component = adjusted_temp * (1 + pressure_ratio) * (1 + humidity_index * 0.1)
        total_score += score_component
    
    # Secondary adjustment based on count
    final_adjustment = total_score * (0.98 ** len(data))
    return round(final_adjustment, 4)

# Final computation
final_diagnostic = process_readings(filtered_data, calibration_factor)

# Output requirement
print(f"Target result: {final_diagnostic}")