def analyze_sequence_pattern(sequence):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consonants = set('bcdfghjklmnpqrstvwxyz')
    
    # Distractor: vowel count that won't be used in final calculation
    vowel_count = sum(1 for char in sequence if char.lower() in vowels)
    
    # Main pattern analysis
    pattern_count = 0
    for i, char in enumerate(sequence):
        if i < len(sequence) - 1:
            if char.lower() in consonants and sequence[i + 1].lower() in vowels:
                pattern_count += 2  # Double weight for consonant-vowel patterns
    
    # Semi-relevant intermediate calculation
    temp_adjust = len([c for c in sequence if c.isupper()]) * 3
    
    # Final adjustments
    adjustment = temp_adjust // 2  # This will be used
    offset = len(sequence) % 4     # This will be used
    
    # Key statement where answer is determined
    result = pattern_count + adjustment - offset
    
    print(f"Result: {result}")
    return result

# Execute with test data
sequence_pattern = "ProgrammingBenchmark2024"
final_result = analyze_sequence_pattern(sequence_pattern)