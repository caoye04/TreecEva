from collections import defaultdict

# Employee access analysis for system security audit
user_roles = {
    'alice': 'admin',
    'bob': 'user',
    'charlie': 'moderator',
    'david': 'user',
    'eve': 'admin',
    'frank': 'guest'
}

login_attempts = defaultdict(int)
login_attempts['alice'] = 15
login_attempts['bob'] = 8
login_attempts['charlie'] = 12
login_attempts['david'] = 3
login_attempts['eve'] = 20
login_attempts['frank'] = 1

# Distractor: analyzing role distribution (not used in final answer)
role_counts = {}
for role in user_roles.values():
    role_counts[role] = role_counts.get(role, 0) + 1

# Distractor: calculating access frequency (not directly relevant)
average_logins = sum(login_attempts.values()) / len(login_attempts)

# Target calculation: sum of login attempts for admin and moderator roles only
active_users = {}
for user, role in user_roles.items():
    if role in ['admin', 'moderator']:
        active_users[user] = login_attempts[user]

# Final target value
target_value = sum(active_users.values())

print(f"Target result: {target_value}")