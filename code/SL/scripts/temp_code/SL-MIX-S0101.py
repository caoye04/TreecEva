def analyze_text_quality(text):
    base_score = len(text.replace(" ", "")) * 2
    vowel_count = sum(1 for char in text.lower() if char in 'aeiou')
    consonant_count = len(text.replace(" ", "")) - vowel_count
    
    intermediate_score = base_score + (vowel_count * 3)
    processed_score = intermediate_score - (consonant_count // 2)
    
    # Distractor operations
    text_upper = text.upper()
    char_frequency = {char: text.count(char) for char in set(text)}
    quality_ratio = vowel_count / len(text) if len(text) > 0 else 0
    
    adjustment_factor = processed_score % 7
    final_quality_score = processed_score - adjustment_factor
    
    print(f"Result: {final_quality_score}")

analyze_text_quality("Programming evaluation benchmark")