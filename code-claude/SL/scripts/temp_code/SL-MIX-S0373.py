from collections import Counter

# Letter values in a word game
letter_values = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

words = ["python", "coding", "challenge"]
bonus_letters = ['p', 'c']

def calculate_word_value(word_list, values):
    # Calculate total value based on letter frequencies
    word_letters = ''.join(word_list)
    letter_counts = Counter(word_letters)
    
    # Apply base scoring
    base_score = sum(count * values.get(letter, 0) for letter, count in letter_counts.items())
    
    # Apply bonus for special letters
    bonus = sum(2 * letter_counts[letter] for letter in bonus_letters if letter in letter_counts)
    
    return base_score + bonus

# Calculate the word value
word_value = calculate_word_value(words, letter_values)

# Display result
print(f"Result: {word_value}")