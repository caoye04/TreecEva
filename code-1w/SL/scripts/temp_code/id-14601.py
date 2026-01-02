def analyze_text_patterns(input_str):
    char_count = len(input_str)
    vowel_list = [c for c in input_str.lower() if c in 'aeiou']
    consonant_count = len([c for c in input_str.lower() if c.isalpha() and c not in 'aeiou'])
    
    # Distractor: word analysis (not used in final result)
    words = input_str.split()
    avg_word_length = sum(len(w) for w in words) / len(words) if words else 0
    palindrome_words = [w for w in words if w.lower() == w.lower()[::-1]]
    
    # Misleading intermediate score based on vowels
    vowel_score = len(vowel_list) * 3.5
    redundant_calc = sum(ord(c) for c in vowel_list) % 7  # Dead-end computation
    
    # Real logic begins: count alternating consonant-vowel patterns
    pattern_count = 0
    for i in range(len(input_str) - 1):
        current, next_char = input_str[i].lower(), input_str[i+1].lower()
        is_curr_cons = current.isalpha() and current not in 'aeiou'
        is_next_vowel = next_char in 'aeiou'
        if is_curr_cons and is_next_vowel:
            pattern_count += 1
    
    # Secondary logic: track uppercase positions
    uppercase_indices = [i for i, c in enumerate(input_str) if c.isupper()]
    index_sum = sum(uppercase_indices)
    
    # Helper function with selective relevance
    def calculate_adjusted_score(base, factor, shift, extra_weight=1.0):
        temp_val = base * factor
        adjustment = 0
        if shift > 0:
            for j in range(shift):
                adjustment += (j * 2) % 5
        # Relevant transformation
        return int(temp_val + (index_sum % 10) - pattern_count)
    
    # Unused distraction variables
    entropy_approx = len(set(input_str)) / (char_count + 1e-5)
    mirrored_pairs = list(zip(input_str, input_str[::-1]))
    symmetry_score = sum(1 for a, b in mirrored_pairs[:len(input_str)//2] if a == b)
    
    # Key statement
    final_score = calculate_adjusted_score(pattern_count, 13, len(palindrome_words), extra_weight=1.2)
    
    print(f"Result: {final_score}")
    return final_score

# Execute with fixed input
text_input = "DynamicProgrammingIsFunAndChallenging"
analyze_text_patterns(text_input)