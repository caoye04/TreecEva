# Calculate the numerical value of a word based on letter positions
# Each letter's value is its position in the alphabet (a=1, b=2, etc.)

text = "programming challenge"
words = text.split()

# Dictionary to track letter positions
alpha_positions = {chr(i + 97): i + 1 for i in range(26)}

# Process each word
for word in words:
    # Remove any non-alphabetic characters
    clean_word = ''.join(c for c in word if c.isalpha())
    
    # Calculate letter scores
    scores = [alpha_positions.get(letter, 0) for letter in clean_word.lower()]
    
    # Total value of this word
    word_value = sum(scores)
    
    # Length of the word for reference
    word_length = len(clean_word)

print(f"Result: {word_value}")