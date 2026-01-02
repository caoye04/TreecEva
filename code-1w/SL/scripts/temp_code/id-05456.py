def calculate_total(scores, adjustment_fn):
    base_total = 0
    penalty = 0
    for subject, score in scores.items():
        if score < 50:
            penalty += 10
        base_total += score
    
    # Apply bonus only if no penalties
    if penalty == 0:
        base_total = adjustment_fn(base_total)
    
    adjusted_total = base_total - penalty
    return adjusted_total

# Student marks in various subjects
marks_dict = {
    'math': 85,
    'physics': 76,
    'chemistry': 90,
    'biology': 88,
    'english': 92
}

# Irrelevant distraction variable
average_temp = 23.5

# Bonus increases total by 5% using lambda
bonus_lambda = lambda x: int(x * 1.05)

# Calculation entry point
final_score = calculate_total(marks_dict, bonus_lambda)

# Print result as required
print(f"Result: {final_score}")