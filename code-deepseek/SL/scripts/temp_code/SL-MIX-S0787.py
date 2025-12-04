def analyze_text_data(text_sequence, filter_threshold):
    words = text_sequence.split(', ')
    word_lengths = [len(word) for word in words]
    
    # Calculate average length (distractor operation)
    avg_length = sum(word_lengths) / len(word_lengths) if word_lengths else 0
    
    # Filter words based on length threshold
    filtered_words = [word for word in words if len(word) >= filter_threshold]
    
    # Count processed items (this is the target)
    processed_count = len(filtered_words)
    
    # Additional operations that don't affect the result
    total_chars = sum(len(word) for word in words)
    longest_word = max(words, key=len) if words else ""
    shortest_word = min(words, key=len) if words else ""
    
    # Unused variable for distraction
    char_difference = len(longest_word) - len(shortest_word) if words else 0
    
    print(f"Result: {processed_count}")

# Main execution
sample_text = "data, processing, algorithm, code, test, validation, result"
threshold_value = 6
analyze_text_data(sample_text, threshold_value)