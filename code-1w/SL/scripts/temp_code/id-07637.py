from itertools import compress

# Simulated student test scores and attendance flags
test_scores = [85, 92, 78, 96, 88, 73, 91]
attendance_flags = [True, True, False, True, True, False, True]
present_scores = list(compress(test_scores, attendance_flags))

# Apply bonus of 5 points to scores below 85 after filtering
adjusted_scores = [score + 5 if score < 85 else score for score in present_scores]

# Filter out any score below 80 for final evaluation
filtered_scores = [s for s in adjusted_scores if s >= 80]

# Key computation step
total_score = sum(filtered_scores)

print(f"Result: {total_score}")