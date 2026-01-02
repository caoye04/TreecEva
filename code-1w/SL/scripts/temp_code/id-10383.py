from collections import defaultdict

# Simulate time-series load data for a power grid segment
time_slots = ['t0', 't1', 't2', 't3', 't4']
load_readings = [120, 150, 130, 160, 140]

# Irrelevant auxiliary mapping (minimal distraction)
diagnostic_codes = defaultdict(str, {'t0': 'OK', 't2': 'OK'})

# Base load computation
base_loads = []
for i, slot in enumerate(time_slots):
    adjusted = load_readings[i] * 0.9  # Apply efficiency factor
    base_loads.append(int(adjusted))

# System status and overload logic
system_active = True
overload_factor = 1.25

# Key assignment with conditional expression
peak_load = max(base_loads) * overload_factor if system_active else 0

# Output result as required
print(f"Target result: {peak_load}")