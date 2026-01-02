def calculate_total(grades, extra):
    base = sum([x for x in grades if x >= 50])
    adjustment = lambda x: x * 1.1 if base > 200 else x * 1.05
    return int(adjustment(base + extra))

# Irrelevant auxiliary data (minimal distraction)
student_id = "S7890"
course = "CS101"

# Core data for computation
marks = [75, 80, 45, 90, 55]
bonus = 10

# Key computation step
final_score = calculate_total(marks, bonus)

print(f"Result: {final_score}")