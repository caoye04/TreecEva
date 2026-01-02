from collections import defaultdict, Counter

# Simulated user interaction log with redundant and misleading fields
tech_conference_log = [
    {'user': 'A', 'action': 'login', 'duration': 120, 'tier': 'premium', 'error': None, 'timestamp': '09:00'},
    {'user': 'B', 'action': 'download', 'duration': 45, 'tier': 'free', 'error': 'timeout', 'timestamp': '09:02'},
    {'user': 'A', 'action': 'upload', 'duration': 60, 'tier': 'premium', 'error': None, 'timestamp': '09:03'},
    {'user': 'C', 'action': 'login', 'duration': 10, 'tier': 'free', 'error': None, 'timestamp': '09:04'},
    {'user': 'B', 'action': 'login', 'duration': 80, 'tier': 'free', 'error': None, 'timestamp': '09:05'},
    {'user': 'D', 'action': 'download', 'duration': 200, 'tier': 'premium', 'error': None, 'timestamp': '09:06'},
    {'user': 'C', 'action': 'download', 'duration': 30, 'tier': 'free', 'error': 'auth', 'timestamp': '09:07'},
    {'user': 'A', 'action': 'logout', 'duration': 0, 'tier': 'premium', 'error': None, 'timestamp': '09:08'},
]

# Irrelevant aggregation: counts per action (not used in final score)
action_counter = Counter([entry['action'] for entry in tech_conference_log])

# Track session states (some state tracking is irrelevant)
session_tracker = defaultdict(list)
for log in tech_conference_log:
    session_tracker[log['user']].append(log['action'])

# Compute auxiliary metric: total errors (misleading - not directly used)
total_errors = sum(1 for log in tech_conference_log if log['error'] is not None)
error_risk_factor = total_errors * 1.5 if total_errors > 0 else 0.0

# Process data: extract premium users with successful uploads
candidate_users = set()
upload_durations = []
for log in tech_conference_log:
    if log['tier'] == 'premium' and log['action'] == 'upload' and log['error'] is None:
        candidate_users.add(log['user'])
        upload_durations.append(log['duration'])

# Additional distraction: compute average duration for all downloads (unused)
download_durations = [log['duration'] for log in tech_conference_log if log['action'] == 'download']
avg_download_time = sum(download_durations) / len(download_durations) if download_durations else 0

# Compute base engagement score from valid uploads
if upload_durations:
    base_engagement = sum(upload_durations)
else:
    base_engagement = 0

# Apply tier-based multiplier (only premium matters here)
tier_multiplier = 2.5

# Secondary filter: must have logged in before uploading (temporal logic)
valid_uploaders = 0
for user in candidate_users:
    actions = [e['action'] for e in tech_conference_log if e['user'] == user]
    login_index = -1
    upload_index = -1
    for i, action in enumerate(actions):
        if action == 'login' and login_index == -1:
            login_index = i
        if action == 'upload' and upload_index == -1:
            upload_index = i
    if login_index != -1 and upload_index != -1 and login_index < upload_index:
        valid_uploaders += 1

# Final scoring logic
def calculate_final_score(processed_data):
    # processed_data is a dummy parameter (misleading signature)
    raw_score = base_engagement * tier_multiplier
    adjustment = valid_uploaders * 10
    return int(raw_score + adjustment)

# Key statement
final_score = calculate_final_score(processed_data=None)

# Print result
print(f"Target result: {final_score}")