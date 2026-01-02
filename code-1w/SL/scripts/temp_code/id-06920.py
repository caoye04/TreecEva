def calculate_final_score(students, threshold):
    filtered_names = [name for name in students.keys() if len(name) > 5]
    scores = []
    
    for name in filtered_names:
        raw_score = students[name]
        adjusted_score = raw_score * 0.9 if raw_score > threshold else raw_score * 1.1
        scores.append(adjusted_score)
    
    average = sum(scores) / len(scores) if scores else 0
    bonus = 5 if len(filtered_names) >= 3 else 0
    final_score = average + bonus
    return final_score

# Dataset representing student names and their raw scores
students = {
    'Alexander': 88,
    'Sam': 92,
    'Gabriella': 75,
    'Tom': 81,
    'Nathaniel': 90
}
threshold = 85

final_score = calculate_final_score(students, threshold)
print(f"Result: {final_score}")