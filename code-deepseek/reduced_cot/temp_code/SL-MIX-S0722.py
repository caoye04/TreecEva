def analyze_text_patterns(text_samples):
    word_frequencies = {}
    processed_items = []
    
    # Distractor: Analyze word frequencies (not used in final result)
    for sample in text_samples:
        words = sample.lower().split()
        for word in words:
            word_frequencies[word] = word_frequencies.get(word, 0) + 1
    
    # Main processing with enumerate
    for idx, sample in enumerate(text_samples):
        cleaned_sample = sample.strip().upper()
        words = cleaned_sample.split()
        
        # Distractor: Calculate word count variance (not used)
        word_count = len(words)
        variance = word_count * 2 - 3
        
        # Relevant: Process first letter of each word
        first_letters = ''.join(word[0] if word else '' for word in words)
        processed_items.append(len(first_letters))
    
    # Set operations for offset calculation
    unique_lengths = set(processed_items)
    base_offset = sum(unique_lengths)
    
    # Conditional offset adjustment
    offset_correction = base_offset - 5 if base_offset > 10 else base_offset + 2
    
    # Distractor: Unused intermediate calculation
    temp_sum = sum(word_frequencies.values())
    
    # Final result calculation
    final_result = processed_items[2] + offset_correction
    print(f"Target result: {final_result}")

# Test data
text_data = [
    "Quick brown fox jumps",
    "Over the lazy dog",
    "Programming benchmark evaluation",
    "Complex reasoning chains"
]

analyze_text_patterns(text_data)