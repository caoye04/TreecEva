def process_text_segments():
    text_data = "Python programming involves working with strings and tuples frequently"
    words_tuple = tuple(text_data.split())
    
    # Count words that start with vowels
    vowel_start_count = 0
    for word in words_tuple:
        if word.lower().startswith(('a', 'e', 'i', 'o', 'u')):
            vowel_start_count += 1
    
    # Process the count with arithmetic
    base_multiplier = 3
    adjustment_factor = 7
    processed_data = (vowel_start_count * base_multiplier) + adjustment_factor
    
    final_count = processed_data
    print(f"Result: {final_count}")

process_text_segments()