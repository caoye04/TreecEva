def analyze_text_patterns(text_samples):
    vowels = 'aeiouAEIOU'
    temp_counts = []
    for sample in text_samples:
        vowel_count = sum(1 for char in sample if char in vowels)
        consonant_count = sum(1 for char in sample if char.isalpha() and char not in vowels)
        temp_counts.append((vowel_count, consonant_count))
    
    # Distractor operations that don't affect final result
    irrelevant_sum = sum(v + c for v, c in temp_counts)
    ratio_calc = irrelevant_sum * 0.75
    
    relevant_data = [(v * 2 + c) for v, c in temp_counts]
    processed_data = sum(relevant_data)
    
    # More distraction - unused intermediate calculations
    pattern_score = processed_data // len(text_samples)
    adjustment_factor = pattern_score + irrelevant_sum
    
    modifier = 3 if processed_data > 20 else 2
    final_output = processed_data * modifier
    
    print(f"Target result: {final_output}")

# Execute the analysis
text_samples = ["Hello", "World", "Python", "Programming"]
analyze_text_patterns(text_samples)