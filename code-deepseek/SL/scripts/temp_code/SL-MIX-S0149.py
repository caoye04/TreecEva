from collections import Counter

# Analyze student performance data across different subjects
math_scores = [85, 92, 78, 96, 88, 91, 74]
science_scores = [79, 85, 92, 88, 81, 95, 90]
history_scores = [82, 88, 75, 91, 86, 89, 93]

# Calculate average scores for each subject (distractor - not used in final result)
math_avg = sum(math_scores) / len(math_scores)
science_avg = sum(science_scores) / len(science_scores)
history_avg = sum(history_scores) / len(history_scores)

# Combine all scores and count occurrences
all_scores = math_scores + science_scores + history_scores
score_counter = Counter(all_scores)

# Process scores by applying bonus and penalty (some operations are relevant, some are not)
processed_data = {}
for score, count in score_counter.items():
    # This bonus calculation doesn't affect the final max value selection
    bonus = 5 if score > 90 else 2
    adjusted_count = count + (1 if score % 2 == 0 else 0)  # Slight adjustment
    processed_data[score] = adjusted_count

# Calculate theoretical maximum (distractor - never used)
theoretical_max = max(all_scores) * 1.1

# The key statement - find the maximum processed value
final_score = max(processed_data.values())
print(f"Result: {final_score}")