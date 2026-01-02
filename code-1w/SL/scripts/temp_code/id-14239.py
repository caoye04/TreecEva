import math

# Irrelevant helper function (dead code path)
def unused_helper(x):
    return x ** 3 + 2 * x - 1

# Decoy transformation chain
def decoy_transform(values):
    temp = [v * 1.5 for v in values]
    temp = [t + 10 for t in temp if t < 50]
    temp = [t for t in temp if t % 2 == 0]
    return sorted(temp, reverse=True)

# Unused but misleading statistics calculator
def calculate_misleading_stats(seq):
    mean_val = sum(seq) / len(seq)
    variance = sum((x - mean_val) ** 2 for x in seq) / len(seq)
    peak = max(seq)
    return {'avg': mean_val, 'var': variance, 'max': peak}  # Never used

# Core bit manipulation preprocessor
def preprocess_bits(n):
    if n <= 0:
        return 0
    binary_str = bin(n)[2:]
    flipped = ''.join('1' if b == '0' else '0' for b in binary_str)
    return int(flipped, 2) ^ 17  # Bitwise XOR with magic number

# Conditional data filter with red herring logic
def filter_noisy_data(records):
    filtered = []
    for r in records:
        # Complex condition with short-circuiting and distractor comparisons
        is_valid = (r > 0) and (r % 2 == 1) and (r < 1000) and (r != 333) and ((r // 100) != 7)
        noise_check = (r & 15) != 7  # Bitwise mask check (partially relevant)
        if is_valid and noise_check:
            filtered.append(r)
    return filtered

# Main processing pipeline with conditional expressions and nesting
def process_pipeline(raw_data):
    # Step 1: Filter out invalid entries
    cleaned = filter_noisy_data(raw_data)
    
    # Step 2: Apply bit preprocessing to each element
    processed_bits = [preprocess_bits(x) for x in cleaned]
    
    # Step 3: Compute derived features (some irrelevant)
    feature_set = []
    total_sum = 0
    max_seen = -1
    for val in processed_bits:
        # Distractor computations
        squared_root = int(math.sqrt(val)) if val > 0 else 0
        mod_cluster = val % 19
        is_special = mod_cluster in [3, 7, 13]
        
        # Real computation path
        adjusted = val + (squared_root if is_special else -mod_cluster)
        total_sum += adjusted
        if adjusted > max_seen:
            max_seen = adjusted
        feature_set.append(adjusted)
    
    # Step 4: Conditional aggregation using ternary-like expression
    size_factor = len(feature_set) if len(feature_set) > 5 else 5
    adjustment = 3.5 if any(f > 100 for f in feature_set) else 1.2
    
    # Step 5: Final transformation with nested logic
    aggregate = 0
    for i, f in enumerate(feature_set):
        weight = (i + 1) / size_factor
        contribution = f * weight
        # Misleading intermediate that looks important
        _ = round(contribution * adjustment, 2)
        aggregate += contribution
    
    # Critical deterministic calculation (answer derivation)
    raw_score = aggregate * adjustment
    final_output = int(raw_score) - 42  # Deterministic integer result
    
    # Red herring: unused complex structure
    _ = [{'index': j, 'value': v, 'flagged': (v % 11 == 0)} for j, v in enumerate(processed_bits)]
    
    return final_output

# Simulated sensor data stream (deterministic input)
data_stream = [123, 456, 789, 101, 202, 303, 404, 505, 606, 707, 808, 909]

# Execution point of interest
final_output = process_pipeline(data_stream)
print(f"Result: {final_output}")