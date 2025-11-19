import math

def modified_fibonacci_with_decay(n, decay_rate=0.1):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Dynamic programming approach to avoid redundant calculations
        fib_cache = [0] * (n + 1)
        fib_cache[1] = 1
        
        for i in range(2, n + 1):
            # Modified Fibonacci: F(n) = F(n-1) + F(n-2) + decay_factor
            decay_factor = math.exp(-decay_rate * i)
            fib_cache[i] = fib_cache[i-1] + fib_cache[i-2] + decay_factor
        
        return fib_cache[n]

# Analysis period
analysis_period = 15

degradation_sequence = [modified_fibonacci_with_decay(i, 0.05) for i in range(1, analysis_period + 1)]

# Calculate cumulative impact with weighted contributions
signal_weights = [math.log(i+2) for i in range(analysis_period)]

weighted_degradations = [degradation_sequence[i] * signal_weights[i] for i in range(len(degradation_sequence))]

# Apply a secondary filter to focus on significant degradation events
significant_degradations = list(filter(lambda x: x > 5, weighted_degradations))

# Calculate the cumulative impact
from functools import reduce
cumulative_impact = reduce(lambda acc, val: acc + val * 0.75, significant_degradations, 0)

cumulative_impact = round(cumulative_impact, 2)

print(f"Result: {cumulative_impact}")