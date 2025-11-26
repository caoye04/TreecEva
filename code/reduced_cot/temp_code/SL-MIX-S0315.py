grade_counts = {"A": 12, "B": 8, "C": 5}
points_per_grade = {"A": 4, "B": 3, "C": 2}
student_names = ["Alice", "Bob", "Charlie", "Diana"]
attendance_records = {name: True for name in student_names}

final_score = grade_counts.get("A", 0) * points_per_grade["A"] + grade_counts.get("B", 0) * points_per_grade["B"]
print(f"Result: {final_score}")