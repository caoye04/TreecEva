from collections import Counter

# Word game scoring system
def calculate_word_score(word):
    # Point values for each letter
    letter_values = {
        'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
        'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
        's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
    }
    
    # Count letter frequencies
    letter_count = Counter(word.lower())
    unique_letters = len(letter_count)
    
    # Calculate base score from letter values
    word_score = sum(letter_values.get(char.lower(), 0) for char in word)
    
    # Apply length bonus if word is longer than 5 letters
    length_bonus = len(word) > 5 and 5 or 0
    
    # Calculate final score
    final_score = word_score + length_bonus
    
    print(f"Result: {word_score}")
    return final_score

# Test with a sample word
word = "Python"
calculate_word_score(word)