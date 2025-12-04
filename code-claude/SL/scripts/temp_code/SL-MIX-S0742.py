import itertools

# Analyze text for unique character distribution
text = "Hello World! Python Programming."
processed_text = text.lower()

# Remove some characters for analysis
chars_to_remove = [' ', '!', '.']
for char in chars_to_remove:
    processed_text = processed_text.replace(char, '')

# Count letter frequencies
letter_freq = {}
for char in processed_text:
    if char in letter_freq:
        letter_freq[char] += 1
    else:
        letter_freq[char] = 1

# Find most common letter
most_common = max(letter_freq.items(), key=lambda x: x[1])[0]

# Calculate unique characters
unique_count = len(set(processed_text))

# Generate all possible pairs of unique characters
all_pairs = list(itertools.combinations(set(processed_text), 2))
pair_count = len(all_pairs)

print(f"Result: {unique_count}")