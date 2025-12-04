import itertools

# Student exam scores from different subjects
math_scores = [85, 92, 78, 90, 88]
science_scores = [79, 85, 91, 76, 82]

# Calculate average scores for reference
avg_math = sum(math_scores) / len(math_scores)
avg_science = sum(science_scores) / len(science_scores)

# Combine scores from both subjects
all_scores = list(itertools.chain(math_scores, science_scores))

# Filter scores that are above average in their respective subject
filtered_scores = [score for score in math_scores if score > avg_math] + \
                  [score for score in science_scores if score > avg_science]

# Calculate bonus points based on highest score
bonus = max(all_scores) - 80 if max(all_scores) > 80 else 0

# Calculate final score
final_score = sum(filtered_scores)

# Apply conditional adjustment
final_score = final_score + bonus if avg_math > avg_science else final_score - 5

print(f"Result: {final_score}")