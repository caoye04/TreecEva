from collections import defaultdict

# Simulate player rank data across multiple game modes
game_modes = ['solo', 'duo', 'squad']
player_ranks = [
    ('alice', 'solo', 1), ('bob', 'solo', 3), ('carol', 'solo', 2),
    ('alice', 'duo', 2), ('bob', 'duo', 1), ('carol', 'duo', 4),
    ('alice', 'squad', 3), ('bob', 'squad', 2), ('carol', 'squad', 1)
]

rank_counter = defaultdict(int)
mode_counts = defaultdict(int)

for name, mode, rank in player_ranks:
    rank_counter[name] += rank
    mode_counts[mode] += 1

# Compute average rank per player
avg_ranks = {}
for name in ['alice', 'bob', 'carol']:
    total = sum(r for n, m, r in player_ranks if n == name)
    avg_ranks[name] = total / 3.0

# Misleading: irrelevant computation involving mode frequency
mode_multiplier = {mode: 1 + (5 - count) * 0.1 for mode, count in mode_counts.items()}
fake_adjustment = sum(mode_multiplier.values()) * 0.05  # Not used later

# Bonus system based on consistency (min difference between ranks)
consistency_scores = {}
for name in ['alice', 'bob', 'carol']:
    ranks = [r for n, m, r in player_ranks if n == name]
    consistency_scores[name] = 10 - (max(ranks) - min(ranks))

# Slice only top performers from sorted list
sorted_by_avg = sorted(avg_ranks.items(), key=lambda x: x[1])
top_performers = sorted_by_avg[:2]

# Bonus weights (arbitrary scaling factors)
bonus_weights = {'base': 0.7, 'consistency': 0.3, 'hidden_factor': 0.05}

# Distractor: unused helper function
def compute_leaderboard_snapshot():
    return {k: v for k, v in sorted_by_avg}

# Main scoring logic
def calculate_final_score(rank_data, weights):
    base_component = 0
    for name, avg in avg_ranks.items():
        base_component += (10 - avg) * weights['base']

    consistency_component = 0
    for score in consistency_scores.values():
        consistency_component += score * weights['consistency']

    # Hidden factor intentionally not applied
    total = base_component + consistency_component

    # Final adjustment based on top performer count
    if len(top_performers) >= 2:
        total += 5  # Reward team depth

    return int(total)

# Execute main logic
final_score = calculate_final_score(rank_counter, bonus_weights)

# Print result as required
print(f"Result: {final_score}")