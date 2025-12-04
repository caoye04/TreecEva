# Calculate Scrabble-like word score based on letter values

# Define letter values (similar to Scrabble)
letter_values = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1,
    'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8,
    'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1,
    'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1,
    'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# Process some words
words = ['python', 'programming', 'code']
all_scores = []

for i, word in enumerate(words):
    # Check if word is valid
    is_valid = all(c.isalpha() for c in word)
    
    # Convert word to lowercase for scoring
    word = word.lower()
    
    # Calculate word score based on letter values
    word_score = sum(letter_values[c] for c in word if c in letter_values)
    
    # Apply bonus for words longer than 7 letters
    length_bonus = len(word) > 7
    if length_bonus:
        word_score += 5
    
    # Store score information
    all_scores.append((word, word_score))

# Display result for the second word
result_word, result_score = all_scores[1]
print(f"Result: {result_score}")