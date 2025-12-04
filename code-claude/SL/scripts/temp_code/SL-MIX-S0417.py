from collections import Counter

# Word game scoring system based on letter frequency
text = "The quick brown fox jumps over the lazy dog"
word_to_score = "Python"

# Count letter frequencies in the sample text
letter_counter = Counter(c.lower() for c in text if c.isalpha())

# Calculate letter values based on inverse frequency (rarer letters worth more)
total_letters = sum(letter_counter.values())
letter_values = {letter: round(10 * (1 - count/total_letters), 1) for letter, count in letter_counter.items()}

# Apply some adjustments to letter values
for vowel in 'aeiou':
    if vowel in letter_values:
        letter_values[vowel] = max(1.0, letter_values[vowel] - 1.5)

# Process the word to score
filtered_word = word_to_score.strip().lower()

# Calculate the word score
word_score = sum(letter_values.get(c.lower(), 0) for c in filtered_word)

# Bonus points for word length
length_bonus = 2 if len(filtered_word) > 5 else 0

# Final score with length bonus
final_score = word_score + length_bonus

print(f"Letter values: {letter_values}")
print(f"Word to score: {word_to_score}")
print(f"Word score: {word_score}")
print(f"Final score: {final_score}")