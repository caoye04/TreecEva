def analyze_text_metrics(text_samples):
    # Text processing with some irrelevant calculations
    processed_samples = [sample.strip().lower() for sample in text_samples]
    
    # This calculation doesn't affect the final result
    character_counts = [len(sample) for sample in processed_samples]
    avg_chars = sum(character_counts) / len(character_counts) if character_counts else 0
    
    # Main processing chain
    combined_text = ' '.join(processed_samples)
    tokens = combined_text.split()
    
    # Intermediate step with semi-relevant calculation
    min_length = 3
    vowel_counts = [sum(1 for char in word if char in 'aeiou') for word in tokens]
    
    # Filter and process relevant data
    filtered_tokens = [word for word in tokens if len(word) > min_length]
    total_chars = sum(len(word) for word in filtered_tokens)
    
    # The key calculation - this is what matters
    final_accuracy = sum([len(word) for word in filtered_tokens if len(word) > min_length]) / max(total_chars, 1)
    
    # Print the target result
    print(f"Target result: {final_accuracy}")

# Test data
text_data = ["Machine learning models", "process natural language", "with high accuracy"]
analyze_text_metrics(text_data)