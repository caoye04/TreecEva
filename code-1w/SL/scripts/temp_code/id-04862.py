def analyze_text(text_blocks):
    char_count = 0
    word_frequency = {}
    block_stats = []

    for i, block in enumerate(text_blocks):
        stripped = block.strip().lower()
        words = stripped.split()
        
        # Irrelevant transformation (distractor)
        reversed_words = [word[::-1] for word in words]
        palindrome_check = [w == w[::-1] for w in words]

        # Actual useful computation
        valid_words = [w for w in words if len(w) > 1]
        char_count += len(stripped.replace(' ', ''))
        
        for word in valid_words:
            word_frequency[word] = word_frequency.get(word, 0) + 1

        # Semi-relevant: tracking length stats but only used indirectly
        block_stats.append({'index': i, 'length': len(words), 'chars': len(stripped)})

    avg_length = sum(bs['length'] for bs in block_stats) / len(block_stats) if block_stats else 0
    
    # Distractor: complex but unused structure
    metadata_summary = {
        'total_blocks': len(text_blocks),
        'average_word_count': avg_length,
        'has_palindromes': any(palindrome_check),
        'transform_flag': True
    }

    return char_count, word_frequency, block_stats


def filter_and_weight(freq_dict, threshold=2):
    filtered = {}
    weight_sum = 0.0
    entropy_approx = 0.0

    total_freq = sum(freq_dict.values())
    
    for k, v in freq_dict.items():
        if v >= threshold:
            filtered[k] = v
            weight_sum += v
            # Fake entropy-like calculation (not really used)
            prob = v / total_freq
            entropy_approx -= prob * __import__('math').log(prob) if prob > 0 else 0
    
    # Dead code path (conditional never met due to logic)
    scaling_factor = 1.0
    if len(filtered) > 100:
        scaling_factor = 0.9
    
    return filtered, weight_sum


def calculate_final_score(data_tuple):
    char_count, word_freq, stats = data_tuple
    filtered_words, total_weight = filter_and_weight(word_freq, threshold=2)
    
    # Core logic step 1: base from character count
    base_score = char_count % 7919  # prime mod for uniqueness
    
    # Core logic step 2: add weighted contribution
    adjustment = int(total_weight * 3.7)
    
    # Core logic step 3: apply bitwise interaction
    combined = (base_score ^ adjustment) & 0xFFFF  # limit to 16 bits
    
    # Core logic step 4: final modulation using number of significant terms
    modifier = len(filtered_words) * 5
    
    # Final score computation
    final_score = combined + modifier - 127
    
    # Red herring: alternate path never taken
    if False and char_count < 0:
        final_score = sum(filtered_words.values()) * 2
        
    return final_score

# Main execution
raw_texts = [
    "The signal integrity improves with proper shielding",
    "Noise reduction is critical in analog circuits",
    "Capacitive coupling can introduce unwanted interference",
    "Use differential signaling for better robustness"
]

# Preprocessing with zip (required feature)
pairs = list(zip(raw_texts, [len(t) for t in raw_texts]))
filtered_texts = [item[0] for item in pairs if item[1] > 30]

# Additional distractor: string method chain with no impact
formatted = [txt.upper().replace(' ', '_').lstrip('_') for txt in raw_texts]

# Process the relevant data
processed_data = analyze_text(filtered_texts)

# Key statement
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")