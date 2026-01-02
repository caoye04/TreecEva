from collections import defaultdict, Counter

# Simulated dataset: user activity logs with action types and durations
data = [
    {'user': 'A', 'action': 'click', 'duration': 1.2, 'timestamp': 100},
    {'user': 'B', 'action': 'scroll', 'duration': 2.5, 'timestamp': 105},
    {'user': 'A', 'action': 'hover', 'duration': 0.8, 'timestamp': 110},
    {'user': 'C', 'action': 'click', 'duration': 1.5, 'timestamp': 115},
    {'user': 'B', 'action': 'click', 'duration': 0.9, 'timestamp': 120},
    {'user': 'A', 'action': 'click', 'duration': 1.1, 'timestamp': 125},
    {'user': 'C', 'action': 'scroll', 'duration': 3.0, 'timestamp': 130},
    {'user': 'B', 'action': 'hover', 'duration': 1.3, 'timestamp': 135},
    {'user': 'D', 'action': 'click', 'duration': 0.7, 'timestamp': 140},
    {'user': 'C', 'action': 'click', 'duration': 1.6, 'timestamp': 145}
]

# Misleading preprocessing: counts per action type (not directly used)
action_counter = Counter(entry['action'] for entry in data)

# Process data: group by user, compute total duration and action count
user_stats = defaultdict(lambda: {'total_duration': 0.0, 'action_count': 0})
for entry in data:
    user_stats[entry['user']]['total_duration'] += entry['duration']
    user_stats[entry['user']]['action_count'] += 1

# Derived metrics: efficiency ratio (duration per action)
efficiency = {}
for user, stats in user_stats.items():
    efficiency[user] = stats['total_duration'] / stats['action_count']

# Distractor computation: find longest session per user (not used later)
user_sessions = defaultdict(list)
for entry in data:
    user_sessions[entry['user']].append(entry['duration'])
longest_session = {u: max(sessions) for u, sessions in user_sessions.items()}

# Normalize efficiency scores to 0-1 scale using min-max scaling
min_eff = min(efficiency.values())
max_eff = max(efficiency.values())
normalized_efficiency = {
    u: (e - min_eff) / (max_eff - min_eff) if max_eff > min_eff else 0 
    for u, e in efficiency.items()
}

# Weighted scoring: combine normalized efficiency and action count
weighted_scores = {}
total_actions = sum(stats['action_count'] for stats in user_stats.values())
for user, stats in user_stats.items():
    action_weight = stats['action_count'] / total_actions
    efficiency_weight = normalized_efficiency[user]
    weighted_scores[user] = (action_weight * 0.4) + (efficiency_weight * 0.6)

# Secondary distractor: frequency of each duration bucket (dead code path)
duration_buckets = defaultdict(int)
for entry in data:
    bucket = int(entry['duration'])
    duration_buckets[bucket] += 1
bucket_popularity = dict(sorted(duration_buckets.items(), key=lambda x: -x[1]))

# Further distraction: simulate confidence intervals (unused)
import math
def compute_ci(count):
    if count == 0:
        return 0, 0
    mean = 1.0
    stderr = 1.96 * math.sqrt((mean * (1 - mean)) / count)
    return mean - stderr, mean + stderr

# Simulate hypothetical trust scores (irrelevant to final result)
trust_scores = {user: min(1.0, 0.5 + 0.1 * stats['action_count']) 
                for user, stats in user_stats.items()}

# Core logic: process data into final form for scoring
processed_data = []
for user, weights in weighted_scores.items():
    entry = {
        'user': user,
        'score': weights,
        'level': 'high' if weights > 0.5 else 'low'
    }
    processed_data.append(entry)

# Final scoring function
def calculate_final_score(data_list):
    high_count = 0
    total_score = 0.0
    for item in data_list:
        total_score += item['score']
        if item['level'] == 'high':
            high_count += 1
    # Bonus for having multiple high-level users
    bonus = 10 if high_count >= 2 else 5
    base_result = total_score * 100
    return int(base_result) + bonus

# Critical execution point
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")