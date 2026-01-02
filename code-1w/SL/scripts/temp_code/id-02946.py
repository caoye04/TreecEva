from collections import defaultdict
from itertools import combinations

# Simulate player ranking data with performance metrics
player_metrics = [
    {'id': 'P1', 'base_score': 85, 'consistency': 0.78, 'streak': 3},
    {'id': 'P2', 'base_score': 92, 'consistency': 0.85, 'streak': 1},
    {'id': 'P3', 'base_score': 78, 'consistency': 0.65, 'streak': 5},
    {'id': 'P4', 'base_score': 96, 'consistency': 0.91, 'streak': 2}
]

# Irrelevant distraction: unused historical stats
historical_averages = defaultdict(float)
for player in player_metrics:
    historical_averages[player['id']] = (player['base_score'] * player['consistency']) // 1

# Extract rank-ordered data by base_score
rank_data = sorted(player_metrics, key=lambda x: x['base_score'], reverse=True)

# Bonus qualification flags (some are red herrings)
bonus_flags = []
for player in rank_data:
    has_streak_bonus = player['streak'] > 2
    high_consistency = player['consistency'] > 0.8
    mid_tier = 80 <= player['base_score'] < 90
    # Complex conditional expression - only streak matters for bonus
    bonus_flags.append({
        'player_id': player['id'],
        'streak_qual': has_streak_bonus,
        'high_consistency': high_consistency,
        'mid_tier': mid_tier,
        'phantom_flag': mid_tier and not has_streak_bonus  # Distractor
    })

# Dead code path: unused combination analysis
unused_pairs = list(combinations(rank_data, 2))
triggered_combos = 0
for p1, p2 in unused_pairs:
    if (p1['base_score'] - p2['base_score']) > 10 and p2['streak'] == 1:
        triggered_combos += 1  # Never used later

# Real logic begins: score adjustment based on rank position and streak
position_weights = [1.2, 1.1, 1.05, 1.0]
adjusted_scores = []
for idx, player in enumerate(rank_data):
    raw_score = player['base_score']
    weight = position_weights[idx]
    adjusted = raw_score * weight
    if bonus_flags[idx]['streak_qual']:
        adjusted += 5  # Streak bonus applied
    adjusted_scores.append(adjusted)

# Secondary distraction: set operation with no impact
active_ids = {p['id'] for p in rank_data}
external_filter = {'P1', 'P3', 'P5'}
filtered_ranks = active_ids & external_filter  # Unused beyond this point

# Final scoring function with multiple inputs
def calculate_final_score(ranked_players, flags):
    total = 0.0
    for i, player in enumerate(ranked_players):
        contribution = adjusted_scores[i] * 0.25
        # Logical short-circuit that doesn't change outcome
        if flags[i]['high_consistency'] or flags[i]['phantom_flag']:
            contribution *= 1.02
        total += contribution
    # Apply rounding to limit decimal places
    return round(total, 4)

# Key execution point
final_score = calculate_final_score(rank_data, bonus_flags)

# Output result
print(f"Target result: {final_score}")