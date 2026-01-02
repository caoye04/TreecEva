def calculate_final_score(data, mult):
    base_scores = [d['rank'] for d in data]
    offsets = {i: (idx % 4) - 1 for i, idx in enumerate(base_scores)}
    adjusted = [base_scores[i] + offsets[i] for i in range(len(base_scores))]
    total = sum(adjusted)
    factor = 1.5 if any(x > 10 for x in base_scores) else mult
    return int(total * factor)

bonus_multiplier = 2.0
rank_data = [
    {'name': 'Alice', 'rank': 8},
    {'name': 'Bob', 'rank': 12},
    {'name': 'Charlie', 'rank': 7},
    {'name': 'Diana', 'rank': 15}
]

# Extraneous but harmless variable
interim_result = sum(d['rank'] for d in rank_data)

final_score = calculate_final_score(rank_data, bonus_multiplier)
print(f"Result: {final_score}")