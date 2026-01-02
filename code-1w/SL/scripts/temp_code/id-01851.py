from collections import defaultdict

# Student grades and attendance data
students = [
    {'name': 'Alice', 'grade': 85, 'attendance_rate': 0.92},
    {'name': 'Bob', 'grade': 76, 'attendance_rate': 0.85},
    {'name': 'Charlie', 'grade': 90, 'attendance_rate': 0.96},
    {'name': 'Diana', 'grade': 95, 'attendance_rate': 0.88}
]

# Bonus points based on attendance tiers
bonus_map = defaultdict(int)
bonus_map[0.95] = 10
bonus_map[0.90] = 5
bonus_map[0.85] = 2

# Irrelevant distraction: unused function
def unused_helper(x):
    return x * 2

# Track performance categories
performance_tiers = set()
for s in students:
    if s['grade'] >= 90:
        performance_tiers.add('excellent')
    elif s['grade'] >= 80:
        performance_tiers.add('good')
    else:
        performance_tiers.add('needs_improvement')

# Calculate final score as average grade + max bonus from attendance
total_grade = 0
max_bonus = 0
for s in students:
    total_grade += s['grade']
    # Determine bonus based on attendance rate (rounded to nearest threshold)
    threshold = round(s['attendance_rate'], 2)
    max_bonus = max(max_bonus, bonus_map[threshold])

average_grade = total_grade / len(students)

# Apply maximum bonus found across all students
final_score = average_grade + max_bonus

# Output result
print(f"Result: {final_score}")