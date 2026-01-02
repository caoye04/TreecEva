import itertools

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 27.1, 25.8, 24.7]
humidity_readings = [45, 47, 50, 52, 58, 60, 55, 53]
pressure_readings = [1013, 1012, 1015, 1010, 1008, 1007, 1009, 1011]

# Irrelevant calibration coefficients (distractor)
calibration_a = 0.987
calibration_b = 1.015
dummy_offset = sum([calibration_a * i for i in range(3)])

# Misleading preprocessing path (dead code)
def legacy_normalize(data):
    mean_val = sum(data) / len(data)
    return [x - mean_val for x in data]

# Unused transformation (red herring)
squared_deltas = [(t - 25)**2 for t in temperature_readings]
smoothed_temp = list(itertools.accumulate(temperature_readings))[:len(temperature_readings)]

# Real processing begins here
status_flags = ['normal' if t < 26 else 'elevated' for t in temperature_readings]

# Composite data packaging
raw_samples = list(zip(temperature_readings, humidity_readings, pressure_readings))
indexed_samples = {i: sample for i, sample in enumerate(raw_samples)}

# Decoy analysis function (never called)
def compute_thermal_index(temp, hum):
    return temp * (hum / 100) + 0.3 * temp**0.5

# Threshold configuration map (used later)
threshold_map = {
    'temp_high': 26.0,
    'humidity_spike': 55,
    'pressure_drop': 1010
}

# Extraneous statistical summary (irrelevant)
mean_temp = sum(temperature_readings) / len(temperature_readings)
variance_temp = sum((t - mean_temp) ** 2 for t in temperature_readings) / len(temperature_readings)
std_dev_temp = variance_temp ** 0.5

# Distractor: unused rolling window calculation
window_size = 3
rolling_avg = [sum(temperature_readings[i:i+window_size]) / window_size 
               for i in range(len(temperature_readings) - window_size + 1)]

# Actual core processing logic
filtered_readings = [
    (t, h, p) for t, h, p in raw_samples 
    if t >= threshold_map['temp_high'] or h >= threshold_map['humidity_spike']
]

# Data enrichment with status tagging
annotated_readings = []
for idx, (t, h, p) in enumerate(filtered_readings):
    flags = []
    if t >= threshold_map['temp_high']:
        flags.append('over_temp')
    if h >= threshold_map['humidity_spike']:
        flags.append('high_humidity')
    if p <= threshold_map['pressure_drop']:
        flags.append('low_pressure')
    annotated_readings.append((idx, t, h, p, flags))

# Secondary filtering based on flag count
qualified_events = [entry for entry in annotated_readings if len(entry[4]) > 1]

# Dummy machine learning mimicry (distraction)
feature_matrix = [[t*0.1, h*0.01] for (_, t, h, _, _) in qualified_events]
predicted_risk = sum([f[0] + f[1] for f in feature_matrix]) if feature_matrix else 0.0

# Real diagnostic logic
processed_data = []
for event in qualified_events:
    _, temp, humid, press, flag_list = event
    score = 0
    if 'over_temp' in flag_list:
        score += int(temp * 2)
    if 'high_humidity' in flag_list:
        score += int(humid / 2)
    if 'low_pressure' in flag_list:
        score -= int(press / 100)
    processed_data.append(score)

# Final analysis function
def analyze_readings(data, thresholds):
    if not data:
        return -1
    base = sum(data)
    adjustment = 0
    # Complex conditional adjustment
    if len(data) >= 2:
        adjustment += 100
        if thresholds['temp_high'] > 25.5:
            adjustment *= 2
        else:
            adjustment //= 2
    else:
        adjustment -= 50
    
    # Bit manipulation twist (concept integration)
    final_value = base ^ adjustment  # XOR operation
    final_value = final_value & 0xFFFF  # Mask to 16 bits
    
    # Additional decoy logic inside function (misleading)
    temp_debug = [d << 1 for d in data]  # Left shift - unused
    if base > 100:
        dummy_flag = True
        redundant_calc = base ** 0.1
    
    return final_value

# Execution point of interest
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Print result as required
Target result: {final_diagnostic}