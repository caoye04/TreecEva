from functools import reduce
from collections import defaultdict

def count_distinct_prime_factors(n):
    if n <= 1:
        return 0
    count = 0
    if n % 2 == 0:
        count += 1
        while n % 2 == 0:
            n //= 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            count += 1
            while n % i == 0:
                n //= i
        i += 2
    if n > 1:
        count += 1
    return count

# Deep space frequency readings in Hz
frequency_readings = [120, 143, 150, 175, 198, 210, 221]

# Step 1: Compute weights based on distinct prime factors
signal_weights = list(map(count_distinct_prime_factors, frequency_readings))

# Step 2: Calculate weighted values (frequency * weight)
weighted_values = [freq * weight for freq, weight in zip(frequency_readings, signal_weights)]

# Step 3: Normalize by subtracting the mean
mean_value = sum(weighted_values) / len(weighted_values)
normalized_values = [val - mean_value for val in weighted_values]

# Step 4: Apply dynamic programming to find maximum subsequence sum
max_ending_here = max_so_far = normalized_values[0]
for val in normalized_values[1:]:
    max_ending_here = max(val, max_ending_here + val)
    max_so_far = max(max_so_far, max_ending_here)

max_subsequence_sum = max_so_far
print(f"Result: {max_subsequence_sum}")