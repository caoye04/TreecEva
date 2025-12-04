import itertools

# Calculate score for letters in a word based on their position in alphabet
def analyze_word(word):
    # Letter values based on position in alphabet (a=1, b=2, etc.)
    letter_values = {chr(i + 97): i + 1 for i in range(26)}
    
    # Track special characters for analysis
    special_chars = '!@#$%^&*()'
    special_count = sum(1 for c in word if c in special_chars)
    
    # Convert word to lowercase and remove non-alphabetic characters
    filtered_word = ''.join(c for c in word.lower() if c.isalpha())
    
    # Calculate the word score - sum of letter values
    word_score = sum(letter_values[c] for c in filtered_word)
    
    # Check if the word has repeated letters
    unique_letters = len(set(filtered_word))
    has_repeats = len(filtered_word) > unique_letters
    
    # Print the results
    print(f"Word: {word}")
    print(f"Filtered word: {filtered_word}")
    print(f"Result: {word_score}")
    
    return word_score

# Analyze a sample word
sample_word = "Hello123!"
final_score = analyze_word(sample_word)