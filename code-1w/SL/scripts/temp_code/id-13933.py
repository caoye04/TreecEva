def analyze_text_patterns(input_text):
    char_frequency = {}
    for char in input_text:
        if char.isalpha():
            lower_char = char.lower()
            char_frequency[lower_char] = char_frequency.get(lower_char, 0) + 1

    sorted_chars = sorted(char_frequency.items(), key=lambda x: (-x[1], x[0]))
    top_five = [item[0] for item in sorted_chars[:5]]

    # Distractor: irrelevant vowel counting
    vowels = 'aeiou'
    total_vowels = sum(1 for c in top_five if c in vowels)

    return top_five


def transform_coordinates(coord_list):
    transformed = []
    for x, y in coord_list:
        rotated_x = int(y * 0.707 - x * 0.707)  # 45-degree rotation approx
        rotated_y = int(x * 0.707 + y * 0.707)
        distance = (rotated_x ** 2 + rotated_y ** 2) ** 0.5
        if distance > 10:
            transformed.append((rotated_x, rotated_y, round(distance, 3)))
    
    # Distractor: unused statistical summary
    lengths = [t[2] for t in transformed]
    avg_length = sum(lengths) / len(lengths) if lengths else 0
    
    return transformed


def calculate_final_score(data_map):
    base_value = data_map['offset']
    multiplier = len(data_map['items'])
    
    # Key computation
    raw_sum = sum(ord(ch) for ch in data_map['seed'])
    checksum = (raw_sum * base_value) % 97
    
    # Real score calculation
    score_components = []
    for idx, item in enumerate(data_map['items']):
        weighted = (idx + 1) * (ord(item[0]) % 10)
        score_components.append(weighted)
    
    aggregate = sum(score_components)
    final_score = (aggregate + checksum) * multiplier
    
    # Dead code: this doesn't affect result
    if final_score < 0:
        final_score += 1000
    
    return final_score

# Main execution
input_str = "QuantumResonanceX"
top_letters = analyze_text_patterns(input_str)

coords = [(3, 4), (5, 12), (8, 15), (7, 24)]
rotated_set = transform_coordinates(coords)

# Build data structure using dictionary operations and zip
indices = list(range(len(top_letters)))
letter_index_map = dict(zip(top_letters, indices))
filtered_pairs = {k: v for k, v in letter_index_map.items() if v % 2 == 0}

processed_data = {
    'seed': 'fx',
    'items': [key.upper() for key in filtered_pairs.keys()],
    'offset': len(rotated_set) + 5,
    'extras': {  # Unused nested data
        'stats': {'max_idx': max(indices), 'vowel_count': 2},
        'config': {'version': 'beta', 'active': True}
    }
}

# Critical statement
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")