from collections import Counter

# Analyzing word frequency in two text samples
sample1 = "data science machine learning artificial intelligence data mining"
sample2 = "big data cloud computing machine learning neural networks"

# Process the text samples
words1 = sample1.split()
words2 = sample2.split()

# Create frequency counters
freq1 = Counter(words1)
freq2 = Counter(words2)

# Some preliminary analysis
unique_words = set(words1).union(set(words2))
total_unique = len(unique_words)

# Words appearing in both samples
common_words = set(words1).intersection(set(words2))

# Calculate word importance scores (not used in final result)
importance_scores = {}
for word in unique_words:
    # Calculate a score based on presence in both samples
    score = freq1[word] * 2 + freq2[word] * 3
    importance_scores[word] = score

# Extract words with high importance (distraction)
high_importance = [word for word, score in importance_scores.items() if score > 5]

# Find words that appear exactly once in each sample
single_occurrences = []
for word in common_words:
    if freq1[word] == 1 and freq2[word] == 1:
        single_occurrences.append(word)

# Create sets based on word position
first_half1 = set(words1[:len(words1)//2])
second_half1 = set(words1[len(words1)//2:])
first_half2 = set(words2[:len(words2)//2])
second_half2 = set(words2[len(words2)//2:])

# Find elements common between first halves of both samples
first_half_common = first_half1.intersection(first_half2)

# Find elements common between second halves of both samples
second_half_common = second_half1.intersection(second_half2)

# Calculate the combined common elements
common_elements = first_half_common.union(second_half_common)

# This is our target value
overlap_count = len(common_elements)

# Additional processing (distraction)
ratio = overlap_count / total_unique if total_unique > 0 else 0
adjusted_score = overlap_count * 2 - len(single_occurrences)

print(f"Result: {overlap_count}")