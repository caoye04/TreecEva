import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 24.9, 23.7]
humidity_readings = [45, 48, 50, 55, 60, 58, 52]
pressure_readings = [1013, 1015, 1012, 1010, 1008, 1009, 1011]

# Irrelevant calibration constants (distractor)
CALIBRATION_OFFSET_A = 0.0032
CALIBRATION_OFFSET_B = -0.0018
REFERENCE_VOLTAGE = 3.3

# Preprocess function with red herring logic
def preprocess_sensor_data(raw_data, sensor_type='generic'):
    normalized = []
    base_ref = sum(raw_data) / len(raw_data)
    for val in raw_data:
        adjusted = (val - base_ref) * 1.05
        normalized.append(round(adjusted + 0.001, 3))  # Minor noise injection (irrelevant)
    
    # Dead code path - never used in final computation
    if sensor_type == 'fake_type':
        return [x * 2 for x in normalized]
        
    return normalized

# Signal processing with multiple distractions
def filter_anomalies(data_sequence):
    filtered = []
    anomaly_flags = []
    threshold = (max(data_sequence) - min(data_sequence)) * 0.1
    
    for x in data_sequence:
        deviation = abs(x - sum(data_sequence)/len(data_sequence))
        if deviation > threshold:
            anomaly_flags.append(True)
        else:
            anomaly_flags.append(False)
            filtered.append(x)
            
    # Decoy return - not actually used
    stats_summary = {
        'count': len(data_sequence),
        'filtered_count': len(filtered),
        'anomaly_rate': sum(anomaly_flags) / len(anomaly_flags)
    }
    
    return filtered  # Only this matters

# Complex transformation with list comprehension and bit manipulation distraction
def transform_signal_components(signal_list):
    transformed = []
    shift_key = 3  # Used in decoy operation
    mask = 0b1111
    
    for i, val in enumerate(signal_list):
        # Real transformation
        scaled = val * math.sin(i + 1)
        quantized = int(abs(scaled * 100)) % 1000
        
        # Irrelevant bitwise chain (red herring)
        decoy_op = (quantized ^ mask) << shift_key
        decoy_op = (decoy_op & 0xFFFF) >> 1
        
        transformed.append(quantized)
    
    # List comprehension - actual relevant use
    squared_components = [x**2 for x in transformed]
    energy_estimate = sum(squared_components) / len(squared_components)
    
    return transformed, energy_estimate

# Higher-level analysis with misleading branching
def integrate_system_metrics(temp_data, hum_data):
    score = 0
    
    temp_trend = sum([temp_data[i+1] - temp_data[i] for i in range(len(temp_data)-1)])
    hum_trend = sum([hum_data[i+1] - hum_data[i] for i in range(len(hum_data)-1)])
    
    # Complex conditional with dead branches
    if temp_trend > 2 and hum_trend < -2:
        score += 10
    elif temp_trend < -1 and hum_trend > 3:
        score += 5  # This branch is unreachable given data
    else:
        score += 3  # Actual path taken
    
    # Unused scoring variants (distraction)
    stability_index = (abs(temp_trend) + abs(hum_trend)) / 2
    reliability_score = 100 - (stability_index * 2)
    
    return score  # Only score matters

# Final diagnostic engine with key logic hidden among noise
def analyze_readings(processed_signals):
    base_value = 0
    
    # Simulated ML-like weighting (simplified)
    weights = [0.8, 1.1, 0.9, 1.2, 1.0, 0.7, 1.3]
    weighted_sum = sum(processed_signals[i] * weights[i % len(weights)] for i in range(len(processed_signals)))
    
    # Normalization using integer division and rounding (relevant)
    normalized_score = int(weighted_sum // 1)  # Floor to integer
    
    # Multiple decoy calculations
    entropy_approx = 0
    for x in processed_signals:
        if x > 0:
            entropy_approx -= x * math.log(x + 1e-8)
    
    complexity_factor = len(processed_signals) ** 1.5
    adjusted_entropy = entropy_approx / (complexity_factor + 1)

    # Fake confidence metric (never used)
    confidence = 97.3 if abs(adjusted_entropy) < 5 else 64.1
    
    # Critical final adjustment based on system integration
    integration_bonus = integrate_system_metrics(temperature_readings, humidity_readings)
    final_diagnostic = normalized_score + integration_bonus * 10
    
    return final_diagnostic

# === EXECUTION FLOW WITH DISTRACTORS ===

# Step 1: Preprocessing (with irrelevant calls)
dummy_call_result = preprocess_sensor_data(pressure_readings, 'fake_type')  # Dead call
processed_temps = preprocess_sensor_data(temperature_readings, 'temp')
processed_humidity = preprocess_sensor_data(humidity_readings, 'humidity')

# Step 2: Anomaly filtering
clean_temps = filter_anomalies(processed_temps)
clean_humidity = filter_anomalies(processed_humidity)

# Step 3: Signal transformation
temp_components, temp_energy = transform_signal_components(clean_temps)
hum_components, hum_energy = transform_signal_components(clean_humidity)

# Step 4: Composite signal generation (list comprehension)
combined_signal = [a + b for a, b in zip(temp_components, hum_components)]
processed_signals = [x % 250 for x in combined_signal]  # Wrap to valid range

# Step 5: Final diagnostic (KEY STATEMENT)
final_diagnostic = analyze_readings(processed_signals)

print(f"Target result: {final_diagnostic}")