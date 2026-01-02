def calculate_performance(base, tweaks):
    adjusted_base = base * 0.85
    modifiers = [val * 0.1 for val in tweaks if val > 0]
    bonus = sum(modifiers) if len(modifiers) > 2 else 0.0
    penalty = 10 if any(x < 0 for x in tweaks) else 0
    return int(adjusted_base + bonus - penalty)

baseline = 120
adjustments = [5, 15, -3, 8, 12]
temp_var_ignore = [x * 2 for x in adjustments]  # Irrelevant computation (distractor)
initial_estimate = baseline + sum(adjustments)  # Distractor variable
final_score = calculate_performance(baseline, adjustments)
print(f"Target result: {final_score}")