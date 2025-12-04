def process_string_data(items, min_length):
    # Calculate preliminary statistics
    total_chars = sum(len(item) for item in items)
    avg_length = total_chars / len(items) if items else 0
    
    # Intermediate filtering (not used in final result)
    long_items = [item.upper() for item in items if len(item) > avg_length]
    
    # Core logic: count items meeting length threshold
    filtered_count = sum(1 for item in items if len(item) >= min_length)
    
    # Distractor operations with lambda
    length_checker = lambda s, threshold: len(s) == threshold
    exact_matches = sum(1 for item in items if length_checker(item, min_length))
    
    # String method operations (semi-relevant)
    vowel_counts = [sum(1 for char in item.lower() if char in 'aeiou') for item in items]
    max_vowels = max(vowel_counts) if vowel_counts else 0
    
    # Final computation with conditional expression
    final_count = filtered_count if filtered_count > exact_matches else exact_matches
    
    return final_count

data_items = ['python', 'java', 'golang', 'rust', 'c', 'javascript']
threshold = 4

# Main execution
result = process_string_data(data_items, threshold)
print(f"Result: {result}")