from collections import Counter

# Analyze word frequency in a technical document fragment
text_sample = "algorithm data structure optimization performance efficiency algorithm data structure complexity"
words = text_sample.split()

# Calculate frequency distribution
word_counts = Counter(words)
unique_words = len(word_counts)
total_words = len(words)

# Compute various metrics (some are distractions)
most_common_count = word_counts.most_common(1)[0][1]
frequency_ratio = most_common_count / total_words

# Distractor calculations that don't affect final result
max_length = max(len(word) for word in words)
avg_length = sum(len(word) for word in words) / total_words

# Core calculations for the actual metric
base_score = sum(word_counts.values()) * 2
adjusted_base = base_score - (unique_words * 3)

# More distraction operations
vowel_count = sum(1 for word in words if any(char in 'aeiou' for char in word.lower()))

# Final processing steps
processed_sum = adjusted_base + (total_words // 2)
adjustment_factor = (most_common_count - 1) * 2

# Target variable - this is what we care about
final_metric = processed_sum - adjustment_factor

print(f"Target result: {final_metric}")