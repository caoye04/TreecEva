def calculate_final_score(ranks, multiplier):
    base_points = 0
    penalty_adjustment = 0
    temp_sum = 0
    rank_counts = {}
    
    for rank in ranks:
        if rank <= 0:
            continue
        if rank == 1:
            base_points += 10
        elif rank == 2:
            base_points += 7
        elif rank == 3:
            base_points += 5
        else:
            base_points += 1
        
        if rank in rank_counts:
            rank_counts[rank] += 1
        else:
            rank_counts[rank] = 1
    
    # Distractor: unused computation on frequencies
    duplicate_penalty = 0
    for count in rank_counts.values():
        if count > 1:
            duplicate_penalty += count * 0.5
    
    # Irrelevant data transformation
    inverted_map = {v: k for k, v in rank_counts.items()}
    unused_inversion_sum = sum(inverted_map.keys()) if inverted_map else 0
    
    # Actual logic path
    streak_bonus = 0
    sorted_ranks = sorted(set(ranks))
    consecutive_count = 0
    for i in range(len(sorted_ranks)):
        if sorted_ranks[i] <= 0:
            continue
        if i > 0 and sorted_ranks[i] == sorted_ranks[i-1] + 1:
            consecutive_count += 1
        else:
            consecutive_count = 1
        if consecutive_count >= 3:
            streak_bonus += 3
    
    # Another red herring: complex conditional expression with partial effect
    adjustment_factor = 1.0 if len(ranks) > 10 else (1.2 if base_points > 20 else 0.9)
    
    # Misleading intermediate calculation
    projected_score = base_points * 1.5 + streak_bonus * 2
    decay_correction = projected_score * 0.1 if projected_score > 50 else 0
    
    # Final computation chain
    raw_score = base_points + streak_bonus
    final_score = raw_score * multiplier * adjustment_factor
    
    return int(final_score)

# Main execution
participant_ranks = [1, 3, 2, 4, 5, 1, 7, 8, 9, 10, 3]
bonus_multiplier = 1.5
auxiliary_data = [x ** 2 for x in participant_ranks if x % 2 == 0]
summary_stats = {'max': max(participant_ranks), 'min': min(participant_ranks), 'range': len(set(participant_ranks))}

# Dead code path (never executed but looks important)
def analyze_distribution(data):
    return {x: data.count(x) for x in set(data)}

# Key statement
final_score = calculate_final_score(participant_ranks, bonus_multiplier)
Result: {final_score}