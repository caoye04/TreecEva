def quality_analysis(text):
    # Initialize analysis metrics
    char_count = len(text)
    vowel_count = sum(1 for c in text.lower() if c in 'aeiou')
    consonant_count = sum(1 for c in text.lower() if c.isalpha() and c not in 'aeiou')
    
    # Intermediate calculations (some not used in final result)
    vowel_ratio = vowel_count / char_count if char_count > 0 else 0
    space_count = text.count(' ')
    digit_count = sum(1 for c in text if c.isdigit())
    
    # Distractor variables that don't affect final score
    uppercase_ratio = sum(1 for c in text if c.isupper()) / char_count
    punctuation_count = sum(1 for c in text if c in '.,;:!?')
    
    # Key quality metrics
    readability_score = vowel_count * 2 + consonant_count
    complexity_penalty = len(text.split()) // 2
    
    # Final quality calculation
    quality_score = readability_score - complexity_penalty
    
    # Additional unused calculation
    theoretical_max = char_count * 3
    
    return quality_score

text_data = "Python programming requires careful attention to code quality and readability standards."
preliminary_score = len(text_data) * 2  # Unused distractor
word_count = len(text_data.split())
final_quality_score = quality_analysis(text_data)
print(f"Result: {final_quality_score}")