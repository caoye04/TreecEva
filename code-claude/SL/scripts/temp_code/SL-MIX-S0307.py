from collections import Counter

def calculate_word_value(word, bonus_letters=None):
    # Letter values in word game (like Scrabble)
    letter_values = {
        'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1,
        'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8,
        'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1,
        'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1,
        'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
    }
    
    # Process the word
    processed_word = word.lower()
    
    # Check for double letter bonus
    letter_counts = Counter(processed_word)
    double_letters = [letter for letter, count in letter_counts.items() if count > 1]
    
    # Calculate base score
    word_score = sum(letter_values.get(c, 0) for c in processed_word)
    
    # Apply bonus for words with double letters
    if double_letters and bonus_letters:
        bonus_factor = len(set(double_letters).intersection(bonus_letters))
        word_score += bonus_factor * 2
    
    # Apply length bonus for words longer than 5 letters
    if len(processed_word) > 5:
        word_score += len(processed_word) - 5
    
    return word_score

# Test the function
input_word = "puzzle"
bonus_set = {'z', 'p'}
result = calculate_word_value(input_word, bonus_set)
print(f"Result: {result}")
