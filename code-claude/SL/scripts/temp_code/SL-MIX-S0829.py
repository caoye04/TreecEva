from collections import Counter

def analyze_text(text):
    # Clean the text by removing punctuation and converting to lowercase
    cleaned_text = ''.join(c.lower() for c in text if c.isalnum() or c.isspace())
    
    # Extract words and count their frequencies
    words = cleaned_text.split()
    word_counts = Counter(words).most_common(3)
    
    # Convert to dictionary for easier handling
    word_counts = dict(word_counts)
    
    # Calculate a weighted frequency score
    # Each word's count is weighted by its position in the frequency list
    frequency_score = sum(value * (i+1) for i, value in enumerate(word_counts.values()))
    
    # Calculate average word length for comparison
    avg_length = sum(len(word) for word in words) / len(words) if words else 0
    
    print(f"Result: {frequency_score}")
    return frequency_score

# Sample text for analysis
sample_text = "The quick brown fox jumps over the lazy dog. The fox was quick and the dog was lazy."
result = analyze_text(sample_text)