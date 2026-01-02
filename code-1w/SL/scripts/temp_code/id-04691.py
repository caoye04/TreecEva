import itertools

def analyze_signal(samples):
    # Irrelevant signal processing function (dead end)
    filtered = [x for x in samples if abs(x) > 0.5]
    normalized = [x / max(filtered) for x in filtered]
    return sum(normalized[:10])

def compute_entropy(sequence):
    # Distractor: computes character frequency entropy
    freq = {}
    for c in sequence:
        freq[c] = freq.get(c, 0) + 1
    entropy = 0
    total = len(sequence)
    for count in freq.values():
        p = count / total
        entropy -= p * __import__('math').log2(p)
    return round(entropy, 3)

def transform_coordinates(coords):
    # Complex but irrelevant coordinate transformation
    result = []
    for x, y in coords:
        rotated_x = x * 0.707 - y * 0.707
        rotated_y = x * 0.707 + y * 0.707
        dist = (rotated_x**2 + rotated_y**2)**0.5
        if dist > 1.0:
            result.append((int(rotated_x), int(rotated_y)))
    return result

def validate_checksum(data_str):
    # Decoy validation with bit manipulation red herring
    checksum = 0
    for char in data_str:
        checksum ^= ord(char)
        checksum = (checksum << 1) & 0xFF
    return checksum % 16 == 0

def evaluate_performance(metrics):
    base_score = 0
    adjustment = 0
    
    # Key logic begins
    for k, v in metrics.items():
        if len(k) % 2 == 1:
            base_score += len(v)
        else:
            base_score -= v.count('A')  # Only some lists contain 'A'
    
    # Conditional path that looks important but is bypassed
    if base_score > 100:
        temp = list(itertools.permutations([1, 2, 3]))
        adjustment += len(temp)
    
    # Critical path: depends on string patterns
    pattern_match = 0
    for v in metrics.values():
        joined = ''.join(v)
        if 'AB' in joined and joined.endswith('C'):
            pattern_match += 1
    
    # Another distractor: unused intermediate calculation
    avg_length = sum(len(v) for v in metrics.values()) / len(metrics)
    scaled = int(avg_length * 1.5)
    
    # Early termination red herring (never reached due to logic)
    if scaled > 20:
        return -1
    
    # Real adjustment logic
    if pattern_match >= 2:
        adjustment += 50
    elif pattern_match == 1:
        adjustment += 20
    
    # Final computation with integer division
    final_score = (base_score * 2 + adjustment) // 3
    
    # Dead code: unreachable due to no exception
    try:
        risky = 1 / 0
    except:
        final_score -= 1000
    
    return final_score

# Main execution
if __name__ == '__main__':
    # Irrelevant data structures
    sensor_log = [0.1, 0.8, -1.2, 0.9, 0.3, -0.4, 1.1]
    geo_positions = [(1, 2), (-3, 4), (5, -6)]
    user_sequence = "ABACAD"
    config_key = "A1B2C3D4"
    
    # Distractor function calls
    _ = analyze_signal(sensor_log)
    _ = compute_entropy(user_sequence)
    _ = transform_coordinates(geo_positions)
    _ = validate_checksum(config_key)
    
    # Relevant input data
    metric_data = {
        'task1': ['X', 'Y', 'AB', 'C'],
        'job2A': ['A', 'B', 'C'],
        'op3': ['Z', 'AB', 'C'],
        'run4': ['A', 'X']
    }
    
    # Key assignment statement
    final_score = evaluate_performance(metric_data)
    
    # Print result as required
    print(f"Result: {final_score}")