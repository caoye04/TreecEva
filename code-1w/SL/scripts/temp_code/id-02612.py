from collections import defaultdict

# Simulate student assessment with weighted components
def calculate_total(grades, extra):
    base = sum(grades[cat] for cat in grades)
    adjustment = (lambda x: x * 0.1)(extra)
    return int(base + adjustment)

# Irrelevant distraction: unused variable
placeholder = [0] * 5

# Grading breakdown
evaluation = defaultdict(int)
evaluation['homework'] = 25
evaluation['quiz'] = 20
evaluation['project'] = 35
evaluation['exam'] = 45

bonus_points = 15

final_score = calculate_total(evaluation, bonus_points)
print(f"Result: {final_score}")