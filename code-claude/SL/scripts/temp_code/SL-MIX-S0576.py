import itertools

# Text analysis function to find matching words
def analyze_text(text_data, pattern_list):
    # Process text data
    words = text_data.split()
    
    # Convert words to lowercase for initial filtering
    lowercase_words = [w.lower() for w in words]
    
    # Generate some word statistics (not used in final calculation)
    word_lengths = [len(word) for word in words]
    avg_length = sum(word_lengths) / len(word_lengths) if word_lengths else 0
    max_length = max(word_lengths) if word_lengths else 0
    
    # Create permutations of patterns for extra processing (distraction)
    pattern_perms = list(itertools.permutations(pattern_list, 2))
    pattern_pairs = [p[0] + p[1] for p in pattern_perms]
    
    # Filter words based on length criteria
    length_threshold = 4  # Words must be longer than this
    filtered_words = []
    for i, word in enumerate(words):
        # Calculate a score (distraction)
        score = len(word) * (i % 3 + 1)
        
        # Apply actual filter criteria
        if len(word) > length_threshold:
            filtered_words.append(word)
    
    # Define target words to match against
    target_words = ['python', 'code', 'analysis', 'text']
    
    # Count words that match our target list (case insensitive)
    valid_words = len([word for word in filtered_words if word.lower() in target_words])
    
    # Extra calculations that don't affect the result
    potential_matches = sum(1 for word in lowercase_words if any(p in word for p in pattern_list))
    ratio = valid_words / len(filtered_words) if filtered_words else 0
    
    return valid_words

# Test data
text = "Python code is fun to write. Text ANALYSIS helps understand Code better. python programming is powerful."
patterns = ['py', 'co', 'te']

result = analyze_text(text, patterns)
print(f"Result: {result}")