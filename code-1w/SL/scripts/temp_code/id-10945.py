from itertools import accumulate

# Simulate daily production output with incremental efficiency gains and maintenance dips
daily_input = [120, 135, 142, 130, 155, 160, 150]
efficiency_factors = [1.0, 1.05, 1.1, 0.95, 1.2, 1.25, 1.15]

# Apply efficiency to raw input to get actual daily output
daily_output = [inp * eff for inp, eff in zip(daily_input, efficiency_factors)]

# Smoothen output using cumulative average as secondary metric (distractor)
cumulative_avg = list(accumulate(daily_output))
total_days = len(daily_output)
cumulative_avg = [avg / (i + 1) for i, avg in enumerate(cumulative_avg)]

# Key computation: find peak capacity
peak_capacity = max(daily_output)

# Print result
print(f"Result: {peak_capacity}")