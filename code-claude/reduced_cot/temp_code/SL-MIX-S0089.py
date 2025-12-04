import itertools

# Calculate word value based on character encoding and bitwise operations
text = "python programming is fun and rewarding"
words = text.split()

# Filter words that contain at least one vowel
def has_vowel(word):
    return any(c in 'aeiou' for c in word)

filtered_words = [word for word in words if has_vowel(word)]

# Select the third word from the filtered list
selected_index = 2
filtered_word = filtered_words[selected_index]

# Apply bit masking to character values
mask = 0x1F  # Binary: 00011111 (keeps the 5 least significant bits)

# Calculate the value by summing masked character codes
word_value = sum(ord(c) & mask for c in filtered_word)

print(f"Selected word: {filtered_word}")
print(f"Result: {word_value}")