def analyze_string_patterns(words, patterns):
    character_frequency = {}
    irrelevant_count = 0
    
    # Process patterns first (distractor)
    for pattern in patterns:
        irrelevant_count += len(pattern)
    
    # Main analysis: find words containing exactly 2 pattern characters
    valid_words = []
    for word in words:
        matching_chars = set(word) & set(patterns)
        if len(matching_chars) == 2:
            valid_words.append(word)
            # Count character frequencies in valid words
            for char in word:
                character_frequency[char] = character_frequency.get(char, 0) + 1
    
    # Calculate target value based on frequency analysis
    target_value = 0
    for word in valid_words:
        for char in word:
            if char in patterns:
                target_value += character_frequency.get(char, 0)
    
    # Final irrelevant computation (doesn't affect result)
    dummy_calc = irrelevant_count * 3 - len(valid_words)
    
    print(f"Target result: {target_value}")
    return target_value

word_list = ['python', 'program', 'logic', 'analysis', 'pattern', 'computation']
pattern_chars = {'a', 'o', 'n'}
result_analysis = analyze_string_patterns(word_list, pattern_chars)