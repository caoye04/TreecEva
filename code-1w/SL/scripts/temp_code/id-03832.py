from itertools import permutations

# Simulate candidate evaluation in a competitive coding contest

def calculate_entropy(seq):
    from collections import Counter
    freq = [v / len(seq) for v in Counter(seq).values()]
    entropy = -sum(f * __import__('math').log2(f) for f in freq if f > 0)
    return round(entropy, 4)

def normalize_scores(raw_scores):
    min_val, max_val = min(raw_scores), max(raw_scores)
    if min_val == max_val:
        return [1.0] * len(raw_scores)
    return [(x - min_val) / (max_val - min_val) for x in raw_scores]

def evaluate_performance(ranks, threshold):
    # Core logic: count how many rank positions are below threshold after offset
    adjusted_ranks = [r + 1 for r in ranks]  # 1-indexed adjustment
    passed = sum(1 for ar in adjusted_ranks if ar <= threshold)
    bonus = 2 if passed >= 3 else 0
    return passed * 5 + bonus

def main():
    # Initial data: mock rankings from preliminary round
    candidate_ids = ['A', 'B', 'C', 'D']
    raw_rank_points = [88, 76, 92, 70]
    
    # Normalize scores for entropy analysis (distractor path)
    norm_scores = normalize_scores(raw_rank_points)
    score_entropy = calculate_entropy([round(s, 2) for s in norm_scores])
    
    # Generate all possible ranking permutations (combinatorics focus)
    base_sequence = [0, 1, 2, 3]  # index-based ranking
    all_permutations = list(permutations(base_sequence))
    
    # Misleading computation: analyze permutation entropy (irrelevant to final result)
    perm_entropies = []
    for perm in all_permutations[:10]:  # only sample first 10
        p_entropy = calculate_entropy(perm)
        perm_entropies.append(p_entropy)
    avg_perm_entropy = sum(perm_entropies) / len(perm_entropies) if perm_entropies else 0
    
    # Key data: use specific permutation based on sum criterion
    target_sum = 6
    selected_perm = None
    for p in all_permutations:
        if sum(p) == target_sum and p[0] == 0:  # constraint for uniqueness
            selected_perm = p
            break
    
    # Secondary distraction: simulate feedback weights
    feedback_weights = [0.1, 0.3, 0.4, 0.2]
    weighted_feedback = sum(norm_scores[i] * feedback_weights[i] for i in range(4))
    
    # Critical threshold logic
    base_threshold = 3
    if score_entropy > 1.8:
        base_threshold += 1
    
    # Execution point: evaluate performance on selected permutation
    final_score = evaluate_performance(selected_perm, base_threshold)
    
    # Dead code branch (never executed but adds cognitive load)
    if False:
        debug_log = {}
        for idx, val in enumerate(selected_perm):
            debug_log[f'entry_{idx}'] = {
                'raw': val,
                'squared': val ** 2,
                'adjusted': val + 5
            }
    
    print(f"Result: {final_score}")
    return final_score

if __name__ == '__main__':
    main()