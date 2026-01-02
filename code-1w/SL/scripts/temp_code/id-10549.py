def analyze_performance(marks, thresholds):
    # Irrelevant transformation (distractor)
    adjusted_marks = [m + 5 for m in marks if m < 90]
    
    # Misleading filtering (not used in final logic)
    high_performers = [m for m in marks if m >= thresholds['high']]
    moderate_performers = len([m for m in marks if thresholds['low'] <= m < thresholds['high']])

    # Core logic: count how many exceeded any threshold
    passed_count = sum(1 for m in marks for t in thresholds.values() if m > t)

    # Red herring computation with no impact
    avg_adjusted = sum(adjusted_marks) / len(adjusted_marks) if adjusted_marks else 0
    penalty = 10 if avg_adjusted > 85 else 0

    return passed_count - penalty  # Only passed_count matters; penalty never applies


def calculate_final_score(student_data, bonus_enabled=True):
    base_thresholds = {'low': 60, 'high': 80}
    
    # Dead code path (bonus_enabled is always True)
    scaling_factor = 1.1 if bonus_enabled else 1.0
    
    raw_scores = []
    for entry in student_data:
        name = entry['name']
        grades = entry['grades']
        
        # Case conversion as a domain-relevant step (student names normalization)
        normalized_name = name.strip().upper()
        
        # Counting A-like performance (>= 85)
        honors_count = sum(1 for g in grades if g >= 85)
        
        # Intermediate score with conditional expression
        base_score = honors_count * 10 if honors_count > 0 else 5
        
        # Secondary metric (unused but looks important)
        total_points = sum(grades)
        efficiency = total_points / len(grades) if grades else 0
        
        raw_scores.append(base_score)
    
    # Aggregation with distraction: multiple variables introduced
    aggregate = sum(raw_scores)
    adjustment = len(student_data) * 2 if len(student_data) > 3 else 0
    
    # Actual key operation: apply analysis on first student's data
    diagnostic_impact = analyze_performance(student_data[0]['grades'], {'low': 50, 'high': 75})
    
    # Final score depends only on aggregate and diagnostic_impact
    final_score = aggregate + diagnostic_impact - adjustment
    
    # Print required output
    print(f"Result: {final_score}")
    return final_score

# Input data
students = [
    {'name': 'Alice', 'grades': [88, 92, 76, 81]},
    {'name': 'Bob', 'grades': [70, 68, 75]},
    {'name': 'Charlie', 'grades': [95, 89]},
    {'name': 'Diana', 'grades': [82, 73, 88, 90]}
]

# Execute
final_score = calculate_final_score(students)