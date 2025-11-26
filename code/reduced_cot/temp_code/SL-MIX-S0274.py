def analyze_text_patterns(text_data):
    # Process character frequencies
    char_counter = {}
    for char in text_data:
        char_counter[char] = char_counter.get(char, 0) + 1
    
    # Calculate vowel distribution (distractor - not used in final result)
    vowels = 'aeiouAEIOU'
    vowel_count = sum(1 for char in text_data if char in vowels)
    
    # Main word processing logic
    words = text_data.lower().split()
    word_count = len(words)
    
    # Filter short words (distractor - not used in final result)
    short_words = [word for word in words if len(word) < 4]
    
    # Calculate adjustment based on unique characters
    unique_chars = len(set(text_data.replace(' ', '')))
    adjustment_factor = unique_chars // 2
    
    # Bonus calculation based on word patterns
    bonus_credit = 0
    for word in words:
        if word.endswith('ing'):
            bonus_credit += 2
        elif word.startswith('pre'):
            bonus_credit += 1
    
    # Final computation (answer target)
    final_count = word_count - adjustment_factor + bonus_credit
    print(f"Result: {final_count}")

# Execute the analysis
text_sample = "Programming is preparing for complex problem solving and creating innovative solutions"
analyze_text_patterns(text_sample)