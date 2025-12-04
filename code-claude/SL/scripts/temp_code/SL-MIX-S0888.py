from collections import Counter

def analyze_text(text):
    # Clean and normalize the text
    text = text.lower().replace(',', '').replace('.', '')
    
    # Split into words
    words = text.split()
    
    # Calculate word length statistics
    word_lengths = [len(word) for word in words]
    avg_length = sum(word_lengths) / len(word_lengths)
    
    # Count word frequencies
    word_frequency = sorted(Counter(words).items(), key=lambda x: (-x[1], x[0]))[2][1]
    
    # Find words with length greater than average
    longer_words = [word for word in words if len(word) > avg_length]
    longer_count = len(longer_words)
    
    print(f"Result: {word_frequency}")
    return word_frequency

# Sample text for analysis
sample_text = "the quick brown fox jumps over the lazy dog the fox was quick and the dog was lazy"
result = analyze_text(sample_text)