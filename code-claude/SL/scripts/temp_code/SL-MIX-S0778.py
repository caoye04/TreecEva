# Finding common letters in two words
word1 = "programming"
word2 = "algorithm"

# Convert to lowercase for consistency
word1 = word1.lower()
word2 = word2.lower()

# Some letter counts (not directly used in calculation)
letters_in_word1 = len(word1)
letters_in_word2 = len(word2)
total_letters = letters_in_word1 + letters_in_word2

# Calculate the number of common letters (case insensitive)
common_letters = len(set(word1) & set(word2))

# Calculate percentage of common letters (not needed for answer)
percentage = (common_letters * 100) / (len(set(word1) | set(word2)))

# Zip the words together for display (not used in calculation)
combined = list(zip(word1[:5], word2[:5]))

print(f"Result: {common_letters}")