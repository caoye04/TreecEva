def analyze_frequency(text):
    # Irrelevant helper function: counts character frequency but not used in final result
    freq = {}
    for char in text.lower():
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1
    return freq


def validate_checksum(sequence):
    # Semi-relevant computation: checksum logic that appears important but only affects filtering
    total = 0
    for i, val in enumerate(sequence):
        total += val * (i + 1)
    return total % 7 == 0


def extract_features(record):
    # Processes record into features, some relevant, some not
    raw_values = [ord(c) % 10 for c in record['tag']]
    offset = record.get('offset', 3)
    adjusted = [v + offset for v in raw_values]
    
    # Distractor: complex transformation that isn't used later
    transformed = [((x ** 2) + 5) % 9 for x in adjusted]
    
    # Relevant value: sum of adjusted values
    base_sum = sum(adjusted)
    
    return base_sum


def calculate_final_score(data, modifiers):
    score = 0
    temp_buffer = []
    
    # Real logic begins
    for item in data:
        if 'active' in item and not item['active']:
            continue
            
        feature_value = extract_features(item)
        
        # Simulate state accumulation
        temp_buffer.append(feature_value * 2)
        
        # Key logic: apply modifier based on category
        cat = item.get('category', 'default')
        mod = modifiers.get(cat, 1.0)
        
        # Intermediate distraction: unused weighted average attempt
        window_avg = sum(temp_buffer[-3:]) / len(temp_buffer[-3:]) if temp_buffer else 0
        
        # Actual contribution to score
        score += feature_value * mod
    
    # Additional interference: set operation that looks meaningful but is unused
    unique_scores = set(temp_buffer)
    outlier_count = len([x for x in unique_scores if x > 50])
    adjustment_factor = 0.9 if outlier_count > 2 else 1.0  # never applied
    
    # Final non-linear transformation actually used
    if score > 100:
        score = (score ** 0.5) * 2
    else:
        score = score * 1.1
    
    return int(score)

# Main execution
if __name__ == "__main__":
    
    # Simulated dataset: product tags with metadata
    data = [
        {'tag': 'AX7', 'category': 'premium', 'offset': 4, 'active': True},
        {'tag': 'BZ3', 'category': 'standard', 'offset': 2, 'active': True},
        {'tag': 'CX9', 'category': 'premium', 'offset': 5, 'active': False},  # inactive
        {'tag': 'DX1', 'category': 'basic', 'offset': 1, 'active': True},
        {'tag': 'EX5', 'category': 'standard', 'offset': 3, 'active': True}
    ]
    
    # Modifier map for scoring
    modifiers = {
        'premium': 1.5,
        'standard': 1.2,
        'basic': 0.8
    }
    
    # Dead code path: looks like preprocessing but unused
    checksum_data = [len(d['tag']) for d in data if d.get('active')]
    is_valid = validate_checksum(checksum_data)
    
    # String processing distractor
    all_tags = ''.join([d['tag'] for d in data])
    tag_analysis = {char: all_tags.count(char) for char in set(all_tags) if char.isdigit()}
    
    # This call contains the key statement
    final_score = calculate_final_score(data, modifiers)
    
    # Print result as required
    print(f"Result: {final_score}")