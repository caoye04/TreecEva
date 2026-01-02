from collections import defaultdict
from itertools import combinations

# Simulate user engagement analytics with multiple metrics
def analyze_engagement(users, actions):
    stats = defaultdict(int)
    for u in users:
        for a in actions:
            key = f'{u}_{a}'
            stats[key] += 1
    return stats

# Auxiliary function to compute derived weights (not directly used)
def compute_weights(factors):
    weighted_sum = 0
    for i, f in enumerate(factors):
        weighted_sum += f * (i + 1) * 0.5
    return round(weighted_sum, 3)

# Core logic to determine ranking score based on activity and thresholds
def calculate_ranking_score(activity_log, threshold=10):
    total_interactions = sum(activity_log.values())
    high_freq_count = sum(1 for cnt in activity_log.values() if cnt > threshold)
    
    adjustment_factor = 1.0
    if high_freq_count > 2:
        adjustment_factor = 1.25
    elif total_interactions > 40:
        adjustment_factor = 1.15
    else:
        adjustment_factor = 0.95

    base_score = total_interactions * adjustment_factor
    
    # Generate unused combo statistics (distractor)
    keys = list(activity_log.keys())
    combo_count = 0
    if len(keys) >= 3:
        for combo in combinations(keys, 3):
            combo_count += 1  # Irrelevant computation
    
    return int(base_score)

# Main scoring pipeline
def calculate_final_score(ranks, multiplier):
    raw_total = sum(ranks)
    penalty = 0
    
    # Apply penalties for rank distribution skew
    sorted_ranks = sorted(ranks)
    if sorted_ranks[-1] - sorted_ranks[0] > 15:
        penalty += 5
    if sorted_ranks[2] < 5:
        penalty += 3
    
    adjusted_total = raw_total - penalty
    final_value = adjusted_total * multiplier
    
    # Dummy tracking state (misleading)
    debug_state = {
        'input_size': len(ranks),
        'max_rank': max(ranks),
        'penalty_applied': penalty,
        'timestamp': 1234567890
    }
    
    return int(final_value)

# --- Simulation Setup ---
users_list = ['alice', 'bob', 'charlie']
action_types = ['click', 'view', 'scroll', 'hover']

engagement_metrics = analyze_engagement(users_list, action_types)

# Populate actual activity log with synthetic but deterministic data
activity_frequency = {
    'alice_click': 8, 'alice_view': 12, 'alice_scroll': 15, 'alice_hover': 4,
    'bob_click': 10, 'bob_view': 9, 'bob_scroll': 6, 'bob_hover': 7,
    'charlie_click': 14, 'charlie_view': 11, 'charlie_scroll': 5, 'charlie_hover': 3
}

# Extract values for processing
freq_values = [v for v in activity_frequency.values()]

# Compute auxiliary weight (unused in final path)
features = [0.8, 1.2, 0.9, 1.5]
irrelevant_weight = compute_weights(features)

# Calculate individual component scores
rank_data = []
for i in range(3):
    segment = freq_values[i*4:(i+1)*4]
    score = calculate_ranking_score(dict(zip(action_types, segment)))
    rank_data.append(score)

bonus_multiplier = 2

# Key execution point
final_score = calculate_final_score(rank_data, bonus_multiplier)

print(f"Result: {final_score}")