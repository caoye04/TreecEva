from math import gcd
from functools import reduce

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def custom_sort(arr):
    # Sort based on GCD with array length, then by value
    return sorted(arr, key=lambda x: (gcd(x, len(arr)), x))

# Initial signal data
signal_strengths = [23, 45, 17, 68, 34, 89, 12, 56, 77, 31]

# Step 1: Apply bit masking to isolate lower 6 bits
masked_signals = [s & 0x3F for s in signal_strengths]

# Step 2: Create verification set with indices that are Fibonacci numbers < 20
fib_indices = {0, 1, 2, 3, 5, 8, 13}
verification_set = frozenset(i for i, v in enumerate(masked_signals) if i in fib_indices)

# Step 3: Custom sort the masked signals
sorted_signals = custom_sort(masked_signals)

# Step 4: Calculate verification score using XOR on prime-indexed elements
verification_score = 0
for idx in verification_set:
    if is_prime(idx):
        verification_score ^= sorted_signals[idx]

print(f"Result: {verification_score}")