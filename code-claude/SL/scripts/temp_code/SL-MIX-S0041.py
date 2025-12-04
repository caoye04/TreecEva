# Calculate student's weighted average score across multiple exams

# Exam weights (midterm, quiz, project, final)
exam_weights = [0.25, 0.15, 0.30, 0.30]

# Student scores for each exam component (out of 100)
student_scores = [85, 92, 78, 88]

# Additional class statistics (not used in calculation)
class_size = 32
class_averages = [82, 88, 75, 84]

# Calculate the weighted score
weighted_score = sum(weight * score for weight, score in zip(exam_weights, student_scores))

# Round to nearest integer for final grade
final_grade = round(weighted_score)

# Determine letter grade (not used in answer)
letter_grade = ''
if weighted_score >= 90:
    letter_grade = 'A'
elif weighted_score >= 80:
    letter_grade = 'B'
elif weighted_score >= 70:
    letter_grade = 'C'
elif weighted_score >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

print(f"Result: {weighted_score}")