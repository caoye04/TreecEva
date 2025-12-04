def process_text_data(text_input):
    # Process text data to extract relevant information
    words = text_input.lower().split()
    word_lengths = [len(word) for word in words if len(word) > 3]
    
    # Create sets based on word properties
    primary_set = {len(word) for word in words if word.endswith('ing')}
    secondary_set = {length for length in word_lengths if length % 2 == 0}
    
    # Distractor operations that don't affect final result
    temp_analysis = sum(len(word) for word in words) / len(words)
    vowel_count = sum(1 for word in words if any(char in 'aeiou' for char in word))
    
    # Key operation - set intersection
    result_set = primary_set.intersection(secondary_set)
    
    # Final calculation
    final_count = len(result_set) * 15
    
    # Additional distractor calculations
    processing_factor = len(words) * 2.5
    verification_value = max(word_lengths) if word_lengths else 0
    
    print(f"Target result: {final_count}")

# Execute the function
sample_text = "The programming challenge involves processing incoming data streams and handling multiple operations"
process_text_data(sample_text)