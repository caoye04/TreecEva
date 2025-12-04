def count_unique_characters(text, filter_type="all"):
    # Process text based on filter type
    processed_text = text.lower()
    
    # Initialize counters for statistics
    vowel_count = sum(1 for char in processed_text if char in "aeiou")
    consonant_count = sum(1 for char in processed_text if char.isalpha() and char not in "aeiou")
    digit_count = sum(1 for char in processed_text if char.isdigit())
    
    # Filter text based on filter_type
    if filter_type == "vowels":
        filtered_text = "".join([c for c in processed_text if c in "aeiou"])
    elif filter_type == "consonants":
        filtered_text = "".join([c for c in processed_text if c.isalpha() and c not in "aeiou"])
    elif filter_type == "digits":
        filtered_text = "".join([c for c in processed_text if c.isdigit()])
    elif filter_type == "letters":
        filtered_text = "".join([c for c in processed_text if c.isalpha()])
    else:  # "all" or any other value
        filtered_text = "".join([c for c in processed_text if c.isalnum()])
    
    # Calculate metrics
    total_chars = len(filtered_text)
    unique_chars = len(set(filtered_text))
    
    # Calculate a complexity score (not used in final result)
    complexity = (vowel_count * 1.5) + (consonant_count * 1.0) + (digit_count * 2.0)
    normalized_complexity = complexity / (total_chars if total_chars > 0 else 1)
    
    # Generate a report dictionary (not used in final calculation)
    report = {
        "total": total_chars,
        "unique": unique_chars,
        "vowels": vowel_count,
        "consonants": consonant_count,
        "digits": digit_count,
        "complexity": normalized_complexity
    }
    
    return unique_chars

# Sample text with mixed content
input_text = "Hello123 World!"

# Process with different filters to compare (only the last one affects the answer)
all_filter = count_unique_characters(input_text)
letters_only = count_unique_characters(input_text, "letters")
digits_only = count_unique_characters(input_text, "digits")

# The one we're interested in
result = count_unique_characters(input_text, "consonants")
print(f"Result: {result}")