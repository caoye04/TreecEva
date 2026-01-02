import math

# Simulate sensor data processing with noise filtering and weighted evaluation
def preprocess_data(raw):
    filtered = []
    noise_floor = 0.1
    for val in raw:
        if abs(val) > noise_floor:
            filtered.append(abs(val))
    return sorted(filtered, reverse=True)

# Determine dynamic weight adjustment based on data distribution
def calculate_weights(values):
    n = len(values)
    base_weight = 1.0 / n if n > 0 else 0
    adjustment_factor = lambda x: math.log(x + 1) / (x + 1) if x > 0 else 0
    weights = []
    for i, v in enumerate(values):
        # Irrelevant complexity: phase shift calculation (not used)
        phase_shift = (i % 3) * 0.01
        w = base_weight * (1 + adjustment_factor(v))
        weights.append(w)
    return weights

# Misleading helper: computes statistical moments but only mean is used
def compute_moments(vals):
    if not vals:
        return 0, 0, 0, 0
    mean_val = sum(vals) / len(vals)
    variance = sum((x - mean_val) ** 2 for x in vals) / len(vals)
    skewness = sum((x - mean_val) ** 3 for x in vals) / (len(vals) * variance ** 1.5) if variance > 0 else 0
    kurtosis = sum((x - mean_val) ** 4 for x in vals) / (len(vals) * variance ** 2) - 3 if variance > 0 else 0
    return mean_val, variance, skewness, kurtosis

# Core evaluation logic
def evaluate_performance(raw_data, custom_weights=None):
    cleaned = preprocess_data(raw_data)
    
    # Dead code path: unused transformation
    transformed = [math.sin(x * 0.5) + math.cos(x * 0.2) for x in raw_data]
    avg_transformed = sum(transformed) / len(transformed) if transformed else 0
    
    weights = custom_weights or calculate_weights(cleaned)
    
    # Extended logic chain: score built incrementally
    raw_score = 0
    for i in range(len(cleaned)):
        if i % 2 == 0:
            contribution = cleaned[i] * weights[i]
            raw_score += contribution
        else:
            temp = cleaned[i] ** 0.5
            raw_score += temp * weights[i]
    
    # Secondary adjustment using modular arithmetic
    adjustment = 0
    for i, w in enumerate(weights):
        if i > 0 and weights[i-1] > w:
            adjustment += (i * 7) % 5  # periodic bump
    
    # Normalization factor (semi-relevant)
    norm_factor = compute_moments(cleaned)[0]  # Only mean is extracted
    if norm_factor > 0:
        normalized = raw_score / norm_factor
    else:
        normalized = raw_score
    
    # Final non-linear scaling
    final = int(normalized ** 2 + adjustment)
    
    # Variables that look important but aren't used in final result
    outlier_count = sum(1 for x in raw_data if abs(x) > 2.0)
    peak_value = max(cleaned) if cleaned else 0
    stability_index = len([x for x in cleaned if x > 0.5])
    
    return final

# Input data with mixed signal and noise
sensor_readings = [0.05, -1.2, 0.8, 0.0, 2.3, -0.9, 1.7, 0.4, -0.03, 3.1, 0.2]
weights_list = calculate_weights(preprocess_data(sensor_readings))

# Key execution point
final_score = evaluate_performance(sensor_readings, weights_list)
print(f"Result: {final_score}")