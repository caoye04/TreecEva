import itertools

# Student exam scores from multiple test sessions
exam_data = [(85, 76, 92, 88), (65, 0, 77, 82), (91, 94, 89, 0)]

# Process scores and calculate average of top 3 valid scores
all_scores = list(itertools.chain.from_iterable(exam_data))
valid_scores = [score for score in all_scores if score > 0]

# Additional course metrics (not used in main calculation)
class_size = len(all_scores)
pass_threshold = 70
pass_count = sum(1 for score in valid_scores if score >= pass_threshold)

# Sort scores for analysis
sorted_valid_scores = sorted(valid_scores)

# Calculate average of top 3 scores
top_scores_avg = sum(sorted_valid_scores[-3:]) / 3

# Final result
print(f"Result: {top_scores_avg}")