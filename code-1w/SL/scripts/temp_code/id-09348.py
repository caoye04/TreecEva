def calculate_performance(base, data):
    adjusted = [val - base for val in data if isinstance(val, (int, float))]
    valid_count = sum(1 for x in adjusted if x > 0)
    bonus = 1.5 if valid_count >= 3 else 0.5
    total = sum(adjusted) * bonus
    outlier_check = any(abs(x) > 20 for x in adjusted)
    penalty = 10 if outlier_check else 0
    return total - penalty

baseline = 50
readings = [65, 48, 70, 52, 80]

# Irrelevant utility function (distractor)
def normalize_values(vals):
    max_val = max(vals)
    return [v / max_val for v in vals]

final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")