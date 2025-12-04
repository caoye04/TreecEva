def process_text(input_text):
    # Remove punctuation and convert to lowercase
    cleaned_text = ''.join(char.lower() if char.isalnum() or char.isspace() else ' ' for char in input_text)
    
    # Split into words
    words = cleaned_text.split()
    
    # Track statistics (not used in final calculation)
    char_count = sum(len(word) for word in words)
    avg_length = char_count / len(words) if words else 0
    
    # Filter words based on length
    length_threshold = 3
    filtered_words = [word for word in words if len(word) > length_threshold]
    
    # Define word validity check
    def is_valid_word(word):
        # Words with vowels are valid
        vowels = 'aeiou'
        contains_vowel = any(v in word for v in vowels)
        
        # Words with repeating letters are invalid
        has_repeats = any(word[i] == word[i+1] for i in range(len(word)-1))
        
        # Words starting with digits are invalid
        starts_with_digit = word[0].isdigit() if word else False
        
        return contains_vowel and not has_repeats and not starts_with_digit
    
    # Process statistics for reporting (not affecting result)
    max_word = max(filtered_words, key=len) if filtered_words else ''
    max_length = len(max_word)
    
    # Count valid words
    valid_count = len([word for word in filtered_words if is_valid_word(word)])
    
    # Attempt to optimize with a different approach (not used)
    alternative_count = 0
    for w in filtered_words:
        if is_valid_word(w):
            alternative_count += 1
    
    # Return the count
    return valid_count

# Sample text to process
sample_text = "The quick brown fox jumps over the lazy dog. 123 testing, test44, apple, banana!"

# Process the text and get result
result = process_text(sample_text)
print(f"Result: {result}")