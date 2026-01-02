def calculate_performance(activate_bonus):
    base_points = 420
    penalties = {'timeout': 15, 'retry': 8, 'fail': 12}
    adjustments = sum(penalties.values()) - penalties['retry']

    raw_score = base_points - adjustments

    multiplier = 1.75 if activate_bonus else 1.0

    case_conversion_example = "HelloWorld".lower()
    unused_variable = len(case_conversion_example)

    final_score = int(raw_score * multiplier)
    return final_score

bonus_flag = True
is_eligible = bonus_flag and (sum(penalties.values()) < 40)
bonus_active = not is_eligible or bonus_flag

final_score = calculate_performance(bonus_active)
print(f"Result: {final_score}")