user_permissions = {'read', 'write', 'execute'}
required_access = {'read', 'write'}

user_count = 0
privileged_count = 0
filtered_users = set()

for uid in range(100, 115):
    if uid % 3 == 0:
        filtered_users.add(f'user_{uid}')
    elif uid % 5 == 0:
        filtered_users.add(f'user_{uid}')

if len(filtered_users) > 10:
    extra_user = 'user_999'
    filtered_users.add(extra_user)

active_threshold = len(filtered_users)

# Final output
print(f"Result: {active_threshold}")