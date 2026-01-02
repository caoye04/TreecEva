def calculate_final_score(grades, weight_map):
    weighted_sum = 0
    total_weight = 0
    for (subject, score), (i, (w_name, w_value)) in zip(grades.items(), enumerate(weight_map.items())):
        if subject == w_name:
            weighted_sum += score * w_value
            total_weight += w_value
    return round(weighted_sum / total_weight, 3) if total_weight > 0 else 0

# Irrelevant auxiliary data (minor distraction)
student_data = {'name': 'Alex', 'age': 20, 'major': 'CS'}
temp_grades = {'math': 85, 'physics': 90, 'chemistry': 78}

# Relevant input data
grades = {'math': 88, 'physics': 92, 'english': 85, 'history': 76}
weights = {'math': 4, 'physics': 5, 'english': 3, 'history': 2}

# Computation
scale_factor = 1.0  # Unused variable (minimal interference)
adjusted_weights = {k: v * scale_factor for k, v in weights.items()}
total_score = calculate_final_score(grades, adjusted_weights)
print(f"Result: {total_score}")