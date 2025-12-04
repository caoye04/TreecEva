from collections import Counter

text1 = "The quick brown fox jumps over the lazy dog while the cat sleeps peacefully"
text2 = "A dog barks at the mailman while the lazy fox watches from afar"

# Process first text
words1 = text1.lower().split()
filtered_words1 = [word for word in words1 if len(word) > 2]
frequency1 = Counter(filtered_words1)

# Process second text
words2 = text2.lower().split()
filtered_words2 = [word.strip(',.!?') for word in words2]
frequency2 = Counter(filtered_words2)

# Calculate metrics
total_unique = len(set(filtered_words1).union(set(filtered_words2)))
frequency_intersection = set(frequency1.keys()).intersection(set(frequency2.keys()))
common_words = len(frequency_intersection)

# Calculate word length statistics
avg_len1 = sum(len(word) for word in filtered_words1) / len(filtered_words1) if filtered_words1 else 0
avg_len2 = sum(len(word) for word in filtered_words2) / len(filtered_words2) if filtered_words2 else 0

# This doesn't affect the answer
importance_factor = 1.5 if avg_len1 > avg_len2 else 0.8

# Calculate weighted score (not used in final answer)
weighted_score = (total_unique * 0.3) + (common_words * importance_factor)

# Define threshold values (distraction)
low_similarity = 3
high_similarity = 7

# Print result
print(f"Result: {common_words}")