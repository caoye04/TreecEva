def analyze_text_patterns(text_list):
    char_frequency = {}
    total_chars = 0
    for text in text_list:
        cleaned = text.strip().lower()
        vowels = sum(1 for c in cleaned if c in 'aeiou')
        consonants = sum(1 for c in cleaned if c.isalpha() and c not in 'aeiou')
        
        # Irrelevant aggregation (distractor)
        special_chars = len([c for c in cleaned if not c.isalnum()])
        redundant_sum = vowels * 2 + consonants // 3 + special_chars

        for char in cleaned:
            if char.isalpha():
                char_frequency[char] = char_frequency.get(char, 0) + 1
                total_chars += 1
    
    # Dead code path - never used later (distractor)
    if total_chars > 1000:
        scaling_factor = 0.9
    else:
        scaling_factor = 1.0
    
    return char_frequency


def transform_scores(freq_dict, base_multiplier=1.7):
    scores = []
    offset = 5
    for idx, (char, count) in enumerate(freq_dict.items()):
        # Semi-relevant transformation with misleading intermediate steps
        raw_score = count * base_multiplier + (idx % 4)
        adjusted = raw_score ** 0.5
        noise = (ord(char) % 7) - 3  # Adds computation but cancels out
        stabilized = adjusted + noise - noise  # Neutralizes noise
        
        # Use of zip and string method (required feature)
        tag_data = list(zip([c.upper() for c in freq_dict.keys()], range(len(freq_dict))))
        tagged_score = stabilized + len(tag_data) * 0.1
        
        scores.append(tagged_score)
    
    # Dead computation (distractor)
    max_tag_len = max(len(t[0]) for t in tag_data) if tag_data else 0
    
    return [round(s, 3) for s in scores]


def calculate_final_score(data, weights):
    # Required use of enumerate (mandatory feature)
    weighted_sum = 0
    total_weight = 0
    temp_buffer = []
    
    for i, (val, w) in enumerate(zip(data, weights)):
        if w <= 0:
            continue
        
        # Simulate intermediate tracking (partially irrelevant)
        temp_entry = {
            'index': i,
            'raw_value': val,
            'weight': w,
            'product': val * w,
            'flagged': False
        }
        
        if val > 10:
            temp_entry['flagged'] = True
            correction = (val % 3) * 0.5
            temp_entry['corrected_val'] = val - correction
        else:
            temp_entry['corrected_val'] = val
        
        temp_buffer.append(temp_entry)
        weighted_sum += temp_entry['corrected_val'] * w
        total_weight += w
    
    # Real answer computation
    final_score = round(weighted_sum / total_weight, 4) if total_weight > 0 else 0
    
    # Additional irrelevant logic (distractor)
    outlier_count = sum(1 for entry in temp_buffer if entry['flagged'])
    if outlier_count > 5:
        final_score *= 0.95
    
    return final_score

# Main execution
input_texts = [
    "The quick brown fox jumps over the lazy dog.",
    "Pack my box with five dozen liquor jugs!",
    "How vexingly quick daft zebras jump!",
    "Bright vixens jump; dozy fowl quack.",
    "Sphinx of black quartz, judge my vow."
]

# Step 1: Extract character frequencies
frequencies = analyze_text_patterns(input_texts)

# Step 2: Transform into normalized scores
transformed = transform_scores(frequencies, base_multiplier=1.7)

# Step 3: Prepare weights based on alphabetical order heuristic (irrelevant complexity)
weights = [(ord(k) % 13) + 1 for k in sorted(frequencies.keys())]

# Final computation
final_score = calculate_final_score(transformed, weights)
print(f"Target result: {final_score}")