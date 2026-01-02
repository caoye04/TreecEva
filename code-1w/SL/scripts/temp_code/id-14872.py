def calculate_final_score(results, multiplier):
    base_score = sum(results.values())
    adjusted_score = base_score * 0.95
    if adjusted_score > 80:
        adjusted_score += multiplier * 2
    return round(adjusted_score, 2)

# Student exam results by subject
cexam_results = {
    'mathematics': 23,
    'physics': 19,
    'chemistry': 22,
    'biology': 18,
    'literature': 20
}
bonus_multiplier = 3

# Irrelevant string operation (minor distraction)
dummy_text = "Processing grades..."
dummy_text.upper()

final_score = calculate_final_score(cexam_results, bonus_multiplier)
print(f"Result: {final_score}")