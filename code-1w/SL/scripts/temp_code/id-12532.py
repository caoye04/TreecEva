from itertools import compress

def analyze_performance(metrics, thresholds):
    above_threshold = [m >= t for m, t in zip(metrics, thresholds)]
    return sum(compress(metrics, above_threshold))

def calculate_entropy(values):
    # Irrelevant helper function - not used in final result
    total = sum(values)
    if total == 0:
        return 0.0
    probs = [v / total for v in values]
    from math import log2
    return -sum(p * log2(p) for p in probs if p > 0)

def calculate_final_score(ranks, multiplier):
    base_score = 0
    penalty = 0
    
    # Primary logic: score based on rank positions and streaks
    for i, rank in enumerate(ranks):
        if rank <= 3:
            base_score += 10
            if i > 0 and ranks[i-1] <= 3:
                base_score += 2  # bonus for consecutive top ranks
        elif rank <= 7:
            base_score += 5
        else:
            penalty += 1
    
    # Distractor block: complex but unused calculation
    shadow_score = 0
    for r in ranks:
        for j in range(3):
            shadow_score += (r % 3) * j
    shadow_score = shadow_score / (len(ranks) + 1) if ranks else 0
    
    # Key conditional expression
    adjustment = 4 if len(ranks) > 5 else 2
    
    # Secondary logic: apply multiplier and adjustments
    raw_score = (base_score - penalty) * multiplier
    final_score = raw_score + adjustment
    
    # More distractors: slicing and unused transformations
    reversed_ranks = ranks[::-1]
    midpoint = len(reversed_ranks) // 2
    first_half_avg = sum(reversed_ranks[:midpoint]) / midpoint if midpoint > 0 else 0
    
    # Final computation chain
    noise_factor = sum(1 for x in ranks if x % 2 == 0) * 0.1
    final_score = int(final_score - noise_factor)  # deterministic truncation
    
    return final_score

# Main execution
rank_data = [1, 2, 4, 6, 3, 2, 8]
bonus_multiplier = 1.5
streak_counter = 0
max_streak = 0

for r in rank_data:
    if r <= 3:
        streak_counter += 1
        max_streak = max(max_streak, streak_counter)
    else:
        streak_counter = 0

# Unused dictionary structure - red herring
performance_summary = {
    'ranks': rank_data,
    'count_low': len([r for r in rank_data if r <= 3]),
    'count_mid': len([r for r in rank_data if 4 <= r <= 7]),
    'count_high': len([r for r in rank_data if r > 7])
}

# Key statement
final_score = calculate_final_score(rank_data, bonus_multiplier)

# Output result
print(f"Result: {final_score}")