def calculate_final_score(names, scores):
    processed_names = {k.lower().capitalize(): v * 1.1 for k, v in names.items()}
    adjusted_scores = [round(s * 0.95) for s in scores if s > 50]
    bonus = len(processed_names) * 5
    total_score = sum(adjusted_scores) + bonus
    return total_score

# Irrelevant auxiliary variable (minor distraction)
user_data = {'Alice': 85, 'Bob': 78, 'charlie': 92}
score_list = [88, 76, 55, 91, 43]

# Key computation
total_score = calculate_final_score(user_data, score_list)
print(f"Result: {total_score}")