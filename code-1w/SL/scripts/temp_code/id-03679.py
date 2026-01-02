from itertools import combinations

# Simulate ranking-based evaluation with weighted aggregation and noise filtering
def analyze_ranks(raw_ranks):
    filtered = [r for r in raw_ranks if r > 0]
    sorted_ranks = sorted(filtered)
    median_rank = sorted_ranks[len(sorted_ranks) // 2]
    
    # Generate all pairs to compute rank dispersion (unused distractor)
    pair_combinations = list(combinations(sorted_ranks, 2))
    dispersion = sum(b - a for a, b in pair_combinations)  # Not used later
    
    # Compute harmonic adjustment factor based on inverse ranks
    harmonic_sum = sum(1 / r for r in sorted_ranks if r != 0)
    adjustment_factor = len(sorted_ranks) / harmonic_sum if harmonic_sum else 1
    
    # Apply adjustment to create normalized scores
    norm_scores = [adjustment_factor / r for r in sorted_ranks]
    return norm_scores, median_rank

# Weighting scheme with redundant components
def apply_weights(scores, weights):
    w1, w2, w3, w4 = weights  # Only w1 and w2 are actually used
    
    # Effective transformation
    amplified = [s * w1 for s in scores]
    dampened = [a / w2 for a in amplified]
    
    # Unused transformations (distractors)
    inverted = [w3 / (1 + s) for s in scores]  # dead path
    shifted = [s + w4 for s in scores]         # dead path
    
    return dampened

# Final scoring with conditional logic
def calculate_final_score(rank_data, weights):
    scores, med = analyze_ranks(rank_data)
    processed = apply_weights(scores, weights)
    
    # Introduce conditional expression based on median
    base_score = sum(processed) * (1.25 if med <= 3 else 0.9)
    
    # Additional adjustments
    penalty = 0
    if any(s < 0.5 for s in processed):
        penalty += 10
    
    # Final nonlinear scaling
    final_score = int(base_score ** 1.5) - penalty
    
    # Irrelevant intermediate (distractor)
    avg_score = sum(processed) / len(processed) if processed else 0
    outlier_count = sum(1 for s in processed if s > avg_score * 2)
    
    return final_score

# Input data
rank_data = [4, 2, 1, 3, 2, 5, 1]
weights = (1.8, 1.2, 0.7, 4.0)  # w3 and w4 are unused

# Execution
final_score = calculate_final_score(rank_data, weights)
print(f"Target result: {final_score}")