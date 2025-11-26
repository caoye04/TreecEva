from collections import Counter

# Analyze text character frequency
text_sample = "programming benchmark evaluation"
char_counts = Counter(text_sample)

# Filter characters that appear more than once
filtered_chars = {char: count for char, count in char_counts.items() if count > 1}

# Calculate total occurrences of repeated characters
counts = {k: v for k, v in filtered_chars.items() if k in 'aeiou'}
final_tally = sum(counts.values())

print(f"Result: {final_tally}")