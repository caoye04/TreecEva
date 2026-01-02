from collections import defaultdict, Counter

# Simulated dataset: user activity logs across multiple platforms
data = [
    {'user': 'alice', 'platform': 'A', 'actions': [1, 0, 1, 1], 'duration': 120},
    {'user': 'bob', 'platform': 'B', 'actions': [1, 1, 0, 0], 'duration': 95},
    {'user': 'alice', 'platform': 'B', 'actions': [0, 1, 1, 1], 'duration': 150},
    {'user': 'carol', 'platform': 'A', 'actions': [1, 1, 1, 0], 'duration': 130},
    {'user': 'bob', 'platform': 'A', 'actions': [0, 0, 1, 1], 'duration': 80}
]

# Weight configuration for scoring model
weights = {
    'action_weight': 1.5,
    'duration_base': 0.01,
    'platform_bonus': {'A': 1.2, 'B': 1.1},
    'streak_multiplier': [1.0, 1.1, 1.25, 1.5]
}

# Irrelevant auxiliary variables (distractors)
baseline_threshold = 75
max_duration_cap = 200
normalization_factor = 0.95
unused_config = {"mode": "legacy", "version": 2.1, "active": False}
temp_results = []

# Misleading intermediate computation (dead path)
def legacy_score_calc(actions):
    score = 0
    for a in actions:
        score += a * 0.8
    return score * 0.9  # Not used in final logic

# Unused helper function (decoy)
def validate_entry(entry):
    return entry['duration'] > baseline_threshold and len(entry['actions']) == 4

# Core processing function with layered logic
def process_user_data(entries):
    user_map = defaultdict(list)
    platform_count = Counter()
    
    # Accumulate entries by user (relevant)
    for entry in entries:
        user_map[entry['user']].append(entry)
        platform_count[entry['platform']] += 1
    
    # Compute action streaks using slicing (relevant)
    user_streaks = defaultdict(int)
    for user, records in user_map.items():
        total_actions = []
        for r in records:
            total_actions.extend(r['actions'])
        # Count consecutive 1s at the end (using slicing)
        reversed_actions = total_actions[::-1]
        streak = 0
        for act in reversed_actions:
            if act == 1:
                streak += 1
            else:
                break
        user_streaks[user] = streak
    
    # Irrelevant transformation (distractor)
    inverted_weights = {k: 1/v if isinstance(v, float) else v for k, v in weights.items()}
    score_offsets = [0.5, -0.3, 0.7, -0.2]
    
    # Main aggregation (relevant)
    aggregated = {}
    for user, records in user_map.items():
        base_action_score = 0
        total_duration = 0
        platform_bonus = 1.0
        
        for record in records:
            base_action_score += sum(record['actions']) * weights['action_weight']
            total_duration += record['duration']
            platform_bonus *= weights['platform_bonus'][record['platform']]
        
        duration_score = total_duration * weights['duration_base']
        streak_index = min(user_streaks[user], 4) - 1
        streak_index = max(streak_index, 0)
        streak_multiplier = weights['streak_multiplier'][streak_index]
        
        # Final individual score before normalization
        raw_score = (base_action_score + duration_score) * platform_bonus * streak_multiplier
        aggregated[user] = raw_score
    
    return aggregated, user_streaks, platform_count  # Only first used

# Secondary weighting function (relevant)
def apply_weight_adjustments(scores, weight_config, streaks):
    adjusted = {}
    adjustment_log = []
    
    # Use enumerate and zip meaningfully
    sorted_users = sorted(scores.keys())
    base_values = [scores[u] for u in sorted_users]
    adjustments = [0.98, 1.02, 0.95]  # Simulated calibration factors
    
    for i, (user, base) in enumerate(zip(sorted_users, base_values)):
        adj_factor = adjustments[i % len(adjustments)]
        # Additional logic involving string manipulation (distractor)
        user_code = ''.join([u.capitalize() for u in user])
        code_sum = sum(ord(c) for c in user_code) % 100
        adj_factor += code_sum * 0.001
        adjustment_log.append(f"{user}:{adj_factor:.3f}")
        
        adjusted[user] = base * adj_factor
    
    # Dead code path (misleading)
    if len(adjustment_log) > 10:
        with open("/tmp/log.txt", "w") as f:
            f.write('\n'.join(adjustment_log))
    
    return adjusted

# Final composition (relevant)
def calculate_final_score(raw_data, config):
    # First stage processing
    user_scores, streak_info, _ = process_user_data(raw_data)
    
    # Second stage refinement
    final_scores = apply_weight_adjustments(user_scores, config, streak_info)
    
    # Aggregate into single metric
    total = 0.0
    count = 0
    for val in final_scores.values():
        total += val
        count += 1
    
    # Introduce distractor calculation (irrelevant average)
    fake_avg = sum(user_scores.values()) / len(user_scores) * 0.85
    temp_results.append(fake_avg)
    
    # Correct final result
    final_score = round(total / count, 6) if count else 0.0
    
    # Red herring: unused complex expression
    outlier_check = any(s > 200 for s in user_scores.values()) or False
    consistency_flag = all(len(v['actions']) == 4 for v in raw_data)
    
    return final_score

# Execution point of interest
final_score = calculate_final_score(data, weights)
print(f"Target result: {final_score}")