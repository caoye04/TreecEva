import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.3, 26.0, 24.7, 23.9]
humidity_readings = [45, 47, 50, 44, 48, 51, 46]
pressure_readings = [1013, 1015, 1012, 1016, 1018, 1014, 1017]

# Irrelevant calibration constants (distractor)
CALIBRATION_OFFSET_A = 0.037
CALIBRATION_OFFSET_B = -0.012
REFERENCE_VOLTAGE = 5.0
NOISE_FLOOR_DB = 42

# Preprocessing: normalize readings using z-score (relevant)
def normalize(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    return [(x - mean_val) / std_dev for x in data]

# Misleading function: appears important but unused (dead code path)
def legacy_calibrate(values, factor=1.05):
    return [v * factor + CALIBRATION_OFFSET_A for v in values]

# Another decoy function with plausible name but no actual use
# Computes moving average but never called
def smooth_signal(signal, window=3):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window + 1)
        smoothed.append(sum(signal[start:i+1]) / (i - start + 1))
    return smoothed

# Composite health metric calculation — only partially used
# This is a red herring: it's defined and used once but doesn't affect final result
def compute_stability_index(vals):
    diffs = [abs(vals[i] - vals[i-1]) for i in range(1, len(vals))]
    return sum(diffs) / len(diffs)

# Key transformation pipeline
normalized_temp = normalize(temperature_readings)
normalized_humid = normalize(humidity_readings)
normalized_press = normalize(pressure_readings)

# Combine into tuples representing synchronized observations (relevant)
synchronized_data = list(zip(normalized_temp, normalized_humid, normalized_press))

# Apply nonlinear transformation to detect extreme conditions (relevant)
detect_extremes = lambda x: 1 if abs(x[0]) > 1.0 or abs(x[1]) > 1.0 else 0
extreme_flags = [detect_extremes(obs) for obs in synchronized_data]

# Distractor variables simulating auxiliary diagnostics
baseline_drift = sum(normalized_press[:3]) / 3
spike_count = 0
for i in range(1, len(normalized_temp)):
    if normalized_temp[i] - normalized_temp[i-1] > 0.8:
        spike_count += 1

# Secondary processing chain with misleading intermediate outputs
efficiency_score = 0.0
for t, h in zip(temperature_readings, humidity_readings):
    if t > 24 and h < 48:
        efficiency_score += 0.15
    elif t < 24:
        efficiency_score -= 0.05
efficiency_score = round(efficiency_score, 3)  # Decoy result

# Real processing: extract observations where temperature anomaly detected
filtered_observations = [obs for obs, flag in zip(synchronized_data, extreme_flags) if flag == 1]

# Transform each tuple by applying weighted combination (relevant)
transform_obs = lambda obs: (obs[0] * 2.1) + (obs[1] * 1.3) - (obs[2] * 0.9)
processed_data = [transform_obs(obs) for obs in filtered_observations]

# Unused complexity: graph-like structure definition (complete red herring)
adjacency_map = {}
for i in range(len(synchronized_data)):
    neighbors = []
    for j in range(len(synchronized_data)):
        if i != j:
            dist = sum((synchronized_data[i][k] - synchronized_data[j][k])**2 for k in range(3))
            if dist < 2.0:
                neighbors.append(j)
    adjacency_map[i] = neighbors

# Function that looks critical but only used on irrelevant data
# Simulates predictive modeling
predict_anomaly = lambda seq: sum(math.sin(x) for x in seq) > 0.5

# Dummy prediction on shuffled data — dead-end computation
shuffled_data = normalized_temp[::-1]
predicted_outcome = predict_anomaly(shuffled_data)
confidence_level = abs(sum(shuffled_data[:4])) if predicted_outcome else 0.0

# Core diagnostic analyzer — determines final output (key function)
def analyze_readings(readings_list):
    if not readings_list:
        return -999.0
    
    # Accumulate transformed values with conditional scaling
    total = 0.0
    for val in readings_list:
        if val > 0:
            total += val * 1.25
        else:
            total += val * 0.75
    
    # Apply logarithmic compression if magnitude is high (avoids overflow appearance)
    magnitude = abs(total)
    if magnitude > 10:
        compressed = math.log(magnitude) * (1 if total >= 0 else -1)
    else:
        compressed = total
    
    # Final adjustment based on count (critical step)
    adjustment_factor = len(readings_list) * 0.33
    return round(compressed + adjustment_factor, 6)

# Execute main analysis
final_diagnostic = analyze_readings(processed_data)

# Print result as required
print(f"Result: {final_diagnostic}")