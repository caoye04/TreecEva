import math

# Irrelevant helper function (decoy)
def normalize_vector(v):
    norm = sum(x ** 2 for x in v) ** 0.5
    return [x / norm for x in v] if norm != 0 else v

# Another decoy function with dead logic
def validate_checksum(sequence):
    checksum = 0
    for i, val in enumerate(sequence):
        checksum += val * (i + 1)
    return checksum % 10 == 0

# Misleading precomputed values (not all used)
baseline_offsets = [1.2, 0.8, -0.5, 3.1, 0.0]
signal_magnitudes = {'a': 4.5, 'b': 2.1, 'c': 6.7}

# Real data used in computation
data_set = [8, 12, 15, 7, 20]
weights = [0.1, 0.3, 0.2, 0.1, 0.3]

# Unused transformation (distractor)
transformed = [math.log(x + 1) for x in data_set]

# Decoy statistical summary
def compute_summary_stats(values):
    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    return {
        'mean': mean,
        'std': variance ** 0.5,
        'skew': sum((x - mean) ** 3 for x in values) / (len(values) * variance ** 1.5) if variance > 0 else 0
    }

# Simulate conditional weighting using nested logic and conditional expressions
def apply_weighting(value, weight, threshold=10):
    adjusted_weight = weight * 1.5 if value > threshold else weight * 0.8
    return value * adjusted_weight

# Recursive smoothing function (only partially relevant)
def smooth_sequence(seq, factor=0.9):
    if len(seq) <= 1:
        return seq[:]
    smoothed = [seq[0]]
    for i in range(1, len(seq)):
        smoothed.append(factor * smoothed[i-1] + (1 - factor) * seq[i])
    return smoothed

# Core calculation with red herring intermediate steps
def calculate_final_score(raw_data, importance_weights):
    # Step 1: Apply conditional weighting (key path)
    weighted_sum = sum(
        apply_weighting(val, wgt) for val, wgt in zip(raw_data, importance_weights)
    )
    
    # Step 2: Normalize to baseline (misleading normalization - not actually used)
    fake_normalized = weighted_sum / (sum(importance_weights) + 0.1)
    
    # Step 3: Apply recursive correction factor (distractor logic)
    temp_series = [weighted_sum, fake_normalized]
    corrected_series = smooth_sequence(temp_series, 0.75)
    
    # Step 4: Conditional adjustment based on parity of sum (red herring branch)
    total_raw = sum(raw_data)
    adjustment_factor = 1.0
    if total_raw % 2 == 0:
        adjustment_factor = 0.95
        secondary_check = sum(math.sin(x) for x in raw_data)  # Dead computation
    else:
        adjustment_factor = 1.05
        secondary_check = sum(math.cos(x) for x in raw_data)  # Also dead
    
    # Step 5: Final non-linear scaling (this one matters)
    scaled_score = math.sqrt(weighted_sum ** 2 + 100)
    
    # Step 6: Apply adjustment only if score exceeds threshold (actual gate)
    final_score = scaled_score * adjustment_factor if scaled_score > 15 else scaled_score
    
    # Irrelevant logging (distractor output)
    debug_info = {
        'raw_weighted': weighted_sum,
        'fake_norm': fake_normalized,
        'correction_tail': corrected_series[-1],
        'secondary_check': secondary_check
    }
    
    return final_score

# Execution with decoy calls
dummy_data = [1, 2, 3]
dummy_weights = [0.2, 0.2, 0.6]
_ = calculate_final_score(dummy_data, dummy_weights)  # Warm-up call (no effect)

# Actual target execution point
final_score = calculate_final_score(data_set, weights)
print(f"Result: {final_score}")