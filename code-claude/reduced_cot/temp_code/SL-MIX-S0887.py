# Student score analysis program

# List of exam scores for a class
scores = [78, 92, 85, 64, 90, 75, 88, 79, 93]

# Flag to determine if we should exclude outliers
exclude_outliers = True

# Threshold for considering a score as an outlier (too low)
min_threshold = 70

# Calculate statistics
total_students = len(scores)
max_score = max(scores)

# Create a filtered list excluding scores below threshold if flag is True
filtered_scores = [score for score in scores if score >= min_threshold or not exclude_outliers]

# Calculate the average of the filtered scores
average_score = sum(filtered_scores) / len(filtered_scores)

# Additional information about class performance
passing_rate = len([s for s in scores if s >= 75]) / total_students * 100

print(f"Result: {average_score}")