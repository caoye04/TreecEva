def analyze_text_patterns(text_data):
    vowels = 'aeiou'
    consonant_count = 0
    vowel_count = 0
    temp_analysis = []
    
    for char in text_data:
        if char.isalpha():
            if char.lower() in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    # Distractor calculations (not used in final result)
    char_frequency = {}
    for char in text_data:
        char_frequency[char] = char_frequency.get(char, 0) + 1
    
    text_pairs = list(zip(text_data, text_data[1:]))
    pair_analysis = [(a, b) for a, b in text_pairs if a.isalpha() and b.isalpha()]
    
    # Core logic
    processing_result = vowel_count * 3 - consonant_count * 2
    adjustment_factor = len(pair_analysis) // 2
    
    # More distractors
    unused_calculation = sum(ord(c) for c in text_data if c.isalpha())
    extra_variable = processing_result * adjustment_factor
    
    final_result = processing_result + adjustment_factor
    print(f"Target result: {final_result}")

# Execute the analysis
sample_text = "programming evaluation benchmark"
analyze_text_patterns(sample_text)