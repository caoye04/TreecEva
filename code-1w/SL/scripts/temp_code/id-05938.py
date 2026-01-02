import math

# Simulated sensor network diagnostics with data filtering and anomaly detection
def collect_sensor_data():
    raw_readings = [
        (101, 'temp', 23.5), (102, 'pressure', 1013.25), (103, 'humidity', 45.0),
        (104, 'temp', 24.1), (105, 'co2', 415), (106, 'humidity', 47.3),
        (107, 'temp', 22.8), (108, 'pressure', 1010.11), (109, 'co2', 420)
    ]
    return raw_readings

def filter_by_type(readings, sensor_type):
    return [r for r in readings if r[1] == sensor_type]

def compute_baseline(dataset):
    values = [d[2] for d in dataset]
    mean = sum(values) / len(values)
    variance = sum((v - mean) ** 2 for v in values) / len(values)
    return {'mean': mean, 'std': math.sqrt(variance)}

def normalize_readings(data_list):
    types = ['temp', 'pressure', 'humidity', 'co2']
    normalized = {}
    for t in types:
        subset = filter_by_type(data_list, t)
        if subset:
            stats = compute_baseline(subset)
            normalized[t] = [((d[2] - stats['mean']) / (stats['std'] + 1e-8)) for d in subset]
    return normalized

def generate_signature(pattern):
    # Irrelevant cryptographic red herring
    sig = 0
    for c in pattern:
        sig = (sig * 31 + ord(c)) % 10007
    return sig

def validate_calibration(token):
    # Dead code path - never actually used
    if len(token) < 5:
        return False
    checksum = 0
    for i, ch in enumerate(token):
        checksum += (i + 1) * ord(ch)
    return checksum % 17 == 0

def encrypt_sequence(seq, key):
    # Distractor function - not related to final result
    return [(x + key) * 2 for x in seq]

def decrypt_sequence(seq, key):
    # Unused decryption logic
    return [(x / 2) - key for x in seq]

def build_lookup_table(keys):
    # Creates a decoy mapping that looks important but isn't used
    table = {}
    for i, k in enumerate(keys):
        table[k] = (i * 137) % 997
    return table

def assess_stability(metric):
    # Misleading intermediate computation
    if metric > 5:
        return "UNSTABLE"
    elif metric > 2:
        return "CAUTION"
    else:
        return "STABLE"

def calculate_entropy(values):
    # Red herring: computes information-theoretic entropy but unused
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log(p) for p in probs)

def merge_diagnostic_maps(map_a, map_b):
    # Complex-looking but irrelevant merging operation
    merged = {}
    for k in set(map_a.keys()) | set(map_b.keys()):
        merged[k] = map_a.get(k, 0) * 0.6 + map_b.get(k, 0) * 0.4
    return merged

def temporal_filter(sequence, window=3):
    # Unused time-series smoothing
    smoothed = []
    for i in range(len(sequence)):
        start = max(0, i - window + 1)
        smoothed.append(sum(sequence[start:i+1]) / (i - start + 1))
    return smoothed

def analyze_readings(normalized_data, thresholds):
    scores = {}
    for sensor_type, readings in normalized_data.items():
        above_threshold = sum(1 for v in readings if abs(v) > thresholds.get(sensor_type, 2.0))
        total = len(readings)
        scores[sensor_type] = (above_threshold / total) * 100 if total > 0 else 0
    
    # Composite score calculation - relevant
    weighted = (
        scores.get('temp', 0) * 0.3 +
        scores.get('pressure', 0) * 0.2 +
        scores.get('humidity', 0) * 0.2 +
        scores.get('co2', 0) * 0.3
    )
    
    # Final diagnostic logic - this is where the answer comes from
    if weighted > 15.0:
        level = 3
    elif weighted > 10.0:
        level = 2
    elif weighted > 5.0:
        level = 1
    else:
        level = 0
    
    return int(weighted) + level

def main():
    # Core execution flow
    raw_data = collect_sensor_data()
    
    # Real processing begins here
    processed_data = normalize_readings(raw_data)
    
    # Decoy operations with misleading outputs
    dummy_token = "CALIB_9A3X"
    validation_result = validate_calibration(dummy_token)  # Unused
    crypto_sig = generate_signature("sensor_net_v2")  # Not used
    
    # Build irrelevant lookup tables
    temp_keys = ['T101', 'T102', 'T103']
    lookup = build_lookup_table(temp_keys)  # Created but unused
    
    # Real threshold logic
    threshold_map = {
        'temp': 1.8,
        'pressure': 2.0,
        'humidity': 1.9,
        'co2': 1.7
    }
    
    # Apply encryption on normalized data? No — just a distraction
    if 'temp' in processed_data and processed_data['temp']:
        encrypted_temps = encrypt_sequence(processed_data['temp'], key=5)  # Computed but unused
        decrypted_temps = decrypt_sequence(encrypted_temps, key=5)  # Also unused
    
    # Temporal filtering on pressure? Defined but not applied
    if 'pressure' in processed_data:
        smoothed_pressure = temporal_filter(processed_data['pressure'])  # Calculated later but ignored
    
    # Calculate entropy of CO2 deviations - looks scientific but irrelevant
    if 'co2' in processed_data:
        co2_abs = [abs(x) for x in processed_data['co2']]
        entropy = calculate_entropy(co2_abs)  # Computed but unused
    
    # Now perform actual analysis
    final_diagnostic = analyze_readings(processed_data, threshold_map)
    
    # Print final result as required
    print(f"Result: {final_diagnostic}")
    
    # Additional decoy: merge fake maps
    fake_map_1 = {'temp': 12.5, 'co2': 8.3}
    fake_map_2 = {'temp': 10.1, 'pressure': 9.7}
    fused = merge_diagnostic_maps(fake_map_1, fake_map_2)  # Useless fusion

if __name__ == "__main__":
    main()