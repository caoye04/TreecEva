def calculate_final_score(name, score, deductions):
    adjusted = score - sum(deductions)
    if len(name.strip()) == 0:
        multiplier = 1
    else:
        multiplier = 2 if name.upper().endswith('X') else 1.5
    return int(adjusted * multiplier)

raw_score = 89
penalties = [5, 3]
user_name = "Alex X"

# Irrelevant string operation (minor distraction)
title_case_name = user_name.title()

final_score = calculate_final_score(user_name, raw_score, penalties)
print(f"Result: {final_score}")