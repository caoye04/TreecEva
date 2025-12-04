from collections import Counter, defaultdict

# User engagement tracking system
login_data = [(101, 'web', 4), (102, 'mobile', 7), (103, 'web', 2), 
             (104, 'tablet', 5), (101, 'mobile', 3), (105, 'web', 8)]

# Track platforms for marketing analysis (not used in final calculation)
platform_counts = Counter(platform for _, platform, _ in login_data)
most_popular = platform_counts.most_common(1)[0][0]
print(f"Most popular platform: {most_popular}")

# Process user session data
user_sessions = defaultdict(list)
for user_id, platform, duration in login_data:
    user_sessions[user_id].append((platform, duration))

# Calculate average session time (distractor)
avg_session = sum(duration for _, _, duration in login_data) / len(login_data)

# Identify power users based on total time
total_time = {}
for user_id, sessions in user_sessions.items():
    # Calculate total time per user
    total = sum(duration for _, duration in sessions)
    # Store users with their total time
    total_time[user_id] = total

# Track users with multi-platform engagement
multi_platform_users = set()
for user_id, sessions in user_sessions.items():
    platforms = {platform for platform, _ in sessions}
    if len(platforms) > 1:
        multi_platform_users.add(user_id)

# Identify active users with significant engagement
user_activity = {}
threshold = 5  # Minimum engagement threshold

for user_id, total in total_time.items():
    # Apply bonus for multi-platform users (1.5x multiplier)
    engagement_score = total * 1.5 if user_id in multi_platform_users else total
    
    # Only count users with significant engagement
    if engagement_score > threshold:
        user_activity[user_id] = engagement_score

# Count active users meeting criteria
active_users = len(user_activity)
print(f"Result: {active_users}")