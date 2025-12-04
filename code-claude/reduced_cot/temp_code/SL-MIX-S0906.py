# User activity analysis for a web application

# User sets
active_users = {101, 102, 105, 108, 110, 112, 115}
all_users = {101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115}
inactive_users = all_users - active_users

# Premium subscription data
premium_users = {102, 104, 105, 108, 111, 114}
free_users = all_users - premium_users

# Login statistics
daily_logins = 21
weekly_unique = len(active_users) + 3

# Calculate user segments
free_active = active_users & free_users
premium_inactive = premium_users & inactive_users

# Calculate overlap and apply bitwise operation
overlap = len(active_users & premium_users) ^ (daily_logins & 0x0F)

# Display summary
print(f"Active users: {len(active_users)}")
print(f"Premium users: {len(premium_users)}")
print(f"Result: {overlap}")