def analyze_text_fragments(text_segments):
    fragment_lengths = list(map(len, text_segments))
    max_len = max(fragment_lengths)
    min_len = min(fragment_lengths)
    
    # Distractor calculations that don't affect final result
    avg_len = sum(fragment_lengths) / len(fragment_lengths)
    length_difference = max_len - min_len
    
    processing_results = []
    for idx, segment in enumerate(text_segments):
        if segment.strip().isalpha():
            # Main processing logic
            processed = len([c for c in segment if c.lower() in 'aeiou'])
            processing_results.append(processed)
        else:
            # Additional distractor processing
            temp_count = sum(1 for c in segment if c.isdigit())
            processing_results.append(temp_count * 2)
    
    # Unused intermediate variable
    total_operations = len(processing_results) * 2
    
    # Final assignment with intervention
    final_processing_count = processing_results[-1]
    
    print(f"Target result: {final_processing_count}")
    return final_processing_count

# Test data
text_samples = ["Hello", "World123", "Python", "Code42", "AI"]
analyze_text_fragments(text_samples)