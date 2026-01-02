student_grades = [
    [85, 90, 78],
    [88, 85, 82],
    [76, 80, 84],
    [90, 92, 88]
]

# Irrelevant distraction: unused variable
unused_threshold = 75

averages = []
for grades in student_grades:
    total = sum(grades)
    avg = total / len(grades)
    averages.append(round(avg, 2))

# Compute final score as highest average
final_score = max(averages)

# Output result
print(f"Result: {final_score}")