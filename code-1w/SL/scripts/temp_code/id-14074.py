from itertools import compress

# System load parameters
cpu_loads = [0.78, 0.85, 0.92, 0.67, 0.74]
memory_loads = [0.64, 0.77, 0.88, 0.55, 0.81]
disk_io = [0.30, 0.45, 0.60, 0.40, 0.50]

# Derived metric: combined system stress index
system_stress = [
    (cpu + mem) * (1 + io) for cpu, mem, io in zip(cpu_loads, memory_loads, disk_io)
]

# Determine periods where stress exceeds threshold (0.85)
high_stress_mask = [stress > 0.85 for stress in system_stress]

# Extract corresponding CPU loads during high-stress periods
spike_cpu_loads = list(compress(cpu_loads, high_stress_mask))

# Calculate capacity headroom as 1 - load
headroom = [round(1 - load, 2) for load in spike_cpu_loads]

# Simulate dynamic scaling: add base reserve to remaining capacity
capacity_levels = [h + 0.15 for h in headroom]

# Critical point: determine peak adjusted capacity
total_available = sum(capacity_levels)
peak_capacity = max(capacity_levels)

# Irrelevant tracking variable (mild distraction)
active_zones = len(spike_cpu_loads)

print(f"Result: {peak_capacity}")