from collections import defaultdict, Counter
import itertools

# Simulated sensor array data (temperature, pressure, humidity)
sensor_logs = [
    (23.5, 101.3, 45), (24.1, 101.5, 47), (22.9, 100.9, 44),
    (35.2, 105.1, 60), (36.0, 105.5, 62), (21.0, 99.8, 40),
    (20.5, 99.5, 38), (34.8, 104.9, 59), (25.0, 102.0, 50)
]

# Irrelevant transformation: convert to hex strings for 'security logging'
security_checksums = [hex(int(sum(x) * 10)) for x in sensor_logs]

# Decoy system: fake anomaly detection using random heuristics
def detect_anomaly_heuristic(logs):
    anomalies = []
    for i, (t, p, h) in enumerate(logs):
        if t > 30 and (p + h) % 7 < 2:
            anomalies.append(i)
    return anomalies

heuristic_flags = detect_anomaly_heuristic(sensor_logs)  # Unused result

# Real processing begins: filter out normal operating range
baseline_thresholds = {'temp': 30.0, 'pressure': 103.0, 'humidity': 55}
filtered_data = [entry for entry in sensor_logs if entry[0] > baseline_thresholds['temp']]

# Misleading aggregation: average of irrelevant combinations
temp_pressure_pairs = list(itertools.combinations([log[0] for log in filtered_data], 2))
avg_temp_diff = sum(abs(a - b) for a, b in temp_pressure_pairs) / len(temp_pressure_pairs) if temp_pressure_pairs else 0

# Another decoy: unused statistical depth calculation
def shannon_entropy(values):
    counts = Counter(values)
    total = len(values)
    return -sum((count/total) * (count/total).__log__(2) for count in counts.values())

entropy_probe = shannon_entropy([int(t) for t, _, _ in sensor_logs])  # Dead code path

# Threshold mapping with red herring entries
threshold_map = defaultdict(lambda: 1.0)
threshold_map.update({
    'critical_temp': 35.0,
    'warning_pressure': 105.0,
    'irrelevant_metric': 999.9,  # Distractor
    'debug_flag': -1  # Never used
})

# Core logic disguised among distractions
def analyze_variance(data_list):
    if not data_list:
        return 0.0
    temps = [x[0] for x in data_list]
    mean = sum(temps) / len(temps)
    variance = sum((x - mean) ** 2 for x in temps) / len(temps)
    return round(variance, 4)

variance_diagnostic = analyze_variance(filtered_data)

# Secondary decoy: recursive bit manipulation with no impact
def encrypt_index(idx, depth=3):
    if depth == 0:
        return idx
    return encrypt_index(idx ^ (idx << 1) & 255, depth - 1)

encrypted_indices = [encrypt_index(i) for i in range(len(filtered_data))]

# Final processing function buried in complexity
def process_readings(readings, thresholds):
    if not readings:
        return -1
    
    # Extract components
    temps, pressures, humidities = zip(*readings)
    
    # Compute weighted risk score (actual answer source)
    temp_score = sum(t > thresholds['critical_temp'] for t in temps) * 100
    pressure_score = sum(p > thresholds['warning_pressure'] for p in pressures) * 50
    humidity_factor = len([h for h in humidities if h > 58]) * 10
    
    # Irrelevant bitwise combination
    magic_key = (temp_score ^ pressure_score) & 0xFFFF
    magic_key = (magic_key >> 4) | ((magic_key << 12) & 0xFFFF)
    
    # Actual diagnostic output
    base_diagnostic = temp_score + pressure_score + humidity_factor
    
    # More distraction: unused cryptographic digest simulation
    digest_parts = [(base_diagnostic + i) % 256 for i in range(4)]
    checksum = 0
    for part in digest_parts:
        checksum = (checksum * 31 + part) & 0xFFFFFFFF
    
    return base_diagnostic  # Only this matters

# Critical execution point
final_diagnostic = process_readings(filtered_data, threshold_map)

# Output the target result
print(f"Target result: {final_diagnostic}")