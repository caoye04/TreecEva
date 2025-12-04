import itertools

def calculate_final_score(scores, weights):
    # Apply weights to scores and sum
    return sum(score * weight for score, weight in zip(scores, weights))

# Student exam scores across different subjects
exam_scores = {
    'math': [85, 92, 78, 90, 88],
    'science': [79, 85, 92, 81, 94],
    'history': [88, 76, 90, 84, 82],
    'language': [91, 84, 82, 88, 95]
}

# Only consider scores above threshold
threshold = 80
filtered_data = {}

for subject, scores in exam_scores.items():
    # Track indices of scores above threshold
    valid_indices = [i for i, score in enumerate(scores) if score > threshold]
    # Apply a bonus to science scores for analysis purposes
    if subject == 'science':
        bonus_scores = [score + 5 for score in scores]
        filtered_data[subject] = [scores[i] for i in valid_indices]
    else:
        filtered_data[subject] = [scores[i] for i in valid_indices]

# Extract only math and language scores for final calculation
subjects_to_use = ['math', 'language']
filtered_scores = []

for subject in subjects_to_use:
    if subject in filtered_data:
        filtered_scores.extend(filtered_data[subject])

# Generate some test weights (won't be used)
test_weights = [0.5, 0.5, 0.5, 0.5]

# Calculate average score for reference
average_score = sum(filtered_scores) / len(filtered_scores)
print(f"Average filtered score: {average_score}")

# Normalize scores for potential curve (not used in final calculation)
normalized = [score / 100 for score in filtered_scores]

# Define actual weights for each score
weights = [0.2, 0.3, 0.15, 0.25, 0.1]

# Slice weights to match number of scores
weights = weights[:len(filtered_scores)]

# Calculate final weighted score
total_score = calculate_final_score(filtered_scores, weights)
print(f"Result: {total_score}")