def analyze_text(text):
    # Remove punctuation and convert to lowercase
    punctuation = '.,;:!?"\'-()[]{}'
    clean_text = ''.join(char.lower() for char in text if char not in punctuation)
    
    # Count words (not used in final calculation)
    word_count = len(clean_text.split())
    
    # Get word frequencies (distraction)
    word_freq = {}
    for word in clean_text.split():
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    # Find longest and shortest words (distraction)
    words = clean_text.split()
    longest = max(words, key=len) if words else ''
    shortest = min(words, key=len) if words else ''
    
    # Process text for character analysis
    processed_text = ''.join(clean_text.split())
    
    # Calculate average word length (not used directly)
    total_length = sum(len(word) for word in words)
    avg_length = total_length / word_count if word_count > 0 else 0
    
    # Count unique characters
    unique_chars = len(set(processed_text))
    
    # Calculate vowel percentage (distraction)
    vowels = 'aeiou'
    vowel_count = sum(1 for char in processed_text if char in vowels)
    consonant_count = len(processed_text) - vowel_count
    vowel_percentage = (vowel_count / len(processed_text)) * 100 if processed_text else 0
    
    return unique_chars

sample_text = "Hello, World! Python programming is fun and educational."
result = analyze_text(sample_text)
print(f"Result: {result}")