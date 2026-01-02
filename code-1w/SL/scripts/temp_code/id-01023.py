from collections import Counter

# System performance logs from two servers
timestamps_server_a = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
timestamps_server_b = [3, 6, 9, 12, 15, 18, 21, 24]

# Filter only successful operations (odd timestamps)
successful_a = {ts for ts in timestamps_server_a if ts % 2 == 1}
successful_b = {ts for ts in timestamps_server_b if ts % 2 == 1}

# Find overlapping successful timestamps
common_items = successful_a.intersection(successful_b)

# Count frequency of each server's successful timestamps (irrelevant but plausible)
count_a = Counter(timestamps_server_a)
count_b = Counter(timestamps_server_b)

total_frequency_impact = sum(count_a.values()) + sum(count_b.values())

result = len(common_items)
print(f"Result: {result}")