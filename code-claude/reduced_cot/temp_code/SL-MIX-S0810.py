# Calculate the value of a word based on letter positions in alphabet
# where a=1, b=2, c=3, etc. but only count letters that appear once

word = "programming"

# Count occurrences of each character
char_counts = {}
for char in word:
    if char in char_counts:
        char_counts[char] += 1
    else:
        char_counts[char] = 1

# Filter to keep only characters that appear once
filtered_word = ''
for char in word:
    if char_counts[char] == 1 and char.isalpha():
        filtered_word += char

# Calculate the word value where a=1, b=2, c=3, etc.
word_value = sum(map(lambda c: ord(c) - ord('a') + 1, filtered_word))

other_value = len(word) * 2  # Not used in final calculation
print(f"Result: {word_value}")