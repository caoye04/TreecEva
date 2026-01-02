def transform_sequence(seq, key):
    shifted = [(x + key) % 256 for x in seq]
    inverted = [255 - x for x in shifted]  # Irrelevant transformation
    return shifted

def validate_checksum(data):
    checksum = 0
    for i, val in enumerate(data):
        checksum ^= (val + i) % 17
    return checksum == 0  # Rarely true, dead logic path

def decode_payload(raw):
    decoded = []
    for i in range(0, len(raw), 2):
        if i + 1 < len(raw):
            combined = (raw[i] << 8) | raw[i + 1]
            decoded.append(combined % 97)
    return decoded  # Unused function in execution flow

def compute_entropy(values):
    from math import log2
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    total = len(values)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return entropy  # Computed but not used

def analyze_patterns(data_list):
    pattern_scores = []
    for idx, item in enumerate(data_list):
        score = 0
        if item % 3 == 0:
            score += 5
        if item > 50:
            score += 3
        temp_str = str(item)
        if temp_str.startswith('7'):
            score += 10
        if len(temp_str) == 2:
            score *= 1.1
        pattern_scores.append(score)
    return pattern_scores

def aggregate_metrics(timestamps, readings):
    metrics = {}
    time_diffs = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps)-1)]
    avg_interval = sum(time_diffs) / len(time_diffs) if time_diffs else 0
    metrics['avg_interval'] = avg_interval
    metrics['peak'] = max(readings) if readings else 0
    metrics['baseline'] = min(readings) if readings else 0
    return metrics

def process_results(data, config_map):
    # Core logic begins here
    base_values = [x for x in data if x % 2 == 1]  # Filter odd numbers
    scaled = [v * config_map['scale'] for v in base_values]
    
    # Apply shifting based on offset
    shifted_scaled = [s + config_map['offset'] for s in scaled]
    
    # Distractor: string-based filtering (irrelevant due to data type)
    valid_chars = '0123456789'
    filtered_scaled = []
    for num in shifted_scaled:
        if all(c in valid_chars for c in str(num)):
            filtered_scaled.append(num)
    
    # Real computation: weighted sum using position
    weighted_sum = 0
    for i, val in enumerate(filtered_scaled):
        weight = config_map['weights'][i % len(config_map['weights'])]
        weighted_sum += val * weight
    
    # Secondary adjustment via modular arithmetic
    adjusted_total = weighted_sum % 8971
    
    # Final nonlinear transformation
    final_score = (adjusted_total ^ 0x5F) + config_map['bonus']
    
    # Dead code branch: never reached due to structure
    if validate_checksum(data):
        final_score -= 1000
    
    return final_score

# Main execution block
if __name__ == '__main__':
    # Simulated encoded sensor-like data (avoiding sensor theme by treating as abstract sequence)
    raw_sequence = list(range(10, 150, 7))  # [10, 17, 24, ...]
    encoded_data = transform_sequence(raw_sequence, key=13)
    
    # Auxiliary analysis with red herring outputs
    ent = compute_entropy(encoded_data)
    patterns = analyze_patterns(encoded_data)
    metrics = aggregate_metrics(list(range(0, 1000, 100)), encoded_data[:10])
    
    # Configuration map with multiple entries, some unused
    weights = {
        'scale': 3,
        'offset': 7,
        'bonus': 42,
        'weights': [1, 2, 4],  # Repeating cycle
        'threshold': 85,
        'decay': 0.9
    }
    
    # Critical execution point
    final_score = process_results(encoded_data, weights)
    
    # Output result
    print(f"Result: {final_score}")