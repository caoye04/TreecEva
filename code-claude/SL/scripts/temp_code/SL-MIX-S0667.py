def analyze_text(text, threshold=4):
    # Split text into words and convert to lowercase
    words = text.lower().split()
    
    # Count letter frequencies for analysis (not directly used in result)
    letter_counts = {}
    for word in words:
        for char in word:
            if char.isalpha():
                letter_counts[char] = letter_counts.get(char, 0) + 1
    
    # Process words with different approaches
    cleaned_words = []
    special_words = []
    for i, word in enumerate(words):
        # Remove punctuation and non-alphabetic characters
        cleaned = ''.join(c for c in word if c.isalpha())
        if cleaned:
            cleaned_words.append(cleaned)
            
        # Track words with special characters (distraction)
        if any(not c.isalnum() for c in word):
            special_words.append(word)
    
    # Calculate average word length (distraction)
    avg_length = sum(len(word) for word in cleaned_words) / max(len(cleaned_words), 1)
    
    # Filter words based on character conditions
    filtered_words = []
    for word in cleaned_words:
        if 'z' in word or 'q' in word:
            continue  # Skip words with 'z' or 'q'
        
        # Check for vowel count
        vowel_count = sum(1 for c in word if c in 'aeiou')
        if vowel_count >= 2:
            filtered_words.append(word)
    
    # Early return condition (distraction)
    if len(filtered_words) < 3:
        return 0
    
    # Calculate minimum length threshold based on average
    min_length = threshold if avg_length < 5 else threshold + 1
    
    # This is the key statement
    valid_words = len([word for word in filtered_words if len(word) >= min_length])
    
    # Additional processing (distraction)
    unique_words = len(set(filtered_words))
    ratio = unique_words / max(len(filtered_words), 1)
    
    print(f"Result: {valid_words}")
    return valid_words

text_sample = "The quick brown fox jumps over the lazy dog near a quiet stream."
result = analyze_text(text_sample)