from collections import Counter

# Simulate timestamps of data packets received over a network
packet_timestamps = [1623, 1623, 1624, 1625, 1625, 1625, 1626, 1627, 1627, 1628, 1629, 1629]

# Count frequency of packets per timestamp
timestamp_counts = Counter(packet_timestamps)

# Auxiliary variable - average frequency (not directly used in final computation)
avg_frequency = sum(timestamp_counts.values()) / len(timestamp_counts)

# Function to compute network load based on frequency distribution
def calculate_network_load(counts):
    load = 0
    for freq in counts.values():
        if freq > 2:
            load += freq * 2
        elif freq == 2:
            load += 3
        else:
            load += 1
    return load

# Compute total network load
total_load = calculate_network_load(timestamp_counts)

# Irrelevant tracking variable (minor distraction)
critical_threshold_exceeded = False
if total_load > 20:
    critical_threshold_exceeded = True

print(f"Result: {total_load}")