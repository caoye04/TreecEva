def calculate_similarity(a, b):
    return abs(a - b) / max(a, b)

rank_data = [10, 25, 30, 45, 50]
binary_flags = [1, 0, 1, 1, 0]
bonus_multiplier = 1.75

# Irrelevant similarity matrix computation (distractor)
similarity_matrix = []
for i, val1 in enumerate(rank_data):
    row = []
    for j, val2 in enumerate(rank_data):
        if i != j:
            row.append(calculate_similarity(val1, val2))
        else:
            row.append(0.0)
    similarity_matrix.append(row)

# Tracking cumulative offset (semi-relevant but not used directly)
cumulative_offset = 0
for idx, (rank, flag) in enumerate(zip(rank_data, binary_flags)):
    if flag:
        cumulative_offset += rank * 0.1

# Actual core logic with distraction from above
adjusted_ranks = []
for rank in rank_data:
    if rank > 20:
        adjusted_ranks.append(rank * 0.9)
    else:
        adjusted_ranks.append(rank)

# Secondary adjustment based on position
position_adjusted = []
for i, adj_rank in enumerate(adjusted_ranks):
    if i % 2 == 0:
        position_adjusted.append(adj_rank * 1.1)
    else:
        position_adjusted.append(adj_rank * 0.95)

# Aggregation
raw_total = sum(position_adjusted)
penalty = len([r for r in rank_data if r < 30]) * 2.5

# Final score calculation
def calculate_final_score(data, mult):
    base = sum(data) * mult
    modifier = 0
    for i, val in enumerate(data):
        if i % 3 == 0:
            modifier += val * 0.05
    return int(base - penalty + modifier)

final_score = calculate_final_score(position_adjusted, bonus_multiplier)
print(f"Result: {final_score}")