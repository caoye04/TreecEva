from collections import defaultdict

def calculate_final_score(data):
    base_score = sum(data['grades'])
    bonus = len(data['achievements']) * 2
    penalty = data['absences'] // 3
    return base_score + bonus - penalty

# Simulate student performance data
student_data = defaultdict(int, {
    'grades': [85, 90, 78, 92],
    'achievements': ['science_fair', 'math_olympiad'],
    'absences': 5
})

# Calculate final academic score
total_score = calculate_final_score(student_data)
print(f"Result: {total_score}")