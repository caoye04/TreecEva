def calculate_performance(base, eff, thresh):
    adjustment = 1.5 if eff > thresh else 0.8
    bonus = 10 if base >= 80 and eff >= 90 else 5
    return int((base * adjustment) + bonus)

baseline = 88
efficiency = 92
threshold = 85

# Irrelevant variables (minor distractions for intervention level 5)
dummy_flag = False
temp_data = [1, 2, 3]
placeholder_value = "N/A"

final_score = calculate_performance(baseline, efficiency, threshold)
print(f"Target result: {final_score}")