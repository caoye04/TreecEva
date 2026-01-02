from collections import defaultdict

# Simulated user activity log with timestamps and actions
data_log = [
    {'user': 'alice', 'action': 'login', 'duration': 120},
    {'user': 'bob', 'action': 'edit', 'duration': 45},
    {'user': 'alice', 'action': 'export', 'duration': 30},
    {'user': 'carol', 'action': 'login', 'duration': 180},
    {'user': 'bob', 'action': 'view', 'duration': 60},
    {'user': 'alice', 'action': 'edit', 'duration': 200},
    {'user': 'dave', 'action': 'login', 'duration': 90},
    {'user': 'carol', 'action': 'edit', 'duration': 75}
]

# Distractor: irrelevant tracking variables
irrelevant_counter = 0
placeholder_values = []
temporary_state = {}

# Track action counts per user
action_count = defaultdict(int)
# Track total session time per user
session_time = defaultdict(int)
# Track suspicious long sessions (distraction metric)
suspicious_sessions = defaultdict(list)

for entry in data_log:
    user = entry['user']
    action = entry['action']
    duration = entry['duration']

    # Relevant: count actions
    action_count[user] += 1

    # Relevant: accumulate session time
    session_time[user] += duration

    # Distractor: flag long durations (not used later)
    if duration > 100:
        suspicious_sessions[user].append(duration)

    # Distractor: fake state update
    temporary_state[user] = temporary_state.get(user, 0) + 1
    irrelevant_counter += len(action) % 2

# Distractor: unused transformation
transformed_data = {k: v * 1.1 for k, v in session_time.items() if v > 100}

# Compute efficiency ratio: total actions / total unique users (intermediate)
efficiency_ratio = sum(action_count.values()) / len(action_count)

# Compute engagement score: average session time across users
engagement_score = sum(session_time.values()) / len(session_time)

# Compute consistency bonus: users with >= 2 actions
consistency_bonus = sum(1 for count in action_count.values() if count >= 2)

# Distractor: fake normalization
normalized_actions = [min(v, 3) for v in action_count.values()]

# Helper function to calculate final score
def calculate_final_score(log_data):
    base_score = 0
    user_stats = defaultdict(dict)

    for record in log_data:
        u = record['user']
        a = record['action']
        d = record['duration']

        if u not in user_stats:
            user_stats[u]['actions'] = 0
            user_stats[u]['total_time'] = 0

        user_stats[u]['actions'] += 1
        user_stats[u]['total_time'] += d

    # Compute weighted score
    for stats in user_stats.values():
        action_weight = stats['actions'] * 10
        time_weight = stats['total_time'] * 0.5
        base_score += action_weight + time_weight

    # Apply consistency multiplier
    active_users = sum(1 for s in user_stats.values() if s['actions'] >= 2)
    multiplier = 1.2 if active_users >= 2 else 1.0

    return int(base_score * multiplier)

# Final computation
final_score = calculate_final_score(data_log)

# Distractor: dead code path
if final_score < 0:
    final_score = abs(final_score)
    placeholder_values.append("negative_adjust")

# Irrelevant post-processing
adjusted_final = final_score * 0.99
rounded_final = round(adjusted_final)

# Output target result
print(f"Result: {final_score}")