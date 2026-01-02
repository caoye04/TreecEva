from collections import deque

# Simulate a rolling window of user activity over time
user_logins = [12, 8, 15, 23, 17, 25, 19]
active_users = deque(maxlen=5)

total_processed = 0
for login_count in user_logins:
    active_users.append(login_count)
    total_processed += login_count

    # Early exit if system reaches capacity
    if sum(active_users) > 60:
        break

# Key statement: determine peak load from recent activity
peak_load = max(active_users[-3:]) if len(active_users) >= 3 else sum(active_users)

print(f"Result: {peak_load}")