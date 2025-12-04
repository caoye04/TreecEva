def analyze_text(text):
    # Count vowels in text
    vowels = 'aeiou'
    vowel_count = sum(1 for char in text.lower() if char in vowels)
    
    # Remove punctuation and convert to lowercase
    import string
    cleaned_text = text.lower().translate(str.maketrans('', '', string.punctuation))
    
    # Get word count
    words = cleaned_text.split()
    word_count = len(words)
    
    # Extract words starting with consonants
    consonant_words = [word for word in words if word and word[0] not in vowels]
    
    # Calculate average word length (not used in final result)
    avg_length = sum(len(word) for word in words) / max(1, word_count)
    
    # Filter text based on position
    positions = [3, 7, 11, 15, 19]
    position_chars = [text[i] for i in positions if i < len(text)]
    
    # Create a string with every third character
    filtered_text = text[::3]
    
    # Count unique characters in filtered text
    unique_chars = len(set(filtered_text))
    
    # Calculate a misleading metric (not used in final result)
    complexity_score = (vowel_count * 1.5) + (word_count * 0.8) - len(consonant_words)
    
    return unique_chars

# Sample text for analysis
sample = "Python slicing is powerful and elegant!"

# Process the text
result = analyze_text(sample)
print(f"Result: {result}")