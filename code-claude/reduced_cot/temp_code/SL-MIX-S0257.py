def analyze_word(word):
    processed_word = word.lower()
    
    # Count vowels in the word
    vowels = 'aeiou'
    vowel_count = sum(1 for char in processed_word if char in vowels)
    
    # Count unique letters (case-insensitive)
    unique_letters_count = len([letter for letter in set(processed_word) if letter.isalpha()])
    
    # Calculate a word score based on unique letters and vowels
    word_score = unique_letters_count * 2 - vowel_count
    
    return {
        "unique": unique_letters_count,
        "vowels": vowel_count,
        "score": word_score
    }

test_word = "Hello-123"
result = analyze_word(test_word)
print(f"Result: {result['unique']}")