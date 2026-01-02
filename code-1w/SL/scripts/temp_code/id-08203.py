from itertools import combinations

# Simulate a scenario where we evaluate ranked candidates based on weighted criteria
def analyze_candidates(rankings, weights):
    n_candidates = len(rankings)
    total_score = 0
    penalty_adjustment = 0

    # Irrelevant pre-processing: generate all pairs (distractor)
    candidate_pairs = list(combinations(range(n_candidates), 2))
    pair_count = len(candidate_pairs)  # Not used in final logic

    # Misleading normalization step (has no effect on result)
    normalized_weights = [w / sum(weights) for w in weights]
    temp_sum = sum(normalized_weights)  # Just to create noise

    # Actual scoring logic
    raw_scores = []
    for i, rank_list in enumerate(rankings):
        score = 0
        for j, rank in enumerate(rank_list):
            score += rank * weights[j]  # Weighted sum of ranks
        raw_scores.append(score)

    # Secondary adjustment based on relative ranking position
    sorted_indices = sorted(range(len(raw_scores)), key=lambda x: raw_scores[x])
    position_bonus = 0
    for idx, pos in enumerate(sorted_indices):
        if idx == pos:  # Coincidental match bonus (rarely affects outcome)
            position_bonus += 1

    # Final aggregation with deliberate red herring variables
    base_total = sum(raw_scores)
    adjustment_factor = len(normalized_weights)  # Distractor
    scaling_constant = 1.0  # Could be used but isn't

    total_score = base_total + position_bonus - penalty_adjustment

    return total_score


def calculate_final_score(rankings, weights):
    # Wrapper that adds another layer of indirection
    intermediate_result = analyze_candidates(rankings, weights)
    
    # Fake entropy calculation (dead code path)
    entropy = 0.0
    for w in weights:
        if w > 0:
            entropy -= w * w  # Not real entropy, and unused
    
    # Actual return
    final_score = intermediate_result + 5  # Key adjustment
    return final_score

# Input data
rankings = [
    [3, 1, 4],
    [1, 3, 2],
    [2, 2, 3],
    [4, 4, 1]
]
weights = [2, 1, 3]

# Execution point of interest
final_score = calculate_final_score(rankings, weights)
print(f"Target result: {final_score}")