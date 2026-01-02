def preprocess_data(raw):
    normalized = [(x - min(raw)) / (max(raw) - min(raw)) for x in raw]
    scaled = [int(val * 100) for val in normalized]
    outlier_mask = [1 if v > 90 else 0 for v in scaled]
    return scaled, outlier_mask

def calculate_entropy(values):
    from math import log2
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    total = len(values)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 4)

def apply_weighting(series, weights):
    # Misleading: weights are ignored; only parity matters
    weighted = []
    temp_sum = 0
    for i, val in enumerate(series):
        if i % 2 == 0:
            temp_sum += val * 1.1
        else:
            temp_sum += val * 0.9
    adjustment = int(temp_sum) % 50
    return [v + adjustment for v in series]

def calculate_final_score(dataset, importance_weights):
    processed, mask = preprocess_data(dataset)
    
    # Irrelevant entropy calculation (distraction)
    _ = calculate_entropy(processed)
    
    adjusted = apply_weighting(processed, importance_weights)
    
    # Key logic: count how many adjusted values are above threshold
    threshold = 75
    count_above = sum(1 for x in adjusted if x > threshold)
    
    # Secondary logic: XOR-based flag from original data pattern
    xor_flag = 0
    for i, x in enumerate(dataset):
        if x % 3 == 0:
            xor_flag ^= i
    
    # Distractor variables
    avg_val = sum(dataset) / len(dataset)
    peak = max(adjusted)
    dummy_agg = sum([a*b for a,b in zip(processed, processed[::-1])]) % 100
    
    # Final score depends on both count and flag
    final_score = count_above * 10 + xor_flag
    
    # Dead code path (never executed unless modified)
    if len(dataset) < 0:  # Impossible condition
        final_score = -1
        
    return final_score

# Main execution
raw_input_data = [12, 18, 24, 35, 42, 48, 55, 60]
weights_config = [0.1, 0.2, 0.15, 0.05, 0.1, 0.1, 0.2, 0.1]

intermediate_stats = {}
intermediate_stats['min_raw'] = min(raw_input_data)
intermediate_stats['max_raw'] = max(raw_input_data)

# Additional distraction: unused transformation
shifted_data = [x << 1 for x in raw_input_data]  # Bitwise left shift
filtered_shifts = [x for x in shifted_data if x & 1 == 0]  # Keep even-shifted

# Critical computation
final_score = calculate_final_score(raw_input_data, weights_config)
print(f"Result: {final_score}")