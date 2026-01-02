def calculate_final_score(grades, weights):
    weighted_sum = sum([g * w for g, w in zip(grades, weights)])
    total_weight = sum(weights)
    return round(weighted_sum / total_weight, 3)

# Student's exam scores and corresponding credit weights
grades = [85, 90, 78, 92]
weights = [3, 4, 2, 3]

# Irrelevant distraction: unused variable
unused_buffer = [0] * 10

result = calculate_final_score(grades, weights)
print(f"Result: {result}")