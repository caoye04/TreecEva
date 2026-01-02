import math

# Simulated sensor data processing for environmental monitoring system
def analyze_readings(readings):
    filtered = [x for x in readings if 10 <= x <= 100]
    smoothed = []
    for i in range(len(filtered)):
        window = filtered[max(0, i-2):min(i+3, len(filtered))]
        smoothed.append(sum(window) / len(window))
    return smoothed

# Irrelevant helper: computes variance (not used in final path)
def compute_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

# Data calibration (distractor with misleading intermediate)
def calibrate_sensor(signal, offset=0.73, gain=1.05):
    adjusted = [(x * gain + offset) for x in signal]
    # Dead code path - never reached due to return
    if False:
        adjusted = [max(x, 0.1) for x in adjusted]
        adjusted = sorted(adjusted, reverse=True)
    return adjusted[:len(adjusted)//2 + 1]  # Partial use, creates confusion

# Core transformation chain
def extract_features(stream):
    chunks = [stream[i:i+4] for i in range(0, len(stream), 4)]
    features = []
    for chunk in chunks:
        if len(chunk) == 4:
            a, b, c, d = chunk
            # Multiple distractor calculations
            temp_1 = (a + b) * 0.5
            temp_2 = (c + d) * 0.5
            synergy = abs(temp_1 - temp_2) + 1e-8
            score = (temp_1 * temp_2) / synergy  # Actual relevant computation
            features.append(score)
    return features

# Red herring function: looks important but unused
def deprecated_normalization(vec):
    max_val = max(vec)
    return [v / max_val for v in vec if v > 0.5]

# Weighted aggregation with decoy logic
def aggregate_performance(metrics, weights):
    # Misleading initialization
    base_adjustment = 0.95
    scaling_factor = 1.08
    penalty_rate = 0.03
    
    # Real computation starts here
    weighted_sum = sum(m * w for m, w in zip(metrics, weights))
    total_weight = sum(weights)
    
    # Distractor block: complex-looking but unused
    if len(metrics) > 3:
        outlier_threshold = sum(metrics) / len(metrics) + 2 * math.sqrt(
            sum((x - sum(metrics)/len(metrics))**2 for x in metrics) / len(metrics)
        )
        filtered_metrics = [m for m in metrics if m < outlier_threshold]
        # This branch is not taken in our case
    else:
        stability_bonus = 0.0
        weighted_sum += stability_bonus  # No effect
    
    # Actual result calculation
    raw_result = weighted_sum / total_weight if total_weight != 0 else 0
    
    # Final adjustment using bit manipulation red herring
    magic_offset = (0x1F & 0x0A) ^ 0x05  # Constant: 10 ^ 5 = 15
    final_score = raw_result + magic_offset
    
    # Decoy output line (commented to mislead reasoning)
    # print(f'Debug: final_score adjusted by {magic_offset}')
    return final_score

# Irrelevant global constants (distractors)
MAX_BUFFER_SIZE = 256
DEFAULT_TIMEOUT = 15.5
CALIBRATION_MODE = False

# Simulated input data
raw_sensor_data = [85.6, 92.1, 15.3, 77.4, 68.2, 95.0, 10.1, 88.9, 45.3, 62.7]

# Processing pipeline with multiple distractions
filtered_data = analyze_readings(raw_sensor_data)

# Unused alternate path (creates interference)
if len(filtered_data) % 2 == 0:
    reversed_data = filtered_data[::-1]
    processed_signal = [x * 0.9 for x in reversed_data]
else:
    processed_signal = [x * 1.1 for x in filtered_data]

# Actual relevant path
calibrated_subset = calibrate_sensor(filtered_data[:6])
feature_vector = extract_features(calibrated_subset)

# Weight configuration (hidden in list comprehension)
weights = [w * 0.5 for w in [2, 3, 1, 4]][:len(feature_vector)]  # Results in [1.0, 1.5, 0.5]

# Critical execution point
final_score = aggregate_performance(feature_vector, weights)

# Output result
print(f'Target result: {final_score}')