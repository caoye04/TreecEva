from collections import Counter

def calculate_final_score(results):
    # Count occurrences of each grade
    grade_counts = Counter(results)
    
    # Base score calculation: A=4, B=3, C=2, D=1, F=0
    grade_points = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
    total_points = 0
    for grade in results:
        total_points += grade_points.get(grade, 0)
    
    # Apply curve: if more than half are A's, add bonus 2 points
    if grade_counts['A'] > len(results) / 2:
        total_points += 2
    
    # Penalty for any F: subtract 1 point per F (max 5)
    total_points -= min(grade_counts['F'], 5)
    
    return total_points

# Irrelevant auxiliary function (minor distraction)
def format_grades_display(grades):
    return ', '.join([g.lower() for g in grades]).title()

# Main data
exam_results = ['A', 'A', 'B', 'A', 'C', 'F', 'A']

# Calculation
final_score = calculate_final_score(exam_results)

# Output result
print(f"Result: {final_score}")