def calculate_final_score(results):
    base_score = 0
    bonus_multiplier = 1
    for category, score in results.items():
        if score < 50:
            continue
        adjusted = score * (2 if category.startswith('advanced') else 1)
        base_score += adjusted
        if base_score > 200:
            bonus_multiplier = 1.5
    return int(base_score * bonus_multiplier)

# Irrelevant auxiliary data (minimal distraction)
temp_data = [0] * 5
offset = 10

results = {
    'basic_algebra': 65,
    'advanced_calculus': 72,
    'intermediate_stats': 48,
    'advanced_physics': 80,
    'basic_chemistry': 55
}

final_score = calculate_final_score(results)
print(f"Result: {final_score}")