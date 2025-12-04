import itertools

# Analyzing word lengths in a book excerpt
def analyze_text(text):
    # Remove punctuation and convert to lowercase
    cleaned_text = ''.join(c.lower() if c.isalpha() or c.isspace() else ' ' for c in text)
    
    # Split into words and filter out empty strings
    words = [word for word in cleaned_text.split() if word]
    
    # Calculate length of each word
    word_lengths = [len(word) for word in words]
    
    # Count occurrences of each length
    length_counts = {}
    for length in word_lengths:
        length_counts[length] = length_counts.get(length, 0) + 1
    
    # Find the most common word length
    most_frequent_word_length = max(length_counts, key=length_counts.get)
    
    # Calculate average word length for comparison
    avg_length = sum(word_lengths) / len(words) if words else 0
    
    return most_frequent_word_length, avg_length, length_counts

# Sample text from a book excerpt
sample_text = "The quick brown fox jumps over the lazy dog. The fox was very quick and the dog was extremely lazy."

# Run analysis
most_frequent_word_length, average_length, counts = analyze_text(sample_text)

# Output results
print(f"Word length distribution: {counts}")
print(f"Average word length: {average_length:.2f}")
print(f"Result: {most_frequent_word_length}")