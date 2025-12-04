from collections import Counter

def analyze_text(text):
    # Remove spaces and convert to lowercase
    processed_text = text.lower().replace(" ", "")
    
    # Count occurrences of each character
    char_counts = Counter(processed_text)
    
    # Find character with highest frequency
    most_common_char = char_counts.most_common(1)[0][0]
    highest_frequency = max(char_counts.values())
    
    # Calculate average character code
    char_codes = [ord(c) for c in processed_text]
    avg_code = sum(char_codes) / len(char_codes) if char_codes else 0
    
    # Generate a complexity score (not used in final result)
    complexity = len(set(processed_text)) * 0.5
    
    # Calculate letter distribution score
    vowels = sum(1 for c in processed_text if c in 'aeiou')
    consonants = sum(1 for c in processed_text if c.isalpha() and c not in 'aeiou')
    
    # Filter special characters (not used in final calculation)
    specials = list(filter(lambda x: not x.isalnum(), processed_text))
    
    # Apply weighting to vowels vs consonants (distraction)
    weighted_ratio = (vowels * 1.5) / (consonants or 1)
    
    # Extract middle portion of text (not used in final answer)
    mid_slice = processed_text[len(processed_text)//4:3*len(processed_text)//4]
    
    return most_common_char, highest_frequency, avg_code

# Sample text to analyze
sample = "The quick brown fox jumps over the lazy dog!"
most_frequent_char, highest_frequency, average_code = analyze_text(sample)

print(f"Result: {highest_frequency}")