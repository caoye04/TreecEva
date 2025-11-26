def analyze_text_patterns(text_sequence):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    
    # Primary analysis - count vowels and consonants
    vowel_counts = [char.lower().count(vowel) for char in text_sequence for vowel in vowels]
    consonant_counts = [sum(1 for c in char.lower() if c in consonants) for char in text_sequence]
    
    # Distractor calculations that don't affect final result
    total_chars = sum(len(char) for char in text_sequence)
    char_ratio = total_chars / len(text_sequence) if text_sequence else 0
    
    # Intermediate processing with list comprehension
    processed = [(x, y) for x, y in zip(vowel_counts, reversed(consonant_counts)) if x > 2]
    
    # Semi-relevant tuple operations
    vowel_tuples = tuple(vowel_counts[:3])
    consonant_tuples = tuple(consonant_counts[-3:])
    
    # Core logic that determines final answer
    final_count = sum(x * y for x, y in processed) if processed else 0
    
    # Additional distractor operations
    unused_sum = sum(vowel_tuples) + sum(consonant_tuples)
    
    print(f"Result: {final_count}")
    return final_count

# Test execution
text_samples = ['python', 'programming', 'evaluation', 'benchmark', 'reasoning']
analyze_text_patterns(text_samples)