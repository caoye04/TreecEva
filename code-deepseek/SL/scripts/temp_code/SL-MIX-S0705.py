def process_data(text_sequence):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consonants = set('bcdfghjklmnpqrstvwxyz')
    
    # Distractor operations that don't affect final result
    total_chars = len(text_sequence)
    uppercase_count = sum(1 for char in text_sequence if char.isupper())
    digit_count = sum(1 for char in text_sequence if char.isdigit())
    
    # Key logic chain
    vowel_count = sum(1 for char in text_sequence.lower() if char in vowels)
    consonant_count = sum(1 for char in text_sequence.lower() if char in consonants)
    
    # More distractor calculations
    ratio_vowel_to_consonant = vowel_count / consonant_count if consonant_count > 0 else 0
    
    # Final calculation with nested logic
    if vowel_count > consonant_count:
        final_count = vowel_count * 3 - consonant_count
    elif consonant_count > vowel_count:
        final_count = consonant_count * 2 + vowel_count
    else:
        final_count = vowel_count * consonant_count
    
    # Unused intermediate variable
    potential_adjustment = final_count // 2
    
    return final_count

text_sequence = "ProgrammingEvaluation2024"
result = process_data(text_sequence)
print(f"Result: {result}")