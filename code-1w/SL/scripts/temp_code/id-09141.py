from itertools import cycle

# Simulate daily system load over a week (in percentage)
daily_loads = [78, 85, 92, 88, 95, 76, 83]

# Use itertools.cycle to extend the pattern for a 10-day forecast
cycle_iter = cycle(daily_loads)
extended_loads = [next(cycle_iter) for _ in range(10)]

# Slice to get the middle 6 days (index 2 to 7 inclusive)
daily_loads_sliced = extended_loads[2:8]

# Identify peak capacity during the observation window
peak_capacity = max(daily_loads_sliced)

# Irrelevant auxiliary variable (minor distraction, intervention level 4)
temp_avg = sum(daily_loads_sliced) / len(daily_loads_sliced)

Result: peak_capacity