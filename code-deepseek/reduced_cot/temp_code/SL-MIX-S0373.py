from collections import Counter

sample_text = "Programming Language Analysis"
vowel_count = 0
consonant_count = 0

# Count vowels and consonants
for char in sample_text.lower():
    if char in 'aeiou':
        vowel_count += 1
    elif char.isalpha():
        consonant_count += 1

# Calculate character frequency using Counter
character_frequency = Counter(sample_text.lower())

# Additional unrelated calculation
word_count = len(sample_text.split())

print(f"Result: {character_frequency}")