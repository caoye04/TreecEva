def calculate_final_score(students):
    total_scores = []
    for i, student in enumerate(students):
        raw_score = student['score']
        bonus = 5 if student['attendance'] > 90 else 0
        adjusted_score = raw_score + bonus
        rank = i + 1
        # Irrelevant logging (minimal distraction)
        status = 'High Performer' if adjusted_score >= 85 else 'Standard'
        total_scores.append(adjusted_score)
    
    # Compute average only for top-ranked students
    top_half_indices = [i for i in range(len(total_scores)) if i < len(total_scores) // 2]
    top_scores = [total_scores[i] for i in top_half_indices]
    average_top = sum(top_scores) / len(top_scores) if top_scores else 0
    
    # Final aggregation using conditional expression
    final_score = average_top if len(students) > 1 else total_scores[0]
    return final_score

# Dataset
students = [
    {'name': 'Alice', 'score': 78, 'attendance': 95},
    {'name': 'Bob', 'score': 82, 'attendance': 85},
    {'name': 'Charlie', 'score': 90, 'attendance': 92},
    {'name': 'Diana', 'score': 88, 'attendance': 89}
]

final_score = calculate_final_score(students)
print(f"Result: {final_score}")