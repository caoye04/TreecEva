import math

# Sensor calibration constants (some irrelevant)
BASE_SENSITIVITY = 0.87
NOISE_FLOOR_DB = -95.0
REFERENCE_VOLTAGE = 3.3
TEMP_CORRECTION_FACTOR = 0.0021
UNUSED_THRESHOLD = 42.0  # Dead variable

# Simulated raw sensor inputs (EMG and EEG hybrid)
raw_emg = [0.45, 0.67, 0.33, 0.89, 0.55, 0.76, 0.21, 0.91, 0.44, 0.65]
raw_eeg = [0.12, 0.15, 0.09, 0.21, 0.13, 0.19, 0.07, 0.23, 0.14, 0.18]

# Irrelevant signal array (decoy)
fake_sensor_data = [x * 0.01 + 0.005 for x in range(10)]

# Step 1: Normalize EMG readings to RMS-like values
normalized_emg = [val ** 2 for val in raw_emg]
total_power = sum(normalized_emg)
rms_emg = math.sqrt(total_power / len(normalized_emg))

# Step 2: Filter EEG by frequency band simulation (only upper half relevant)
alpha_band = [x for i, x in enumerate(raw_eeg) if i % 2 == 0]
beta_band = [x for i, x in enumerate(raw_eeg) if i % 2 == 1]

# Compute dominant rhythm strength (beta dominates here)
dominant_rhythm = sum(beta_band) * 1.8  # Weighted contribution

# Step 3: Apply temperature drift compensation (irrelevant in this case)
temp_offset = 0
calibrated_rhythm = dominant_rhythm - TEMP_CORRECTION_FACTOR * temp_offset  # No effect

# Step 4: Combine signals with gain staging
gain_staged = []
for e, a in zip(normalized_emg, alpha_band):
    adjusted = (e * BASE_SENSITIVITY) + (a * 0.5)
    gain_staged.append(round(adjusted, 4))

# Step 5: Detect anomalies above dynamic threshold
dynamic_threshold = rms_emg * 0.6
anomalies_detected = 0
for g in gain_staged:
    if g > dynamic_threshold:
        anomalies_detected += 1

# Step 6: Misleading diagnostic path (dead code branch)
def legacy_diagnosis(data):
    return sum(data) * 0.1  # Unused function

# Step 7: Signal processing chain
filtered_signal = list(map(lambda x: x * REFERENCE_VOLTAGE, gain_staged))
compressed_signal = [math.log(1 + abs(x)) for x in filtered_signal]

# Step 8: Extract peak deviation from compressed domain
peak_deviation = max(compressed_signal) - min(compressed_signal)

# Step 9: Process signals through diagnostic pipeline
processed_signals = {
    'rms': rms_emg,
    'rhythm': calibrated_rhythm,
    'anomalies': anomalies_detected,
    'peak_dev': peak_deviation,
    'size_hint': len(gain_staged)
}

# Step 10: Real-time system health check (distraction)
system_health = 100
if processed_signals['anomalies'] > 5:
    system_health -= 20
else:
    system_health -= 5  # Actual path, but not critical

# Step 11: Core analysis function with red herring variables
def analyze_readings(data_dict):
    base_score = data_dict['rms'] * 100
    rhythm_bonus = data_dict['rhythm'] * 10
    anomaly_penalty = data_dict['anomalies'] * 15
    stability_factor = 1.0 + (data_dict['peak_dev'] / 10)
    
    # Distractor calculation (unused)
    fake_index = math.sin(data_dict['rhythm']) * 1000
    temp_cache = [base_score / (i+1) for i in range(5)]  # Unused list comp
    
    # Actual computation path
    intermediate = base_score + rhythm_bonus - anomaly_penalty
    final_value = intermediate * stability_factor
    
    # Additional correction based on size (deterministic)
    if data_dict['size_hint'] >= 10:
        final_value *= 1.1
    else:
        final_value *= 0.9
    
    return int(round(final_value))

# Step 12: Execute main analysis
diagnostic_code = 200  # Status code, irrelevant
data_valid = True

if data_valid:
    final_diagnostic = analyze_readings(processed_signals)
    # Final printout
    print(f"Result: {final_diagnostic}")
else:
    final_diagnostic = -1
