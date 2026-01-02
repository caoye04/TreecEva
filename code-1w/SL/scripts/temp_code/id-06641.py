import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 19.8, 22.0, 25.3, 20.4, 21.8, 26.7, 18.9, 24.2]
humidity_readings = [45, 52, 58, 47, 60, 55, 50, 62, 44, 57]
pressure_readings = [1013, 1015, 1012, 1018, 1010, 1014, 1016, 1009, 1017, 1011]

# Irrelevant calibration coefficients (distractor)
calibration_a = 0.987
nonlinear_offset = 1.023
reference_bias = -0.045

def apply_filter(data, method='moving_avg', window=3):
    if method == 'moving_avg':
        filtered = []
        for i in range(len(data) - window + 1):
            filtered.append(sum(data[i:i+window]) / window)
        return filtered
    elif method == 'exponential':
        alpha = 0.3
        result = [data[0]]
        for i in range(1, len(data)):
            smoothed = alpha * data[i] + (1 - alpha) * result[-1]
            result.append(smoothed)
        return result
    else:
        return data  # no-op fallback

# Apply filter with irrelevant exponential smoothing (dead path)
decoy_temps = apply_filter(temperature_readings, method='exponential')

def detect_anomalies(seq, factor=1.5):
    median_val = sorted(seq)[len(seq)//2]
    mad = sorted([abs(x - median_val) for x in seq])[len(seq)//2]
    threshold = factor * mad
    anomalies = []
    for idx, val in enumerate(seq):
        if abs(val - median_val) > threshold:
            anomalies.append((idx, val))
    return anomalies

# Anomaly detection on humidity (distractor usage)
anomalous_humidity = detect_anomalies(humidity_readings, factor=1.8)

# Core processing begins here — meaningful transformation
evaluated_pairs = list(zip(temperature_readings, humidity_readings, pressure_readings))

# Filter out readings where temperature < 20 or pressure < 1010 (critical filtering)
filtered_data = [entry for entry in evaluated_pairs if entry[0] >= 20 and entry[2] >= 1010]

# Irrelevant derived metrics (misleading intermediate values)
virtual_index = sum([int(t * h / 10) for t, h, p in filtered_data])
entropy_proxy = math.log(len(filtered_data) + 1) * 1.5

# Threshold map based on empirical models (used later)
threshold_map = {
    'temp_baseline': 22.5,
    'humid_weight': 0.75,
    'pressure_decay': 0.01
}

# Unused function — red herring for data inversion
def invert_sequence(data_list):
    return [(d[2], d[1], d[0]) for d in reversed(data_list)]

# Secondary distraction: simulate false correlation
fake_correlation = 0
for i in range(len(humidity_readings) - 1):
    if humidity_readings[i] < humidity_readings[i+1]:
        fake_correlation += 1

# Bit manipulation decoy — simulates low-level diagnostics
status_flags = 0b10101100
masked_flags = status_flags & 0b11110000
extended_diagnostics = masked_flags << 2

# Real logic: multi-step processing function
def process_readings(readings, config):
    base_temp = config['temp_baseline']
    weight = config['humid_weight']
    decay = config['pressure_decay']
    
    cumulative_score = 0.0
    
    for temp, hum, press in readings:
        # Complex conditional expression with scientific rationale
        adjustment = (temp - base_temp) * weight
        if temp > base_temp:
            adjustment += math.sin(hum / 50)  # trigonometric influence
        
        # Pressure normalization with decay factor
        normalized_pressure = press * (1 - decay)
        
        # Conditional early boost
        if hum > 55 and temp < 24:
            adjustment *= 1.2
            break  # early exit changes accumulation
        
        # Accumulate score
        cumulative_score += adjustment + (normalized_pressure - 1010) / 10
    
    # Final nonlinear transformation
    if cumulative_score > 0:
        final_value = math.sqrt(abs(cumulative_score)) * 100
    else:
        final_value = -math.pow(abs(cumulative_score), 0.7) * 50
    
    return int(final_value)  # deterministic integral output

# Critical execution point
final_diagnostic = process_readings(filtered_data, threshold_map)

# Output required format
print(f"Target result: {final_diagnostic}")