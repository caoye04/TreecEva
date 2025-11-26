def analyze_text_data(text_segments):
    # Initialize word counter with some irrelevant processing
    segment_lengths = [len(seg) for seg in text_segments]
    total_chars = sum(segment_lengths)
    
    # Distractor: character frequency analysis that won't be used
    char_freq = {}
    for seg in text_segments:
        for char in seg:
            char_freq[char] = char_freq.get(char, 0) + 1
    
    # Main word counting logic with slicing operations
    all_words = []
    for segment in text_segments:
        words = segment.split()
        # Use slicing to exclude first and last word for some segments
        if len(words) > 2:
            processed_words = words[1:-1]
            all_words.extend(processed_words)
        else:
            all_words.extend(words)
    
    # Build word counts using dictionary operations
    word_counts = {}
    for word in all_words:
        word_counts[word] = word_counts.get(word, 0) + 1
    
    # Distractor: lambda function for filtering that's not actually used
    filter_long_words = lambda w, threshold: len(w) > threshold
    
    # The key operation we care about
    final_count = word_counts.get("target", 0)
    
    # Print the result
    print(f"Result: {final_count}")
    return final_count

# Test data with mixed content
text_data = ["find the target word here", "no target in this sentence", "target appears multiple target words target"]
result = analyze_text_data(text_data)