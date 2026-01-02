user_ids = {101, 102, 103, 104, 105, 106, 107, 108}
active_flags = [True, False, True, True, False, True, True, False]
priority_threshold = 103

# Compute set of active users above priority threshold
active_ids = {uid for i, uid in enumerate(user_ids) if active_flags[i]}
high_priority_ids = {uid for uid in user_ids if uid > priority_threshold}

filtered_ids = active_ids.intersection(high_priority_ids)
banned_set = {104, 108}
result_set = filtered_ids.difference(banned_set)

result_set_size = len(result_set)
print(f"Target result: {result_set_size}")