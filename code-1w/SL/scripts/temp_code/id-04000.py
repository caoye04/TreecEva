students = ['Alice', 'Bob', 'Charlie', 'Diana', 'Evan']
exam_scores = [85, 92, 78, 96, 83]
attendance_rate = [0.94, 0.88, 0.91, 0.97, 0.90]

# Determine passing records based on score >= 80 and attendance >= 0.85
passing_records = set()
for i in range(len(students)):
    if exam_scores[i] >= 80 and attendance_rate[i] >= 0.85:
        passing_records.add(students[i])

# Honor roll: score >= 90
honor_roll = set()
for i in range(len(students)):
    if exam_scores[i] >= 90:
        honor_roll.add(students[i])

base_reward = 50
bonus_factor = 3
final_score = len(passing_records & honor_roll) * bonus_factor
print(f"Result: {final_score}")