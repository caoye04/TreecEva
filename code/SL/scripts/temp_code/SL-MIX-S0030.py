from collections import Counter

text_sample = "algorithmic complexity analysis demonstrates recursive patterns"
words = text_sample.split()

# Analyze word length distribution
word_lengths = [len(word) for word in words]
length_stats = Counter(word_lengths)
max_length = max(word_lengths)

# Count character frequencies (main analysis)
all_chars = ''.join(words)
char_frequencies = Counter(all_chars.lower())

# Some intermediate calculations (partially relevant)
vowel_count = sum(1 for char in all_chars.lower() if char in 'aeiou')
consonant_count = len(all_chars) - vowel_count
ratio_analysis = vowel_count / consonant_count if consonant_count > 0 else 0

# Target analysis: specific character statistics
word_stats = {}
for word in words:
    first_char = word[0].lower()
    word_stats[first_char] = word_stats.get(first_char, 0) + 1

# Some additional processing (distraction)
processed_words = [word.upper() for word in words[:3]]
reverse_analysis = sum(len(word) for word in processed_words)

target_letter = 'a'
final_count = word_stats[target_letter]

print(f"Target result: {final_count}")