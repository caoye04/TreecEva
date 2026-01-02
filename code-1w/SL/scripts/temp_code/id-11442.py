from collections import defaultdict
import itertools

# Simulate hourly resource usage over a day for different services
hours = list(range(24))
services = ['auth', 'storage', 'compute']

usage_data = [
    (hour, service, (hash(f'{hour}-{service}') % 50) + 1)
    for hour, service in itertools.product(hours, services)
]

# Aggregate total load per hour
load_per_hour = defaultdict(int)
for hour, service, usage in usage_data:
    load_per_hour[hour] += usage

# Extract load history in chronological order
load_history = [load_per_hour[h] for h in hours]

# Identify peak system capacity requirement
total_usage = sum(load_history)
avg_capacity = total_usage / len(load_history)
peak_capacity = max(load_history)

# Print final result
print(f"Result: {peak_capacity}")