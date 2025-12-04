def calculate_word_value(word):
    """Calculate the value of a word by summing position values of each character.
    Position value: position of letter in alphabet (a=1, b=2, ..., z=26)
    """
    base_score = 0
    for char in word.lower():
        if 'a' <= char <= 'z':
            base_score += (ord(char) - ord('a') + 1)
    return base_score

# Some sample words from a word game
words = ["PYTHON", "JAVA", "RUBY", "CODE"]

# Select a specific word for scoring
selected_word = words[2]  # This selects "RUBY"

# Clean the word by removing any potential non-alphabetic characters
cleaned_word = ''.join(c for c in selected_word if c.isalpha())

# Calculate the word's value
total_points = calculate_word_value(cleaned_word)

# Apply a bonus multiplier for words with more than 3 characters
bonus_multiplier = 1.0
if len(cleaned_word) > 3:
    bonus_multiplier = 1.2

# Print the final result
print(f"Result: {total_points}")