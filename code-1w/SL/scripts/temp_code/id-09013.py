from collections import defaultdict

# Student exam scores and weighting factors
exam_scores = [85, 90, 78, 92]
base_adjustment = 5

# Irrelevant distraction: unused variable (minimal interference)
unused_buffer = [0] * 10

# Weighting for different exams using lambda to compute dynamic factors
calculate_weighted = lambda scores: [score * 1.1 for score in scores]
adjusted_scores = calculate_weighted(exam_scores)

# Apply base adjustment to all scores
adjusted_scores = [score + base_adjustment for score in adjusted_scores]

# Use slicing to only consider the last three exam scores
recent_scores = adjusted_scores[1:]

# Aggregate using defaultdict for frequency counting (though not fully utilized)
score_freq = defaultdict(int)
for s in recent_scores:
    score_freq[s] += 1

# Final calculation based on average of recent, adjusted scores
def calculate_final(weights):
    return int(sum(recent_scores) / len(recent_scores))

final_score = calculate_final([])
print(f"Result: {final_score}")