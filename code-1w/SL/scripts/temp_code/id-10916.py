from collections import Counter

# System performance parameters
task_list = ['A', 'B', 'C', 'A', 'B', 'A']
base_capacity = 120
downtime_minutes = 15
maintenance_cost = 37

# Count task frequency
task_freq = Counter(task_list)
most_common_task_count = task_freq.most_common(1)[0][1]

# Calculate processing load based on dominant task
process_load = base_capacity * (most_common_task_count / len(task_list))

# Redundancy factor based on system uptime
uptime_ratio = (60 - downtime_minutes) / 60
redundancy_factor = 1 - uptime_ratio

# Critical computation step
efficiency_score = process_load * (1 + redundancy_factor)

# Output result
print(f"Result: {efficiency_score}")