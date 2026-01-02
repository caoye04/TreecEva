from collections import defaultdict, Counter
import math

# Simulated sensor data with noise and redundant readings
data = [
    {'sensor': 'temp', 'value': 25.3, 'status': 'ok'},
    {'sensor': 'pressure', 'value': 1013.25, 'status': 'ok'},
    {'sensor': 'humidity', 'value': 45.0, 'status': 'ok'},
    {'sensor': 'temp', 'value': 26.1, 'status': 'ok'},
    {'sensor': 'temp', 'value': 24.9, 'status': 'faulty'},  # faulty reading
    {'sensor': 'light', 'value': 300, 'status': 'ok'},
    {'sensor': 'humidity', 'value': 47.2, 'status': 'ok'},
    {'sensor': 'pressure', 'value': 1012.8, 'status': 'ok'},
    {'sensor': 'co2', 'value': 410, 'status': 'ok'}
]

# Weight configuration for scoring (some are red herrings)
weights = {
    'temp': 0.3,
    'pressure': 0.1,
    'humidity': 0.2,
    'light': 0.05,
    'co2': 0.15,
    'o2': 0.1,  # unused sensor - distractor
    'voc': 0.05   # not present in data - decoy
}

# Irrelevant statistical tracker
stats_tracker = defaultdict(int)
reading_counter = Counter(entry['sensor'] for entry in data)

# Accumulate raw values by sensor type
temp_values = []
pressure_values = []
humidity_values = []
light_values = []
co2_values = []

for entry in data:
    sensor = entry['sensor']
    value = entry['value']
    status = entry['status']

    # Filter out faulty readings
    if status != 'ok':
        continue

    if sensor == 'temp':
        temp_values.append(value)
        stats_tracker['valid_temp_reads'] += 1
    elif sensor == 'pressure':
        pressure_values.append(value)
        stats_tracker['valid_pressure_reads'] += 1
    elif sensor == 'humidity':
        humidity_values.append(value)
        stats_tracker['valid_humidity_reads'] += 1
    elif sensor == 'light':
        light_values.append(value)
        stats_tracker['valid_light_reads'] += 1
    elif sensor == 'co2':
        co2_values.append(value)
        stats_tracker['valid_co2_reads'] += 1

# Compute base averages (some used later, some not)
avg_temp = sum(temp_values) / len(temp_values) if temp_values else 0
avg_pressure = sum(pressure_values) / len(pressure_values) if pressure_values else 0
avg_humidity = sum(humidity_values) / len(humidity_values) if humidity_values else 0
avg_light = sum(light_values) / len(light_values) if light_values else 0
avg_co2 = sum(co2_values) / len(co2_values) if co2_values else 0

# Derived metrics (many are distractions)
normalized_temp = (avg_temp - 20) * 1.8 if avg_temp > 20 else (avg_temp - 18) * 1.2
scaled_pressure = avg_pressure / 1000
humidity_ratio = avg_humidity / 100
co2_level_index = math.log(avg_co2) if avg_co2 > 0 else 0
light_intensity_factor = math.sqrt(avg_light) if avg_light > 0 else 0

# Unused transformations - dead code paths
if avg_temp > 25:
    temp_alert_level = 2
    pressure_compensation = scaled_pressure * 0.95
else:
    temp_alert_level = 1
    pressure_compensation = scaled_pressure * 1.05

# Simulated risk scores (irrelevant to final score)
risk_score = 0
if avg_humidity > 60:
    risk_score += 30
if avg_co2 > 1000:
    risk_score += 50
if avg_temp > 30:
    risk_score += 40

# Decoy function that's never called
def compute_air_quality_index(values):
    return sum(values) * 0.1  # never used

# Real scoring logic buried among noise
def calculate_baseline(sensor_avg, base_ref, weight):
    deviation = abs(sensor_avg - base_ref)
    return max(0, 100 - deviation * weight)

# Main scoring function
def calculate_final_score(data, weights):
    score_components = {}
    
    # Only these five contribute to final score
    if 'temp' in weights:
        temp_score = calculate_baseline(avg_temp, 25.0, 2.0)
        score_components['temp'] = temp_score * weights['temp']
    
    if 'pressure' in weights:
        pressure_score = calculate_baseline(avg_pressure, 1013.0, 0.01)
        score_components['pressure'] = pressure_score * weights['pressure']
    
    if 'humidity' in weights:
        humidity_score = calculate_baseline(avg_humidity, 50.0, 1.0)
        score_components['humidity'] = humidity_score * weights['humidity']
    
    if 'light' in weights:
        light_score = calculate_baseline(avg_light, 300, 0.01)
        score_components['light'] = light_score * weights['light']
    
    if 'co2' in weights:
        co2_score = calculate_baseline(avg_co2, 400, 0.05)
        score_components['co2'] = co2_score * weights['co2']
    
    # Irrelevant bonus logic (never triggered in this case)
    bonus_multiplier = 1.0
    if all(sc > 80 for sc in score_components.values()):
        bonus_multiplier = 1.1
    
    # Final weighted aggregation
    total_weighted_score = sum(score_components.values())
    normalized_score = total_weighted_score * 10  # scale to larger integer range
    
    # Additional adjustment based on number of sensors
    active_sensors = len([k for k in weights.keys() if k in ['temp','pressure','humidity','light','co2']])
    final_adjustment = normalized_score + (active_sensors * 2.5)
    
    return int(round(final_adjustment))

# Execution point of interest
final_score = calculate_final_score(data, weights)

# Print result as required
Target result: {final_score}