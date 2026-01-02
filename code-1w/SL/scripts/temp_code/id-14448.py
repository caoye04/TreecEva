import math

# Simulated sensor data from environmental monitoring stations
temperature_readings = [23.5, 24.1, 19.8, 22.0, 25.3, 20.2, 21.8, 24.0]
humidity_readings = [45, 52, 61, 48, 55, 67, 50, 53]
pressure_readings = [1013, 1015, 1009, 1018, 1012, 1007, 1014, 1016]

# Irrelevant auxiliary data (distractor)
sound_levels = [32, 45, 50, 30, 38, 44, 55, 60]
lux_values = [12000, 15000, 8000, 2000, 60000, 55000, 10000, 30000]

# Misleading intermediate calculations (red herring)
avg_sound = sum(sound_levels) / len(sound_levels)
total_light = sum(lux_values)

def normalize(data):
    max_val = max(data)
    min_val = min(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

# Distractor function with dead-end logic
def compute_entropy(values):
    normalized = normalize(values)
    entropy = 0
    for p in normalized:
        if p > 0:
            entropy -= p * math.log(p)
    return entropy

# Unused entropy results (dead code path)
humidity_entropy = compute_entropy(humidity_readings)
temp_entropy = compute_entropy(temperature_readings)

# Core processing: extract anomalies based on thresholds
def detect_anomalies(data, threshold_multiplier=1.8):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    upper_bound = mean + threshold_multiplier * std_dev
    lower_bound = mean - threshold_multiplier * std_dev
    return [i for i, x in enumerate(data) if x < lower_bound or x > upper_bound]

# Apply anomaly detection (relevant)
temp_anomalies = detect_anomalies(temperature_readings)
humidity_anomalies = detect_anomalies(humidity_readings, 2.0)

# Combine readings into tuples (tuple usage)
sensor_tuples = list(zip(temperature_readings, humidity_readings, pressure_readings))

# Data transformation pipeline
processing_pipeline = [
    lambda x: (x[0] + 273.15, x[1], x[2]),  # Kelvin conversion (irrelevant later)
    lambda x: (x[0], x[1] * 100 / 100, x[2]),  # Identity-like (distractor)
    lambda x: (round(x[0], 1), x[1], x[2] - 1000)  # Normalize pressure
]

processed_tuples = []
for tup in sensor_tuples:
    temp = tup
    for func in processing_pipeline:
        temp = func(temp)
    processed_tuples.append(temp)

# Extract processed values back into lists
temp_processed = [t[0] for t in processed_tuples]
humid_processed = [t[1] for t in processed_tuples]
press_processed = [t[2] for t in processed_tuples]

# Dictionary mapping for threshold levels by metric (dictionary usage)
threshold_map = {
    'temperature': {'high': 24.5, 'low': 20.0},
    'humidity': {'high': 60, 'low': 45},
    'pressure': {'high': 18, 'low': 5}
}

# Linear search to find first critical reading (linear search)
def find_first_critical_index(readings, low_threshold, high_threshold):
    for i, val in enumerate(readings):
        if val < low_threshold or val > high_threshold:
            return i
    return -1

# Dead-end calls with misleading names (distractor)
first_unstable_temp = find_first_critical_index(temperature_readings, 18.0, 26.0)
first_unstable_humid = find_first_critical_index(humidity_readings, 40, 70)

# Actual relevant data structure: dictionary of processed data
processed_data = {
    'temperatures': temp_processed,
    'humidity': humid_processed,
    'pressure': press_processed,
    'station_count': len(temp_processed)
}

# Decoy function that is never called (dead code)
def forecast_trend(data_list):
    if len(data_list) < 2:
        return 0
    trend = sum(data_list[i+1] - data_list[i] for i in range(len(data_list)-1))
    return trend / (len(data_list) - 1)

# Character counting in station IDs (string method)
station_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008']
valid_id_count = sum(1 for sid in station_ids if sid.count('0') >= 2)

# Lambda-based filtering (lambda function)
high_pressure_stations = list(filter(lambda p: p > 15, press_processed))

# Core analysis function combining multiple concepts
def analyze_readings(data, thresholds):
    temp_src = data['temperatures']
    humid_src = data['humidity']
    press_src = data['pressure']
    
    # Count how many readings exceed thresholds
    temp_high = sum(1 for t in temp_src if t > thresholds['temperature']['high'] + 273.15)
    temp_low = sum(1 for t in temp_src if t < thresholds['temperature']['low'] + 273.15)
    humid_high = sum(1 for h in humid_src if h > thresholds['humidity']['high'])
    humid_low = sum(1 for h in humid_src if h < thresholds['humidity']['low'])
    press_high = sum(1 for p in press_src if p > thresholds['pressure']['high'])
    press_low = sum(1 for p in press_src if p < thresholds['pressure']['low'])
    
    # Compute composite diagnostic score
    temp_score = abs(temp_high - temp_low) * 10
    humid_score = min(humid_high, humid_low) * 5 if humid_high and humid_low else max(humid_high, humid_low) * 3
    press_score = len(press_src) - len(high_pressure_stations)  # Cross-reference
    
    # Final diagnostic using bit manipulation (bitwise operation)
    raw_diagnostic = (temp_score << 2) ^ (humid_score << 1) | (press_score)
    
    # Final adjustment using string-derived count
    adjustment = valid_id_count & 7  # Bitwise AND
    final_diagnostic = raw_diagnostic + adjustment
    
    return final_diagnostic

# Execute main analysis
final_diagnostic = analyze_readings(processed_data, threshold_map)

print(f"Result: {final_diagnostic}")