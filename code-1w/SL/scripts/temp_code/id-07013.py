from collections import Counter

def calculate_final_score(ranks, weight_map):
    score = 0
    for rank, count in ranks.items():
        if rank in weight_map:
            score += weight_map[rank] * count
    return score

# Simulate user ranking data from survey responses
responses = [1, 2, 2, 3, 3, 3, 4, 4, 5]
rank_counter = Counter(responses)

# Weighting system for ranked preferences
weights = {1: 10, 2: 8, 3: 6, 4: 4, 5: 2}

temp_factor = 1.5  # unused distractor variable
intermediate = sum(rank_counter.keys())  # minor distraction

total_score = calculate_final_score(rank_counter, weights)
print(f"Result: {total_score}")