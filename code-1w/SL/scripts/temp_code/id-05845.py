def preprocess_signal(raw_samples):
    """Apply normalization and filter noise (distractor: not used in final path)"""
    normalized = [x / max(raw_samples) for x in raw_samples]
    filtered = [x for x in normalized if x > 0.1]
    return filtered


def encode_sequence(seq):
    """Irrelevant encoding function - dead end"""
    return [bin(ord(c))[2:] for c in str(hash(str(seq)))[:10]]


def generate_checksum(data):
    """Decoy function: looks important but unused"""
    chk = 0
    for i, val in enumerate(data):
        chk ^= int(val * 100) + i
    return chk % 1000


def recursive_transform(values, depth=0):
    """Core transformation with modular arithmetic and recursion"""
    if depth >= 3:
        return [v * 1.5 for v in values]
    
    transformed = []
    for i, v in enumerate(values):
        if i % 2 == 0:
            transformed.append((v ** 2) % 17)
        else:
            transformed.append((v + i) % 11)
    
    return recursive_transform(transformed, depth + 1)


def build_threshold_map(keys, base_offset):
    """Constructs mapping used in final analysis"""
    # Uses zip and enumerate meaningfully
    labels = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
    key_pairs = list(zip(keys, labels[:len(keys)]))
    threshold_map = {}
    for idx, (key, label) in enumerate(key_pairs):
        if label.startswith('b') or label.endswith('a'):
            threshold_map[label] = (key * idx + base_offset) % 97
        else:
            threshold_map[label] = (key ** idx + base_offset) % 127
    return threshold_map


def analyze_signal(data, thresholds):
    """Final analysis combining boolean logic and arithmetic"""
    activation_scores = []
    for i, point in enumerate(data):
        score = 0
        # Conditional expression chain
        score += 7 if point > thresholds['gamma'] else -3
        score += 5 if point < thresholds['alpha'] else 0
        score += 10 if (point % 2 == 0) and (i % 3 == 0) else -2
        
        # Boolean short-circuit with relevance
        bonus = (thresholds.get('delta') > 50) and (score > 0) and 8
        score += bonus if isinstance(bonus, int) else 0
        
        activation_scores.append(score)
    
    # Final aggregation using string method on dummy tag (red herring usage)
    tag = "diagnostic_run_2024"
    multiplier = len(tag.split('_'))  # Always 3
    
    total = sum(activation_scores) * multiplier
    
    # Key decoy variable - looks like it matters
    validation_key = generate_checksum(data)  # Unused after this
    
    return int(total)

# Main execution flow
if __name__ == "__main__":
    # Initial dataset
    sensor_readings = [3, 7, 2, 8, 5]
    
    # Irrelevant preprocessing (distractor)
    cleaned = preprocess_signal(sensor_readings + [1, 0, 4])
    encoded = encode_sequence(cleaned)
    
    # Core computation begins
    transformed_data = recursive_transform(sensor_readings, 0)
    
    # Build map with meaningful structure
    keys = [4, 6, 9, 3, 8]
    threshold_map = build_threshold_map(keys, base_offset=13)
    
    # Critical statement
    final_diagnostic = analyze_signal(transformed_data, threshold_map)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")