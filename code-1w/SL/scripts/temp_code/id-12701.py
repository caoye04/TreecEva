from itertools import combinations

def analyze_performance(metrics):
    base_score = sum(metrics) / len(metrics)
    bonus = 0.0
    if base_score > 80:
        bonus = 10
    elif base_score > 60:
        bonus = 5
    adjusted = base_score + bonus
    penalty = len([m for m in metrics if m < 50]) * 2
    return adjusted - penalty

def validate_sequence(seq):
    return all(a < b for a, b in zip(seq, seq[1:]))

def calculate_final_score(ranks, wts):
    weighted_sum = sum(r * w for r, w in zip(ranks, wts))
    norm_factor = sum(wts)
    normalized = weighted_sum / norm_factor
    
    # Distractor: irrelevant transformation on permuted data
    perms = list(combinations(ranks, 3))
    perm_avg = sum(sum(p)/3 for p in perms) / len(perms) if perms else 0
    temp_debug = perm_avg * 0.1  # unused beyond this
    
    # Semi-relevant filtering
    valid_ranks = [r for r in ranks if r > 0]
    rank_mean = sum(valid_ranks) / len(valid_ranks) if valid_ranks else 0
    
    # Final adjustment based on spread
    spread = max(ranks) - min(ranks) if ranks else 0
    adjustment = -0.5 if spread > 20 else 0.5
    
    return int(normalized + adjustment)

# Main execution block
metrics_data = [85, 90, 78, 92, 88]
score = analyze_performance(metrics_data)

rankings = [25, 18, 22, 30, 15]
weights = [0.1, 0.2, 0.3, 0.25, 0.15]

# Irrelevant string processing (distractor)
diag_label = "RANK_DIAG_" + "_".join(str(len(weights)) in 'odd' if len(weights)%2 else 'even')
diag_code = diag_label.lower().replace('odd', 'O').replace('even', 'E').strip('X') if 'X' not in diag_label else 'DEFAULT'

# Key computation
final_score = calculate_final_score(rankings, weights)

# Print result
print(f"Result: {final_score}")