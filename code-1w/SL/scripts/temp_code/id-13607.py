import itertools

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 19.8, 25.6, 22.3, 20.9, 26.1, 24.7, 21.4]
humidity_readings = [45, 52, 61, 48, 55, 67, 43, 50, 58]
pressure_readings = [1013, 1015, 1010, 1020, 1012, 1008, 1022, 1014, 1016]

# Irrelevant auxiliary data (distractor)
sound_levels = [34, 36, 45, 33, 38, 41, 35, 37, 40]  # Not used in final calculation
light_intensity = [800, 900, 1200, 750, 880, 1100, 700, 950, 1050]  # Dead code path

# Preprocessing: Normalize temperature to Kelvin (relevant)
temp_kelvin = [t + 273.15 for t in temperature_readings]

# Misleading transformation chain (partially irrelevant)
adjusted_humidity = [(h * 1.02) + 3.1 for h in humidity_readings]  # Slight adjustment but not critical
dew_point_approx = [temp_kelvin[i] - ((100 - adjusted_humidity[i]) * 0.5) for i in range(len(temp_kelvin))]

# Threshold definitions for anomaly detection
threshold_map = {
    'high_temp': 25.0,
    'low_pressure': 1010,
    'humidity_spike': 60
}

# Decoy function (never called)
def analyze_light_patterns(data):
    return sum(x > 1000 for x in data) * 0.75

# Another red herring: unused pressure trend analyzer
def compute_pressure_gradient(pressure_list):
    return [pressure_list[i+1] - pressure_list[i] for i in range(len(pressure_list)-1)]

# Real processing begins here
zipped_data = list(zip(temperature_readings, humidity_readings, pressure_readings))

# Filter out readings where temperature < 21 or pressure < 1010 (conditional filtering)
filtered_data = [entry for entry in zipped_data if entry[0] >= 21 and entry[2] >= 1010]

# Auxiliary computation: rolling average attempt (unused)
window_size = 3
rolling_avg_temp = [sum(temperature_readings[i:i+window_size]) / window_size 
                      for i in range(len(temperature_readings) - window_size + 1)]

# Core logic: detect anomalies based on multiple conditions
def detect_anomalies(entry, thresholds):
    temp, hum, pres = entry
    issues = 0
    if temp > thresholds['high_temp']:
        issues += 2
    if hum > thresholds['humidity_spike']:
        issues += 1
    if pres < thresholds['low_pressure']:
        issues += 3
    return issues

# Apply anomaly detection across filtered entries
anomaly_scores = [detect_anomalies(entry, threshold_map) for entry in filtered_data]

# Bit manipulation layer (adds complexity, relevant)
encoded_flags = [score ^ 5 | 2 for score in anomaly_scores]  # XOR with 5 then OR with 2

# Secondary filter: only keep encoded flags divisible by 3 (additional constraint)
valid_flags = [flag for flag in encoded_flags if flag % 3 == 0]

# Complex aggregation using itertools.groupby (required python feature)
sorted_flags = sorted(valid_flags)
grouped_flags = [list(group) for k, group in itertools.groupby(sorted_flags)]
max_group_sum = max(sum(group) for group in grouped_flags) if grouped_flags else 0

# Final diagnostic computation
baseline = 100
adjustment_factor = len(filtered_data) * 0.8

# Critical execution point
final_diagnostic = process_readings(filtered_data, threshold_map)

# Function definition placed AFTER usage (misleading structure)
def process_readings(data, thresholds):
    base_score = sum(1 for entry in data if entry[0] > thresholds['high_temp'])
    humid_burst = sum(1 for entry in data if entry[1] > thresholds['humidity_spike'])
    stable_pressure = sum(1 for entry in data if entry[2] > 1014)
    
    # Composite formula with weighted effects
    score = (base_score * 7) + (humid_burst * 4) - (stable_pressure * 2)
    
    # Inject bit-level noise for confusion (but neutralized)
    noise_mask = 0b1101 ^ 0b1101  # Always zero
    score ^= noise_mask
    
    # Final adjustment via external-seeming but internal logic
    multiplier = 3 if score > 10 else 2
    return int(score * multiplier) + max_group_sum

# Print result as required
Result: {final_diagnostic}