# User activity tracking system analysis
# Identifying users who are both active and have premium subscriptions

active_users = [103, 105, 108, 110, 112, 115, 118, 120]
regular_users = [101, 103, 106, 108, 109, 112, 114, 116, 118]
premium_users = [102, 105, 108, 110, 115, 118, 121]

# Calculate statistics for different user segments
total_users = len(set(active_users) | set(regular_users) | set(premium_users))

# Find users who are active but not regular
active_not_regular = len(set(active_users) - set(regular_users))

# Find users who are both active and premium
common_elements = len(set(active_users) & set(premium_users))

# Find users who are either regular or premium but not both
exclusive_membership = len(set(regular_users) ^ set(premium_users))

print(f"Result: {common_elements}")