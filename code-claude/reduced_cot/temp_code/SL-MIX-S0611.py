# Word scoring system for a word game

# Define letter scores (similar to Scrabble)
letter_scores = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# Input word and processing
raw_word = "QuiZzicAL"

# Convert to lowercase for processing
processed_word = raw_word.lower()

# Create some statistics about the word
vowels = 'aeiou'
vowel_count = sum(1 for char in processed_word if char in vowels)
consonant_count = sum(1 for char in processed_word if char.isalpha() and char not in vowels)

# Apply bonus multiplier based on word characteristics
bonus_multiplier = 1.5 if vowel_count >= 3 else 1.0

# Generate a filtered version removing every other character
filtered_indices = [i for i in range(len(processed_word)) if i % 2 == 0]
filtered_word = ''.join(processed_word[i] for i in filtered_indices)

# Calculate letter frequency for analysis (not used in final score)
letter_frequency = {}
for letter in processed_word:
    if letter.isalpha():
        letter_frequency[letter] = letter_frequency.get(letter, 0) + 1

# Calculate the raw score based on letter values
raw_score = sum(letter_scores.get(c, 0) for c in processed_word)

# Calculate word value using only the filtered word
word_value = sum(letter_scores[c] for c in filtered_word)

# Apply bonus multiplier to raw score (not to word_value)
final_score = int(raw_score * bonus_multiplier)

# Print results
print(f"Word: {raw_word}")
print(f"Filtered word: {filtered_word}")
print(f"Raw score: {raw_score}")
print(f"Final score: {final_score}")
print(f"Result: {word_value}")