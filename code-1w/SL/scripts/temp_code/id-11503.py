from collections import defaultdict

# Simulate sensor data with some noise
data = [104, 98, 112, 97, 108, 115, 95]
weights = [0.1, 0.15, 0.2, 0.05, 0.1, 0.25, 0.1]

# Irrelevant baseline metrics (distractor)
baseline_avg = sum(range(100, 110)) / 10
offset_correction = 0.95
adjusted_offsets = [x * offset_correction for x in range(len(data))]

# Misleading transformation using lambda (not used in final path)
transform = lambda x: (x - min(data)) / (max(data) - min(data)) if max(data) != min(data) else 0
normalized_data = list(map(transform, data))

# Auxiliary tracking structure (semi-relevant)
signal_history = defaultdict(int)
for i, val in enumerate(data):
    signal_history[i] = val * weights[i]

# Noise threshold filter (partially relevant but not directly used)
noise_floor = 90
filtered_data = [x for x in data if x > noise_floor]

# Weighted calculation with distraction from unused branches
running_total = 0.0
distortion_factor = 1.03  # Unused red herring
clip_threshold = 110
clipped_values = []

for val in data:
    if val > clip_threshold:
        clipped_values.append(clip_threshold)
    else:
        clipped_values.append(val)

# Actual core logic embedded in distractions
temp_weighted_sum = 0
weight_accumulator = 0

for i in range(len(clipped_values)):
    temp_weighted_sum += clipped_values[i] * weights[i]
    weight_accumulator += weights[i]

# Final evaluation function that uses correct path
def evaluate_performance(readings, importance_weights):
    weighted_sum = 0
    total_weight = sum(importance_weights)
    
    # Secondary filtering that doesn't change outcome due to data properties
    valid_indices = [i for i in range(len(readings)) if readings[i] >= 95]
    
    for i in valid_indices:
        weighted_sum += readings[i] * importance_weights[i]
    
    # This scaling is redundant since total_weight == 1.0, but included for confusion
    scaled_result = weighted_sum / total_weight if total_weight else 0
    
    # Apply arbitrary domain-specific adjustment
    calibration_offset = 2.5
    return int(scaled_result + calibration_offset)

# Execution point of interest
final_score = evaluate_performance(data, weights)

print(f"Result: {final_score}")