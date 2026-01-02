user_ids = set(range(100, 200))
new_registrations = set(range(150, 250))
active_subscribers = set(range(120, 180))
premium_users = set(range(160, 200))

# Filter regular users who are not premium
filtered_users = user_ids.difference(premium_users)

# Find overlap between filtered users and active subscribers
result_set = filtered_users.intersection(active_subscribers).difference(premium_users)

# Final size of eligible standard-tier active users
result_set_size = len(result_set)

print(f"Target result: {result_set_size}")