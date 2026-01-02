from itertools import takewhile

# Game performance data
base_scores = [85, 90, 78, 92, 88]
efficiency_flags = [True, False, True, True, False]

# Apply efficiency bonus using conditional logic
adjusted_scores = [
    score + 5 if flag else score - 2
    for score, flag in zip(base_scores, efficiency_flags)
]

# Filter out scores below passing threshold using itertools
passing_scores = list(takewhile(lambda x: x >= 85, sorted(adjusted_scores, reverse=True)))

# Irrelevant distraction: unused variable (minimal interference)
max_possible = max(adjusted_scores) if adjusted_scores else 0

# Compute final ranking score with enumeration
total_score = sum(rank * score for rank, score in enumerate(passing_scores, start=1))

print(f"Result: {total_score}")