import math

# Simulated sensor data and calibration parameters
temperature_readings = [23.5, 24.1, 22.9, 25.3, 26.0, 24.8, 23.7]
pressure_readings = [101.3, 102.1, 100.9, 103.2, 104.0, 101.8, 99.7]
humidity_readings = [45.2, 47.1, 44.8, 48.3, 50.0, 46.5, 43.9]

# Irrelevant auxiliary arrays (distractors)
echo_reflections = [0.1, 0.3, 0.2, 0.5, 0.4, 0.6, 0.7]
baseline_noise = [0.05, 0.07, 0.04, 0.08, 0.06, 0.09, 0.11]
ghost_signals = [1, 0, 1, 0, 1, 1, 0]  # Unused in logic

# Calibration constants (some irrelevant)
CALIBRATION_OFFSET_A = 0.987
CALIBRATION_OFFSET_B = 1.013
NOISE_FLOOR = 0.02
TEMP_CORRECTION_FACTOR = 0.85  # Not used
PRESSURE_SCALE = 1.0

# Preprocessing: normalize and filter relevant signals
def preprocess_sensor_data(raw_data, scale=1.0, offset=0.0):
    filtered = []
    for val in raw_data:
        corrected = (val + offset) * scale
        if corrected > 0:
            filtered.append(round(corrected, 3))
    return filtered

# Misleading transformation chain (partially unused)
def compute_spectral_entropy(signal):
    n = len(signal)
    power_spectrum = [x ** 2 for x in signal[:n//2]]
    total_power = sum(power_spectrum)
    if total_power == 0:
        return 0.0
    probabilities = [p / total_power for p in power_spectrum]
    entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)
    return round(entropy, 4)

# Real-time anomaly detection with red herring branches
def detect_anomalies(stream, threshold=1.5):
    moving_avg = sum(stream[:3]) / 3
    deviations = []
    for i in range(len(stream)):
        dev = abs(stream[i] - moving_avg)
        deviations.append(dev)
        if i >= 2:
            moving_avg = sum(stream[i-2:i+1]) / 3
    
    # Dead code path: never executed due to fixed threshold
    if threshold < 0:
        return [0] * len(stream)  # Impossible condition
    
    return [1 if d > threshold else 0 for d in deviations]

# Core processing function with conditional expressions
processed_temperature = preprocess_sensor_data(temperature_readings, PRESSURE_SCALE, CALIBRATION_OFFSET_A - 1)
processed_pressure = preprocess_sensor_data(pressure_readings, 1.01, -0.1)
processed_humidity = preprocess_sensor_data(humidity_readings, 0.99, 0.05)

# Distractor: complex but unused computation
spectral_temp = compute_spectral_entropy(processed_temperature)
spectral_pres = compute_spectral_entropy(processed_pressure)
spectral_hum = compute_spectral_entropy(processed_humidity)
composite_entropy = (spectral_temp + spectral_pres + spectral_hum) / 3

# Anomaly flags (only pressure anomalies are used later)
temp_anomalies = detect_anomalies(processed_temperature, 1.5)
pres_anomalies = detect_anomalies(processed_pressure, 1.2)  # Used
hum_anomalies = detect_anomalies(processed_humidity, 1.5)

# Simulated packet buffer with decoy operations
packet_buffer = []
for i in range(len(processed_temperature)):
    packet = {
        'seq': i,
        'temp': processed_temperature[i],
        'pres': processed_pressure[i],
        'hum': processed_humidity[i],
        'flags': {
            't': temp_anomalies[i],
            'p': pres_anomalies[i],
            'h': hum_anomalies[i]
        }
    }
    # Conditional expression (python feature)
    status_code = 200 if packet['flags']['p'] == 0 else 503
    packet['status'] = status_code
    packet_buffer.append(packet)

# Extract only non-anomalous pressure readings for final analysis
valid_pressure_samples = [p['pres'] for p in packet_buffer if p['flags']['p'] == 0]

# Secondary filtering based on temperature range (additional logic)
reference_temp = sum(processed_temperature) / len(processed_temperature)
temp_stable_mask = [1 if abs(t - reference_temp) < 1.0 else 0 for t in processed_temperature]

# Final data alignment: cross-validate pressure with temperature stability
aligned_data = []
for i in range(len(valid_pressure_samples)):
    # Map index back through original structure (complex indexing)
    orig_idx = [j for j, p in enumerate(packet_buffer) if p['flags']['p'] == 0][i]
    if orig_idx < len(temp_stable_mask) and temp_stable_mask[orig_idx]:
        aligned_data.append(valid_pressure_samples[i])

# Signal transformation pyramid (with distractor layers)
def transform_signal(x, level=1):
    if level == 1:
        return x ** 2
    elif level == 2:
        return math.sqrt(abs(x))
    else:
        return abs(x) * math.pi  # Unused branch

# Apply real transformation
transformed_alphas = [transform_signal(x, 1) for x in aligned_data]

# Weighted accumulation with conditional weights
base_weight = 0.7
adjusted_weights = [base_weight if x < 105 else base_weight * 1.3 for x in transformed_alphas]
cumulative_signal = 0.0
for i in range(len(transformed_alphas)):
    cumulative_signal += transformed_alphas[i] * adjusted_weights[i]

cumulative_signal = round(cumulative_signal, 4)

# Final diagnostic computation
intermediate_metric = len(aligned_data) * math.log2(max(transformed_alphas) + 1)
penalty_factor = 0.95 ** sum(pres_anomalies)  # Depends on anomaly count

# Critical statement
final_diagnostic = analyze_signal(processed_data)

# Supporting functions defined after use (misdirection)
def analyze_signal(data_list):
    """Actually uses global state despite parameter"""
    raw_sum = sum(valid_pressure_samples)
    adjustment = math.sin(math.pi / 6) * penalty_factor
    result = (cumulative_signal + intermediate_metric) * adjustment
    return int(round(result))

processed_data = [1.1, 2.2, 3.3]  # Never used in actual computation

# Print final result as required
print(f"Result: {final_diagnostic}")