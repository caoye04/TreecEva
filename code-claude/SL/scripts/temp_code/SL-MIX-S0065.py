def analyze_text(text, min_length=3):
    # Clean the text by removing punctuation and converting to lowercase
    cleaned_text = ''.join(char.lower() if char.isalnum() or char.isspace() else ' ' for char in text)
    
    # Split into words
    words = cleaned_text.split()
    
    # Count total words
    total_words = len(words)
    
    # Count words longer than minimum length
    filtered_word_count = len([word for word in words if len(word) > min_length])
    
    # Calculate average word length (for information only)
    avg_length = sum(len(word) for word in words) / total_words if total_words > 0 else 0
    
    print(f"Result: {filtered_word_count}")
    return filtered_word_count

# Sample text to analyze
sample = "The quick brown fox jumps over the lazy dog!"
result = analyze_text(sample, 3)