from collections import Counter

def calculate_word_value(word):
    # Dictionary of letter values (like in a word game)
    letter_values = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2,
                     'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
                     'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1,
                     'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}
    
    # Convert to lowercase for consistency
    processed_word = word.lower()
    
    # Some words get bonus points if they contain specific letter combinations
    bonus = 5 if 'qu' in processed_word else 0
    
    # Count letter frequencies
    letter_count = Counter(processed_word)
    most_common_letter = letter_count.most_common(1)[0][0] if letter_count else ''
    
    # Calculate word score based on letter values
    word_score = sum(letter_values.get(char, 0) for char in processed_word)
    
    # Apply bonus if applicable
    total_score = word_score + bonus
    
    return word_score, total_score

# Test with the word "python"
input_word = "python"
word_value, total = calculate_word_value(input_word)

print(f"Result: {word_value}")