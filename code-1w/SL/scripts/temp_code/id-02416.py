import itertools

# Simulate sensor data stream with noise
data_stream = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6]
noise_mask = [1, -1, 1, -1, 1]  # Alternating noise pattern
calibration_factor = 0.95

# Apply noise correction using zip_longest for irregular patterns
corrected_data = []
for val, noise in itertools.zip_longest(data_stream, noise_mask, fillvalue=0):
    corrected_val = (val + noise) * calibration_factor
    corrected_data.append(round(corrected_val, 2))

# Extract every third reading (sensor sampling strategy)
sampled_data = [v for i, v in enumerate(corrected_data) if i % 3 == 0]

# Misleading block: entropy calculation (not used later)
entropy_proxy = 0
for x in sampled_data:
    if x > 4:
        entropy_proxy += 0.1
    else:
        entropy_proxy -= 0.05

# Normalize data to [0,1] range using min-max scaling
min_val, max_val = min(sampled_data), max(sampled_data)
normalized_data = [(x - min_val) / (max_val - min_val) for x in sampled_data]

# Filter out values below dynamic threshold (median-based)
median_val = sorted(normalized_data)[len(normalized_data) // 2]
dynamic_threshold = median_val * 1.1
filtered_data = [x for x in normalized_data if x >= dynamic_threshold]

# Auxiliary function to compute weighted signal quality
def compute_quality(seq):
    weights = [0.5 ** i for i in range(len(seq))]
    return sum(x * w for x, w in zip(seq, weights))

# Red herring: hypothetical backup threshold (unused)
backup_sensitivity = list(map(lambda x: x * 0.75, filtered_data))
peak_value = max(backup_sensitivity) if backup_sensitivity else 0

threshold = 0.45

# Core processing function with lambda and conditional logic
def process_signals(signal_list, thresh):
    # Assign importance scores using exponential weighting
    score_func = lambda x: 1.0 if x >= thresh else 0.3
    scores = [score_func(x) for x in signal_list]
    
    # Compute aggregate metrics
    avg_score = sum(scores) / len(scores) if scores else 0
    total_energy = sum(x**2 for x in signal_list)
    
    # Simulate decay over time using cumulative logic
    decay_chain = [total_energy]
    for _ in range(2):
        decay_chain.append(decay_chain[-1] * 0.85)
    
    final_energy = decay_chain[-1]
    
    # Final output combines quality, score, and stabilized energy
    quality_metric = compute_quality(signal_list)
    result = (avg_score * 100) + (quality_metric * 10) + (final_energy * 0.01)
    
    # Dead code branch: simulation override (never triggered in this input)
    override_mode = False
    if sum(signal_list) < 0:
        result *= 0.1  # Not applicable
        override_mode = True
    
    return round(result, 3)

# Execute main computation
final_output = process_signals(filtered_data, threshold)
print(f"Result: {final_output}")