from collections import defaultdict

# Simulate server load monitoring over a week
hours = ['morning', 'afternoon', 'evening']
days = ['mon', 'tue', 'wed', 'thu', 'fri']
base_loads = {'morning': 120, 'afternoon': 180, 'evening': 220}

# Initialize daily totals
daily_totals = defaultdict(float)

# Simulate fluctuating load with small variance
for day in days:
    for hour in hours:
        base = base_loads[hour]
        fluctuation = len(day) * (hours.index(hour) + 1)
        daily_totals[day] += base + fluctuation

# Extract daily loads as list
daily_loads = [daily_totals[d] for d in days]

# Add smoothing adjustment for weekends (not active here but modeled)
adjusted_loads = [load * 0.95 if i < 2 else load for i, load in enumerate(daily_loads)]

# Critical statement
peak_load = max(daily_loads)

# Debug variables (irrelevant to main logic - minor distraction)
count_high_load_days = sum(1 for x in daily_loads if x > 600)
avg_load = sum(daily_loads) / len(daily_loads)

print(f"Result: {peak_load}")