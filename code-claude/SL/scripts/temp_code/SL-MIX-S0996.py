# Analyze student exam scores and identify high performers

def calculate_statistics(scores):
    # Calculate some statistics for reference
    average = sum(scores) / len(scores)
    variance = sum((x - average) ** 2 for x in scores) / len(scores)
    std_dev = variance ** 0.5
    return average, std_dev

# Raw exam scores for different subjects
math_scores = [78, 85, 92, 67, 95, 88, 72, 91, 84]
science_scores = [81, 76, 94, 68, 87, 92, 79, 85, 90]

# Process scores and identify potential candidates for advanced placement
all_scores = math_scores + science_scores
all_scores.sort(reverse=True)  # Sort in descending order

# Extract top performing scores (those in the top half)
top_scores = all_scores[:len(all_scores)//2]

# Apply weighting to prioritize extremely high scores
weighted_scores = [score * 1.2 if score > 90 else score for score in all_scores]

# Check for anomalies (scores that deviate significantly)
avg, std = calculate_statistics(all_scores)
potential_anomalies = [score for score in all_scores if abs(score - avg) > 1.5 * std]

# Extract valid scores (between 60 and 100)
valid_scores = [score for score in all_scores if 60 <= score <= 100]

# Calculate a threshold for high performers (75% of max score)
max_possible = 100  # Maximum possible exam score
threshold = max_possible * 0.75

# Count scores in each grade band (just for reporting)
grade_counts = {
    'A': len([s for s in valid_scores if s >= 90]),
    'B': len([s for s in valid_scores if 80 <= s < 90]),
    'C': len([s for s in valid_scores if 70 <= s < 80]),
    'D': len([s for s in valid_scores if 60 <= s < 70])
}

# Get the sum of scores above the threshold
filtered_score = sum(filter(lambda x: x > threshold, valid_scores))

# Calculate average of high performers for reporting
high_performer_avg = filtered_score / len([s for s in valid_scores if s > threshold])

print(f"Result: {filtered_score}")