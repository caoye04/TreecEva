def calculate_final_score(rankings):
    base_scores = [10 - rank for rank in rankings]
    weighted_scores = [score * (index + 1) for index, score in enumerate(base_scores)]
    filtered_scores = [score for score in weighted_scores if score > 15]
    return sum(filtered_scores) // len(filtered_scores) if filtered_scores else 0

# Initial contestant rankings
rankings = [1, 3, 2, 5, 4]

# Irrelevant distraction: unused variable
initial_total = sum(rankings)

final_score = calculate_final_score(rankings)
print(f"Target result: {final_score}")