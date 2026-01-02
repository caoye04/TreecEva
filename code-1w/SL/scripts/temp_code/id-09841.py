def analyze_text_patterns(text_data):
    # Count occurrences of each character
    char_freq = {}
    for char in text_data:
        char_freq[char] = char_freq.get(char, 0) + 1
    
    # Extract counts and sort them for positional weighting
    char_counts = sorted(char_freq.values())
    
    # Irrelevant distraction: unused variable (minimal interference)
    avg_length = len(text_data) / len(char_freq) if char_freq else 0
    
    # Key computation: weighted sum of character counts by their sorted position
    total_weighted_chars = sum(index * char_count for index, char_count in enumerate(char_counts))
    
    # Print result as required
    print(f"Result: {total_weighted_chars}")
    return total_weighted_chars

# Input data with non-uniform character distribution
text_input = "aabbcccdddeeeeffffggggg"
analyze_text_patterns(text_input)