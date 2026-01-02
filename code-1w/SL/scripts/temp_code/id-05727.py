from collections import defaultdict

# Simulated dataset: user activity logs with redundant fields
data_entries = [
    {'user': 'A', 'action': 'login', 'duration': 120, 'temp_flag': True, 'meta_x': 0.5},
    {'user': 'B', 'action': 'edit', 'duration': 45, 'temp_flag': False, 'meta_x': 0.3},
    {'user': 'A', 'action': 'save', 'duration': 10, 'temp_flag': True, 'meta_x': 0.8},
    {'user': 'C', 'action': 'login', 'duration': 200, 'temp_flag': True, 'meta_x': 0.1},
    {'user': 'B', 'action': 'view', 'duration': 60, 'temp_flag': False, 'meta_x': 0.9},
    {'user': 'D', 'action': 'login', 'duration': 30, 'temp_flag': True, 'meta_x': 0.4}
]

# Irrelevant transformation: converts action names to uppercase (not used in final logic)
def transform_action_names(entries):
    return [e['action'].upper() for e in entries]

temporary_actions = transform_action_names(data_entries)  # Dead-end computation

# State tracker for user sessions (relevant)
session_tracker = defaultdict(list)
for entry in data_entries:
    session_tracker[entry['user']].append(entry['duration'])

# Compute baseline metrics (some are distractions)
user_durations_sum = {u: sum(times) for u, times in session_tracker.items()}  # Used later
user_durations_count = {u: len(times) for u, times in session_tracker.items()}  # Semi-relevant
user_avg_duration = {u: user_durations_sum[u] / user_durations_count[u] for u in user_durations_sum}  # Not directly used

# Dummy scoring based on meta_x (never actually used)
dummy_scores = []
for entry in data_entries:
    if entry['meta_x'] > 0.4:
        dummy_scores.append(10)
    else:
        dummy_scores.append(5)

total_dummy = sum(dummy_scores)  # Red herring variable

# Real processing function
def preprocess_entries(entries):
    result = []
    for e in entries:
        # Only care about login duration and user
        if e['action'] == 'login':
            # Apply arbitrary weight for login
            weighted_duration = e['duration'] * 1.5
            result.append({'user': e['user'], 'score': weighted_duration})
    return result

processed_data = preprocess_entries(data_entries)

# Secondary irrelevant filter: counts non-login actions (distractor)
non_login_count = 0
for e in data_entries:
    if e['action'] != 'login':
        non_login_count += 1

# Core scoring logic
def calculate_final_score(login_records):
    score_accum = 0
    bonus_applied = 0
    for record in login_records:
        base = record['score']
        # Bonus rule: users with 'A' or 'C' get +5
        if record['user'] in ['A', 'C']:
            base += 5
            bonus_applied += 5
        score_accum += base
    
    # Final adjustment: subtract dummy-based penalty (but dummy not related)
    # This is a red herring but syntactically present
    penalty = len(login_records) * 2  # Simple penalty per login
    final = score_accum - penalty
    
    return int(final)  # Ensure integer result

final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")