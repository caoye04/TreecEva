import itertools
from collections import Counter

# Analyzing text overlap between two product descriptions
description1 = "premium leather ergonomic office chair with lumbar support and adjustable height"
description2 = "ergonomic mesh office chair featuring lumbar support and reclining function"

# Process descriptions
def tokenize(text):
    # Convert to lowercase and split into words
    return set(text.lower().split())

# Extract words
words1 = tokenize(description1)
words2 = tokenize(description2)

# Find potential alternative descriptions
alternate_desc = "comfortable executive chair with premium materials"
alternate_words = tokenize(alternate_desc)

# Calculate character frequencies for analytics
char_freq1 = Counter(description1.replace(" ", ""))
char_freq2 = Counter(description2.replace(" ", ""))

# Most common characters in descriptions (unused in final calculation)
common_chars_count = sum((char_freq1 & char_freq2).values())

# Analyze word overlap between descriptions
word_intersection = words1.intersection(words2)
word_union = words1.union(words2)

# Calculate metrics
unique_to_desc1 = len(words1 - words2)
unique_to_desc2 = len(words2 - words1)

# This is our target calculation
common_characters = len(word_intersection)

# Calculate similarity score (not used in final answer)
overlap_ratio = common_characters / len(word_union) if word_union else 0

# Check if alternate description shares any words
alternate_overlap = len(word_intersection.intersection(alternate_words))

# Final product similarity metrics
print(f"Words unique to description 1: {unique_to_desc1}")
print(f"Words unique to description 2: {unique_to_desc2}")
print(f"Result: {common_characters}")