from collections import Counter, defaultdict

# Simulate user interaction logs with various actions
def analyze_user_behavior(log_entries):
    action_counter = Counter()
    session_data = defaultdict(list)
    total_interactions = 0
    suspicious_count = 0
    
    for entry in log_entries:
        user_id = entry['user']
        action = entry['action']
        timestamp = entry['time']
        
        action_counter[action] += 1
        session_data[user_id].append((timestamp, action))
        
        total_interactions += 1
        
        # Track potentially suspicious patterns (distraction)
        if action == 'retry_login' and 'failed_login' in [a for t, a in session_data[user_id][:-1]]:
            suspicious_count += 1

    # Compute basic metrics
    unique_users = len(session_data)
    avg_actions_per_user = total_interactions / unique_users if unique_users else 0
    
    # Distractor: Analyze action diversity per user (not used later)
    action_diversity = {}
    for user, actions in session_data.items():
        unique_actions = len(set(a for t, a in actions))
        action_diversity[user] = unique_actions
    
    # Real logic: Score based on frequency of key actions
    critical_actions = ['file_upload', 'data_export', 'config_change']
    critical_weight_map = {'file_upload': 2, 'data_export': 3, 'config_change': 5}
    base_score = 0
    
    for action in critical_actions:
        count = action_counter[action]
        base_score += count * critical_weight_map[action]
    
    # Apply multiplier based on interaction density
    peak_hour_interactions = 0
    for entry in log_entries:
        if 9 <= entry['time'] % 24 < 17:  # Between 9-5
            peak_hour_interactions += 1
    
    peak_ratio = peak_hour_interactions / total_interactions if total_interactions else 0
    engagement_bonus = int(peak_ratio * 100) // 10  # Bonus per 10% peak usage
    
    # Irrelevant stats (dead code path)
    off_peak_avg = (total_interactions - peak_hour_interactions) / (24 - 8) if total_interactions else 0
    idle_periods = sum(1 for v in session_data.values() if len(v) < 3)
    
    # Final scoring with adjustment factor
    adjustment_factor = 1.0
    if action_counter['logout'] > action_counter['login']:
        adjustment_factor *= 0.9
    if action_counter['session_timeout'] > 0:
        adjustment_factor *= 0.95
    
    raw_score = base_score + engagement_bonus
    final_score = int(raw_score * adjustment_factor)
    
    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Generate deterministic log data
logs = [
    {'user': 'u1', 'action': 'login', 'time': 8},
    {'user': 'u1', 'action': 'file_upload', 'time': 10},
    {'user': 'u2', 'action': 'login', 'time': 9},
    {'user': 'u2', 'action': 'data_export', 'time': 11},
    {'user': 'u1', 'action': 'config_change', 'time': 12},
    {'user': 'u3', 'action': 'login', 'time': 13},
    {'user': 'u3', 'action': 'file_upload', 'time': 14},
    {'user': 'u2', 'action': 'file_upload', 'time': 15},
    {'user': 'u1', 'action': 'logout', 'time': 16},
    {'user': 'u2', 'action': 'logout', 'time': 17},
    {'user': 'u3', 'action': 'logout', 'time': 18},
    {'user': 'u1', 'action': 'login', 'time': 19},
    {'user': 'u1', 'action': 'retry_login', 'time': 20},
    {'user': 'u1', 'action': 'session_timeout', 'time': 21}
]

# Execute analysis
final_score = analyze_user_behavior(logs)