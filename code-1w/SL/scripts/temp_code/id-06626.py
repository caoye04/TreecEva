from itertools import compress, cycle

# System performance monitoring simulation
timestamps = [101, 102, 103, 104, 105]
loads = [0.78, 0.92, 0.61, 0.95, 0.83]
servers_active = [12, 14, 10, 16, 13]

# Construct system states as (timestamp, load, servers)
system_states = list(zip(timestamps, loads, servers_active))

# Calculate effective capacity as load * servers_active
# Identify peak effective capacity state
peak_capacity = max(system_states, key=lambda x: x[1] * x[2])

# Irrelevant filtering operation (minor distraction)
valid_periods = list(compress(timestamps, (load > 0.85 for load in loads)))

cycle_iter = cycle(['A', 'B'])
next(cycle_iter)  # Unused operation

Result: {peak_capacity}