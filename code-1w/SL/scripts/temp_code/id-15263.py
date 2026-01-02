import math

# Irrelevant helper function (decoy)
def dummy_transform(x):
    return (x ** 2 + 3) % 7

# Misleading data preprocessing path
def bad_normalization(data):
    mean_val = sum(data) / len(data)
    return [math.sqrt(abs(x - mean_val)) for x in data]  # Not used

# Real processing function
def clean_and_filter(raw):
    # Remove outliers beyond 2 standard deviations
    mean_raw = sum(raw) / len(raw)
    std_raw = math.sqrt(sum((x - mean_raw) ** 2 for x in raw) / len(raw))
    filtered = [x for x in raw if abs(x - mean_raw) <= 2 * std_raw]
    
    # Apply logarithmic scaling to compress dynamic range
    scaled = [math.log(x) if x > 0 else 0 for x in filtered]
    return scaled

# Secondary transformation with red herring variables
def enhance_features(data_list):
    enhanced = []
    temp_accum = 0  # Irrelevant accumulator
    decoy_sum = 0   # Dead variable
    
    for i, val in enumerate(data_list):
        if i % 2 == 0:
            transformed = val * 1.5
        else:
            transformed = val * 0.8
        
        # Bit manipulation red herring
        bit_fiddle = int(transformed) ^ 255
        decoy_sum += bit_fiddle  # Unused
        
        enhanced.append(transformed)
    
    # Dummy zip usage (not impactful)
    indices = list(range(len(enhanced)))
    paired = list(zip(indices, enhanced))
    shuffled_back = [val for idx, val in sorted(paired, key=lambda x: x[0])]  # Same order
    
    return shuffled_back

# Core scoring logic
def compute_weighted_average(values, weights=None):
    if not weights:
        weights = [1] * len(values)
    weighted_sum = sum(v * w for v, w in zip(values, weights))
    total_weight = sum(weights)
    return weighted_sum / total_weight if total_weight != 0 else 0

# Complex final computation with conditional logic
def compute_final_score(dataset):
    base_avg = compute_weighted_average(dataset)
    
    # Conditional adjustment based on distribution skew
    n = len(dataset)
    median_val = sorted(dataset)[n // 2]
    if base_avg > median_val:
        adjustment_factor = 1.1
    else:
        adjustment_factor = 0.95
    
    # Apply adjustment and clamp to realistic bounds
    adjusted = base_avg * adjustment_factor
    clamped = max(10, min(adjusted, 1000))  # Score cap
    
    # Extra distraction: simulate unused cryptographic hash
    hash_accum = 0
    for x in dataset:
        hash_accum ^= int(x * 100) & 0xFFFF
        hash_accum = (hash_accum << 1 | hash_accum >> 15) & 0xFFFF  # Roll left
    # hash_accum never used
    
    return round(clamped, 3)

# Main execution flow
if __name__ == '__main__':
    # Initial raw data (simulated sensor readings)
    raw_readings = [120, 150, 90, 200, 130, 140, 155, 110, 85, 160, 145, 135, 152]
    
    # Step 1: Clean and filter outliers
    processed_data = clean_and_filter(raw_readings)
    
    # Step 2: Enhance features (with internal distractions)
    processed_data = enhance_features(processed_data)
    
    # Step 3: Compute final score
    final_score = compute_final_score(processed_data)
    
    # Irrelevant post-processing block (dead code path)
    if final_score < 0:
        backup_model = [math.exp(x) for x in processed_data]
        final_score = sum(backup_model) / len(backup_model)
    
    # Print result
    print(f"Result: {final_score}")