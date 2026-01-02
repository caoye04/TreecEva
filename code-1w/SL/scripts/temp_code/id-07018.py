from itertools import compress

# System monitoring simulation with time-series data
time_intervals = list(range(10))
base_loads = [30, 45, 60, 80, 95, 110, 90, 70, 50, 40]
emergency_override = True

trending_up = [base_loads[i] > base_loads[i-1] for i in range(1, len(base_loads))]
system_status_flags = [1 if x >= 75 else 0 for x in base_loads]

# Slice: extract mid-period load values (index 3 to 7 inclusive)
start, end = 3, 8
system_loads_sliced = base_loads[start:end]

# Simulate conditional alert masking using itertools.compress
active_alerts = list(compress(system_loads_sliced, [flag == 1 for flag in system_status_flags[start:end]]))

# Critical capacity evaluation
peak_capacity = max(system_loads_sliced)

# Irrelevant status log (minimal distraction)
current_state = 'STANDBY' if sum(system_loads_sliced) < 300 else 'ACTIVE'

Result: peak_capacity