text = "The algorithm processes data using iterative refinement and optimization."

# Extract components for analysis
tokens = text.split()
sentence_length = len(tokens)
char_count = sum(len(word) for word in tokens)
unique_chars = len(set(text.lower().replace(' ', '')))

# Auxiliary distraction variables (minimal interference)
vowel_ratio = sum(1 for c in text.lower() if c in 'aeiou') / len(text.replace(' ', '')) if text.replace(' ', '') else 0
word_lengths = [len(word) for word in tokens]
median_length = sorted(word_lengths)[len(word_lengths)//2]

# Core computation
word_factor = len([w for w in tokens if len(w) > 4])
density_score = char_count * word_factor / sentence_length if sentence_length > 0 else 0

# Output result
print(f"Result: {density_score}")