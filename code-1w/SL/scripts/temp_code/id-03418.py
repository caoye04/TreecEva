def process_student_data(records):
    # Irrelevant preprocessing: normalize names (not used in final calculation)
    normalized_names = [name.strip().title() for name, _ in records]
    
    grades = []
    weights = []
    temp_max = -float('inf')
    
    # Extract and scale grades, compute auxiliary stats
    for i, (name, subject_grades) in enumerate(records):
        avg_grade = sum(subject_grades) / len(subject_grades)
        scaled = avg_grade * 0.85  # arbitrary scaling factor
        if avg_grade > temp_max:
            temp_max = avg_grade
        
        # Only use every other record for actual weighting
        if i % 2 == 0:
            grades.append(round(scaled))
            weight = len(subject_grades) + i
            weights.append(weight)

    # Dead code path: unused statistical summary
    summary_stats = {
        'peak': temp_max,
        'count': len(grades),
        'over_75': sum(1 for g in grades if g > 75)
    }

    # Distractor computation: harmonic mean (not used)
    h_mean = 0
    if grades:
        reciprocals = [1/g if g != 0 else 0 for g in grades]
        h_mean = len(grades) / sum(reciprocals) if sum(reciprocals) != 0 else 0

    def calculate_rating(g_list, w_list):
        total_weighted = 0
        total_weight = 0
        for idx, (g, w) in enumerate(zip(g_list, w_list)):
            adjustment = 1 + (idx * 0.1)
            total_weighted += g * w * adjustment
            total_weight += w * adjustment
        return round(total_weighted / total_weight) if total_weight != 0 else 0

    # Key statement
    final_score = calculate_rating(grades, weights)
    
    # Print required output
    print(f"Result: {final_score}")
    
    return final_score

# Input data
student_records = [
    (" alice ", [88, 92, 85]),
    (" bob ", [76, 81, 79]),
    (" charlie ", [90, 87, 93]),
    (" diana ", [83, 85, 80])
]

# Execute
process_student_data(student_records)