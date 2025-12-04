# Analyze student exam scores and pairing preferences
exam_scores = [72, 85, 63, 91, 77, 68]
preference_ratings = [4, 2, 5, 1, 3, 4]

# Track some additional metrics that might be useful
average_score = sum(exam_scores) / len(exam_scores)
median_index = len(exam_scores) // 2
sorted_scores = sorted(exam_scores)
median_score = (sorted_scores[median_index] + sorted_scores[median_index - 1]) / 2 if len(exam_scores) % 2 == 0 else sorted_scores[median_index]

# Create student pairs with their combined potential
combined_data = list(zip(exam_scores, preference_ratings))

# Process the data to find compatible study pairs
pairs = []
for i, (score, pref) in enumerate(combined_data):
    # Calculate a compatibility score for each student
    compatibility = score * (6 - pref)  # Invert preference scale so lower is better
    
    # Track additional metrics per student
    score_diff = score - average_score
    normalized_score = score / 100
    
    # Only include pairs that meet certain criteria
    if score >= 70 or pref <= 3:
        pairs.append((i, compatibility))
    elif score_diff > -10:
        # Alternative qualification path
        adjustment = normalized_score * 10
        pairs.append((i, score_diff + adjustment))

# Apply a threshold filter to the pairs
threshold = 250
filtered_pairs = [(idx, comp) for idx, comp in pairs if comp < threshold]

# Count valid pairs based on positive compatibility
valid_pairs_count = len([p for p in filtered_pairs if p[1] > 0])

# Calculate a weighted average of the pairs for reporting
total_weight = sum(p[1] for p in filtered_pairs if p[1] > 0)
average_weight = total_weight / valid_pairs_count if valid_pairs_count > 0 else 0

# Final report metrics
final_metric = valid_pairs_count * (average_weight / 100) if average_weight > 0 else 0

print(f"Result: {valid_pairs_count}")