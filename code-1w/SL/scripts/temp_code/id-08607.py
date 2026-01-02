from collections import Counter

event_log = [
    'signup', 'login', 'signup', 'logout', 'signup', 'login',
    'signup', 'profile_view', 'login', 'signup', 'logout'
]

event_counter = Counter(event_log)
daily_counts = []

for event, count in event_counter.items():
    if event.startswith('log'):
        adjusted_count = count * 2
    else:
        adjusted_count = count
    daily_counts.append(adjusted_count)

# Irrelevant variable (minor distraction)
temp_multiplier = 1.5

peak_capacity = max(daily_counts)
Result: peak_capacity