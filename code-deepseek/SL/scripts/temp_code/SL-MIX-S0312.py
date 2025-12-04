def analyze_text_metrics(text_data):
    # Distractor variables that don't affect final result
    char_count = len(text_data)
    word_list = text_data.split()
    total_words = len(word_list)
    
    # Relevant processing
    vowel_count = sum(1 for char in text_data.lower() if char in 'aeiou')
    consonant_count = sum(1 for char in text_data.lower() if char.isalpha() and char not in 'aeiou')
    
    # Intermediate calculation (not used in final result)
    ratio_attempt = vowel_count / consonant_count if consonant_count > 0 else 0
    
    # Key calculation chain
    vowel_score = vowel_count * 2
    consonant_penalty = consonant_count // 3
    base_score = vowel_score - consonant_penalty
    
    # Final adjustment with string method
    if text_data.endswith('!'):
        emphasis_bonus = 5
    elif text_data.endswith('?'):
        emphasis_bonus = 3
    else:
        emphasis_bonus = 1
    
    analysis_result = base_score + emphasis_bonus
    
    # Unused intermediate variable
    alternative_calc = (vowel_count * 3) - (consonant_count // 2)
    
    return analysis_result

sample_data = "Hello world! This is a test sentence for analysis."
final_processing = analyze_text_metrics(sample_data)
print(f"Result: {final_processing}")