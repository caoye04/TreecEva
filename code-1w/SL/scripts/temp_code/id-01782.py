from collections import defaultdict

# Simulate player ranking and performance data
def analyze_player_trends(scores):
    avg = sum(scores) / len(scores)
    above_avg = [s for s in scores if s > avg]
    return len(above_avg), avg

# Misleading helper function (not used in final result)
def compute_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

# Core logic for score calculation
def calculate_final_score(ranks, bonuses):
    base_score = 0
    multiplier = 1
    temp_tracker = defaultdict(int)
    
    for rank, (player, score) in enumerate(ranks):
        temp_tracker[player] += score // (rank + 1) or 1
        if score % 2 == 0:
            base_score += score // 3
        else:
            base_score += score // 4
        
        # Red herring: tracking unused stats
        cumulative_shift = 0
        for i, val in enumerate([score, rank]):
            cumulative_shift ^= (val << 1)
            
    # Use bonus map with zip and enumerate
    for idx, (k, v) in enumerate(zip(bonuses.keys(), bonuses.values())):
        if idx % 2 == 0:
            multiplier += v // 10
    
    # Actual critical computation
    adjustment = len(temp_tracker) * 2
    base_score -= adjustment  # Subtle correction factor
    
    final_value = base_score * multiplier
    return int(final_value)

# Input data
rank_data = [
    ('alice', 88),
    ('bob', 75),
    ('charlie', 92),
    ('diana', 61)
]

bonus_map = {
    'level1': 25,
    'level2': 30,
    'level3': 35
}

# Dead code path - never executed but adds cognitive load
def deprecated_calc(*args):
    return sum(args) >> 2

unused_counter = 0
for _ in range(3):
    unused_counter += 10
    continue

# Key execution point
final_score = calculate_final_score(rank_data, bonus_map)

print(f"Result: {final_score}")