# Calculate average test score after filtering out invalid entries
test_scores = [85, 92, 78, -1, 88, 91, -1, 76]
bonus_points = 3  # Extra points awarded to all valid scores
minimum_valid = 0  # Scores below this are invalid entries

# Filter out invalid scores and apply bonus
filtered_scores = []
for score in test_scores:
    if score >= minimum_valid:
        # Apply bonus to valid scores
        filtered_scores.append(score + bonus_points)
    # Track number of invalid entries for reporting
    else:
        invalid_count = test_scores.count(-1)

# Calculate class statistics
lowest_score = min(filtered_scores)
highest_score = max(filtered_scores)
average_score = sum(filtered_scores) / len(filtered_scores)

# Format for reporting
report = f"Class average: {average_score:.1f}"
print(f"Result: {average_score}")