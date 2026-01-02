from collections import defaultdict

def calculate_final_score(raw_scores, deductions):
    adjusted = defaultdict(float)
    total_penalty = sum(deductions)
    
    for subject, score in raw_scores.items():
        if score >= 60:
            adjusted[subject] = score - total_penalty * 0.5
        else:
            adjusted[subject] = score - total_penalty * 1.2
    
    final_values = [v for v in adjusted.values() if v > 0]
    result = round(sum(final_values) / len(final_values), 3) if final_values else 0
    return result

# Irrelevant auxiliary data (minimal distraction)
student_data = {'id': 'S9920', 'enrollment_year': 2023}
scores = {'math': 85, 'physics': 72, 'chemistry': 58, 'biology': 90}
penalties = [5, 3, 2]

result = calculate_final_score(scores, penalties)
print(f"Result: {result}")