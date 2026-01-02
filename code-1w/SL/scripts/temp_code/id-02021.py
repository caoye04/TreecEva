def calculate_adjusted_average(grades, extra):
    total = sum(grades)
    count = len(grades)
    average = total / count if count > 0 else 0
    
    # Irrelevant transformation (distractor)
    normalized = [round((g - average) ** 2, 2) for g in grades]
    variance_proxy = sum(normalized) / count if count > 0 else 0
    
    # Semi-relevant filtering (only some elements matter)
    filtered = [g for g in grades if g >= average]
    adjustment = len(filtered) * 0.5
    
    # String-based logic to track grade distribution (partly irrelevant)
    letter_grades = ''.join(["A" if g >= 90 else "B" if g >= 80 else "C" for g in grades])
    a_count = letter_grades.count("A")
    b_count = letter_grades.count("B")
    c_count = letter_grades.count("C")
    distribution_hint = f'{a_count}A-{b_count}B-{c_count}C'
    
    # Core computation path
    base_score = sum(filtered) + adjustment
    applied_bonus = base_score * (1 + extra / 100)
    penalty = 0
    if 'C' in distribution_hint:
        penalty = 2.5
    
    final_value = applied_bonus - penalty
    return final_value

# Main execution context
raw_input = "85,92,78,96,88"
grade_list = list(map(int, raw_input.split(',')))
bonus_factor = 5

# Dead code path - not used but adds cognitive load
if len(grade_list) > 10:
    grade_list = grade_list[:10]
    scale_factor = 1.1
else:
    scale_factor = 1.0

# Unused statistical variables (distractors)
deviation_estimate = sum([abs(g - sum(grade_list)/len(grade_list)) for g in grade_list])
entropy_proxy = deviation_estimate / len(grade_list) if grade_list else 0

# Key statement
final_score = calculate_adjusted_average(grade_list, bonus_factor)
print(f"Result: {final_score}")