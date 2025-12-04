def process_text(text):
    # Remove punctuation and convert to lowercase
    cleaned_text = ''.join(char.lower() if char.isalnum() or char.isspace() else ' ' for char in text)
    
    # Split into words
    words = cleaned_text.split()
    
    # Count initial words for reference
    initial_count = len(words)
    
    # Track word frequencies (not used in final calculation)
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    # Find most common word (distraction)
    most_common = ''
    max_freq = 0
    for word, freq in word_freq.items():
        if freq > max_freq:
            max_freq = freq
            most_common = word
    
    # Filter out stopwords (simplified list)
    stopwords = ['the', 'and', 'is', 'in', 'to', 'a', 'of']
    filtered_words = [w for w in words if w not in stopwords]
    
    # Calculate average word length (distraction)
    if filtered_words:
        avg_length = sum(len(word) for word in filtered_words) / len(filtered_words)
    else:
        avg_length = 0
    
    # Count words longer than 3 characters
    final_word_count = len([word for word in filtered_words if len(word) > 3])
    
    # Apply some transformations that don't affect the result
    transformation_factor = 1
    if avg_length > 4:
        transformation_factor = 1.5
    elif avg_length < 3:
        transformation_factor = 0.8
    
    # This calculation doesn't affect final_word_count
    adjusted_count = int(initial_count * transformation_factor)
    
    return final_word_count, most_common, adjusted_count

# Sample text for analysis
sample_text = "The quick brown fox jumps over the lazy dog. It was the best of times."

# Process the text and get results
result, common_word, adjusted = process_text(sample_text)

print(f"Result: {result}")