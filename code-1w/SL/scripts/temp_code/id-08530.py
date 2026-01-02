from collections import defaultdict, Counter

# Simulate user activity logs with action types and timestamps
def preprocess_logs(raw_logs):
    action_count = defaultdict(int)
    time_stamps = []
    
    for entry in raw_logs:
        action = entry['action']
        timestamp = entry['time']
        action_count[action] += 1
        time_stamps.append(timestamp)
    
    # Distractor: unused variable tracking
    total_entries = len(raw_logs)
    unique_actions = len(action_count)
    avg_interval = sum(time_stamps[i+1] - time_stamps[i] 
                       for i in range(len(time_stamps)-1)) / (len(time_stamps)-1) if len(time_stamps) > 1 else 0
    
    return dict(action_count), time_stamps

# Process frequency and derive engagement metrics
def analyze_engagement(action_freq):
    freq_counter = Counter(action_freq)
    top_actions = freq_counter.most_common(3)
    
    base_score = 0
    decay_factor = 1.0
    for action, count in freq_counter.items():
        if count >= 5:
            base_score += count * 2
        elif count >= 3:
            base_score += count * 1.5
        else:
            base_score += count * 0.8
        decay_factor *= 0.95  # Irrelevant decay not used later
    
    # Distractor computation
    weighted_sum = sum(count * (i+1) for i, (_, count) in enumerate(top_actions))
    diversity_bonus = len(freq_counter) * 1.2 if len(freq_counter) > 2 else 0
    
    return base_score, diversity_bonus

# Final scoring with normalization
def calculate_final_score(data):
    raw_logs = data['logs']
    config = data['config']
    
    action_freq, _ = preprocess_logs(raw_logs)
    base_score, bonus = analyze_engagement(action_freq)
    
    # Key logic: final score derived from normalized base and adjusted bonus
    normalized_base = int(base_score * config['scale'])
    adjustment = config['offset']
    final_score = normalized_base + int(bonus) + adjustment
    
    # Red herring variables
    hypothetical_max = 100 * config['scale'] + 10
    efficiency_ratio = normalized_base / hypothetical_max if hypothetical_max > 0 else 0
    
    return final_score

# Generate synthetic log data
raw_activity_log = [
    {'action': 'click', 'time': 10},
    {'action': 'scroll', 'time': 15},
    {'action': 'click', 'time': 20},
    {'action': 'hover', 'time': 25},
    {'action': 'click', 'time': 30},
    {'action': 'scroll', 'time': 35},
    {'action': 'click', 'time': 40},
    {'action': 'keypress', 'time': 45},
    {'action': 'scroll', 'time': 50},
    {'action': 'click', 'time': 55},
    {'action': 'hover', 'time': 60},
    {'action': 'click', 'time': 65},
    {'action': 'scroll', 'time': 70},
    {'action': 'keypress', 'time': 75},
    {'action': 'click', 'time': 80}
]

config_settings = {
    'scale': 3.5,
    'offset': 5
}

log_data = {'logs': raw_activity_log, 'config': config_settings}
final_score = calculate_final_score(log_data)
print(f"Result: {final_score}")