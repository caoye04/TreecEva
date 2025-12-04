def analyze_text(text):
    # Remove punctuation and convert to lowercase
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum() or char.isspace())
    
    # Split into words
    words = cleaned_text.split()
    
    # Count word occurrences
    word_counts = {}
    for word in words:
        if len(word) > 0:  # Skip empty strings
            word_counts[word] = word_counts.get(word, 0) + 1
    
    # Calculate metrics
    avg_length = sum(len(word) for word in words) / len(words) if words else 0
    max_word = max(words, key=len) if words else ""
    min_word = min(words, key=len) if words else ""
    
    # Extract words starting with vowels
    vowel_words = [w for w in words if w and w[0].lower() in 'aeiou']
    vowel_count = len(vowel_words)
    
    # Filter words with more than 4 characters
    long_words = [word for word in words if len(word) > 4]
    long_word_ratio = len(long_words) / len(words) if words else 0
    
    # Calculate total frequency
    total_frequency = sum(word_counts.values())
    
    # Calculate weighted score (not used in final result)
    weighted_score = sum(len(w) * word_counts[w] for w in word_counts)
    
    return total_frequency, avg_length, vowel_count, long_word_ratio

# Sample text
sample_text = "The quick brown fox jumps over the lazy dog. The fox was quick and brown."

# Process the text
total_frequency, avg_length, vowel_count, long_word_ratio = analyze_text(sample_text)

print(f"Result: {total_frequency}")