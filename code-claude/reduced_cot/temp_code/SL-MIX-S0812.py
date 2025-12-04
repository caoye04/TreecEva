import itertools

def calculate_weighted_average(scores, weights):
    """Calculate weighted average of scores."""
    total_weighted = 0
    total_weights = 0
    
    # Process scores and weights using zip
    for score, weight in zip(scores, weights):
        total_weighted += score * weight
        total_weights += weight
    
    # Avoid division by zero
    if total_weights == 0:
        return 0
    
    return round(total_weighted / total_weights, 2)

# Student exam data
student_scores = [85, 92, 78, 90]
student_attendance = [True, True, False, True]  # Not used in final calculation

# Define weights for different exams
weights = [0.2, 0.3, 0.15, 0.35]

# Some preprocessing of data (not relevant to final result)
bonus_points = [5, 0, 10, 3]  # Potential bonus points
penalty_points = [2, 1, 8, 0]  # Potential penalty points

# Apply bonuses and penalties based on complex conditions
for i, (attendance, score) in enumerate(zip(student_attendance, student_scores)):
    if attendance and score > 80:  # This condition is checked but not used
        potential_bonus = bonus_points[i] // 2
    else:
        potential_bonus = 0
    
    # This adjusted_score is calculated but not used in the final calculation
    adjusted_score = score + potential_bonus - penalty_points[i] // 2

# Track number of high scores (not used in final calculation)
high_score_count = sum(1 for score in student_scores if score >= 85)

# Create pairs of scores and weights (not directly used)
score_weight_pairs = list(zip(student_scores, weights))

# Compute some alternative statistics (not used in final calculation)
min_score = min(student_scores)
max_score = max(student_scores)
score_range = max_score - min_score

# Calculate the weighted average (this is the key operation)
final_score = calculate_weighted_average(student_scores, weights)

# Generate a letter grade (not relevant to the question)
letter_grade = ''
if final_score >= 90:
    letter_grade = 'A'
elif final_score >= 80:
    letter_grade = 'B'
elif final_score >= 70:
    letter_grade = 'C'
elif final_score >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

print(f"Result: {final_score}")