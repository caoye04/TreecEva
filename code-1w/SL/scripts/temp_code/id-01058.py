import math

# Sensor calibration constants (irrelevant to final result)
CALIBRATION_OFFSET = 0.023
NOISE_FLOOR = 0.0012
MAX_SENSOR_RANGE = 1024

# Environmental simulation parameters (distractors)
def generate_background_noise(level):
    return [math.sin(i * 0.1) * level for i in range(5)]

noise_profile = generate_background_noise(0.05)
baseline_shift = sum(noise_profile) / len(noise_profile)

# Irrelevant data transformation chain
temp_buffers = [i * 0.01 for i in range(10)]
shifted_data = [x + baseline_shift for x in temp_buffers]
scaled_buffer = [x * 100 for x in shifted_data]

# Core system: Water Purity Analysis Pipeline
raw_readings = [88, 92, 76, 105, 89, 94, 77, 101, 85, 90, 96, 73, 88, 95]

# Step 1: Filter out-of-range values (simulated sensor clipping)
valid_range_mask = [70 <= val <= 100 for val in raw_readings]
filtered_readings = [raw_readings[i] for i in range(len(raw_readings)) if valid_range_mask[i]]

# Misleading intermediate calculation (dead path)
compression_factor = len(raw_readings) / (len(filtered_readings) + 1e-8)
adjusted_ratio = compression_factor * 100 if compression_factor > 1 else 0

# Step 2: Apply non-linear correction (red herring function)
def apply_nonlinear_correction(x):
    if x < 80:
        return x * 1.05
    elif x > 95:
        return x * 0.98
    else:
        return x  # No change

corrected_readings = [apply_nonlinear_correction(x) for x in filtered_readings]

# Unused diagnostic metric
variance_proxy = sum([(x - 85) ** 2 for x in corrected_readings]) / len(corrected_readings)

# Step 3: Analyze purity levels based on distribution characteristics
def analyze_purity_levels(readings):
    if not readings:
        return -1
    
    # Compute mean and dispersion (relevant)
    mean_val = sum(readings) / len(readings)
    
    # Compute mode using frequency map (partially relevant)
    freq_map = {}
    for val in readings:
        freq_map[val] = freq_map.get(val, 0) + 1
    mode_val = max(freq_map, key=freq_map.get)
    
    # Determine stability index based on clustering (key logic)
    close_to_mode = sum(1 for val in readings if abs(val - mode_val) <= 2)
    cluster_ratio = close_to_mode / len(readings)
    
    # Compute entropy-like score (distraction)
    entropy = 0
    for count in freq_map.values():
        p = count / len(readings)
        entropy -= p * math.log(p) if p > 0 else 0
    
    # Final score computation — only cluster_ratio and mean_val matter
    stability_bonus = 10 if cluster_ratio >= 0.6 else 0
    base_score = mean_val * 0.8
    mode_influence = abs(mean_val - mode_val) <= 3
    
    # Critical formula: this is where the answer comes from
    final_score = base_score + stability_bonus + (5 if mode_influence else 0)
    
    # Dead code branch (never executed due to logic)
    if entropy > 10:
        final_score *= 0.9
        
    return int(final_score)

# Step 4: Execute core analysis
filtration_score = analyze_purity_levels(filtered_readings)

# Unused secondary metrics (more distractions)
outlier_count = len(raw_readings) - len(filtered_readings)
drift_estimate = abs(filtered_readings[-1] - filtered_readings[0])
consistency_flag = drift_estimate < 15

# Additional red herring: set operation with no impact
duplicate_check_set = set([x for x in raw_readings if raw_readings.count(x) > 1])
unique_count = len(duplicate_check_set)

# Final output
print(f"Result: {filtration_score}")