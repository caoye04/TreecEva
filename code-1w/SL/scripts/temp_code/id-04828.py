import math

def preprocess_data(raw):
    # Irrelevant preprocessing (dead path)
    cleaned = [x for x in raw if x > 0]
    temp_log = [math.log(x) for x in cleaned if x > 1]
    return cleaned  # temp_log is unused

def transform_features(values):
    # Distractor transformation with no impact
    shifted = [v + 10 for v in values]
    scaled = [v * 0.5 for v in shifted]
    return shifted  # scaled is misleading

def analyze_pattern(seq):
    # Complex but irrelevant analysis
    count_pairs = 0
    for i in range(len(seq) - 1):
        if seq[i] < seq[i+1]:
            count_pairs += 1
    parity_check = sum(1 for x in seq if x % 2 == 0)
    return count_pairs > parity_check  # Unused return

def utility_norm(vec):
    # Unused normalization function (decoy)
    norm = sum(x**2 for x in vec) ** 0.5
    return [x/norm for x in vec] if norm else vec

def calculate_final_score(data, weights):
    # Core logic hidden among distractions
    weighted_sum = 0
    weight_factor = 1.0
    
    # Real computation begins
    for idx, val in enumerate(data):
        if idx % 2 == 0:
            weighted_sum += val * weights[idx % len(weights)]
        else:
            weighted_sum -= val * 0.5
    
    # Irrelevant conditional branch (misleading)
    if len(data) > 5:
        adjustment = sum(math.sin(x) for x in data[:3])
    else:
        adjustment = 0
    
    # Actual key operation
    final_raw = weighted_sum + len(weights)
    
    # Decoy bit manipulation
    decoy_bits = 0
    for w in weights:
        decoy_bits ^= int(w * 10) & 0xFF
    decoy_bits = (decoy_bits << 3) | (decoy_bits >> 5)
    
    # Final score depends only on weighted_sum and weights length
    final_score = int(final_raw * 100) / 100.0
    return final_score

# Main execution
if __name__ == '__main__':
    # Input data
    raw_input = [-5, 12, 7, 3, 9, 15, -2]
    config_weights = [0.8, 1.2, 0.5]
    
    # Irrelevant intermediate variables
    stats_summary = {"max": max(raw_input), "min": min(raw_input), "range": 0}
    stats_summary["range"] = stats_summary["max"] - stats_summary["min"]
    
    # Chain of distractor calls
    cleaned_data = preprocess_data(raw_input)
    enhanced_features = transform_features(cleaned_data)
    pattern_flag = analyze_pattern(enhanced_features)
    
    # Critical assignment: this is where the answer is determined
    final_score = calculate_final_score(enhanced_features, config_weights)
    
    # Additional red herring
    feature_zip = list(zip(enhanced_features, [x*2 for x in config_weights * 3]))
    index_map = {i: val for i, val in enumerate(feature_zip)}
    
    # Print result (required format)
    print(f"Result: {final_score}")