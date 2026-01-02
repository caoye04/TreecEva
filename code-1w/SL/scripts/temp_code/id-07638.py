from itertools import groupby

text = 'aaabbcdddddccbaa'

# Group consecutive characters and count their occurrences
groups = [(char, len(list(group))) for char, group in groupby(text)]

# Extract counts only for vowels (a, e, i, o, u)
vowel_counts = [count for char, count in groups if char in 'aeiou']

# For consonants, we're just tracking them but not using them directly
consonant_counts = [count for char, count in groups if char not in 'aeiou']

# Only vowels contribute to final result
valid_counts = [count for count in vowel_counts if count > 1]

result = sum(valid_counts)
print(f'Result: {result}')