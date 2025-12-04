# Calculate a vowel score for text analysis

text = "The quick brown fox jumps over the lazy dog"
letters = [char.lower() for char in text if char.isalpha()]

# Define vowels and their point values
vowels = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}

# Count total characters for reference
total_chars = len(letters)
consonants = len([c for c in letters if c.lower() not in vowels])

# Calculate vowel points
scores = [vowels[char] for char in letters if char in vowels]
vowel_score = sum(scores)

# Calculate average score per vowel
if len(scores) > 0:
    avg_score = vowel_score / len(scores)
else:
    avg_score = 0

print(f"Result: {vowel_score}")