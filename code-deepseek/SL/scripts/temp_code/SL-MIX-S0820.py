def analyze_string_patterns(text_samples):
    # Convert all samples to uppercase (distraction)
    upper_samples = [sample.upper() for sample in text_samples]
    
    # Analyze vowel patterns - main logic
    vowel_counts = [sum(1 for char in sample if char in 'aeiouAEIOU') for sample in text_samples]
    
    # Calculate consonant ratios (distraction)
    total_chars = [len(sample) for sample in text_samples]
    consonant_ratios = [(total - vowels) / max(total, 1) for total, vowels in zip(total_chars, vowel_counts)]
    
    # Process vowel data with adjustment
    processed_data = [count * 2 + 1 for count in vowel_counts]
    
    # Unused intermediate calculation (distraction)
    weighted_sum = sum(count * ratio for count, ratio in zip(vowel_counts, consonant_ratios))
    
    # Final result extraction
    final_count = processed_data[-1]
    
    print(f"Target result: {final_count}")
    return final_count

# Test execution
text_data = ["hello", "world", "python", "programming", "analysis"]
analyze_string_patterns(text_data)