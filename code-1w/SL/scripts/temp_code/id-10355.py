def analyze_text_sequence(raw_input):
    # Preprocess: clean and normalize input string
    cleaned = raw_input.strip().lower()
    tokens = cleaned.split()
    
    # Irrelevant distraction: count vowels (not used in final logic)
    vowel_count = sum([1 for c in cleaned if c in 'aeiou'])
    temp_vowel_density = vowel_count / len(cleaned) if cleaned else 0

    # Key data extraction
    word_lengths = [len(word.strip('.,!?"')) for word in tokens]
    valid_words = [w for w in tokens if len(w.strip('.,!?"')) > 1]
    
    # Distraction: unused transformation
    reversed_words = [word[::-1] for word in tokens]
    palindrome_flags = [word == word[::-1] for word in valid_words]

    # Compute statistical features (some used, some not)
    avg_length = sum(word_lengths) / len(word_lengths) if word_lengths else 0
    max_length = max(word_lengths) if word_lengths else 0
    length_variance = sum((x - avg_length) ** 2 for x in word_lengths) / len(word_lengths) if word_lengths else 0

    # Hidden key pattern: count how many words have length equal to average (rounded)
    target_len = round(avg_length)
    matching_words = len([lw for lw in word_lengths if lw == target_len])

    # Generate intermediate score with red herring calculations
    entropy_proxy = 0
    if length_variance > 0:
        entropy_proxy = (avg_length * matching_words) / (length_variance + 1)
    
    noise_factor = sum(1 for lw in word_lengths if lw % 3 == 0)  # unused
    dummy_shift = (max_length * 2) - vowel_count  # dead computation

    return {
        'count': len(valid_words),
        'average': avg_length,
        'peak': max_length,
        'matches': matching_words,
        'entropy': entropy_proxy,
        'variance': length_variance
    }


def compute_final_score(metrics):
    # Secondary processing with conditional logic
    base = metrics['count'] * metrics['average']
    bonus = 0
    
    if metrics['matches'] > 0:
        bonus += metrics['matches'] * 2.5
    
    if metrics['variance'] < 2.0:
        bonus += 5.0
    
    # Dead branch: this condition is never met due to constraints
    debug_mode = False
    if debug_mode and metrics['entropy'] > 10:
        bonus += 20  # unreachable
    
    penalty = 0
    if metrics['peak'] > 8:
        penalty = 3.0
    
    # Final calculation
    raw_score = base + bonus - penalty
    normalized = max(0, raw_score)  # clamp to non-negative
    final_score = round(normalized, 2)
    
    return final_score

# Main execution
input_text = "The quick brown fox jumps over the lazy dog near the river."
processed_data = analyze_text_sequence(input_text)
final_score = compute_final_score(processed_data)
print(f"Target result: {final_score}")