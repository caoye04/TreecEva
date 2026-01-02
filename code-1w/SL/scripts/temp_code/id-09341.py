def calculate_final_score(ranks):
    filtered = [r for r in ranks if r > 0]
    weighted = list(map(lambda x: x * 1.5, filtered))
    adjusted = [w - 0.5 for w in weighted]
    return int(sum(adjusted))

# Irrelevant distraction variables
initial_offset = 10
placeholder_data = [0, -1, -2]

rank_list = [4, -3, 2, 0, 5]
final_score = calculate_final_score(rank_list)
print(f"Result: {final_score}")