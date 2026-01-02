from collections import defaultdict, Counter
import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 27.1, 24.9, 23.7]
humidity_readings = [45, 48, 50, 55, 60, 62, 58, 53]
co2_levels = [400, 410, 415, 430, 450, 470, 500, 520]

# Irrelevant auxiliary data (distractor)
legacy_system_flags = [0x1A, 0x2C, 0x3E, 0x4B]
checksum_lookup = {i: (i ** 2 + 3 * i + 7) % 256 for i in range(64)}

# Preprocessing phase with red herrings
def normalize(values):
    mean_val = sum(values) / len(values)
    return [(v - mean_val) for v in values]

def calculate_entropy(data):
    # Unused function - dead code path (distractor)
    counts = Counter(data)
    total = len(data)
    return -sum((count / total) * math.log2(count / total) for count in counts.values())

def bitwise_scramble(n):
    # Obfuscation function not used in main logic (distractor)
    return ((n << 3) & 0xFF) ^ 0xAA

# Core processing pipeline
raw_matrix = list(zip(temperature_readings, humidity_readings, co2_levels))

# Apply normalization to each sensor stream
norm_temp = normalize(temperature_readings)
norm_humid = normalize(humidity_readings)
norm_co2 = normalize(co2_levels)

# Reconstruct aligned dataset
processed_data = []
for i in range(len(raw_matrix)):
    processed_data.append({
        'idx': i,
        'temp_norm': norm_temp[i],
        'humid_norm': norm_humid[i],
        'co2_norm': norm_co2[i],
        'temp_raw': temperature_readings[i],
        'risk_flag': False
    })

# Threshold configuration map (used later)
threshold_map = defaultdict(lambda: defaultdict(float))
thresh = threshold_map['anomaly']
thresh['temp_z'] = 1.5
thresh['humid_z'] = 1.2
thresh['co2_z'] = 1.8

# Decoy statistical analysis (irrelevant computation)
decoy_stats = {}
decoy_stats['temp_skew'] = (3 * (sum(norm_temp) / len(norm_temp)) - sum(t**3 for t in norm_temp)**(1/3)) / (sum(t**2 for t in norm_temp)**(1/2) + 1e-9)
decoy_stats['phantom_index'] = max(checksum_lookup.values()) - min(checksum_lookup.values())

# Secondary distraction: unused transformation graph
transform_graph = {}
for i in range(8):
    transform_graph[i] = {
        'input': raw_matrix[i],
        'scrambled': tuple(bitwise_scramble(int(x)) for x in raw_matrix[i]),
        'valid': False
    }

# Anomaly detection engine
def detect_spikes(data_chunk, thresholds):
    spike_count = 0
    for entry in data_chunk:
        z_temp = abs(entry['temp_norm'])
        z_humid = abs(entry['humid_norm'])
        z_co2 = abs(entry['co2_norm'])
        
        # Actual logic: count multi-sensor anomalies
        if z_temp > thresholds['temp_z'] and z_co2 > thresholds['co2_z']:
            spike_count += 1
            entry['risk_flag'] = True  # Mutate original data
    return spike_count

# Misleading intermediate result (distractor)
baseline_stability = sum(1 for x in norm_temp if abs(x) < 1.0) + sum(1 for x in norm_humid if abs(x) < 1.0)

# Real signal processing step
spike_total = detect_spikes(processed_data, threshold_map['anomaly'])

# Diagnostic engine with conditional logic chain
status_codes = []
for record in processed_data:
    code = 0
    if record['risk_flag']:
        code += 100
    if record['temp_raw'] > 25.0:
        code += 10
    if record['idx'] % 3 == 0:
        code += 1
    status_codes.append(code)

# Aggregation via set operations (required feature)
unique_codes = set(status_codes)
code_frequency = Counter(status_codes)

# Final diagnostic calculation
weighted_sum = 0
for code, freq in code_frequency.items():
    if code >= 100:
        weighted_sum += code * freq * 1.5
    elif code >= 10:
        weighted_sum += code * freq

# Introduce irrelevant geometric factor (red herring)
coverage_angle = math.atan2(7, 5) * (math.pi / 180)
phantom_energy = sum(math.sin(i * coverage_angle) for i in range(1, 9))

# Final analysis function
def analyze_readings(data, config):
    # Extract flagged entries
    flagged = [d for d in data if d['risk_flag']]
    if not flagged:
        return 0
    
    # Compute composite index
    indices = []
    for f in flagged:
        base_idx = f['idx']
        temp_contrib = f['temp_raw'] * 0.8
        co2_contrib = (f['co2_norm'] + 5) * 10  # Normalize CO2 impact
        idx_value = int(temp_contrib + co2_contrib + base_idx)
        indices.append(idx_value)
    
    # Apply secret offset (hidden in logic chain)
    secret_offset = len(threshold_map['anomaly']) * 2  # evaluates to 3*2=6
    final_score = sum(indices) + secret_offset
    
    # Distractor: unused entropy-based weight
    dummy_weight = calculate_entropy([int(x) for x in norm_temp]) if indices else 0
    
    return final_score

# Execute key statement
diagnostic_snapshot = [analyze_readings(processed_data, threshold_map)]
final_diagnostic = analyze_readings(processed_data, threshold_map)

print(f"Result: {final_diagnostic}")