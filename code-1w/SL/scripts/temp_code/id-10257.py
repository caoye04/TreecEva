user_permissions = {1, 3, 4, 5, 7, 9, 10}
admin_roles = {2, 4, 6, 8, 10}
system_flags = {1, 2, 3, 4}

# Determine active user IDs with elevated access
active_users = {x for x in range(1, 12) if x % 2 == 1}  # Odd IDs are active
privileged_users = user_permissions.union(admin_roles)
recognized_entities = privileged_users.intersection(system_flags)

# Filter valid operational zones
all_zones = [3, 4, 5, 6, 7]
valid_records = set(all_zones)
filtered_ids = {x for x in active_users if x in privileged_users}
excluded_zones = {3, 5}

# Critical computation point
result_set = filtered_ids.intersection(valid_records).difference(excluded_zones)
result_set_size = len(result_set)

print(f"Result: {result_set_size}")