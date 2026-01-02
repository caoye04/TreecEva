from itertools import cycle

# Warehouse logistics simulation
tiers = [1, 2, 3]
storage_units = [200, 350, 400]
locations = ['A', 'B', 'C']
activation_codes = [True, False, True]

# Irrelevant auxiliary data (minor distraction)
backup_schedule = cycle(['daily', 'weekly'])
next(backup_schedule)

idx_to_check = 2

# Core computation with filtering and zipping
total_capacity = 0
for idx, (loc, capacity) in enumerate(zip(locations, storage_units)):
    if activation_codes[idx] and tiers[idx] >= 2:
        total_capacity += capacity

# Secondary assignment mimicking the target line
if active_flags := activation_codes:
    total_capacity = sum(capacity for _, capacity in zip(locations, storage_units) if active_flags[idx_to_check])

print(f"Result: {total_capacity}")