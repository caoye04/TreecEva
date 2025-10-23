from collections import deque
from functools import reduce
from statistics import mean

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Deep space telemetry frequency bins
frequency_bins = [120, 245, 312, 408, 516, 625, 732, 840]
window_size = 3

# Step 1: Compute sliding window means
window_means = []
window = deque(maxlen=window_size)
for freq in frequency_bins:
    window.append(freq)
    if len(window) == window_size:
        window_means.append(round(mean(window)))

# Step 2: Filter values where (value mod 17) == 5
filtered_values = [val for val in window_means if val % 17 == 5]

# Step 3: Apply bit reversal to each filtered value (assuming 10-bit representation)
bit_reversed_values = []
for val in filtered_values:
    reversed_val = int(format(val, '010b')[::-1], 2)
    bit_reversed_values.append(reversed_val)

# Step 4: Compute LCM of first two reversed values
if len(bit_reversed_values) >= 2:
    partial_lcm = lcm(bit_reversed_values[0], bit_reversed_values[1])
else:
    partial_lcm = bit_reversed_values[0] if bit_reversed_values else 0

# Step 5: Compute GCD of partial_lcm and remaining reversed values
remaining_values = bit_reversed_values[2:] if len(bit_reversed_values) > 2 else [partial_lcm]
final_gcd = reduce(gcd, [partial_lcm] + remaining_values)

print(f"Result: {final_gcd}")