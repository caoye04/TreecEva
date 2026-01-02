def analyze_performance(scores):
    avg = sum(scores) / len(scores)
    above_avg = [s for s in scores if s > avg]
    deviation = sum([(s - avg) ** 2 for s in scores]) / len(scores)
    variance_check = deviation > 50
    return avg, len(above_avg), variance_check


def adjust_ranks(rankings):
    adjusted = []
    offset = len(rankings) // 2
    for i, r in enumerate(rankings):
        if i % 2 == 0:
            adjusted.append(r + offset)
        else:
            adjusted.append(r - 1)
    # Irrelevant transformation
    temp_str = "rank_data_processed"
    temp_len = len(temp_str)
    temp_set = set(temp_str) | {"x", "y"}
    return adjusted


def calculate_final_score(ranks, multiplier):
    base_score = 0
    penalty = 0
    
    for i, rank in enumerate(ranks):
        if rank <= 10:
            base_score += 10 - rank
        else:
            penalty += 1
    
    # Simulate streak logic
    streak = 0
    max_streak = 0
    for r in ranks:
        if r < 5:
            streak += 1
            max_streak = max(max_streak, streak)
        else:
            streak = 0
    
    streak_bonus = max_streak * 2
    final = (base_score - penalty * 3) * multiplier + streak_bonus
    
    # Dead code - irrelevant calculation
    dummy_calc = sum([i**2 for i in range(len(ranks))]) / (len(ranks) or 1)
    dummy_set = {x % 5 for x in ranks}
    dummy_str_op = "final_calc_complete".replace("_", "-").upper()
    
    return int(final)

# Main execution
raw_scores = [85, 92, 78, 90, 88, 76, 95, 87]
rank_list = [12, 3, 6, 1, 15, 4, 9, 2]
bonus_multiplier = 1.5

# Partially used analysis
mean_score, high_performers, high_variance = analyze_performance(raw_scores)
scaled_ranks = adjust_ranks(rank_list)

# Key computation
final_score = calculate_final_score(rank_list, bonus_multiplier)

print(f"Result: {final_score}")