def process_text(input_text):
    # Text processing function that counts valid words
    words = input_text.lower().split()
    
    # Word filtering conditions
    min_length = 4
    max_length = 8
    excluded_chars = set(['!', '@', '#', '$', '%'])
    
    # Process words using lambda and filtering
    word_scores = {}
    for word in words:
        # Calculate word score (not used in final calculation)
        score = sum(ord(c) % 10 for c in word)
        word_scores[word] = score
    
    # Apply different filters to words
    length_filtered = list(filter(lambda w: min_length <= len(w) <= max_length, words))
    
    # Remove words containing excluded characters
    filtered_words = []
    excluded_words = []
    for word in length_filtered:
        if any(char in word for char in excluded_chars):
            excluded_words.append(word)
        else:
            filtered_words.append(word)
    
    # Calculate some statistics (not used in final result)
    avg_length = sum(len(w) for w in filtered_words) / len(filtered_words) if filtered_words else 0
    max_score = max(word_scores.values()) if word_scores else 0
    
    # Count unique valid words
    valid_count = len(set(filtered_words))
    
    # Additional processing that doesn't affect the result
    word_freq = {}
    for word in filtered_words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
            
    return valid_count, avg_length, max_score

# Sample text input
sample_text = "Python is great for text processing! It handles words and #hashtags efficiently. Python Python."

# Process the text
valid_count, avg_length, max_score = process_text(sample_text)

# Display the result
print(f"Result: {valid_count}")