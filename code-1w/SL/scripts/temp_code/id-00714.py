from collections import defaultdict, Counter

# Simulated sensor network data processing with red herrings
def analyze_pattern(seq):
    return sum(a * b for a, b in zip(seq, seq[1:]))

# Irrelevant helper function (dead code path)
def deprecated_normalization(vec):
    norm = sum(x ** 2 for x in vec) ** 0.5
    return [x / norm for x in vec]

# Unused transformation matrix (distractor)
transform_matrix = [
    [1.1, -0.3, 0.05],
    [0.2, 0.95, -0.1],
    [-0.05, 0.15, 1.0]
]

# Fake calibration constants (misleading intermediate results)
CALIBRATION_OFFSETS = {
    'A1': 0.021,
    'A2': -0.018,
    'B1': 0.033,
    'B2': -0.029,
    'C1': 0.017,
    'C2': -0.022
}

# Sensor metadata (partially relevant, partially distractor)
sensor_specs = {
    'range': {'low': -40, 'high': 85},
    'precision': 0.1,
    'units': '°C',
    'sampling_rate': 100
}

# Raw unprocessed readings with noise and anomalies
event_log = [
    {'sensor': 'TH1', 'val': 23.1, 'status': 'OK'},
    {'sensor': 'TH2', 'val': 22.8, 'status': 'OK'},
    {'sensor': 'PS1', 'val': 101.3, 'status': 'ERR'},
    {'sensor': 'TH3', 'val': 24.0, 'status': 'OK'},
    {'sensor': 'PS2', 'val': 102.1, 'status': 'OK'},
    {'sensor': 'TH1', 'val': 23.3, 'status': 'OK'},
    {'sensor': 'LS1', 'val': 450, 'status': 'OK'},
    {'sensor': 'TH2', 'val': 22.9, 'status': 'OK'}
]

# Accumulate temperature readings only (key filtering logic)
temp_readings = []
sensor_count = defaultdict(int)
error_flags = set()

for entry in event_log:
    sensor_count[entry['sensor']] += 1
    if entry['status'] == 'ERR':
        error_flags.add(entry['sensor'])
    # Only collect temperature sensors (THx)
    if entry['sensor'].startswith('TH') and entry['status'] == 'OK':
        temp_readings.append(entry['val'])

# Decoy statistical analysis (irrelevant computation)
mean_temp = sum(temp_readings) / len(temp_readings)
variance = sum((x - mean_temp) ** 2 for x in temp_readings) / len(temp_readings)
std_deviation = variance ** 0.5

# Distractor: frequency count of all sensors (not used later)
all_sensor_types = [rec['sensor'][:2] for rec in event_log]
sensor_type_freq = Counter(all_sensor_types)

# Real work begins: filter valid temperature data above threshold
baseline_ref = 22.5
filtered_data = [temp for temp in temp_readings if temp > baseline_ref]

# Create threshold map with dummy entries (mix of relevant and irrelevant)
threshold_map = defaultdict(lambda: 0.0)
threshold_map.update({
    'TH1': 23.0,
    'TH2': 22.7,
    'TH3': 23.5,
    'PS1': 100.0,  # unused
    'PS2': 105.0,  # unused
    'LS1': 400.0   # unused
})

# Core processing function with conditional logic
def process_readings(readings, limits):
    if not readings:
        return -1
    
    # Summation with case-based adjustment (conditional expression)
    base_score = sum(r ** 2 for r in readings)
    adjustment = 1.1 if len(readings) > 2 else 0.9
    
    # Bit manipulation red herring (never actually affects result)
    magic_key = 0xABCDEF
    masked = magic_key & 0xFFFF
    shifted = (masked >> 4) ^ 0xAA
    
    # Actual decision logic: apply dynamic offset based on reading magnitude
    offset = 0
    for val in readings:
        if val < 23.0:
            offset += 5
        elif val < 23.5:
            offset += 8
        else:
            offset += 12
    
    # Final computation chain
    raw_diagnostic = int(base_score * adjustment)
    final_diagnostic = raw_diagnostic + offset
    
    # Dead code branch (never reached due to structure)
    if False and shifted > 1000:
        backup = sum(readings) // len(readings)
        final_diagnostic ^= backup
        
    return final_diagnostic

# Execute critical statement
temp_counter = Counter(temp_readings)  # another distractor
reference_snapshot = temp_readings.copy()  # unused deep copy
final_diagnostic = process_readings(filtered_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")