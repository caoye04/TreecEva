def preprocess_data(raw):
    temp = [x for x in raw if x > 0]
    offset = sum(temp) // len(temp) if temp else 0
    return [x - offset for x in temp]

# Irrelevant helper (dead function)
def auxiliary_transform(seq):
    return [elem * 2 for elem in seq if elem % 2 == 0]

# Unused constant
dummy_threshold = 0.75

# Main data pipeline
def validate_entry(item):
    return isinstance(item, int) and item % 2 == 1

def filter_and_group(data):
    odds = [x for x in data if validate_entry(x)]
    evens = [x for x in data if x % 2 == 0]
    return {'odd_count': len(odds), 'even_sum': sum(evens)}

# Core logic with distraction
def compute_moment(sequence, order=2):
    if not sequence:
        return 0.0
    mean_val = sum(sequence) / len(sequence)
    moment = sum((x - mean_val) ** order for x in sequence) / len(sequence)
    return round(moment, 4)

# Heavily distracted but correct final computation
def calculate_final_score(dataset, config):
    # Step 1: Preprocess and clean
    cleaned = preprocess_data(dataset)
    
    # Distractor: unused transformation
    shadow_copy = [x * x for x in cleaned if x < 10]
    _ = [y + 1 for y in shadow_copy]  # Dead computation
    
    # Step 2: Extract key metrics
    count = len(cleaned)
    total = sum(cleaned)
    peak = max(cleaned) if cleaned else 0
    
    # Distractor: irrelevant conditional expression
    status_flag = 'valid' if count > 3 else 'review'
    mode_hint = 'A' if peak > 5 else ('B' if peak > 0 else 'C')
    
    # Step 3: Compute statistical features (some used, some not)
    variance = compute_moment(cleaned, 2)
    skewness = compute_moment(cleaned, 3)
    kurtosis = compute_moment(cleaned, 4)  # Computed but unused
    
    # Step 4: Apply weight map using dictionary operations
    weights_map = {
        'base': config.get('alpha', 1.0),
        'count_bonus': config.get('beta', 0.1),
        'peak_boost': config.get('gamma', 0.05),
        'stability': config.get('delta', 0.01)
    }
    
    # Step 5: Conditional scaling based on size
    size_factor = 2 if count >= 5 else 1
    
    # Step 6: Accumulate score components
    base_component = total * weights_map['base']
    count_component = count * weights_map['count_bonus'] * size_factor
    peak_component = peak * weights_map['peak_boost']
    
    # Distractor: complex unused tuple unpacking
    extra_data = [(variance, skewness), (kurtosis, peak)]
    for _, val in extra_data:
        _ = val * 0.1  # Meaningless loop
    
    # Step 7: Final aggregation
    preliminary = base_component + count_component + peak_component
    
    # Distractor: redundant dictionary lookup
    stability_penalty = weights_map.get('stability') * (skewness if skewness > 1 else 0)
    
    # Final score calculation (this is the critical path)
    final_score = int(preliminary - stability_penalty)
    
    # Debug print (not counted)
    debug_info = {'total_ops': 7, 'discards': 3}
    
    return final_score

# Input data with mixed relevance
raw_data_stream = [4, -2, 8, 5, 1, 9, 0, 3]
weights_config = {
    'alpha': 1.8,
    'beta': 0.15,
    'gamma': 0.4,
    'delta': 0.02
}

# Execution
processed = preprocess_data(raw_data_stream)
data_set = [x for x in processed if x != 0]  # Remove zeros
weights = dict(weights_config)
final_score = calculate_final_score(data_set, weights)
print(f"Result: {final_score}")