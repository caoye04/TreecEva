def calculate_similarity(a, b):
    return sum(1 for x, y in zip(a, b) if x == y)

# Simulate ranking comparison with weighted scoring
def calculate_final_score(ranks, weight_map):
    base_scores = []
    temp_offset = 0
    
    for i, (rank, weight) in enumerate(zip(ranks, weight_map.values())):
        adjusted = (rank + i) * weight
        base_scores.append(adjusted)
        temp_offset += rank % 2

    # Dummy transformation - irrelevant to final result
    transformed = [x * 0.95 for x in base_scores if x > 5]
    noise_correction = sum(transformed) / len(transformed) if transformed else 0

    # Actual score computation
    raw_total = sum(base_scores)
    penalty = 0
    
    for idx, val in enumerate(base_scores):
        if idx % 2 == 0 and val > 10:
            penalty += val * 0.1

    # Secondary fake metric (distraction)
    average_rank = sum(ranks) / len(ranks)
    stability_index = 0
    for j in range(len(ranks) - 1):
        stability_index += abs(ranks[j] - ranks[j+1])
    normalized_stability = stability_index / (len(ranks) - 1) if len(ranks) > 1 else 0

    # Final calculation - only depends on raw_total and penalty
    final_value = raw_total - penalty - noise_correction * 0  # noise_correction has no effect due to * 0

    return int(final_value)

# Input data
rank_data = [3, 7, 2, 8, 5]
weights = {'w1': 1.2, 'w2': 0.8, 'w3': 1.5, 'w4': 0.6, 'w5': 1.0}

# Irrelevant preprocessing (distractor)
duplicate_check = {x: rank_data.count(x) for x in set(rank_data)}
sorted_ranks = sorted(enumerate(rank_data), key=lambda x: x[1], reverse=True)

# Unused helper function (dead code path)
def validate_rank_integrity(data):
    return all(isinstance(x, int) and 1 <= x <= 10 for x in data)

# Unused variables
threshold = 4.5
scaling_factor = 1.05
buffer_zone = [0] * len(rank_data)

# Key execution point
final_score = calculate_final_score(rank_data, weights)
print(f"Result: {final_score}")