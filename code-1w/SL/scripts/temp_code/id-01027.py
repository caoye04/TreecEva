from itertools import compress

# System monitoring simulation: filter and analyze server load peaks
cpu_loads = [78, 85, 90, 65, 40, 95, 88, 77, 63, 54]
memory_usage = [80, 75, 85, 60, 30, 90, 82, 70, 55, 50]
disk_io_active = [True, True, False, True, False, True, True, True, False, True]

time_of_day_hour = 14  # Midday, affects filtering threshold

# Determine high-load threshold based on time of day
base_threshold = 70 if time_of_day_hour in range(9, 18) else 50

# Create condition: CPU load above threshold and memory within critical limit
is_high_load = [load > base_threshold for load in cpu_loads]
within_memory_limit = [usage < 88 for usage in memory_usage]

# Apply combined conditions using logical AND via generator expression
system_stress_condition = [cpu and mem for cpu, mem in zip(is_high_load, within_memory_limit)]

# Filter active servers with disk I/O and stress condition
active_stress_servers = list(compress(system_stress_condition, disk_io_active))
system_loads_filtered = list(compress(cpu_loads, active_stress_servers))

# Key statement
peak_capacity = max(system_loads_filtered)

print(f"Result: {peak_capacity}")