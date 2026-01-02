from collections import defaultdict

# Simulate hourly resource load across servers
server_loads = [
    ('server_a', 45), ('server_b', 32), ('server_a', 50),
    ('server_c', 67), ('server_b', 41), ('server_d', 55),
    ('server_c', 60), ('server_a', 53), ('server_d', 58)
]

load_distribution = defaultdict(int)
for server, load in server_loads:
    load_distribution[server] += load

# Efficiency factor based on cooling performance
cooling_log = [0.92, 0.95, 0.98, 0.94]
efficiency_factor = sum(cooling_log) / len(cooling_log)

# Calculate peak capacity requirement
peak_capacity = max(load_distribution.values()) * efficiency_factor

# Irrelevant metric (minor distraction)
idle_time = 120

print(f"Result: {peak_capacity}")