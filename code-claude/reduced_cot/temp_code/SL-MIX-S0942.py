def calculate_word_values(phrase):
    # Dictionary mapping letters to their positions in alphabet
    letter_values = {chr(i + 97): i + 1 for i in range(26)}
    
    # Split the phrase into words
    words = phrase.lower().split()
    
    # Track highest scoring word
    max_score = 0
    best_word = ""
    
    # Process each word
    for i, word in enumerate(words):
        # Clean the word (remove non-alphabetic characters)
        clean_word = ''.join(c for c in word if c.isalpha())
        
        # Calculate score for each character
        char_scores = [letter_values.get(char, 0) for char in clean_word]
        
        # Sum up the character scores
        word_score = sum(char_scores)
        
        # Track the highest score
        if word_score > max_score:
            max_score = word_score
            best_word = clean_word
    
    # Return information about the phrase analysis
    return best_word, max_score

# Test with a sample phrase
phrase = "The quick brown fox jumps"
word, score = calculate_word_values(phrase)

print(f"Result: {score}")