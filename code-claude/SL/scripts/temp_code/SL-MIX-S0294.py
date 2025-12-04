from collections import Counter

def calculate_word_score(word, letter_values):
    # Convert to lowercase for processing
    word = word.strip()
    
    # Count letter frequencies
    letter_count = Counter(word.lower())
    
    # Create a dictionary of character values
    char_values = {}
    for char, value in letter_values:
        char_values[char.lower()] = value
    
    # Calculate word score based on letter values
    word_score = sum(char_values.get(char.lower(), 0) for char in word)
    
    # Count vowels for bonus (not used in final calculation)
    vowels = sum(1 for c in word.lower() if c in 'aeiou')
    
    return word_score

# Scrabble-inspired letter values (character, point value)
letter_values = [('a', 1), ('b', 3), ('c', 3), ('d', 2), 
                ('e', 1), ('f', 4), ('g', 2), ('h', 4), 
                ('i', 1), ('j', 8), ('k', 5), ('l', 1), 
                ('m', 3), ('n', 1), ('o', 1), ('p', 3), 
                ('q', 10), ('r', 1), ('s', 1), ('t', 1), 
                ('u', 1), ('v', 4), ('w', 4), ('x', 8), 
                ('y', 4), ('z', 10)]

# Word to evaluate
word = "Python"

# Calculate and print the result
result = calculate_word_score(word, letter_values)
print(f"Result: {result}")