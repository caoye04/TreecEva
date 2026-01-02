def analyze_pattern(sequence):
    """Irrelevant analysis function - distractor"""
    count = 0
    for i in range(len(sequence)):
        if sequence[i] % 2 == 0:
            count += 1
    return count * 2  # Dead end

def dummy_transform(x):
    """Decoy transformation - never used in critical path"""
    return (x << 2) ^ 5

def compute_hash(values):
    """Misleading hash computation - looks important but unused"""
    result = 0
    for idx, val in enumerate(values):
        result ^= val * (idx + 1)
    return result

def extract_features(dataset):
    """Red herring feature extraction with nested distractions"""
    temp = []
    decoy_sum = 0
    for i, row in enumerate(dataset):
        for j, col in enumerate(row):
            if i == j:
                decoy_sum += col
            temp.append(col * (i + 1))
    # This function returns something irrelevant
    return [sum(temp) // len(temp)]

def validate_input(config):
    """Unused validation logic - adds nesting depth"""
    if not config.get('active'):
        return False
    rules = config.get('rules', [])
    for rule in rules:
        if 'flag' in rule:
            if rule['flag'] < 0:
                return False
    return True

def process_metrics(data, weights):
    """Core function: combines arithmetic, logic, and data structure ops"""
    normalized = []
    total_weight = sum(weights)
    
    # Normalize weights
    norm_weights = [w / total_weight for w in weights]
    
    # Apply normalization and transform data
    for idx, (val, w) in enumerate(zip(data, norm_weights)):
        adjusted = val * w * 100
        if adjusted > 50:
            adjusted = adjusted ** 0.5  # Square root for high values
        else:
            adjusted = adjusted + 10
        normalized.append(round(adjusted, 4))
    
    # Secondary processing with conditional logic
    filtered = []
    for i, v in enumerate(normalized):
        if i % 2 == 0:
            filtered.append(v * 1.1)
        else:
            filtered.append(v * 0.9)
    
    # Compute final score using controlled bit manipulation
    base_score = sum(filtered)
    modifier = 0
    for v in filtered:
        # Bit trick: use fractional part to influence modifier
        int_part = int(v)
        frac_part = int((v - int_part) * 10000)
        modifier += (int_part ^ frac_part) & 0xF  # Use lower nibble
    
    # Final adjustment
    final_score = base_score - (modifier * 0.25)
    
    # Irrelevant cleanup
    temp_var = [0] * len(filtered)
    for k in range(len(temp_var)):
        temp_var[k] = k * 2
    
    return round(final_score, 4)

# Main execution block
if __name__ == '__main__':
    # Input data - meaningful signal embedded in noise
    raw_sequence = [2, 4, 6, 8, 10]
    hash_values = [17, 23, 19, 41, 37]
    config_data = {'active': True, 'rules': [{'flag': 1}, {'priority': -5}]}
    
    # Distractor calls
    _ = analyze_pattern(raw_sequence)
    _ = compute_hash(hash_values)
    _ = validate_input(config_data)
    
    # Critical data
    data = [88, 72, 91, 65, 83]
    weights = [3, 2, 4, 1, 3]
    
    # Dead code path - looks like it does something
    if len(data) > 10:
        scaled = [x * 1.5 for x in data]
    elif sum(weights) == 13:
        temp = 0
        for x in data:
            temp += x >> 1
    else:
        pass  # Silence
    
    # Key execution point
    final_score = process_metrics(data, weights)
    
    # Output result as required
    print(f"Target result: {final_score}")