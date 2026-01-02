from collections import defaultdict, Counter

def analyze_frequency(tokens):
    freq_map = defaultdict(int)
    for token in tokens:
        freq_map[token] += 1
    return freq_map

def extract_vowels(text):
    vowels = 'aeiou'
    vowel_count = 0
    for char in text.lower():
        if char in vowels:
            vowel_count += 1
    return vowel_count

def preprocess_entries(entries):
    cleaned = []
    stats = defaultdict(int)
    temp_buffer = []

    for idx, entry in enumerate(entries):
        stripped = entry.strip().lower()
        if len(stripped) == 0:
            continue
        
        # Irrelevant transformation (distractor)
        reversed_str = stripped[::-1]
        capitalized = stripped.title()
        
        words = stripped.split(' ')
        word_count = len(words)
        
        stats['total_words'] += word_count
        stats['entry_count'] += 1
        
        if word_count > 1:
            temp_buffer.append(words)
        else:
            temp_buffer.append([stripped])
        
        # Dead computation: used nowhere
        dummy_sum = sum(ord(c) for c in stripped) % 7
        
    cleaned = [item for sublist in temp_buffer for item in sublist]
    return cleaned, dict(stats)

def compute_entropy(freq_dict):
    import math
    total = sum(freq_dict.values())
    entropy = 0.0
    for count in freq_dict.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

def compute_final_score(data):
    raw_freq = Counter(data)
    filtered_tokens = [t for t, c in raw_freq.items() if c >= 2]
    
    # Secondary distractor: character-level analysis with no impact
    char_length_sum = 0
    for token in data:
        char_length_sum += len(token)
    average_length = char_length_sum / len(data) if data else 0
    
    # Core logic step 1: frequency-based weighting
    weight_map = {}
    for token in filtered_tokens:
        base_weight = len(token)
        frequency_bonus = raw_freq[token] - 1
        weight_map[token] = base_weight + frequency_bonus * 0.5
    
    # Core logic step 2: score aggregation
    raw_score = sum(weight_map.values())
    
    # Core logic step 3: normalization by unique token count
    penalty = len(raw_freq) - len(filtered_tokens)
    final_score = int(raw_score * 10) - (penalty * 3)
    
    # Red herring variable
    debug_trace = f'Score computed with {len(filtered_tokens)} tokens'
    
    return final_score

# Main execution
if __name__ == '__main__':
    input_data = [
        'apple banana cherry',
        'banana date elderberry',
        'fig grape apple',
        'cherry fig date',
        'kiwi lemon mango',
        'apple grape kiwi',
        'mango orange',
        'grape kiwi mango'
    ]

    # Step 1: Preprocess and extract tokens
    processed_data, summary_stats = preprocess_entries(input_data)
    
    # Step 2: Analyze frequencies (used later)
    frequency_analysis = analyze_frequency(processed_data)
    
    # Step 3: Compute entropy (distractor - not used in final score)
    entropy_value = compute_entropy(frequency_analysis)
    
    # Step 4: Extract vowel counts from original entries (irrelevant)
    total_vowels = 0
    for entry in input_data:
        total_vowels += extract_vowels(entry)
    
    # Step 5: Compute final score - KEY STATEMENT
    final_score = compute_final_score(processed_data)
    
    # Output result
    print(f"Result: {final_score}")