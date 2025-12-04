# Function to analyze character overlap between two phrases
def get_overlap(phrase1, phrase2):
    # Convert phrases to lowercase for case-insensitive comparison
    p1_lower = phrase1.lower()
    p2_lower = phrase2.lower()
    
    # Create sets of characters from each phrase
    chars1 = set(p1_lower)
    chars2 = set(p2_lower)
    
    # Find common characters between phrases
    common_chars = chars1.intersection(chars2)
    
    # Remove spaces from consideration
    if ' ' in common_chars:
        common_chars.remove(' ')
    
    # Count unique characters in the overlap
    unique_chars = len(common_chars)
    
    # Calculate a weighted score based on character frequencies
    freq_score = sum(min(p1_lower.count(c), p2_lower.count(c)) for c in common_chars)
    
    return unique_chars, freq_score

# Test with sample phrases
phrase_a = "python programming"
phrase_b = "coding practice"

# Get overlap metrics
char_count, frequency_score = get_overlap(phrase_a, phrase_b)

# Display results
print(f"Result: {char_count}")