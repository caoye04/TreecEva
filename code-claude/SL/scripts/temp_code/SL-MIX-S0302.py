from collections import Counter

def analyze_text(text):
    # Clean and normalize the text
    cleaned_text = text.lower()
    
    # Split into words and count frequencies
    words = cleaned_text.split()
    word_frequencies = Counter(words)
    
    # Calculate average word length for reference
    total_length = sum(len(word) for word in words)
    avg_length = total_length / len(words) if words else 0
    
    # Find the most common word and its count
    most_common_word, most_common_word_count = word_frequencies.most_common(1)[0]
    
    # Calculate unique word ratio
    unique_ratio = len(word_frequencies) / len(words) if words else 0
    
    return most_common_word_count

# Sample text for analysis
sample_text = "the quick brown fox jumps over the lazy dog the fox was quick and the dog was lazy"

# Process the text
result = analyze_text(sample_text)

# Display the result
print(f"Result: {result}")