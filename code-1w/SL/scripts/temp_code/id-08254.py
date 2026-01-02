from itertools import groupby

def analyze_performance(metrics):
    avg = sum(metrics) / len(metrics)
    variance = sum((x - avg) ** 2 for x in metrics) / len(metrics)
    return avg, variance

def calculate_bonus(base, level):
    if level == 'high':
        return base * 0.5
    elif level == 'medium':
        return base * 0.2
    else:
        return base * 0.05

def calculate_final_score(ranks, multiplier):
    # Group consecutive ranks with same performance tier
    sorted_ranks = sorted(ranks.items(), key=lambda x: x[1]['score'], reverse=True)
    grouped = {k: list(g) for k, g in groupby(sorted_ranks, key=lambda x: x[1]['tier'])}
    
    # Compute base score from top performers
    top_tier = grouped.get('S', [])
    base_score = sum(entry[1]['score'] for entry in top_tier)
    
    # Apply multiplier only if certain conditions are met
    if len(top_tier) >= 3:
        adjustment_factor = 1.1
    else:
        adjustment_factor = 0.95
    
    # Irrelevant computation - distractor (dead logic path)
    temp_analysis = [entry[1]['score'] * 0.1 for entry in sorted_ranks if entry[1]['tier'] == 'C']
    temp_sum = sum(temp_analysis)  # Not used anywhere
    
    # Bonus logic with red herring variables
    raw_metrics = [entry[1]['score'] for entry in sorted_ranks]
    mean_val, var_val = analyze_performance(raw_metrics)
    bonus_level = 'high' if mean_val > 80 else 'medium'
    bonus_amt = calculate_bonus(base_score, bonus_level)
    
    # Misleading intermediate calculation (not affecting final outcome)
    phantom_score = 0
    for i in range(len(raw_metrics)):
        if raw_metrics[i] > 90:
            phantom_score += raw_metrics[i] * 0.01  # negligible and unused
    
    # Final composition
    final_raw = base_score * adjustment_factor
    final_with_bonus = final_raw + bonus_amt
    scaling_offset = 5  # constant offset
    final_score = int(final_with_bonus + scaling_offset)
    
    return final_score

# Main execution block
if __name__ == '__main__':
    # Simulated dataset: employee rank data
    rank_data = {
        'Alice': {'score': 95, 'tier': 'S'},
        'Bob': {'score': 88, 'tier': 'S'},
        'Charlie': {'score': 92, 'tier': 'S'},
        'Diana': {'score': 78, 'tier': 'A'},
        'Eve': {'score': 65, 'tier': 'B'},
        'Frank': {'score': 54, 'tier': 'C'},
        'Grace': {'score': 90, 'tier': 'S'},
        'Heidi': {'score': 82, 'tier': 'A'}
    }

    # Bonus configuration
    bonus_multiplier = 1.3  # Unused in logic but looks important
    config_flags = {'debug': False, 'strict_mode': True}
    
    # Auxiliary tracking variables (distractors)
    total_entries = len(rank_data)
    tier_counts = {tier: sum(1 for v in rank_data.values() if v['tier'] == tier) for tier in 'SABC'}
    average_base_score = sum(v['score'] for v in rank_data.values()) / total_entries
    
    # Critical execution point
    final_score = calculate_final_score(rank_data, bonus_multiplier)
    
    # Output result
    print(f"Result: {final_score}")