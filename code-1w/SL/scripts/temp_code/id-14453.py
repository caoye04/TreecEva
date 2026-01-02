def calculate_performance(base, mods):
    adjustment_factor = sum(mods) / len(mods) if mods else 0
    enhanced = base * (1 + adjustment_factor)
    penalty = 0.1 if base < 50 else 0.05
    return round(enhanced * (1 - penalty))

baseline = 78
adjustments = [0.08, -0.02, 0.11, 0.03]

# Irrelevant tracking variables (minimal distraction)
current_status = "active"
last_updated = "2023-09-15"

final_score = calculate_performance(baseline, adjustments)
print(f"Target result: {final_score}")