def analyze_text(text, min_length=3):
    # Split text into words and remove punctuation
    words = [word.strip('.,!?;:"()') for word in text.split()]
    
    # Some common words we might want to exclude
    excluded = ['the', 'and', 'but', 'for', 'nor', 'yet', 'so']
    
    # Track character frequencies (not used in final calculation)
    char_freq = {}
    for word in words:
        for char in word.lower():
            if char.isalpha():
                char_freq[char] = char_freq.get(char, 0) + 1
    
    # Calculate average word length
    total_length = sum(len(word) for word in words)
    avg_length = total_length / len(words) if words else 0
    
    # Adjust threshold based on average (with some complexity)
    threshold = min_length
    if avg_length > 5:
        threshold = min_length + 1
    elif avg_length < 3:
        threshold = max(1, min_length - 1)
    
    # Count words that exceed threshold length
    long_words = [word for word in words if len(word) > threshold]
    long_word_count = len(long_words)
    
    # Apply lambda function to filter words based on threshold and exclusion list
    filtered_word_count = len(list(filter(lambda x: len(x) > threshold and x.lower() not in excluded, words)))
    
    # Calculate a complexity score (not used in final result)
    complexity = sum(len(set(word.lower())) for word in words) / len(words) if words else 0
    
    # Some additional processing that doesn't affect our target variable
    unique_words = len(set([word.lower() for word in words]))
    diversity_ratio = unique_words / len(words) if words else 0
    
    print(f"Result: {filtered_word_count}")
    return filtered_word_count

# Sample text for analysis
sample_text = "The quick brown fox jumps over the lazy dog while a nearby hunter watches carefully."

# Execute the function
result = analyze_text(sample_text, 4)