from itertools import accumulate

# Simulate daily power load adjustments over a week
base_load = [120, 150, 130, 180, 160, 200, 140]
daily_adjustments = [10, -5, 20, -10, 15, -20, 25]

# Apply adjustments to base load
corrected_load = [base_load[i] + daily_adjustments[i] for i in range(len(base_load))]

# Compute cumulative effect of corrected loads over time using rolling 3-day smoothing
smoothed_load = [sum(corrected_load[max(0, i-2):i+1]) / min(3, i+1) for i in range(7)]

# Accumulate smoothed values to simulate grid stress buildup
accumulated_loads = list(accumulate(smoothed_load, lambda acc, x: acc + x * 0.9))

# Determine peak accumulated stress level
peak_capacity = max(accumulated_loads)

# Irrelevant distraction: unused variable
unused_metric = sum(base_load) / len(base_load)

print(f"Result: {peak_capacity}")