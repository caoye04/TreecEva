from collections import Counter

text = "the quick brown fox jumps over the lazy dog"
char_freq = Counter(text)
total_chars = len(text)

# Calculate frequency-based density score for letter 'e'
density_score = char_freq['e'] / total_chars if 'e' in char_freq else 0

# Irrelevant auxiliary variable (minor distraction)
unused_metric = sum(1 for c in text if c in 'aeiou')

print(f"Result: {density_score}")