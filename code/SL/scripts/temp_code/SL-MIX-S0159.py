def calculate_text_analysis(text_samples):
    character_counts = {}
    
    for sample in text_samples:
        for char in sample:
            if char.isalpha():
                character_counts[char.lower()] = character_counts.get(char.lower(), 0) + 1
    
    total_chars = sum(character_counts.values())
    unique_chars = len(character_counts)
    
    base_score = total_chars * unique_chars
    
    adjustment_factor = 2
    adjusted_sum = base_score + adjustment_factor
    
    normalization_factor = 3
    final_score = adjusted_sum // normalization_factor
    
    print(f"Result: {final_score}")
    return final_score

# Sample text data for analysis
text_data = ["Hello", "World", "Python", "Programming"]
calculate_text_analysis(text_data)