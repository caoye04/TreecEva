def calculate_final_score(grades, bonus_func):
    base_score = sum(grades) // len(grades)
    bonus = bonus_func(base_score)
    return base_score + bonus

student_grades = [85, 92, 78, 96, 88]
bonus_function = lambda score: 5 if score >= 85 else 0

final_score = calculate_final_score(student_grades, bonus_function)
print(f"Target result: {final_score}")