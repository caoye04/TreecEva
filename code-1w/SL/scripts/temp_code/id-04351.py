from itertools import combinations

def evaluate_performance(levels):
    base_score = 0
    for i, level in enumerate(levels):
        base_score += (i + 1) * level
    return base_score

def generate_rank_pairs(rank_list):
    return list(combinations(rank_list, 2))

def calculate_final_score(ranks, multiplier):
    total = evaluate_performance(ranks)
    pairs = generate_rank_pairs(ranks)
    pair_count = len(pairs)
    adjustment = 0
    for a, b in pairs:
        if abs(a - b) > 2:
            adjustment += 1
    # Irrelevant string operation (minimal distraction)
    status_msg = "Processing complete".replace("complete", "final")
    final_value = total * multiplier - adjustment
    return final_value

# Main execution
skill_levels = [3, 6, 2, 8]
bonus_multiplier = 1.5
extra_data = [1, 1, 1]  # Unused variable (slight interference)
calibration_mode = False  # Unused flag

final_score = calculate_final_score(skill_levels, bonus_multiplier)
print(f"Result: {final_score}")