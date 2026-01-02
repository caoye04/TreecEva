from collections import Counter

# Simulate two data streams from network packets
timestamps_a = [1001, 1003, 1004, 1007, 1010, 1012, 1013]
timestamps_b = [1002, 1003, 1005, 1007, 1008, 1010, 1014]

# Find overlapping timestamps (possible synchronized events)
set_a = set(timestamps_a)
set_b = set(timestamps_b)
common_elements = set_a & set_b

# Count frequency of each timestamp in original streams (for anomaly detection)
freq_a = Counter(timestamps_a)
freq_b = Counter(timestamps_b)

# Dummy variable for logging overhead
log_entry_count = len(timestamps_a) + len(timestamps_b)

# Compute final result
result = sum(common_elements)

# Irrelevant transformation (distractor with minimal interference)
doubled = [x * 2 for x in common_elements if x > 1005]

print(f"Result: {result}")