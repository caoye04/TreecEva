from itertools import compress, cycle

def analyze_performance(metrics):
    base_scores = [m * 1.1 for m in metrics if m > 50]
    adjusted = [s + 5 for s in base_scores]
    return adjusted

def calculate_final_score(ranks, bonuses):
    # Irrelevant transformation
    temp_normalized = [r / max(ranks) for r in ranks]
    filtered_ranks = [r for i, r in enumerate(ranks) if r % 2 == 1]
    
    # Semi-relevant processing with distractor variables
    multiplier_sequence = list(zip(filtered_ranks, cycle([2, 3])))
    weighted = [a * b for a, b in multiplier_sequence]
    
    # Key computation path
    raw_total = sum(weighted)
    bonus_factor = sum(bonuses.values()) * 0.2
    scaling_offset = len(filtered_ranks)  # Distractor: not used directly
    
    # Final score calculation
    final_score = raw_total + bonus_factor
    return int(final_score)

# Main execution
metrics_log = [45, 60, 70, 80, 90]
bonus_map = {'q1': 10, 'q2': 15, 'q3': 5}
rank_data = [10, 15, 20, 25, 30, 35]

# Dead code path (distractor)
if False:
    dummy = [x**2 for x in rank_data]
    extra_calc = sum(dummy) // 100

interim_results = analyze_performance(metrics_log)
sparse_weights = list(compress(rank_data, [r % 5 == 0 for r in rank_data]))
scaling_constant = 1.0  # Unused variable

final_score = calculate_final_score(rank_data, bonus_map)
print(f"Result: {final_score}")