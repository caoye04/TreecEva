import itertools

# Simulated sensor fusion system for environmental monitoring
sensor_a_data = [0.88, 0.91, 0.85, 0.93, 0.87]
sensor_b_data = [0.76, 0.82, 0.79, 0.81, 0.77]
sensor_c_data = [0.94, 0.90, 0.92, 0.89, 0.95]

# Irrelevant calibration constants (distractors)
calib_x = 1.02
kalman_gain = 0.88
offset_zeta = -0.05
threshold_alpha = 0.75

# Preprocess: normalize sensor readings to z-scores (only some are actually used)
def normalize(data):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_dev = variance ** 0.5
    return [(x - mean) / std_dev for x in data]

z_scores_a = normalize(sensor_a_data)
z_scores_b = normalize(sensor_b_data)  # Computed but not used
z_scores_c = normalize(sensor_c_data)

# Misleading intermediate calculation (dead path)
efficiency_metric = (sum(sensor_a_data) / 5) * 0.9
redundant_flag = False
if efficiency_metric > 0.8:
    redundant_flag = True
    temp_adjustment = 0.03  # Unused variable

# Weight configuration (some weights are decoys)
weights = {
    'primary': 0.6,
    'secondary': 0.3,
    'tertiary': 0.1,
    'deprecated': 0.0  # Explicitly unused weight
}

# Real-time anomaly detection (side computation)
anomalies = []
for val in sensor_a_data:
    if abs(val - 0.89) > 0.05:
        anomalies.append(True)
    else:
        anomalies.append(False)

# Masked confidence scoring using list comprehension and itertools
confidence_mask = [1 if not anomaly else 0.5 for anomaly in anomalies]
expanded_mask = list(itertools.chain.from_iterable(itertools.repeat(m, 3) for m in confidence_mask[:2]))  # Partial use

# Core metric computation
base_accuracy = sum(z_scores_a) / len(z_scores_a)
consistency_score = len([x for x in sensor_a_data if x > threshold_alpha])  # Uses distracting threshold_alpha
raw_stability = sum(abs(sensor_a_data[i] - sensor_a_data[i+1]) for i in range(len(sensor_a_data)-1))
stability_penalty = raw_stability * 0.1

# Simulated multi-source metrics (tertiary is fake)
metrics = {
    'primary': base_accuracy * 100 + 10,
    'secondary': consistency_score * 5,
    'tertiary': 42  # Arbitrary placeholder, will be scaled by 0.1 but still contributes
}

# Hidden correction factor based on mask length (subtle but valid)
correction_factor = len(expanded_mask) % 7 / 100  # Value: 6 % 7 / 100 → 6/100 → 0.06

# Critical statement
final_score = aggregate_performance(metrics, weights)

# Function defined after usage (misdirection)
def aggregate_performance(met, w):
    raw = (met['primary'] * w['primary'] + 
           met['secondary'] * w['secondary'] + 
           met['tertiary'] * w['tertiary'])
    return raw + correction_factor

# Print result as required
print(f"Result: {final_score}")