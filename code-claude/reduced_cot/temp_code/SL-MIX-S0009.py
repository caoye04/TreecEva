from collections import Counter

def analyze_text_frequencies(text):
    # Remove punctuation and convert to lowercase
    cleaned_text = ''.join(c.lower() for c in text if c.isalpha() or c.isspace())
    
    # Split into words
    words = cleaned_text.split()
    
    # Calculate average word length (not used in final result)
    avg_length = sum(len(word) for word in words) / len(words) if words else 0
    
    # Count letter frequencies
    letter_counts = Counter(c for c in cleaned_text if c.isalpha())
    
    # Find most and least common letters
    most_common_letter = letter_counts.most_common(1)[0][0]
    most_common = letter_counts[most_common_letter]
    
    # Sort letters by frequency
    sorted_letters = sorted(letter_counts.items(), key=lambda x: (x[1], x[0]))
    least_common_letter = sorted_letters[0][0]
    least_common = letter_counts[least_common_letter]
    
    # Calculate difference between most and least common frequencies
    frequency_difference = most_common - least_common
    
    # Calculate some statistics that aren't used in the final result
    unique_letters = len(letter_counts)
    total_letters = sum(letter_counts.values())
    letter_diversity = unique_letters / total_letters if total_letters else 0
    
    return frequency_difference, most_common_letter, least_common_letter

# Sample text to analyze
sample_text = "The quick brown fox jumps over the lazy dog."

# Analyze frequencies
result, mc_letter, lc_letter = analyze_text_frequencies(sample_text)

# Extract middle slice of text (not used in final calculation)
middle_slice = sample_text[10:25]

# Create a tuple of results (not used in final calculation)
result_data = (result, mc_letter, lc_letter, len(sample_text))

print(f"Result: {result}")