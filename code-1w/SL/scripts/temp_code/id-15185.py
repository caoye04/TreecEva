def calculate_latency(nodes, base_latency):
    total = 0
    for node in nodes:
        if node % 3 == 0:
            total += base_latency * 1.5
        elif node % 5 == 0:
            total += base_latency * 0.8
        else:
            total += base_latency
    return total

# Simulate network node load distribution
event_loads = [i**2 for i in range(1, 12) if i % 2 != 0]
processed_nodes = set()
dummy_counter = 0

for val in event_loads:
    if val > 50:
        break
    processed_nodes.add(val)
    dummy_counter += 1  # irrelevant to final result

# Red herring computation: power consumption estimate (not used)
power_estimate = sum([x * 0.77 for x in event_loads])
scaling_factor = len(processed_nodes) / 4.0 if processed_nodes else 1.0

# Actual bandwidth logic with interference from above
initial_bandwidth = 120.0
utilization_log = []

for i in range(len(event_loads)):
    if i % 3 == 0:
        utilization_log.append(initial_bandwidth * (0.3 + i * 0.05))
    else:
        utilization_log.append(initial_bandwidth * 0.6)

# Secondary distraction: peak detection (unused)
peaks = [utilization_log[i] for i in range(1, len(utilization_log)-1)
         if utilization_log[i-1] < utilization_log[i] > utilization_log[i+1]]

# Core optimization using set difference and modular arithmetic
active_set = {x % 7 for x in processed_nodes}
available_channels = {1, 2, 3, 4, 5, 6}
allocated_channels = available_channels - active_set

# Use min/max/average pattern on meaningful subset
channel_score = 0
if allocated_channels:
    channel_score = (max(allocated_channels) + min(allocated_channels)) / 2.0

# Final calculation influenced by latency and channel efficiency
total_events = len(event_loads)
adjusted_latency = calculate_latency(list(processed_nodes), base_latency=2.5)

# Key statement
final_bandwidth = initial_bandwidth * (len(allocated_channels) / 5.0)
final_bandwidth -= adjusted_latency * channel_score

print(f"Result: {final_bandwidth}")