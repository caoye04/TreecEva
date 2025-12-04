from collections import Counter

# Student exam scores data
scores = [85, 92, 78, 95, 88, 76, 90, 85, 92, 80]

# Calculate frequency of each score
score_freq = Counter(scores)
most_common = score_freq.most_common(2)

# Filter scores based on frequency
occurrence_threshold = 1
filtered_scores = [score for score in scores if score_freq[score] > occurrence_threshold]

# Calculate statistics on filtered scores
avg_filtered = sum(filtered_scores) / len(filtered_scores) if filtered_scores else 0
min_score = min(scores)
max_score = max(scores)

# Calculate final score based on filtered values
final_score = sum(filtered_scores)

print(f"Result: {final_score}")