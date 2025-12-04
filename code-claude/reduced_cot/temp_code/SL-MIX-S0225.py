# User activity tracking system
user_data = {
    'user1': {'name': 'Alex', 'joined': '2023-01-15', 'status': 'active'},
    'user2': {'name': 'Blake', 'joined': '2023-02-20', 'status': 'inactive'},
    'user3': {'name': 'Casey', 'joined': '2023-03-05', 'status': 'active'},
    'user4': {'name': 'Dana', 'joined': '2023-01-30', 'status': 'active'},
    'user5': {'name': 'Eli', 'joined': '2023-04-10', 'status': 'inactive'}
}

# Extract user IDs for reporting
user_ids = list(user_data.keys())

# Create activity log (1 = active in last week, 0 = not active)
user_activity = {}
for user_id in user_ids:
    if user_data[user_id]['status'] == 'active':
        user_activity[user_id] = 1
    else:
        user_activity[user_id] = 0

# Get slice of relevant users for weekly report
recent_users = user_ids[1:4]  # users 2, 3, 4

# Update activity based on recent login data
recent_logins = {'user1': 3, 'user3': 5, 'user5': 0}
for user_id in recent_logins:
    if recent_logins[user_id] > 0:
        user_activity[user_id] = 1

# Calculate total active users
active_users = sum(user_activity.values())

print(f"Total active users: {active_users}")