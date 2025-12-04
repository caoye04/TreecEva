# User activity tracking system
# Track which users are currently active in the system

user_statuses = {
    'user_123': True,    # Online
    'user_456': False,   # Offline
    'user_789': True,    # Online
    'user_012': False,   # Offline
    'user_345': True,    # Online
    'user_678': True,    # Online
    'user_901': False    # Offline
}

max_capacity = 10
total_users = len(user_statuses)

# Calculate users who are currently online
active_users = sum(1 for status in user_statuses.values() if status)

# Calculate percentage of active users
if total_users > 0:
    active_percentage = (active_users / total_users) * 100
else:
    active_percentage = 0

available_slots = max_capacity - total_users

print(f"Result: {active_users}")