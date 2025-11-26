def analyze_text_patterns(text_sequence):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    
    # Main processing with various intermediate calculations
    upper_count = sum(1 for char in text_sequence if char.isupper())
    lower_count = sum(1 for char in text_sequence if char.islower())
    vowel_count = sum(1 for char in text_sequence if char in vowels)
    consonant_count = sum(1 for char in text_sequence if char in consonants)
    
    # Irrelevant intermediate calculations (distractors)
    temp_sum = upper_count * 3 + lower_count // 2
    unused_product = vowel_count * consonant_count
    misleading_total = len(text_sequence) * 2 - 5
    
    # Dead code path that doesn't affect final result
    if misleading_total > 50:
        dead_result = misleading_total // 3
    else:
        dead_result = misleading_total * 2
    
    # Key logic chain with slicing and itertools
    import itertools
    
    # Process first half and second half differently
    mid_point = len(text_sequence) // 2
    first_half = text_sequence[:mid_point]
    second_half = text_sequence[mid_point:]
    
    # More irrelevant computations
    first_vowels = sum(1 for char in first_half if char in vowels)
    second_consonants = sum(1 for char in second_half if char in consonants)
    
    # Critical calculation path
    base_count = first_vowels + second_consonants
    adjustment = abs(upper_count - lower_count) // 2
    
    # Final variable assignment
    final_count = base_count - adjustment + 3
    
    # One more misleading operation
    processed_chars = final_count * 2 - temp_sum
    
    print(f"Result: {processed_chars}")

# Execute the function with test input
analyze_text_patterns("ProgrammingChallenge2024")