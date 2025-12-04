# User management system analysis
active_users = {101, 102, 103, 104, 105, 106, 107}
verified_users = {104, 105, 106, 107, 108, 109, 110}
suspended_users = {102, 108, 111}

# Remove suspended users from consideration
active_users = active_users - suspended_users
verified_users = verified_users - suspended_users

# Calculate unique intersection
unique_intersection_count = len(active_users.intersection(verified_users))

print(f"Result: {unique_intersection_count}")