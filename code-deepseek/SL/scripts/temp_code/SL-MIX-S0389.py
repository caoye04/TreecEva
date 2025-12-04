def calculate_word_metrics(text_sample):
    words = text_sample.lower().split()
    word_lengths = [len(word) for word in words if word.isalpha()]
    
    # Calculate average word length
    total_chars = sum(word_lengths)
    word_count = len(word_lengths)
    avg_length = total_chars / word_count if word_count > 0 else 0
    
    # Calculate word frequency (distractor - not used in final result)
    word_freq = {}
    for word in words:
        if word.isalpha():
            word_freq[word] = word_freq.get(word, 0) + 1
    
    # Apply length filter and calculate filtered average
    filtered_lengths = [length for length in word_lengths if length >= 4]
    filtered_count = len(filtered_lengths)
    filtered_avg = sum(filtered_lengths) / filtered_count if filtered_count > 0 else 0
    
    # Calculate bonus based on text characteristics (distractor)
    unique_words = len(set([w for w in words if w.isalpha()]))
    bonus_multiplier = unique_words / word_count if word_count > 0 else 0
    
    # Apply bonus adjustment
    bonus_adjustment = 2.5 if filtered_avg > 5.0 else 1.0
    final_score = filtered_avg + bonus_adjustment
    
    print(f"Result: {final_score}")

# Execute the function
text = "The quick brown fox jumps over the lazy dog and runs through the forest"
calculate_word_metrics(text)