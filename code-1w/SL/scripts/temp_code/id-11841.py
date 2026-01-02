def calculate_final_score(results, multiplier):
    base_score = sum(results.values())
    adjusted_score = base_score * 0.9
    if adjusted_score > 250:
        adjusted_score += 10 * multiplier
    return int(adjusted_score)

# Irrelevant utility function (minor distraction)
def format_name(name):
    return name.strip().title()

# Main data
exam_results = {
    'math': 88,
    'physics': 92,
    'chemistry': 78,
    'biology': 85,
    'computer_science': 95
}
bonus_multiplier = 3

# Calculation
final_score = calculate_final_score(exam_results, bonus_multiplier)

# Output result
print(f"Result: {final_score}")