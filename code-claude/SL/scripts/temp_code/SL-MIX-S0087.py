# Analysis of common words between two text samples
text1 = "the quick brown fox jumps over the lazy dog"
text2 = "a quick brown dog barks at the fox"

# Extract unique words from each text
words1 = text1.split()
words2 = text2.split()

# Create sets for efficient comparison
set1 = set(words1)
set2 = set(words2)

# Count words in each set
total_words1 = len(set1)
total_words2 = len(set2)

# Find words that appear in both texts
common_words = len(set1.intersection(set2))

# Find words that appear in exactly one of the texts
unique_elements = len(set1.symmetric_difference(set2))

# Calculate percentage of unique words relative to total unique vocabulary
total_vocabulary = len(set1.union(set2))
uniqueness_ratio = unique_elements / total_vocabulary if total_vocabulary > 0 else 0

print(f"Result: {unique_elements}")