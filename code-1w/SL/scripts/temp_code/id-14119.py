from collections import defaultdict, Counter
import math

# Simulated sensor data stream with multiple channels
data_stream = [
    {'time': 0.0, 'sensor_A': 3.2, 'sensor_B': -1.1, 'sensor_C': 4.5, 'status': 'active'},
    {'time': 0.1, 'sensor_A': 3.3, 'sensor_B': -1.3, 'sensor_C': 4.4, 'status': 'active'},
    {'time': 0.2, 'sensor_A': 3.5, 'sensor_B': -0.9, 'sensor_C': 4.6, 'status': 'noisy'},
    {'time': 0.3, 'sensor_A': 3.8, 'sensor_B': -1.5, 'sensor_C': 4.3, 'status': 'active'},
    {'time': 0.4, 'sensor_A': 4.0, 'sensor_B': -1.0, 'sensor_C': 4.7, 'status': 'active'},
    {'time': 0.5, 'sensor_A': 4.3, 'sensor_B': -0.8, 'sensor_C': 4.8, 'status': 'noisy'},
    {'time': 0.6, 'sensor_A': 4.5, 'sensor_B': -1.2, 'sensor_C': 4.6, 'status': 'active'},
    {'time': 0.7, 'sensor_A': 4.8, 'sensor_B': -0.7, 'sensor_C': 4.9, 'status': 'active'},
    {'time': 0.8, 'sensor_A': 5.0, 'sensor_B': -0.5, 'sensor_C': 5.0, 'status': 'active'},
    {'time': 0.9, 'sensor_A': 5.3, 'sensor_B': -0.3, 'sensor_C': 5.1, 'status': 'active'},
    {'time': 1.0, 'sensor_A': 5.5, 'sensor_B': -0.2, 'sensor_C': 5.3, 'status': 'active'}
]

# Irrelevant baseline calibration (distractor)
calibration_offsets = {'A': 0.1, 'B': -0.05, 'C': 0.15}
baseline_readings = {k: 0.0 for k in ['A', 'B', 'C']}
for entry in data_stream[:3]:
    baseline_readings['A'] += entry['sensor_A']
    baseline_readings['B'] += entry['sensor_B']
    baseline_readings['C'] += entry['sensor_C']
baseline_readings = {k: v/3 for k, v in baseline_readings.items()}

# Data filtering based on status and thresholds
valid_entries = [e for e in data_stream if e['status'] == 'active']
filtered_data = []
for entry in valid_entries:
    temp_entry = {}
    for key, val in entry.items():
        if key.startswith('sensor_'):
            sensor_id = key.split('_')[1]
            # Apply fake hysteresis correction (mostly irrelevant)
            if sensor_id == 'A' and val > 4.0:
                temp_entry[sensor_id] = val - 0.05
            elif sensor_id == 'B' and val < -0.5:
                temp_entry[sensor_id] = val + 0.03
            else:
                temp_entry[sensor_id] = val
    filtered_data.append(temp_entry)

# Dead code path: unused transformation function
def transform_legacy(data):
    """Legacy function - not used in current logic"""
    result = []
    for d in data:
        x = d.get('A', 0) * 0.9
        y = abs(d.get('B', 0)) ** 0.5
        z = d.get('C', 0) + x - y
        result.append({'transformed': x + y + z})
    return result

# Decoy statistical analysis (distractor)
decoys = []
for i in range(len(filtered_data)):
    a_val = filtered_data[i].get('A', 0)
    b_val = filtered_data[i].get('B', 0)
    c_val = filtered_data[i].get('C', 0)
    decoy_metric = (a_val ** 2 + b_val ** 2 + c_val ** 2) ** 0.5
    if decoy_metric > 5.0:
        decoys.append(decoy_metric * 0.1)

# Build threshold map using counter statistics (partially relevant)
sensor_A_values = [d['A'] for d in filtered_data]
sensor_B_values = [d['B'] for d in filtered_data]
sensor_C_values = [d['C'] for d in filtered_data]

A_stats = Counter(sensor_A_values)
B_stats = Counter(sensor_B_values)
C_stats = Counter(sensor_C_values)

# Threshold calculation with red herring logic
base_threshold = sum(A_stats.keys()) / len(A_stats)
noise_floor = sum(abs(x) for x in B_stats.keys()) / len(B_stats)
peak_reference = max(C_stats.keys())

# Actual threshold determination uses only A_stats peak frequency
main_peak = A_stats.most_common(1)[0][1]  # frequency of most common A value
threshold_map = defaultdict(float)
for val, count in A_stats.items():
    if count >= main_peak * 0.8:  # values within 80% of peak frequency
        threshold_map[val] = math.log(val + 1) * 0.7

# Secondary mapping distraction
temp_map = {}
for k, v in threshold_map.items():
    temp_map[k * 1.1] = v * 1.05  # never used

# Core signal processing function
def process_signals(data_chunk, thresholds):
    accumulator = 0.0
    history = []
    
    for idx, record in enumerate(data_chunk):
        a_val = record['A']
        b_val = record['B']
        c_val = record['C']
        
        # Conditional signal weighting
        if a_val in thresholds:
            weight = thresholds[a_val]
        else:
            weight = 0.5  # default
        
        # Complex but partially irrelevant transformation chain
        intermediate = (a_val * 1.1) + (abs(b_val) ** 1.5) - (c_val * 0.9)
        normalized = intermediate / (weight + 0.1)
        
        # Hidden logic: only even-indexed entries contribute
        if idx % 2 == 0:
            # Additional filtering: only when C > 4.5
            if c_val > 4.5:
                # Final computation uses XOR of truncated floats as seed
                hex_seed = int(a_val) ^ int(c_val * 10)
                contribution = normalized * (hex_seed % 7)
                accumulator += contribution
        
        # Dead branch: never executed due to data constraints
        if a_val < 2.0:
            fallback = math.atan(normalized)
            history.append(fallback)
    
    # Final adjustment based on accumulation pattern
    if len(history) > 3:
        final_adjustment = sum(history) / len(history)
    else:
        final_adjustment = 0.25  # fixed offset
    
    return int(accumulator - final_adjustment)  # integer truncation

# Execute main processing
final_output = process_signals(filtered_data, threshold_map)

# Critical output statement
print(f"Target result: {final_output}")