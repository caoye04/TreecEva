def analyze_performance(marks):
    passing = list(filter(lambda x: x >= 50, marks))
    ranked = sorted(passing, reverse=True)
    categories = {i: score for i, score in enumerate(ranked)}
    
    # Irrelevant distractor variables (minimal interference)
    avg_mark = sum(marks) / len(marks)
    max_possible = 100
    
    if len(ranked) > 3:
        top_three = [ranked[i] for i in range(3)]
        mid_range = ranked[1:-1]
        filtered_scores = [s for s in mid_range if s > avg_mark]
    else:
        filtered_scores = ranked
    
    threshold_score = filtered_scores[-1]
    return threshold_score

# Input data
student_marks = [45, 76, 85, 52, 91, 68, 47]
result = analyze_performance(student_marks)
print(f"Result: {result}")