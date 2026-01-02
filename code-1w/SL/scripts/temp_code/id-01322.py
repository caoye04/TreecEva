from collections import defaultdict

def calculate_total(scores, modifiers):
    base = sum(scores)
    adjustment_factor = 1.0
    
    # Apply conditional multipliers based on subject performance
    if scores['math'] > 85:
        adjustment_factor += 0.1
    if scores['science'] >= 90:
        adjustment_factor += 0.15
    
    temp_result = base * adjustment_factor
    
    # Additional flat bonus from external adjustments
    bonus = sum(modifiers.values())
    final = temp_result + bonus
    
    return int(final)

# Student academic marks
marks = {
    'math': 92,
    'science': 88,
    'english': 76,
    'history': 81
}

# Adjustment factors (e.g., extra credit, participation)
adjustments = defaultdict(int)
adjustments['project'] = 5
adjustments['attendance'] = 3

irrelevant_counter = 0
for subject in marks:
    if marks[subject] < 80:
        irrelevant_counter += 1

# Compute final evaluated score
final_score = calculate_total(marks, adjustments)

print(f"Result: {final_score}")