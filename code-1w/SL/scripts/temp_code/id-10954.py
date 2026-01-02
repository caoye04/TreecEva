from collections import defaultdict

# Simulate daily active users for two different app features over a week
days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
feature_a_users = [120, 135, 140, 128, 150, 160, 145]
feature_b_users = [110, 135, 130, 128, 160, 155, 140]

# Map user activity counts to days using defaultdict for robustness
day_to_a = defaultdict(int)
day_to_b = defaultdict(int)
for i, day in enumerate(days):
    day_to_a[day] = feature_a_users[i]
    day_to_b[day] = feature_b_users[i]

# Identify days where both features had identical user counts
common_days = []
for day in days:
    if day_to_a[day] == day_to_b[day]:
        common_days.append(day)

# Compute set intersection to find overlapping user counts across features
a_counts = set(feature_a_users)
b_counts = set(feature_b_users)
common_elements = a_counts & b_counts

overlap_count = len(common_elements)

# Irrelevant distraction: another variable tracking something unrelated
total_unique_counts = len(a_counts | b_counts)

Result: overlap_count