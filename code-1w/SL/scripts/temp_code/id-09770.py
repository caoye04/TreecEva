from collections import defaultdict, Counter

# Simulated sensor data ingestion with noise and redundant metrics
data_stream = [
    ('temp', 34.5), ('humidity', 45), ('temp', 36.1), ('pressure', 1013),
    ('humidity', 47), ('co2', 420), ('temp', 35.8), ('motion', 1),
    ('pressure', 1015), ('co2', 410), ('temp', 33.9), ('humidity', 44),
    ('light', 200), ('temp', 37.2), ('co2', 430), ('humidity', 48)
]

# Irrelevant auxiliary mapping (distractor)
unit_conversion = {
    'temp': 'C',
    'humidity': '%',
    'pressure': 'hPa',
    'co2': 'ppm',
    'motion': 'bool',
    'light': 'lux'
}

# Misleading preprocessing: normalizes units but not used later
converted_data = []
for sensor, value in data_stream:
    if sensor == 'temp':
        converted_data.append((sensor, round((value * 9/5) + 32, 2)))  # Convert to Fahrenheit (unused)
    else:
        converted_data.append((sensor, value))

# Primary data aggregation (relevant path)
raw_aggregation = defaultdict(list)
for sensor, value in data_stream:
    raw_aggregation[sensor].append(value)

# Dead code path: computes average but never used
average_readings = {}
for sensor, values in raw_aggregation.items():
    average_readings[sensor] = sum(values) / len(values)  # Computed but ignored

# Redundant character analysis on sensor names (distractor)
sensor_chars = ''.join(raw_aggregation.keys())
char_freq = Counter(sensor_chars)
total_chars = sum(char_freq.values())
unique_consonants = len([c for c in char_freq if c not in 'aeiou' and c.isalpha()])

# Actual filtering: isolate temperature readings above baseline
baseline_ref = 35.0
filtered_data = [v for k, v in data_stream if k == 'temp' and v > baseline_ref]

# Decoy threshold logic with unused branches
threshold_map = {}
for key in raw_aggregation:
    if key == 'temp':
        threshold_map[key] = (30.0, 40.0)
    elif key == 'co2':
        threshold_map[key] = (400, 500)
    elif key == 'humidity':
        threshold_map[key] = (30, 70)
    else:
        threshold_map[key] = (0, 100)  # Placeholder (partially misleading)

# Unused bit manipulation sequence (red herring)
bit_flags = 0
for i, val in enumerate(filtered_data):
    if val > 36.0:
        bit_flags |= (1 << i)
    else:
        bit_flags &= ~(1 << i)

# Conditional inversion test (never invoked)
def invert_bits(n):
    return ~n & ((1 << 8) - 1)

# Core processing function with early returns and slicing
def process_readings(readings, thresholds):
    if not readings:
        return -1
    
    # Apply moving window average using slicing (relevant)
    window_size = 2
    smoothed = []
    for i in range(len(readings) - window_size + 1):
        window = readings[i:i+window_size]
        smoothed.append(sum(window) / len(window))
    
    if len(smoothed) < 2:
        return int(smoothed[0] * 10) if smoothed else 0
    
    # Secondary filter: only high-confidence trends
    trend_up = 0
    for i in range(1, len(smoothed)):
        if smoothed[i] > smoothed[i-1]:
            trend_up += 1
    
    # Final decision based on trend ratio and initial slice
    initial_baseline = filtered_data[:2]
    base_avg = sum(initial_baseline) / len(initial_baseline)
    trend_ratio = trend_up / (len(smoothed) - 1)
    
    if trend_ratio > 0.5 and base_avg > 35.5:
        adjustment = 1.8
    else:
        adjustment = -0.9
    
    # Final computation
    result = (base_avg + trend_ratio * 100) + adjustment
    
    # Dead return branch (misleading)
    if result < 0:
        return int(result - 100)
        
    return round(result, 4)

# Execution point of interest
final_diagnostic = process_readings(filtered_data, threshold_map)

# Spurious post-processing (irrelevant)
status_flag = 'OK' if final_diagnostic > 50 else 'CALIBRATE'
diag_code = hash(status_flag) % 1000

# Output the target variable
print(f"Result: {final_diagnostic}")