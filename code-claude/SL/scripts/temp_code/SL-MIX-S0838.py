from collections import Counter

# Text processing for word frequency analysis
text = "The quick brown fox jumps over the lazy dog. A quick movement of the enemy will jeopardize five gunboats."
text = text.lower().replace('.', ' ').replace(',', ' ')

# Extract words and apply filters
all_words = [word for word in text.split() if len(word) >= 3]

# Count word occurrences for later analysis
word_counts = Counter(all_words)

# Get words starting with common letters
prefix_length = 2  # We'll look at the first 2 letters
prefixes = [word[:prefix_length] for word in all_words if len(word) >= prefix_length]

# Find the most common prefix
prefix_counter = Counter(prefixes)
most_common_prefix = prefix_counter.most_common(1)[0][0]

# Process words based on length criteria
min_length = 4
max_length = 8
length_filtered = [word for word in all_words if min_length <= len(word) <= max_length]

# Apply additional filtering criteria (not directly related to result)
filtered_by_vowels = []
for word in all_words:
    vowel_count = sum(1 for char in word if char in 'aeiou')
    if vowel_count >= 2:
        filtered_by_vowels.append(word)

# Merge filtering criteria with some redundancy
filtered_words = list(set(length_filtered))

# Calculate the target value
valid_words = len([word for word in filtered_words if word.startswith(most_common_prefix)])

# Apply some additional transformations (distraction)
transformed_words = [word.upper() for word in filtered_words if len(word) > min_length]

# Calculate alternative statistics (not used in final result)
avg_word_length = sum(len(word) for word in all_words) / len(all_words)

print(f"Result: {valid_words}")