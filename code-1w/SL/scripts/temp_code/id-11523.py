import itertools

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 19.8, 22.0, 25.3, 26.7, 20.4, 21.9, 24.8, 23.0]
humidity_readings = [45, 48, 52, 60, 58, 54, 49, 51, 57, 59]
pressure_readings = [1013, 1015, 1012, 1010, 1008, 1007, 1009, 1011, 1014, 1016]

# Irrelevant auxiliary arrays (distractors)
legacy_sensor_flags = [True, False, True, False, True, False, True, False, True, False]
calibration_offsets = [0.1, -0.2, 0.3, -0.1, 0.0, 0.2, -0.3, 0.1, 0.0, -0.2]

# Mapping of thresholds for different zones (used later)
threshold_map = {
    'zone_a': {'temp': 24.0, 'humidity': 55},
    'zone_b': {'temp': 22.5, 'humidity': 50},
    'zone_c': {'temp': 25.0, 'humidity': 60}
}

# Dead code path - never invoked (misleading function)
def legacy_diagnostic(data):
    return sum(x * 0.95 for x in data if x > 0) // len(data)

# Unused transformation (red herring)
squared_humidity = [h**2 for h in humidity_readings]

# Generate composite index using itertools (actual usage)
reading_pairs = list(itertools.combinations(range(len(temperature_readings)), 2))
fluctuation_index = 0
for i, j in reading_pairs:
    fluctuation_index += abs(temperature_readings[i] - temperature_readings[j])
fluctuation_index = round(fluctuation_index / len(reading_pairs), 3) if reading_pairs else 0

# Distractor: complex-looking but unused bitwise analysis
bit_analysis = 0
for val in pressure_readings:
    bit_analysis ^= (val & 0xFF) >> 2

# Real processing begins: filter data based on conditions
valid_indices = []
for idx in range(len(temperature_readings)):
    temp_ok = temperature_readings[idx] >= threshold_map['zone_a']['temp']
    humid_ok = humidity_readings[idx] >= threshold_map['zone_a']['humidity']
    if temp_ok or humid_ok:
        valid_indices.append(idx)

filtered_data = [(temperature_readings[i], humidity_readings[i], pressure_readings[i]) for i in valid_indices]

# Secondary filtering based on set logic (set operation)
high_temp_set = {i for i, t in enumerate(temperature_readings) if t > 24.5}
high_humid_set = {i for i, h in enumerate(humidity_readings) if h > 55}
overlap_zone = high_temp_set & high_humid_set  # intersection

# Another red herring: unused statistical transform
weighted_avg = sum(t * (h / 100) for t, h, _ in filtered_data) / len(filtered_data) if filtered_data else 0

# Core diagnostic logic (deceptively simple among noise)
def analyze_stability(data_list):
    if not data_list:
        return 0
    temp_range = max(d[0] for d in data_list) - min(d[0] for d in data_list)
    humid_range = max(d[1] for d in data_list) - min(d[1] for d in data_list)
    return int((temp_range * 1.5) + (humid_range * 0.8))

# Misleading recursive function (never used)
def recursive_smooth(arr, depth=0):
    if depth >= 2 or len(arr) < 2:
        return arr
    smoothed = [(arr[i] + arr[i+1]) / 2 for i in range(len(arr)-1)]
    return recursive_smooth(smoothed, depth + 1)

# Main processing function that will be called
def process_readings(readings, limits):
    if not readings:
        return -1
    
    # Extract slices for analysis
    recent_temps = [r[0] for r in readings[-5:]]  # slicing operation
    recent_humid = [r[1] for r in readings[-5:]]
    
    # Compute derived metrics
    avg_temp = sum(recent_temps) / len(recent_temps)
    avg_humid = sum(recent_humid) / len(recent_humid)
    
    # Apply zone-specific adjustment
    adjustment = 0
    if avg_temp > limits['zone_c']['temp']:
        adjustment += 3
    elif avg_temp > limits['zone_a']['temp']:
        adjustment += 1
        
    if avg_humid > limits['zone_c']['humidity']:
        adjustment += 2
    
    base_score = analyze_stability(readings)
    return base_score * 2 + adjustment

# Trigger point: this assignment determines the answer
final_diagnostic = process_readings(filtered_data, threshold_map)

# Print result for evaluation
print(f"Result: {final_diagnostic}")