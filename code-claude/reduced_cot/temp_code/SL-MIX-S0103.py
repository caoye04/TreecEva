# Analyzing user activity patterns in a web application

# Active users from today's log (user IDs)
active_users = {45, 12, 78, 23, 56, 89, 34}

# Users who haven't logged in for over 30 days
inactive_users = {12, 45, 67, 90, 34}

# Calculate metrics
active_count = len(active_users)
inactive_count = len(inactive_users)

# Users who are either active or inactive but not both
unique_status_users = active_users.symmetric_difference(inactive_users)

# Prepare user retention report
common_users = active_users.intersection(inactive_users)
all_tracked_users = active_users.union(inactive_users)

# Calculate key metric for retention analysis
symmetric_difference = len(active_users ^ inactive_users) & (active_count | 2)

# Display report summary
print(f"Total tracked users: {len(all_tracked_users)}")
print(f"Result: {symmetric_difference}")