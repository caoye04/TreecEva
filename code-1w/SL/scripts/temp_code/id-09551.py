from itertools import accumulate

# Simulate daily resource consumption over a week
usage_data = [120, 200, -50, 300, -80, 150, -30]
base_level = 50

# Apply cumulative adjustments to simulate net capacity changes
capacity_changes = [base_level + delta for delta in usage_data]
capacity_levels = list(accumulate(capacity_changes))

# Track minimum and maximum observed capacities
min_capacity = min(capacity_levels)
peak_capacity = max(capacity_levels)

# Irrelevant distraction: unused variable representing theoretical limit
theoretical_max = 1000

Result: peak_capacity