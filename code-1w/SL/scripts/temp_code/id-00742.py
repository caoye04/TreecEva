import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.6, 26.7, 23.9, 24.4]
humidity_readings = [45, 48, 50, 55, 60, 62, 58]
pressure_readings = [1013, 1015, 1012, 1009, 1007, 1010, 1014]

# Irrelevant auxiliary variables (distractors)
baseline_offset = 0.78
scaling_factor = 1.02
epoch_timestamps = [1712050000, 1712050600, 1712051200, 1712051800, 1712052400, 1712053000, 1712053600]
noise_floor = 0.05

# Signal processing functions
def normalize_signal(signal):
    mean_val = sum(signal) / len(signal)
    return [(x - mean_val) * scaling_factor for x in signal]

def detect_anomalies(data, threshold=1.5):
    avg = sum(data) / len(data)
    deviations = [(abs(x - avg)) for x in data]
    return [i for i, dev in enumerate(deviations) if dev > threshold]

def calculate_entropy(values):
    total = sum(values)
    probabilities = [(v / total) for v in values if v > 0]
    return -sum(p * math.log(p) for p in probabilities if p > 0)

# Decoy function – never called (dead code path)
def legacy_compatibility_mode(data):
    transformed = []
    for x in data:
        if x < 0:
            transformed.append(math.exp(x))
        else:
            transformed.append(math.sqrt(x + 1))
    return transformed

# Dictionary-based mapping of diagnostic codes (used later)
diagnostic_map = {
    'normal': 100,
    'caution': 210,
    'warning': 350,
    'critical': 500,
    'resolved': 88
}

# Intermediate processing with red herrings
norm_temp = normalize_signal(temperature_readings)
norm_humidity = normalize_signal(humidity_readings)

anomalous_indices = detect_anomalies(norm_temp, threshold=0.8)

# Misleading entropy calculation on pressure (not used in final result)
pressure_entropy = calculate_entropy(pressure_readings)

# Real processing chain begins here
aggregated_diagnostics = []
for i, temp in enumerate(norm_temp):
    score = 0
    if abs(temp) > 1.0:
        score += diagnostic_map['warning']
    elif abs(temp) > 0.5:
        score += diagnostic_map['caution']
    else:
        score += diagnostic_map['normal']
    
    # Humidity influence (minor factor)
    if norm_humidity[i] > 1.2:
        score += 40
    
    aggregated_diagnostics.append(score)

# Bit manipulation decoy (irrelevant computation)
bitwise_checksum = 0
for val in humidity_readings:
    bitwise_checksum ^= int(val * 10) & 0xFF

# Unused transformation tree
transform_tree = {
    'level_1': {'branch_a': [], 'branch_b': []},
    'level_2': {
        'metrics': [
            {'type': 'temporal', 'value': baseline_offset},
            {'type': 'spatial', 'value': noise_floor}
        ]
    }
}

# Actual core logic disguised among distractions
processed_signals = []
for i, reading in enumerate(temperature_readings):
    # Apply moving average filter (3-point)
    window = temperature_readings[max(0, i-1):min(i+2, len(temperature_readings))]
    smoothed = sum(window) / len(window)
    processed_signals.append(smoothed * 1.05)  # Minor calibration

# Secondary decoy: string-based status encoding
status_flags = []
for x in processed_signals:
    if x > 25:
        status_flags.append('H')
    elif x < 23:
        status_flags.append('L')
    else:
        status_flags.append('M')

def analyze_readings(readings):
    base_score = 0
    critical_count = 0
    
    # Character frequency distractor
    flag_str = ''.join(status_flags)
    h_count = flag_str.count('H')
    l_count = flag_str.count('L')
    m_count = flag_str.count('M')
    
    # Real scoring logic
    for val in readings:
        if val > 26.0:
            base_score += diagnostic_map['critical']
            critical_count += 1
        elif val > 24.5:
            base_score += diagnostic_map['warning']
        elif val > 23.0:
            base_score += diagnostic_map['caution']
        else:
            base_score += diagnostic_map['normal']
    
    # Final adjustment based on trend (last 3)
    recent_trend = readings[-3:]
    if len(recent_trend) >= 3 and recent_trend[0] < recent_trend[1] < recent_trend[2]:
        base_score = int(base_score * 0.9)  # Slight reduction for improving trend
    
    # Irrelevant bitwise adjustment (never affects output due to order)
    temp_key = 0
    for x in pressure_readings:
        temp_key = (temp_key << 1) ^ int(x % 16)
    
    return base_score  # This is what matters

# Execution point of interest
final_diagnostic = analyze_readings(processed_signals)

# Print result as required
print(f"Target result: {final_diagnostic}")