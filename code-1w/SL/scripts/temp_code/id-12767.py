import math

# Simulated sensor data processing with performance evaluation
raw_data = [0.85, 0.92, 0.78, 0.96, 0.88]
offsets = [0.02, -0.01, 0.03, -0.02, 0.01]
adjusted_readings = [raw_data[i] + offsets[i] for i in range(len(raw_data))]

# Normalize readings to [0,1] using sigmoid transformation
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

normalized = [sigmoid(x) for x in adjusted_readings]

# Weight calibration factors (some are red herrings)
calibration_multipliers = [1.1, 0.95, 1.05, 0.9, 1.2]  # Not actually used
temp_buffers = [0.0] * 5
for i in range(5):
    temp_buffers[i] = normalized[i] * (1 + (i % 2) * 0.1)  # Artificial inflation

# Actual metric weights used in final calculation
metric_weights = [0.4, 0.3, 0.2, 0.05, 0.05]

# Simulate score adjustment based on environmental interference
interference_level = 0.08
attenuation_factor = 1 - interference_level
filtered_scores = [score * attenuation_factor for score in normalized]

# Raw scores after filtering
raw_scores = [round(score, 3) for score in filtered_scores]

# Dead code: Emulates legacy system compatibility
legacy_mode = False
compatibility_layer = lambda x: [val * 0.99 for val in x] if legacy_mode else x
processed_legacy = compatibility_layer(raw_scores.copy())  # Unused

# Performance evaluation function
def evaluate_performance(weights, scores):
    total = 0.0
    weighted_sum = 0.0
    weight_accum = 0.0
    
    # Secondary validation threshold
    threshold_check = 0.75
    valid_count = 0
    auxiliary_metric = 0.0
    
    for i in range(len(scores)):
        if scores[i] >= threshold_check:
            valid_count += 1
            auxiliary_metric += scores[i] ** 2  # Distractor metric
        # Irrelevant conditional branch
        if i % 3 == 0:
            auxiliary_metric *= 1.01
    
    # Main weighted scoring (core logic)
    for i in range(len(weights)):
        weighted_sum += weights[i] * scores[i]
        weight_accum += weights[i]
    
    # Normalize by total weight
    if weight_accum > 0:
        total = weighted_sum / weight_accum
    
    # Final nonlinear boost (only applied if conditions met)
    if valid_count >= 3:
        total = total * (1 + 0.05 * (valid_count - 3))
    
    return round(total, 4)

# Execute key computation
temperature_proxy = sum(adjusted_readings) / len(adjusted_readings)
drift_correction = math.log(temperature_proxy + 1)  # Unused physical model proxy

final_score = evaluate_performance(metric_weights, raw_scores)
print(f"Result: {final_score}")