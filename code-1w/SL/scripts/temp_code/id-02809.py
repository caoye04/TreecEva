import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 19.8, 25.6, 30.2, 28.7, 27.3, 22.0, 20.5, 26.8]
humidity_readings = [45, 52, 61, 48, 33, 37, 41, 56, 59, 44]
pressure_readings = [1013, 1015, 1012, 1018, 1009, 1011, 1014, 1016, 1010, 1017]

# Irrelevant auxiliary data (distractor)
sound_levels = [34, 36, 38, 41, 45, 43, 39, 37, 35, 33]
luminosity = [800, 850, 900, 920, 870, 830, 810, 860, 890, 910]

# Data normalization function - not used in final computation (dead path)
def normalize(data):
    min_val, max_val = min(data), max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

# Misleading transformation (not actually contributing to result)
transformed_humidity = [h ** 0.5 * 1.2 for h in humidity_readings if h > 40]

# Core processing begins here
raw_data_tuples = list(zip(temperature_readings, humidity_readings, pressure_readings))

# Filter based on temperature threshold (key logic step 1)
filtered_data = [entry for entry in raw_data_tuples if 20 <= entry[0] <= 28]

# Decoy statistical summary (irrelevant)
avg_temp = sum(t[0] for t in raw_data_tuples) / len(raw_data_tuples)
avg_humidity = sum(h[1] for h in raw_data_tuples) / len(raw_data_tuples)

# Complex threshold map construction with red herring conditions (key logic step 2)
threshold_map = {
    'temp_band': (22, 27),
    'humidity_critical': 60,
    'pressure_stable': lambda p: abs(p - 1014) < 5,
    'ignore_zone': set([25.6, 30.2])  # Distractor: never actually used
}

# Spurious bit manipulation (misleading intermediate)
pressure_flags = 0
for p in pressure_readings:
    if p > 1015:
        pressure_flags |= (1 << (p - 1010))

# Auxiliary diagnostic function that seems important but isn't used (decoy)
def compute_stability_index(data_list):
    variance = sum((x - sum(data_list)/len(data_list))**2 for x in data_list) / len(data_list)
    return round(100 / (1 + variance), 2)

# Key processing function with multiple concepts
def analyze_variability(readings):
    n = len(readings)
    if n == 0:
        return 0.0
    mean = sum(readings) / n
    squared_diffs = [(x - mean)**2 for x in readings]
    variance = sum(squared_diffs) / n
    return math.sqrt(variance)

# Another irrelevant utility (distractor)
def generate_timestamps(count):
    return [f"2023-11-01T{str(10+i).zfill(2)}:00:00Z" for i in range(count)]
timestamps = generate_timestamps(len(temperature_readings))

# Critical data transformation chain
variability_metrics = {
    'temp_var': analyze_variability([t[0] for t in filtered_data]),
    'humidity_var': analyze_variability([t[1] for t in filtered_data]),
    'pressure_trend': sum(1 for t in filtered_data if t[2] > 1013)
}

# Boolean logic cascade with short-circuiting (key logic steps 3-5)
base_condition = len(filtered_data) > 5
amplifier = 1.0
if base_condition and variability_metrics['temp_var'] < 3.0:
    amplifier *= 1.5
if not (variability_metrics['humidity_var'] > 8.0 or len(filtered_data) < 3):
    amplifier *= 1.2

# Nested conditional with tuple unpacking and logical operations (key logic steps 6-7)
critical_count = 0
for temp, hum, press in filtered_data:
    in_temp_band = threshold_map['temp_band'][0] <= temp <= threshold_map['temp_band'][1]
    high_humidity_risk = hum > threshold_map['humidity_critical']
    stable_pressure = threshold_map['pressure_stable'](press)
    
    if in_temp_band and (high_humidity_risk or not stable_pressure):
        critical_count += 1

# Primary result calculation with string-based switch (key logic steps 8-9)
def process_readings(data, thresholds):
    if not data:
        return -1
    
    # Use of string method as control flow (python idiom)
    mode_flag = 'extended' if 'temp_band' in thresholds.keys() else 'basic'
    
    base_score = 0
    for t, h, p in data:
        base_score += t * 2
        base_score -= h // 10
        if p > 1014:
            base_score += 5
    
    # Final adjustment using logical and arithmetic combination
    adjustment = 0
    if mode_flag.startswith('extend'):
        adjustment += 10
    if critical_count > 0:
        adjustment -= critical_count * 3
    
    return int(base_score * amplifier + adjustment)

# Execution point of interest
final_diagnostic = process_readings(filtered_data, threshold_map)

# Print result as required
print(f"Target result: {final_diagnostic}")