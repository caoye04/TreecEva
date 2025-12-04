# Student test score analysis
raw_scores = [78, 92, 85, 92, 76, 85, 88, 91, 76, 92]
supplemental_points = [2, 0, 1, 0, 3, 1, 0, 2, 1, 0]

# Apply curve based on position in list
curved_scores = []
for idx, (score, extra) in enumerate(zip(raw_scores, supplemental_points)):
    # Add position-based bonus: even positions get +1, odd positions get +2
    position_bonus = 1 if idx % 2 == 0 else 2
    curved_scores.append(score + extra + position_bonus)

# Filter scores based on threshold
threshold = 90
filtered_scores = [score for score in curved_scores if score >= threshold]

# Count unique scores that meet the threshold
unique_count = len(set(filtered_scores))

# Calculate average of filtered scores for reference
avg_filtered = sum(filtered_scores) / len(filtered_scores) if filtered_scores else 0

print(f"Result: {unique_count}")