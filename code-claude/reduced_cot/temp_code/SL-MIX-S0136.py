import itertools

def analyze_user_activity(log_data):
    # Process user activity logs
    # Format: (user_id, action_type, duration_minutes)
    inactive_threshold = 15
    premium_bonus = 5
    
    # Extract user IDs who performed actions
    all_users = set(user[0] for user in log_data)
    
    # Find users with long sessions (not relevant for active count)
    long_sessions = [user for user in log_data if user[2] > 45]
    
    # Track premium users (affects sorting but not active count)
    premium_users = {'user123', 'user456', 'user789'}
    
    # Calculate average time per user (not directly used in result)
    user_times = {}
    for user_id, action, duration in log_data:
        if user_id not in user_times:
            user_times[user_id] = []
        user_times[user_id].append(duration)
    
    avg_times = {user: sum(times)/len(times) for user, times in user_times.items()}
    
    # Sort users by activity time (not affecting active count)
    sorted_users = sorted(
        avg_times.items(),
        key=lambda x: x[1] + (premium_bonus if x[0] in premium_users else 0),
        reverse=True
    )
    
    # Filter active users (those with average activity above threshold)
    active_user_ids = [user_id for user_id, avg_time in avg_times.items() 
                      if avg_time >= inactive_threshold]
    
    # Some data transformation (doesn't affect active count)
    user_combinations = list(itertools.combinations(active_user_ids[:4], 2))
    potential_groups = len(user_combinations)
    
    # Get final filtered users
    filtered_users = set(active_user_ids)
    
    # Count active users
    active_users = len(filtered_users)
    
    return active_users

# Sample log data: (user_id, action_type, duration_minutes)
log_data = [
    ('user123', 'login', 5),
    ('user456', 'search', 12),
    ('user789', 'post', 8),
    ('user123', 'message', 25),
    ('user456', 'logout', 3),
    ('user101', 'login', 4),
    ('user202', 'search', 18),
    ('user101', 'logout', 2),
    ('user789', 'message', 30),
    ('user202', 'post', 22)
]

result = analyze_user_activity(log_data)
print(f"Result: {result}")