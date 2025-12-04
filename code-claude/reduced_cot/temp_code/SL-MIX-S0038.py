from itertools import chain

def analyze_text(text):
    # Split text into words and filter out empty strings
    words = [word.strip('.,!?;:"()') for word in text.lower().split()]
    words = [word for word in words if word]
    
    # Calculate word lengths
    word_lengths = [len(word) for word in words]
    
    # Some statistics about the text
    total_words = len(words)
    avg_length = sum(word_lengths) / total_words if total_words > 0 else 0
    max_length = max(word_lengths) if word_lengths else 0
    
    # Count unique word lengths
    unique_count = len(set(word_lengths))
    
    # Calculate frequency of each length
    frequency = {}
    for length in word_lengths:
        if length in frequency:
            frequency[length] += 1
        else:
            frequency[length] = 1
    
    return unique_count, avg_length, frequency

# Sample text for analysis
sample_text = "The quick brown fox jumps over the lazy dog. It's a pangram!"

# Analyze the text
unique_count, avg_length, frequency = analyze_text(sample_text)

# Display results
print(f"Result: {unique_count}")