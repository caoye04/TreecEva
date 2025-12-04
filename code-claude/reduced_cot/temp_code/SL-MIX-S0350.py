# Analyzing text for unique words above a certain length
text = "The quick brown fox jumps over the lazy dog near the river bank"
min_length = 3
word_count = len(text.split())
average_length = sum(len(word) for word in text.split()) / word_count

# Count unique words with length greater than min_length
unique_count = len(set([word.lower() for word in text.split() if len(word) > min_length]))

# Additional analysis
vowels = 'aeiou'
vowel_count = sum(1 for char in text.lower() if char in vowels)

print(f"Result: {unique_count}")