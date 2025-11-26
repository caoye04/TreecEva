def process_text_data(text_samples, threshold):
    char_frequency = {}
    temp_counts = []
    
    # Process each text sample
    for text in text_samples:
        upper_text = text.upper()
        count_vowels = sum(1 for char in upper_text if char in 'AEIOU')
        temp_counts.append(count_vowels)
        
        # Build character frequency (distractor operation)
        for char in upper_text:
            char_frequency[char] = char_frequency.get(char, 0) + 1
    
    # Filter based on threshold
    filtered_counts = [count for count in temp_counts if count > threshold]
    
    # Calculate final result using conditional expression
    final_count = len(filtered_counts) if len(filtered_counts) > 0 else -1
    
    # Distractor: unused calculation
    total_chars = sum(char_frequency.values())
    most_common_char = max(char_frequency, key=char_frequency.get)
    
    print(f"Result: {final_count}")
    return final_count

# Sample data
text_samples = ['hello', 'world', 'programming', 'test', 'example']
result = process_text_data(text_samples, threshold=3)
final_count = result