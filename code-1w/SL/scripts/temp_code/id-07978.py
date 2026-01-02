from collections import defaultdict
import math

# Simulate hourly resource allocation across departments
time_slots = list(range(8, 18))  # Operating hours 8 AM to 5 PM
departments = ['dev', 'qa', 'ops', 'research']

# Initialize usage tracker
usage_tracker = defaultdict(int)
allocation_log = []

# Base load per department (arbitrary units)
base_loads = {'dev': 12, 'qa': 8, 'ops': 15, 'research': 10}

# Simulate fluctuating demand with periodic spikes
for hour in time_slots:
    hourly_load = 0
    
    # Compute hour-specific multipliers
    if hour < 12:
        morning_boost = 1.2
        afternoon_boost = 1.0
    else:
        morning_boost = 1.0
        afternoon_boost = 1.3
    
    # Additional distraction: unused evening prep logic
    evening_prep = 0
    for i in range(2):
        evening_prep += int(5 * (i + 1) // 2)
    
    # Real computation: accumulate usage per department
    for dept in departments:
        base = base_loads[dept]
        
        # Cyclical variation using sine function (e.g., meeting lulls)
        cyclical_factor = (math.sin(math.pi * (hour - 8) / 6) + 1.5)  # Bias above zero
        
        # Department-specific scaling
        if dept == 'dev':
            scale = morning_boost * 1.1
        elif dept == 'research':
            scale = afternoon_boost * 1.4
        else:
            scale = 1.0
        
        allocated = int(base * cyclical_factor * scale)
        usage_tracker[dept] += allocated
        allocation_log.append((hour, dept, allocated))

# Irrelevant aggregation: total over-allocation (not used)
total_allocations = sum([x[2] for x in allocation_log])
overhead_estimate = total_allocations * 0.05  # Assumed overhead

# Dummy filtering operation with lambda (no effect)
valid_logs = list(filter(lambda x: x[2] > 10, allocation_log))

# Secondary distraction: complex list comprehension with unused result
consolidated = [
    f'{dept}:{sum(alloc for h, d, alloc in allocation_log if d == dept)}'
    for dept in sorted(set(d for _, d, _ in allocation_log))
]

# Critical execution point
peak_capacity = max(usage_tracker.values())

# Final output
print(f"Result: {peak_capacity}")