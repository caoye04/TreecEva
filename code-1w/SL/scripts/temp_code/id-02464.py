from itertools import combinations

def analyze_performance(grades, weights):
    # Irrelevant transformation (distractor)
    normalized = [g / max(grades) for g in grades]
    weighted_sum = sum(g * w for g, w in zip(grades, weights))
    adjustment_factor = len([g for g in grades if g >= 75])  # Count of passing grades
    return weighted_sum + adjustment_factor

def evaluate_candidates(test_scores):
    base_weights = [0.2, 0.3, 0.3, 0.2]
    candidates = []
    
    for score_set in test_scores:
        # Misleading computation: entropy-like measure (not used later)
        total = sum(score_set)
        entropy = sum((s/total) * ((s/total) ** 0.5) for s in score_set if s > 0)
        
        # Relevant logic: boost scores based on consistency
        variance = sum((x - sum(score_set)/len(score_set))**2 for x in score_set) / len(score_set)
        consistency_bonus = 10 if variance < 64 else 5
        
        # Actual performance analysis
        raw_evaluation = analyze_performance(score_set, base_weights)
        adjusted_evaluation = raw_evaluation + (consistency_bonus * 0.8)
        
        candidates.append(adjusted_evaluation)
    
    # Distractor: unused candidate ranking
    ranked = sorted(enumerate(candidates), key=lambda x: x[1], reverse=True)
    top_indices = [i for i, _ in ranked[:2]]
    
    return candidates

def compute_aggregate(data):
    # Generate all possible weight triplets (combinatorics distraction)
    possible_weights = list(combinations(range(1, 6), 3))
    filtered_weights = [w for w in possible_weights if sum(w) == 9]  # Only those summing to 9
    
    # Main logic path
    candidate_evaluations = evaluate_candidates(data)
    
    # Compute aggregate using specific rule
    primary_component = sum(candidate_evaluations)
    secondary_component = max(candidate_evaluations) - min(candidate_evaluations)
    
    # Final adjustment based on bitwise pattern of lengths
    length_xor = len(data) ^ len(candidate_evaluations[0].as_integer_ratio())  # Using float property as red herring
    fluctuation_mask = (secondary_component | 5) & 7
    
    # Key result calculation
    final_value = primary_component - fluctuation_mask + (length_xor & 1)
    
    # Dead code path (never executed)
    if False:
        fallback = sum(sum(ds) for ds in data) // 10
        final_value = fallback
    
    return int(final_value)

# Input data
applicant_data = [
    [85, 78, 92, 88],
    [76, 81, 79, 85],
    [90, 88, 94, 87],
    [82, 75, 80, 84]
]

# Execution point of interest
final_score = compute_aggregate(applicant_data)
print(f"Result: {final_score}")