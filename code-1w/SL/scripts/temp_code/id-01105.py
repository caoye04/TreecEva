user_activity_scores = [85, 90, 78, 92, 88, 76, 95, 89]
threshold = 85

active_users = {f'user_{i}' for i, score in enumerate(user_activity_scores) if score >= threshold}
premium_users = {'user_1', 'user_3', 'user_4', 'user_6', 'user_7'}

# Filter active users based on engagement
filtered_users = {user for user in active_users if int(user.split('_')[1]) % 2 == 1}

# Key intersection operation
temp_var_ignore = len(active_users)
result_set = filtered_users & premium_users
result_set_size = len(result_set)

print(f"Result: {result_set_size}")