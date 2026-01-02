import itertools

# Simulated sensor data with noise and redundant readings
temperature_readings = [23.4, 24.1, 22.7, 25.3, 26.0, 24.8, 23.9]
humidity_readings = [45, 47, 50, 44, 60, 55, 48]
pressure_readings = [1013, 1015, 1012, 1010, 1008, 1014, 1016]

# Irrelevant backup arrays (distractor)
backup_temps = temperature_readings[::-1]
backup_humidity = [h * 1.05 for h in humidity_readings]

# Noise injection simulation (mostly unused)
def apply_noise(lst, factor=0.02):
    import random
    random.seed(42)
    return [x + random.uniform(-factor*x, factor*x) for x in lst]

noisy_temps = apply_noise(temperature_readings, 0.01)  # Computed but not used

# Decoy transformation functions
def deprecated_filter(data):
    # This function is never called
    return [x for x in data if x > sum(data)/len(data)]

def obsolete_normalize(arr):
    max_val, min_val = max(arr), min(arr)
    return [(x - min_val) / (max_val - min_val) for x in arr]

# Real processing begins here
sensor_matrix = list(zip(temperature_readings, humidity_readings, pressure_readings))

# Extract high temp indices (distraction)
high_temp_indices = [i for i, t in enumerate(temperature_readings) if t > 24.0]

# Generate sliding windows of sensor data
windowed_data = []
for i in range(len(sensor_matrix) - 2):
    windowed_data.append(sensor_matrix[i:i+3])

# Compute moving averages (partially relevant)
moving_avg_temps = []
for i in range(len(temperature_readings) - 2):
    avg = sum(temperature_readings[i:i+3]) / 3
    moving_avg_temps.append(round(avg, 2))

# Flag anomalies based on pressure deviation (red herring)
anomaly_flags = []
pressure_avg = sum(pressure_readings) / len(pressure_readings)
for p in pressure_readings:
    if abs(p - pressure_avg) > 5:
        anomaly_flags.append(True)
    else:
        anomaly_flags.append(False)

# Unused set operations (distractor)
unique_pressures = set(pressure_readings)
pressure_changes = set(abs(pressure_readings[i] - pressure_readings[i-1]) 
                        for i in range(1, len(pressure_readings)))
critical_pressure_events = unique_pressures & {1008, 1010}  # intersection, unused

# String-based status encoding (irrelevant)
status_map = []
for t, h in zip(temperature_readings, humidity_readings):
    if t > 24.5 and h > 50:
        status_map.append('HIGH_LOAD')
    elif t < 23.0:
        status_map.append('LOW_TEMP')
    else:
        status_map.append('NORMAL')
status_summary = ''.join(s[0] for s in status_map)  # 'HLNNNHN'

# Core logic: frequency analysis of humidity patterns
humidity_pairs = list(itertools.pairwise(humidity_readings))
frequent_pairs = {}
for pair in humidity_pairs:
    freq_key = (pair[0], pair[1])
    frequent_pairs[freq_key] = frequent_pairs.get(freq_key, 0) + 1

# Identify dominant transition
max_freq = max(frequent_pairs.values())
dominant_pair = [k for k, v in frequent_pairs.items() if v == max_freq][0]

delta_h = dominant_pair[1] - dominant_pair[0]

# Data stream preparation (key step)
data_stream = [
    temperature_readings[0],
    humidity_readings[2],
    pressure_readings[4],
    delta_h,
    len(windowed_data),
    len(moving_avg_temps)
]

# Actual computation pipeline
def transform_value(x, shift):
    return (x << 1) ^ shift  # Bit manipulation: left shift and XOR

def validate_checksum(seq):
    total = sum(seq)
    return total % 7 == 0

def process_pipeline(stream):
    # Unpack with destructuring
    t_init, h_ref, p_evt, dh, win_len, avg_len = stream
    
    # Multiple assignments and intermediate calculations
    a = int(t_init * 2.1)
    b = h_ref + p_evt // 100
    c = dh ** 3
    d = win_len * avg_len
    
    # Redundant validation (appears important but doesn't alter flow)
    is_valid = validate_checksum([a, b, c, d])  # True, but unused in decision
    
    # Key calculation hidden among distractions
    temp_score = transform_value(a, 5)
    base_result = temp_score + b
    adjustment = abs(c) + d
    
    # Final output derived from multiple sources
    final_output = base_result - adjustment
    
    # Dead code branch (never executed)
    if False:
        fallback = (a ^ b) & (c | d)
        final_output = fallback * 2
    
    return final_output

# Execute main logic
final_output = process_pipeline(data_stream)
print(f"Result: {final_output}")