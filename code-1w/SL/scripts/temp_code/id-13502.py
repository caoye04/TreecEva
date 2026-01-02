import itertools

def analyze_response_time(raw_data, threshold=0.5):
    """Irrelevant helper function for response time analysis."""
    filtered = [x for x in raw_data if x > threshold]
    return sum(filtered) / len(filtered) if filtered else 0.0

def validate_checksum(sequence):
    """Dummy checksum validator - not used in final result."""
    return sum(sequence) % 7 == 0

def transform_input(user_str):
    """Transforms string input into mixed-type list - partially relevant."""
    cleaned = user_str.strip().lower().replace('x', '')
    parts = cleaned.split(',')
    result = []
    for p in parts:
        if p.isdigit():
            result.append(int(p))
        elif '.' in p and p.replace('.', '').isdigit():
            result.append(float(p))
        else:
            result.append(len(p))
    # Distractor: modifies state but not used downstream
    temp_offset = sum(1 for r in result if isinstance(r, int)) * 0.1
    return result

def compute_entropy(values):
    """Calculates entropy-like metric - red herring."""
    from math import log
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * log(p) for p in probs)

def extract_features(data_stream):
    """Extract numerical features with decoy transformations."""
    feature_set = {}
    even_count = 0
    odd_sum = 0
    for item in data_stream:
        if isinstance(item, int) and item % 2 == 0:
            even_count += 1
        elif isinstance(item, int):
            odd_sum += item
    feature_set['evens'] = even_count
    feature_set['odd_total'] = odd_sum
    feature_set['ratio'] = even_count / (odd_sum + 1)
    # Dead code path
    if False:
        feature_set['fake_flag'] = True
    return feature_set

def calculate_baseline(reference_list):
    """Computes baseline score - irrelevant to final answer."""
    return sum(ref * (i + 1) for i, ref in enumerate(reference_list)) // len(reference_list)

def aggregate_performance(log_entries, weights):
    """Core function: computes final score based on filtered metrics."""
    cumulative = 0
    weight_keys = sorted(weights.keys())
    for entry in log_entries:
        # Only entries with 'active' flag contribute
        if not entry.get('active', False):
            continue
        mode = entry.get('mode', 'standard')
        raw_value = entry['value']
        
        # Transform value based on mode
        if mode == 'boosted':
            transformed = raw_value * 1.5
        elif mode == 'attenuated':
            transformed = raw_value * 0.7
        else:
            transformed = raw_value
        
        # Apply corresponding weight
        key = entry.get('category', 'default')
        w = weights.get(key, 1.0)
        cumulative += transformed * w
    
    # Final adjustment using string-derived constant
    adjustment_str = 'x7m9k2p'
    offset_char = adjustment_str[1]  # '7'
    adjustment = int(offset_char)  # 7
    return int(cumulative - adjustment)

# --- Main Execution ---
if __name__ == '__main__':
    # Simulated input data (mixed types)
    raw_timing_data = [0.1, 0.8, 0.3, 0.9, 0.6]
    checksum_sequence = [1, 2, 3, 4, 5]
    user_input = "12,x,hello,4.5,,world"
    
    # Irrelevant computations (distractors)
    avg_response = analyze_response_time(raw_timing_data)
    is_valid = validate_checksum(checksum_sequence)
    processed_input = transform_input(user_input)
    entropy_metric = compute_entropy([4, 5, 6, 7])
    features = extract_features(processed_input)
    baseline = calculate_baseline([3, 1, 4, 1])
    
    # Relevant data structures
    metrics_log = [
        {'value': 10, 'category': 'compute', 'mode': 'standard', 'active': True},
        {'value': 20, 'category': 'memory', 'mode': 'boosted', 'active': True},
        {'value': 15, 'category': 'compute', 'mode': 'standard', 'active': False},  # inactive
        {'value': 25, 'category': 'network', 'mode': 'attenuated', 'active': True},
        {'value': 30, 'category': 'storage', 'mode': 'standard', 'active': True}
    ]
    
    user_weights = {
        'compute': 1.2,
        'memory': 0.8,
        'network': 1.5,
        'storage': 1.0,
        'default': 1.0
    }
    
    # Key computation
    final_score = aggregate_performance(metrics_log, user_weights)
    
    # Generate auxiliary statistics (dead-end paths)
    stats_pairs = list(itertools.combinations([10, 20, 25, 30], 2))
    valid_pairs = [p for p in stats_pairs if (p[0] + p[1]) % 10 == 0]
    
    # Output target result
    print(f"Result: {final_score}")