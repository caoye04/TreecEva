from collections import Counter, defaultdict

def analyze_text_patterns(input_text):
    char_freq = Counter(input_text)
    vowel_count = sum(char_freq[c] for c in 'aeiou' if c in char_freq)
    consonant_count = sum(char_freq[c] for c in char_freq if c.isalpha() and c not in 'aeiou')
    
    # Distractor: Calculate average character position (not used in final result)
    total_pos = 0
    for i, c in enumerate(input_text):
        total_pos += i
    avg_position = total_pos / len(input_text) if input_text else 0

    # Transform text by shifting vowels cyclically
    vowel_list = 'aeiou'
    shifted_text = ''
    vowel_mapping = {vowel_list[i]: vowel_list[(i+1) % 5] for i in range(5)}
    for c in input_text:
        if c in vowel_mapping:
            shifted_text += vowel_mapping[c]
        else:
            shifted_text += c
    
    return shifted_text, vowel_count, consonant_count

def process_shifted_analysis(text):
    # Track character transitions
    transition_count = defaultdict(int)
    for i in range(len(text) - 1):
        pair = text[i:i+2]
        transition_count[pair] += 1
    
    # Distractor: Unused frequency analysis
    pair_freq = Counter(transition_count.values())
    rare_transitions = sum(1 for v in pair_freq.values() if v < 2)

    # Compute weighted score based on transition density
    length_factor = len(text) if len(text) > 0 else 1
    unique_pairs = len(transition_count)
    density_score = unique_pairs / length_factor

    # Additional distractor computation
    entropy_approx = 0
    for count in transition_count.values():
        prob = count / (len(text) - 1)
        if prob > 0:
            entropy_approx -= prob * __import__('math').log(prob, 2)
    
    return density_score, unique_pairs

def calculate_final_score(data_dict):
    base = data_dict['density']
    adjustment = data_dict['vowels'] - data_dict['consonants']
    multiplier = data_dict['unique_pairs'] % 7 or 1
    
    # Complex but deterministic scoring
    intermediate = (base * 100) + abs(adjustment)
    if adjustment > 0:
        intermediate *= 1.1
    elif adjustment < 0:
        intermediate *= 0.9
    
    final = intermediate * multiplier
    
    # Red herring: unused smoothing operation
    smoothed = round(final, 2) if final > 50 else round(final, 3)
    
    return int(final)

# Main execution
raw_input = "algorithmic reasoning enables powerful abstractions"
shifted_output, vowels, consonants = analyze_text_patterns(raw_input)
density_result, unique_pair_count = process_shifted_analysis(shifted_output)

# Build data structure for final calculation
processed_data = {
    'density': density_result,
    'vowels': vowels,
    'consonants': consonants,
    'unique_pairs': unique_pair_count,
    'raw_length': len(raw_input),
    'shifted_length': len(shifted_output)
}

# Key statement
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")