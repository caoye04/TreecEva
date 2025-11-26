def analyze_text_patterns(text_segments):
    vowel_counts = []
    consonant_totals = []
    irrelevant_sum = 0
    
    for i, segment in enumerate(text_segments):
        vowels = sum(1 for char in segment if char.lower() in 'aeiou')
        consonants = sum(1 for char in segment if char.isalpha() and char.lower() not in 'aeiou')
        vowel_counts.append(vowels)
        consonant_totals.append(consonants)
        
        # Distractor operation - doesn't affect final result
        irrelevant_sum += len(segment) * 2
    
    # Main logic with conditional expressions
    paired_data = list(zip(vowel_counts, consonant_totals))
    processed_values = [vowels * 10 + consonants if vowels > consonants else consonants * 5 - vowels 
                       for vowels, consonants in paired_data]
    
    # Additional intermediate step (not directly used)
    temp_max = max(processed_values) if processed_values else 0
    
    # Final computation
    final_count = sum(processed_values) // len(processed_values) if processed_values else 0
    
    result = final_count
    print(f"Result: {result}")

# Execute with sample data
text_samples = ["hello", "world", "python", "programming"]
analyze_text_patterns(text_samples)